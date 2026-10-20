"""Ejecuta un caso del taller de proyectos en una carpeta temporal aislada."""

import contextlib
import io
import json
import logging
from pathlib import Path
import runpy
import sqlite3
import sys
import traceback


def main():
    payload = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    folder = Path.cwd()
    for name, content in payload["files"].items():
        (folder / name).write_text(content, encoding="utf-8")
    for name, content in payload.get("seed_files", {}).items():
        (folder / name).write_text(content, encoding="utf-8")
    if payload.get("harness"):
        (folder / "__prueba__.py").write_text(payload["harness"], encoding="utf-8")
    sys.path.insert(0, str(folder))
    sys.argv = ["__prueba__.py" if payload.get("harness") else "main.py", *payload.get("argv", [])]
    sys.stdin = io.StringIO(payload.get("stdin", ""))
    output = io.StringIO()
    error = ""
    try:
        with contextlib.redirect_stdout(output), contextlib.redirect_stderr(output):
            runpy.run_path(str(folder / sys.argv[0]), run_name="__main__")
    except BaseException:
        error = traceback.format_exc(limit=5)
    logging.shutdown()
    generated = {}
    for name in payload.get("expected_file_names", []):
        target = folder / name
        if target.is_file():
            try:
                generated[name] = target.read_text(encoding="utf-8")
            except (UnicodeError, OSError):
                generated[name] = None
    databases = {}
    for name, query in payload.get("db_checks", {}).items():
        target = folder / name
        if target.is_file():
            try:
                with sqlite3.connect(target) as connection:
                    databases[name] = connection.execute(query).fetchall()
            except sqlite3.Error:
                databases[name] = None
    print(json.dumps({"stdout": output.getvalue()[-16000:], "error": error[-4000:], "files": generated, "databases": databases}, ensure_ascii=True))


if __name__ == "__main__":
    main()
