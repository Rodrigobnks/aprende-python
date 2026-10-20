"""Execute the beginner subset in a short-lived, separate Python process."""

import io
import json
import sys


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    with open(sys.argv[1], encoding="utf-8") as payload_file:
        payload = json.load(payload_file)

    output = io.StringIO()
    lines = iter(payload.get("input", "").splitlines())

    def limited_print(*values, sep=" ", end="\n"):
        value = sep.join(str(item) for item in values) + end
        if output.tell() + len(value) > 4000:
            raise RuntimeError("La salida superó el límite de 4000 caracteres")
        output.write(value)

    def limited_input(prompt=""):
        if prompt:
            limited_print(prompt, end="")
        try:
            return next(lines)
        except StopIteration:
            raise EOFError("No hay más datos de entrada") from None

    safe_builtins = {
        "print": limited_print, "input": limited_input,
        "str": str, "int": int, "float": float, "bool": bool,
        "len": len, "range": range, "sum": sum, "abs": abs,
        "min": min, "max": max, "round": round, "list": list, "dict": dict,
        "tuple": tuple, "set": set, "enumerate": enumerate,
    }

    try:
        exec(compile(payload["code"], "tu_codigo.py", "exec"), {"__builtins__": safe_builtins})
        result = {"stdout": output.getvalue(), "error": "", "ok": True}
    except BaseException as exc:
        result = {
            "stdout": output.getvalue(),
            "error": f"{type(exc).__name__}: {exc}",
            "ok": False,
        }
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
