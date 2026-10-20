"""Ejecutor separado para los retos de bibliotecas (uso local, no sandbox de seguridad)."""

import contextlib
import io
import json
import sys


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    with open(sys.argv[1], encoding="utf-8") as source:
        payload = json.load(source)
    output = io.StringIO()
    safe_builtins = {
        "__import__": __import__,
        "str": str, "int": int, "float": float, "bool": bool,
        "len": len, "range": range, "sum": sum, "abs": abs,
        "min": min, "max": max, "round": round, "list": list,
        "dict": dict, "tuple": tuple, "set": set, "enumerate": enumerate,
        "zip": zip, "sorted": sorted, "any": any, "all": all,
    }
    try:
        namespace = {"__builtins__": safe_builtins, "__name__": "tu_codigo"}
        with contextlib.redirect_stdout(output):
            exec(compile(payload["code"], "tu_codigo.py", "exec"), namespace)
            solve = namespace["solve"]
            results = []
            for args in payload["cases"]:
                try:
                    value = solve(*args)
                    serialized = json.dumps(value, ensure_ascii=False, allow_nan=False)
                    results.append({"ok": True, "value": json.loads(serialized)})
                except BaseException as exc:
                    results.append({"ok": False, "error": f"{type(exc).__name__}: {exc}"[:400]})
        result = {"ok": True, "results": results}
    except BaseException as exc:
        result = {"ok": False, "error": f"{type(exc).__name__}: {exc}"[:400]}
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
