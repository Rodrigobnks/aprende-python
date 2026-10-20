"""Public deployment: Streamlit serves the UI; Python runs in each browser."""
import json
from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

ROOT = Path(__file__).resolve().parent
st.set_page_config(page_title="Aprende Python", page_icon="🐍", layout="wide")
st.markdown("<style>.block-container{padding:0;max-width:100%}header{visibility:hidden}</style>", unsafe_allow_html=True)

@st.cache_data
def build_html():
    sources = {p.name: p.read_text(encoding="utf-8") for p in ROOT.glob("*.py")
               if p.name not in {"streamlit_app.py", "browser_backend.py"}}
    # The browser needs the teaching functions, never the local HTTP server.
    sources["app.py"] = sources["app.py"].split("class Handler(")[0].replace(
        "from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer", "")
    for name in ("runner.py", "lab_runner.py"):
        sources[name] = sources[name].replace('    sys.stdout.reconfigure(encoding="utf-8")', '')
    worker = (ROOT / "browser_worker.js").read_text(encoding="utf-8")
    bridge = (ROOT / "browser_bridge.js").read_text(encoding="utf-8")
    boot = "const PY_SOURCES=" + json.dumps(sources, ensure_ascii=True) + ";\n"
    boot += "const PY_BACKEND=" + json.dumps((ROOT / "browser_backend.py").read_text(encoding="utf-8")) + ";\n"
    boot += "const WORKER_SOURCE=" + json.dumps(worker) + ";\n" + bridge
    html = (ROOT / "index.html").read_text(encoding="utf-8")
    html = html.replace('<link rel="stylesheet" href="/styles.css">', '<style>' + (ROOT / "styles.css").read_text(encoding="utf-8") + '</style>')
    html = html.replace("Tu espacio local", "Tu espacio personal en línea")
    script = boot + "\n" + (ROOT / "app.js").read_text(encoding="utf-8")
    return html.replace('<script src="/app.js" defer></script>', '<script>' + script.replace('</script', '<\\/script') + '</script>')

components.html(build_html(), height=1100, scrolling=True)
