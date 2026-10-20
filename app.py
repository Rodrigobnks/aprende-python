"""Servidor local para aprender Python desde cero. Solo escucha en 127.0.0.1."""

import argparse
import ast
from contextlib import closing
import csv
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import io
import json
import os
from pathlib import Path
import re
import sqlite3
import subprocess
import sys
import tempfile
from threading import Timer
import webbrowser

from curriculum import LESSONS, LESSON_BY_ID, public_lessons
from guide import public_guide
from library_catalog import public_catalog
from library_labs import LABS, LAB_BY_ID, lab_packages, lab_import_roots, public_labs
from learning_support import installation_diagnosis, mismatch_diagnosis, runtime_diagnosis
from advanced_curriculum import ADVANCED, ADVANCED_BY_ID, public_advanced, workspace_id


ROOT = Path(__file__).resolve().parent
DATABASE = ROOT / "data" / "progreso.db"
LAB_ENV = ROOT / "data" / "library_venv"
FORBIDDEN = (
    ast.Import, ast.ImportFrom, ast.ClassDef, ast.Lambda,
    ast.With, ast.AsyncWith, ast.Try, ast.Raise, ast.Delete,
    ast.Global, ast.Nonlocal, ast.Yield, ast.YieldFrom, ast.Await,
    ast.AsyncFunctionDef, ast.NamedExpr,
)
ALLOWED_METHODS = {"upper", "lower", "strip", "replace", "split", "count", "append", "get", "values"}


def init_db():
    DATABASE.parent.mkdir(parents=True, exist_ok=True)
    with closing(sqlite3.connect(DATABASE)) as connection, connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS progress (
                lesson_id TEXT PRIMARY KEY,
                attempts INTEGER NOT NULL DEFAULT 0,
                completed_at TEXT
            )
        """)
        connection.execute("""
            CREATE TABLE IF NOT EXISTS lab_progress (
                lab_id TEXT PRIMARY KEY,
                attempts INTEGER NOT NULL DEFAULT 0,
                completed_at TEXT
            )
        """)
        connection.execute("""
            CREATE TABLE IF NOT EXISTS advanced_progress (
                item_id TEXT PRIMARY KEY,
                attempts INTEGER NOT NULL DEFAULT 0,
                completed_at TEXT
            )
        """)
        connection.execute("""
            CREATE TABLE IF NOT EXISTS advanced_drafts (
                workspace_id TEXT PRIMARY KEY,
                files_json TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )
        """)


def progress_data():
    with closing(sqlite3.connect(DATABASE)) as connection:
        rows = connection.execute(
            "SELECT lesson_id, attempts, completed_at FROM progress"
        ).fetchall()
    progress = {
        lesson_id: {"attempts": attempts, "completed_at": completed_at}
        for lesson_id, attempts, completed_at in rows
    }
    completed = sum(bool(progress.get(lesson["id"], {}).get("completed_at")) for lesson in LESSONS)
    return {"lessons": progress, "completed": completed, "total": len(LESSONS)}


def record_attempt(lesson_id, passed):
    completed_at = datetime.now(timezone.utc).isoformat() if passed else None
    with closing(sqlite3.connect(DATABASE)) as connection, connection:
        connection.execute("""
            INSERT INTO progress (lesson_id, attempts, completed_at)
            VALUES (?, 1, ?)
            ON CONFLICT(lesson_id) DO UPDATE SET
                attempts = attempts + 1,
                completed_at = COALESCE(progress.completed_at, excluded.completed_at)
        """, (lesson_id, completed_at))


def lab_progress_data():
    with closing(sqlite3.connect(DATABASE)) as connection:
        rows = connection.execute("SELECT lab_id, attempts, completed_at FROM lab_progress").fetchall()
    entries = {lab_id: {"attempts": attempts, "completed_at": completed_at} for lab_id, attempts, completed_at in rows}
    return {"labs": entries, "completed": sum(bool(entries.get(lab["id"], {}).get("completed_at")) for lab in LABS), "total": len(LABS)}


def record_lab_attempt(lab_id, passed):
    completed_at = datetime.now(timezone.utc).isoformat() if passed else None
    with closing(sqlite3.connect(DATABASE)) as connection, connection:
        connection.execute("""
            INSERT INTO lab_progress (lab_id, attempts, completed_at) VALUES (?, 1, ?)
            ON CONFLICT(lab_id) DO UPDATE SET
                attempts = attempts + 1,
                completed_at = COALESCE(lab_progress.completed_at, excluded.completed_at)
        """, (lab_id, completed_at))


def advanced_progress_data():
    with closing(sqlite3.connect(DATABASE)) as connection:
        rows = connection.execute("SELECT item_id, attempts, completed_at FROM advanced_progress").fetchall()
    entries = {item_id: {"attempts": attempts, "completed_at": completed_at} for item_id, attempts, completed_at in rows}
    return {"items": entries, "completed": sum(bool(entries.get(item["id"], {}).get("completed_at")) for item in ADVANCED), "total": len(ADVANCED)}


def advanced_drafts_data():
    with closing(sqlite3.connect(DATABASE)) as connection:
        rows = connection.execute("SELECT workspace_id, files_json FROM advanced_drafts").fetchall()
    return {key: json.loads(value) for key, value in rows}


def record_advanced_attempt(item_id, passed):
    completed_at = datetime.now(timezone.utc).isoformat() if passed else None
    with closing(sqlite3.connect(DATABASE)) as connection, connection:
        connection.execute("""
            INSERT INTO advanced_progress (item_id, attempts, completed_at) VALUES (?, 1, ?)
            ON CONFLICT(item_id) DO UPDATE SET
                attempts = attempts + 1,
                completed_at = COALESCE(advanced_progress.completed_at, excluded.completed_at)
        """, (item_id, completed_at))


def validate_advanced_files(files):
    if not isinstance(files, dict) or "main.py" not in files or len(files) > 8:
        raise ValueError("El proyecto debe incluir main.py y tener como máximo 8 archivos Python.")
    if any(not isinstance(name, str) or not re.fullmatch(r"[a-z][a-z0-9_]*\.py", name) or name == "__prueba__.py" for name in files):
        raise ValueError("Usa nombres simples de archivos .py, sin carpetas ni rutas.")
    if any(not isinstance(code, str) or len(code) > 10000 for code in files.values()) or sum(map(len, files.values())) > 30000:
        raise ValueError("Cada archivo admite hasta 10000 caracteres y el proyecto hasta 30000.")
    return files


def save_advanced_draft(item_id, files):
    item = ADVANCED_BY_ID[item_id]
    validate_advanced_files(files)
    key = workspace_id(item)
    with closing(sqlite3.connect(DATABASE)) as connection, connection:
        connection.execute("""
            INSERT INTO advanced_drafts (workspace_id, files_json, updated_at) VALUES (?, ?, ?)
            ON CONFLICT(workspace_id) DO UPDATE SET files_json = excluded.files_json, updated_at = excluded.updated_at
        """, (key, json.dumps(files, ensure_ascii=False), datetime.now(timezone.utc).isoformat()))
    return {"saved": True, "workspace_id": key}


def validate_advanced_imports(files, item):
    imported = set()
    for name, code in files.items():
        try:
            tree = ast.parse(code, filename=name)
        except SyntaxError as exc:
            return f"{name}, línea {exc.lineno}: {exc.msg}"
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imported.update(alias.name.split(".", 1)[0] for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                imported.add(node.module.split(".", 1)[0])
    missing = set(item["required_imports"]) - imported
    if missing:
        return "Falta importar: " + ", ".join(sorted(missing)) + "."
    return None


def run_advanced_case(files, case):
    temporary_root = ROOT / "data" / "tmp"
    temporary_root.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="proyecto-", dir=temporary_root) as folder:
        payload = Path(folder) / "entrada.json"
        payload.write_text(json.dumps({
            "files": files,
            "seed_files": case.get("files", {}),
            "stdin": case.get("stdin", ""),
            "argv": case.get("argv", []),
            "harness": case.get("harness"),
            "expected_file_names": list(case.get("expected_files", {})),
            "db_checks": {name: check["query"] for name, check in case.get("expected_db", {}).items()},
        }, ensure_ascii=False), encoding="utf-8")
        try:
            process = subprocess.run(
                [sys.executable, "-I", "-B", str(ROOT / "advanced_runner.py"), str(payload)],
                cwd=folder, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=5, check=False,
            )
        except subprocess.TimeoutExpired:
            return {"stdout": "", "error": "El programa tardó demasiado. Revisa si hay un bucle infinito.", "files": {}}
        except OSError as exc:
            return {"stdout": "", "error": f"No se pudo iniciar Python: {exc}", "files": {}}
    if process.returncode or len(process.stdout) > 50000:
        return {"stdout": "", "error": (process.stderr or "No se pudo leer la ejecución.")[-2000:], "files": {}}
    try:
        return json.loads(process.stdout)
    except json.JSONDecodeError:
        return {"stdout": "", "error": "No se pudo leer el resultado del programa.", "files": {}}


def compare_advanced_file(name, received, expected):
    if received is None:
        return False
    try:
        if name.endswith(".json"):
            return json.loads(received) == expected
        if name.endswith(".csv"):
            return list(csv.DictReader(io.StringIO(received))) == expected
    except (json.JSONDecodeError, csv.Error, TypeError):
        return False
    return received == expected


def execute_advanced(item_id, files, check=False):
    item = ADVANCED_BY_ID[item_id]
    validate_advanced_files(files)
    error = validate_advanced_imports(files, item)
    if error:
        result = {"passed": False, "message": error, "diagnosis": runtime_diagnosis(error)}
    else:
        cases = item["cases"] if check else item["cases"][:1]
        result = {"passed": True, "message": "El ejemplo salió bien. Comprueba la etapa para evaluar más casos."}
        for index, case in enumerate(cases, 1):
            received = run_advanced_case(files, case)
            if received["error"]:
                result = {"passed": False, "message": f"Prueba {index}: el programa produjo un error.", "received": received["stdout"], "error": received["error"], "diagnosis": runtime_diagnosis(received["error"])}
                break
            if received["stdout"].strip() != case["expected_stdout"].strip():
                result = {"passed": False, "message": f"Prueba {index}: la salida no coincide.", "received": received["stdout"].strip(), "expected": case["expected_stdout"], "diagnosis": "Revisa los datos de entrada, el formato y los saltos de línea."}
                break
            for name, expected in case.get("expected_files", {}).items():
                content = received["files"].get(name)
                if not compare_advanced_file(name, content, expected):
                    result = {"passed": False, "message": f"Prueba {index}: el archivo {name} no contiene el resultado esperado.", "received": content if content is not None else "(archivo no creado)", "expected": expected, "diagnosis": f"Abre o crea {name} en la carpeta del programa y comprueba su contenido."}
                    break
            if not result["passed"]:
                break
            for name, check in case.get("expected_db", {}).items():
                rows = received.get("databases", {}).get(name)
                if rows != check["rows"]:
                    result = {"passed": False, "message": f"Prueba {index}: la base {name} no contiene los movimientos esperados.", "received": rows if rows is not None else "(base o tabla no creada)", "expected": check["rows"], "diagnosis": "Comprueba CREATE TABLE, INSERT con parámetros y commit de la conexión."}
                    break
            if not result["passed"]:
                break
            if check:
                result["message"] = f"¡Etapa superada! Pasaste {len(cases)} pruebas."
        if not result["passed"]:
            result["case_input"] = {key: case[key] for key in ("stdin", "argv", "files") if key in case}
    if check:
        record_advanced_attempt(item_id, result["passed"])
        result["progress"] = advanced_progress_data()
    return result


def lab_python():
    return LAB_ENV / ("Scripts/python.exe" if os.name == "nt" else "bin/python")


def lab_environment_ready():
    pip_executable = LAB_ENV / ("Scripts/pip.exe" if os.name == "nt" else "bin/pip")
    return lab_python().is_file() and pip_executable.is_file()


def lab_install_command(package):
    packages = package if isinstance(package, list) else [package]
    prefix = f'& "{lab_python()}"' if os.name == "nt" else f'"{lab_python()}"'
    return f'{prefix} -m pip install ' + " ".join(f'"{item}"' for item in packages)


def setup_lab_environment():
    if lab_environment_ready():
        return {"ready": True, "message": "El entorno del laboratorio ya está preparado."}
    LAB_ENV.parent.mkdir(parents=True, exist_ok=True)
    setup_tmp = LAB_ENV.parent / "tmp" / "venv-setup"
    setup_tmp.mkdir(parents=True, exist_ok=True)
    environment = os.environ.copy()
    environment.update({"TMP": str(setup_tmp), "TEMP": str(setup_tmp), "TMPDIR": str(setup_tmp)})
    try:
        process = subprocess.run([sys.executable, "-m", "venv", str(LAB_ENV)], capture_output=True, text=True, timeout=90, check=False, env=environment)
    except (OSError, subprocess.TimeoutExpired) as exc:
        return {"ready": False, "error": f"No se pudo crear el entorno: {exc}"}
    if process.returncode or not lab_environment_ready():
        return {"ready": False, "error": (process.stderr or process.stdout or "No se pudo preparar el entorno de Python.")[-1200:]}
    return {"ready": True, "message": "Entorno preparado. Ejecuta el comando de instalación que aparece en cada reto."}


def lab_package_status(lab_id):
    lab = LAB_BY_ID[lab_id]
    packages = lab_packages(lab)
    roots = lab_import_roots(lab)
    command = lab_install_command(packages)
    if not lab_environment_ready():
        return {"ready": False, "installed": False, "message": "Prepara primero el entorno del laboratorio.", "command": command}
    versions = {}
    for package, root in zip(packages, roots):
        try:
            process = subprocess.run(
                [str(lab_python()), "-I", "-B", "-c", "import importlib.metadata,sys; print(importlib.metadata.version(sys.argv[1]))", package],
                capture_output=True, text=True, timeout=10, check=False,
            )
            if process.returncode:
                return {"ready": True, "installed": False, "message": f"Falta instalar {package} en el entorno del curso.", "command": command}
            versions[package] = process.stdout.strip()
            imported = subprocess.run(
                [str(lab_python()), "-I", "-B", "-c", "import importlib,sys; importlib.import_module(sys.argv[1])", root],
                capture_output=True, text=True, timeout=10, check=False,
            )
        except (OSError, subprocess.TimeoutExpired):
            return {"ready": False, "installed": False, "message": "No se pudo comprobar el entorno. Prueba a prepararlo de nuevo.", "command": command}
        if imported.returncode:
            return {"ready": True, "installed": False, "message": f"{package} figura como instalado, pero import {root} falló. Revisa la instalación y sus dependencias.", "command": command}
    summary = ", ".join(f"{package} {version}" for package, version in versions.items())
    return {"ready": True, "installed": True, "versions": versions, "message": f"Instalación e importación comprobadas: {summary}.", "command": command}


def diagnose_lab_install(lab_id, output):
    if not isinstance(output, str) or len(output) > 6000:
        raise ValueError("Pega un mensaje de error de hasta 6000 caracteres.")
    lab = LAB_BY_ID[lab_id]
    return {"diagnosis": installation_diagnosis(output, lab, lab_install_command(lab_packages(lab)))}


def validate_lab_code(code, lab):
    if not isinstance(code, str) or not code.strip():
        return "Escribe el import y la función solve antes de ejecutar."
    if len(code) > 6000:
        return "El código supera el límite de 6000 caracteres."
    try:
        tree = ast.parse(code)
    except SyntaxError as exc:
        return f"Error de sintaxis en la línea {exc.lineno}: {exc.msg}"
    allowed_roots = set(lab_import_roots(lab))
    imported = set()
    imported_names = {root: set() for root in allowed_roots}
    defined = False
    solve_node = None
    forbidden = (ast.ClassDef, ast.Lambda, ast.With, ast.AsyncWith, ast.Try, ast.Raise,
                 ast.Delete, ast.Global, ast.Nonlocal, ast.Yield, ast.YieldFrom,
                 ast.Await, ast.AsyncFunctionDef, ast.NamedExpr)
    for node in ast.walk(tree):
        if isinstance(node, forbidden):
            return "Este laboratorio admite funciones, condiciones y bucles, pero no clases ni operaciones avanzadas."
        if isinstance(node, ast.Import):
            roots = {alias.name.split(".", 1)[0] for alias in node.names}
            if not roots <= allowed_roots:
                return "Importa solo las bibliotecas indicadas para este reto: " + ", ".join(sorted(allowed_roots)) + "."
            imported.update(roots)
            for alias in node.names:
                imported_names[alias.name.split(".", 1)[0]].add(alias.asname or alias.name.split(".", 1)[0])
        if isinstance(node, ast.ImportFrom):
            root = node.module.split(".", 1)[0] if node.module else None
            if node.level or root not in allowed_roots or any(alias.name == "*" for alias in node.names):
                return "Importa solo las bibliotecas indicadas para este reto: " + ", ".join(sorted(allowed_roots)) + "."
            imported.add(root)
            imported_names[root].update(alias.asname or alias.name for alias in node.names)
        if isinstance(node, ast.FunctionDef) and node.name == "solve":
            defined = True
            solve_node = node
        if isinstance(node, ast.Name) and node.id.startswith("_"):
            return "No uses nombres que comiencen con _."
        if isinstance(node, ast.Attribute) and node.attr.startswith("_"):
            return "No uses atributos que comiencen con _."
        if isinstance(node, ast.arg) and node.arg.startswith("_"):
            return "No uses parámetros que comiencen con _."
        if isinstance(node, ast.alias) and node.asname and node.asname.startswith("_"):
            return "No uses alias que comiencen con _."
    if imported != allowed_roots:
        return "Falta importar " + ", ".join(sorted(allowed_roots - imported)) + " en tu código."
    if not defined:
        return "Define una función llamada solve con los parámetros indicados."
    names_used = {node.id for node in ast.walk(solve_node) if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load)}
    for root in sorted(allowed_roots):
        if not imported_names[root] & names_used:
            return f"Importaste {root}, pero todavía no lo usas dentro de solve."
    return None


def execute_lab(lab_id, code, check=False):
    lab = LAB_BY_ID[lab_id]
    error = validate_lab_code(code, lab)
    if error:
        diagnosis = ("Escribe el import indicado y usa esa biblioteca dentro de solve; instalarla y mencionarla sin usarla no resuelve el reto."
                     if "importar" in error or "Importaste" in error else runtime_diagnosis(error))
        result = {"passed": False, "message": error, "diagnosis": diagnosis}
    else:
        status = lab_package_status(lab_id)
        if not status["installed"]:
            result = {"passed": False, "message": status["message"], "install_command": status["command"], "diagnosis": "Prepara el entorno, ejecuta el comando mostrado en PowerShell y pulsa Comprobar instalación."}
        else:
            cases = lab["cases"] if check else lab["cases"][:1]
            temporary_root = ROOT / "data" / "tmp"
            temporary_root.mkdir(parents=True, exist_ok=True)
            with tempfile.TemporaryDirectory(prefix="laboratorio-", dir=temporary_root) as folder:
                payload = Path(folder) / "entrada.json"
                payload.write_text(json.dumps({"code": code, "cases": [case["args"] for case in cases]}, ensure_ascii=False), encoding="utf-8")
                try:
                    process = subprocess.run([str(lab_python()), "-I", "-B", str(ROOT / "lab_runner.py"), str(payload)], cwd=folder, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=15, check=False)
                except (OSError, subprocess.TimeoutExpired):
                    process = None
            if process is None:
                result = {"passed": False, "message": "El programa tardó demasiado o el entorno no pudo iniciarse.", "diagnosis": "Revisa si hay un bucle que no termina o una operación que espera una conexión."}
            elif process.returncode or len(process.stdout) > 50000:
                result = {"passed": False, "message": "No se pudo ejecutar el programa. Revisa tus importaciones.", "diagnosis": "Ejecuta primero el ejemplo más pequeño y comprueba que el paquete aparece como instalado."}
            else:
                try:
                    report = json.loads(process.stdout)
                except json.JSONDecodeError:
                    report = {"ok": False, "error": "No se pudo leer el resultado."}
                if not report["ok"]:
                    result = {"passed": False, "message": report["error"], "diagnosis": runtime_diagnosis(report["error"])}
                else:
                    result = {"passed": True, "message": "¡Correcto! El código pasó las pruebas."}
                    for index, (case, received) in enumerate(zip(cases, report["results"]), start=1):
                        if not received["ok"]:
                            result = {"passed": False, "message": f"Prueba {index}: {received['error']}", "case_input": case["args"], "diagnosis": runtime_diagnosis(received["error"])}
                            break
                        if received["value"] != case["expected"] or type(received["value"]) is not type(case["expected"]):
                            result = {"passed": False, "message": f"Prueba {index}: el resultado aún no coincide.", "case_input": case["args"], "expected": case["expected"], "received": received["value"], "diagnosis": mismatch_diagnosis(lab_id=lab_id)}
                            break
                    if not check and result["passed"]:
                        result["message"] = "El ejemplo salió bien. Comprueba el reto para evaluar más casos."
    if check:
        record_lab_attempt(lab_id, result["passed"])
        result["progress"] = lab_progress_data()
    return result


def validate_code(code):
    if not isinstance(code, str) or not code.strip():
        return "Escribe algunas instrucciones antes de ejecutar."
    if len(code) > 6000:
        return "El código supera el límite de 6000 caracteres."
    try:
        tree = ast.parse(code)
    except SyntaxError as exc:
        return f"Error de sintaxis en la línea {exc.lineno}: {exc.msg}"
    for node in ast.walk(tree):
        if isinstance(node, FORBIDDEN):
            return "Esta ruta admite Python sin importaciones ni clases por ahora."
        if isinstance(node, ast.Name) and node.id.startswith("_"):
            return "En esta ruta, los nombres no pueden empezar con _."
        if isinstance(node, ast.FunctionDef) and node.name.startswith("_"):
            return "En esta ruta, los nombres no pueden empezar con _."
        if isinstance(node, ast.arg) and node.arg.startswith("_"):
            return "En esta ruta, los nombres no pueden empezar con _."
        if isinstance(node, ast.Attribute) and node.attr not in ALLOWED_METHODS:
            return "Ese método todavía no forma parte de los ejercicios."
        if isinstance(node, ast.Call) and not isinstance(node.func, (ast.Name, ast.Attribute)):
            return "Llama funciones por su nombre o usa los métodos enseñados en las lecciones."
    return None


def execute(code, user_input="", suffix=""):
    error = validate_code(code)
    if error:
        return {"stdout": "", "error": error, "ok": False}
    if len(user_input) > 1000:
        return {"stdout": "", "error": "La entrada es demasiado larga.", "ok": False}
    temporary_root = ROOT / "data" / "tmp"
    temporary_root.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="ejecucion-", dir=temporary_root) as folder:
        payload = Path(folder) / "entrada.json"
        payload.write_text(
            json.dumps({"code": code + suffix, "input": user_input}, ensure_ascii=False),
            encoding="utf-8",
        )
        try:
            process = subprocess.run(
                [sys.executable, "-I", "-S", "-B", str(ROOT / "runner.py"), str(payload)],
                cwd=folder,
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=3,
                check=False,
            )
        except subprocess.TimeoutExpired:
            return {"stdout": "", "error": "El programa tardó demasiado. Revisa si hay un bucle infinito.", "ok": False}
    if process.returncode != 0:
        return {"stdout": "", "error": "No se pudo ejecutar el programa.", "ok": False}
    try:
        return json.loads(process.stdout)
    except json.JSONDecodeError:
        return {"stdout": "", "error": "La salida del programa no se pudo leer.", "ok": False}


def check_lesson(lesson_id, code):
    lesson = LESSON_BY_ID[lesson_id]
    for index, case in enumerate(lesson["tests"], start=1):
        result = execute(code, case["input"], case.get("suffix", ""))
        if not result["ok"]:
            record_attempt(lesson_id, False)
            return {
                "passed": False,
                "message": f"Prueba {index}: {result['error']}",
                "case_input": case["input"],
                "received": result["stdout"],
                "expected": case["expected"],
                "diagnosis": runtime_diagnosis(result["error"]),
                "progress": progress_data(),
            }
        received = result["stdout"].strip()
        if received != case["expected"]:
            record_attempt(lesson_id, False)
            return {
                "passed": False,
                "message": f"Prueba {index}: la salida aún no coincide.",
                "case_input": case["input"],
                "received": received,
                "expected": case["expected"],
                "diagnosis": mismatch_diagnosis(unit=lesson["unit"]),
                "progress": progress_data(),
            }
    record_attempt(lesson_id, True)
    return {
        "passed": True,
        "message": "¡Correcto! Superaste todas las pruebas.",
        "progress": progress_data(),
    }


class Handler(BaseHTTPRequestHandler):
    def send_json(self, payload, status=200):
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/api/state":
            self.send_json({"lessons": public_lessons(), "guide": public_guide(), "catalog": public_catalog(), "progress": progress_data(), "labs": public_labs(), "lab_progress": lab_progress_data(), "lab_environment_ready": lab_environment_ready(), "advanced": public_advanced(), "advanced_progress": advanced_progress_data(), "advanced_drafts": advanced_drafts_data()})
            return
        assets = {
            "/": ("index.html", "text/html; charset=utf-8"),
            "/styles.css": ("styles.css", "text/css; charset=utf-8"),
            "/app.js": ("app.js", "text/javascript; charset=utf-8"),
        }
        if self.path not in assets:
            self.send_error(404)
            return
        filename, media_type = assets[self.path]
        body = (ROOT / filename).read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", media_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self):
        if self.path not in {"/api/run", "/api/check", "/api/labs/setup", "/api/labs/status", "/api/labs/diagnose", "/api/labs/run", "/api/labs/check", "/api/advanced/save", "/api/advanced/run", "/api/advanced/check"}:
            self.send_json({"error": "Ruta desconocida."}, 404)
            return
        try:
            size = int(self.headers.get("Content-Length", "0"))
            if size < 1 or size > 50000:
                raise ValueError("La solicitud está vacía o es demasiado grande.")
            payload = json.loads(self.rfile.read(size))
            if not isinstance(payload, dict):
                raise ValueError("La solicitud debe ser un objeto JSON.")
            if self.path.startswith("/api/advanced/"):
                item_id = payload.get("item_id")
                if item_id not in ADVANCED_BY_ID:
                    raise ValueError("Reto o etapa desconocidos.")
                files = payload.get("files")
                save_result = save_advanced_draft(item_id, files)
                if self.path == "/api/advanced/save":
                    self.send_json(save_result)
                else:
                    self.send_json(execute_advanced(item_id, files, self.path == "/api/advanced/check"))
                return
            if self.path.startswith("/api/labs/"):
                if self.path == "/api/labs/setup":
                    self.send_json(setup_lab_environment())
                    return
                lab_id = payload.get("lab_id")
                if lab_id not in LAB_BY_ID:
                    raise ValueError("Reto de biblioteca desconocido.")
                if self.path == "/api/labs/status":
                    self.send_json(lab_package_status(lab_id))
                    return
                if self.path == "/api/labs/diagnose":
                    self.send_json(diagnose_lab_install(lab_id, payload.get("output", "")))
                    return
                code = payload.get("code", "")
                if not isinstance(code, str):
                    raise ValueError("El código debe ser texto.")
                self.send_json(execute_lab(lab_id, code, self.path == "/api/labs/check"))
                return
            lesson_id = payload.get("lesson_id")
            code = payload.get("code", "")
            if lesson_id not in LESSON_BY_ID:
                raise ValueError("Lección desconocida.")
            if not isinstance(code, str):
                raise ValueError("El código debe ser texto.")
            if self.path == "/api/run":
                user_input = payload.get("input", "")
                if not isinstance(user_input, str):
                    raise ValueError("La entrada debe ser texto.")
                result = execute(code, user_input, LESSON_BY_ID[lesson_id].get("preview_suffix", ""))
                if not result["ok"]:
                    result["diagnosis"] = runtime_diagnosis(result["error"])
                self.send_json(result)
            else:
                self.send_json(check_lesson(lesson_id, code))
        except (ValueError, json.JSONDecodeError) as exc:
            self.send_json({"error": str(exc)}, 400)

    def log_message(self, format, *args):
        if not self.path.startswith("/api/"):
            return
        super().log_message(format, *args)


def main():
    parser = argparse.ArgumentParser(description="Plataforma local para aprender Python")
    parser.add_argument("--port", type=int, default=8765)
    parser.add_argument("--no-browser", action="store_true")
    args = parser.parse_args()
    init_db()
    server = ThreadingHTTPServer(("127.0.0.1", args.port), Handler)
    url = f"http://127.0.0.1:{server.server_port}"
    print(f"Aprende Python está listo en {url}", flush=True)
    if not args.no_browser:
        Timer(0.5, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nHasta la próxima lección.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
