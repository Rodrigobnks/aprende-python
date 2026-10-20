"""Compatibility bridge inside Pyodide only; never execute learner code on host."""
import contextlib
import io
import json
import os
from pathlib import Path
import runpy
import sys
import tempfile
import types
import app


def browser_process(args, **kwargs):
    old_cwd, old_argv, old_path, old_stdin = os.getcwd(), sys.argv[:], sys.path[:], sys.stdin
    previous_modules = set(sys.modules)
    output, errors = io.StringIO(), io.StringIO()
    status = 0
    try:
        if kwargs.get("cwd"):
            os.chdir(kwargs["cwd"])
        with contextlib.redirect_stdout(output), contextlib.redirect_stderr(errors):
            if "-c" in args:
                pos = args.index("-c")
                sys.argv = ["-c", *args[pos + 2:]]
                exec(args[pos + 1], {"__name__": "__main__"})
            else:
                pos = next(i for i, value in enumerate(args) if str(value).endswith("_runner.py") or str(value).endswith("/runner.py"))
                sys.argv = [str(value) for value in args[pos:]]
                runpy.run_path(str(args[pos]), run_name="__main__")
    except BaseException as exc:
        status = 1
        errors.write(f"{type(exc).__name__}: {exc}")
    finally:
        os.chdir(old_cwd)
        sys.argv, sys.path[:], sys.stdin = old_argv, old_path, old_stdin
        # Project modules must not leak into later exercises.
        for name in set(sys.modules) - previous_modules:
            module_file = str(getattr(sys.modules[name], "__file__", ""))
            if "/data/tmp/" in module_file:
                del sys.modules[name]
    return types.SimpleNamespace(returncode=status, stdout=output.getvalue(), stderr=errors.getvalue())


app.subprocess.run = browser_process
app.lab_python = lambda: Path(sys.executable)
app.lab_environment_ready = lambda: True
app.lab_install_command = lambda package: "Paquetes preparados en tu navegador al abrir el laboratorio."
app.setup_lab_environment = lambda: {"ready": True, "message": "Bibliotecas preparadas en este navegador."}
app.init_db()


def dispatch(path, payload):
    if path == "/api/state":
        return dict(lessons=app.public_lessons(), guide=app.public_guide(), catalog=app.public_catalog(),
                    progress=app.progress_data(), labs=app.public_labs(), lab_progress=app.lab_progress_data(),
                    lab_environment_ready=True, advanced=app.public_advanced(),
                    advanced_progress=app.advanced_progress_data(), advanced_drafts=app.advanced_drafts_data())
    if path.startswith("/api/advanced/"):
        result = app.save_advanced_draft(payload["item_id"], payload["files"])
        return result if path.endswith("/save") else app.execute_advanced(payload["item_id"], payload["files"], path.endswith("/check"))
    if path == "/api/labs/setup":
        return app.setup_lab_environment()
    if path == "/api/labs/status":
        return app.lab_package_status(payload["lab_id"])
    if path == "/api/labs/diagnose":
        return app.diagnose_lab_install(payload["lab_id"], payload.get("output", ""))
    if path.startswith("/api/labs/"):
        return app.execute_lab(payload["lab_id"], payload.get("code", ""), path.endswith("/check"))
    if path == "/api/check":
        return app.check_lesson(payload["lesson_id"], payload.get("code", ""))
    if path == "/api/run":
        return app.execute(payload.get("code", ""), payload.get("input", ""), app.LESSON_BY_ID[payload["lesson_id"]].get("preview_suffix", ""))
    raise ValueError("Ruta desconocida")
