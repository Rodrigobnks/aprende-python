const CDN = 'https://cdn.jsdelivr.net/pyodide/v0.28.3/full/';
let py, initialized, labsReady = false;
async function initialize(data) {
  importScripts(CDN + 'pyodide.js');
  py = await loadPyodide({indexURL: CDN});
  await py.loadPackage('sqlite3');
  py.FS.mkdirTree('/home/pyodide/course/data');
  for (const [name, source] of Object.entries(data.sources)) py.FS.writeFile('/home/pyodide/course/' + name, source);
  if (data.database) py.FS.writeFile('/home/pyodide/course/data/progreso.db', Uint8Array.from(atob(data.database), c => c.charCodeAt(0)));
  py.FS.writeFile('/home/pyodide/course/browser_backend.py', data.backend);
  await py.runPythonAsync("import sys, os, json\nos.chdir('/home/pyodide/course')\nsys.path.insert(0, os.getcwd())\nfrom browser_backend import dispatch\n");
}
self.onmessage = async ({data}) => {
  try {
    if (!initialized) initialized = initialize(data);
    await initialized;
    if (data.path.startsWith('/api/labs/') && !labsReady) {
      await py.loadPackage(['micropip', 'numpy', 'pandas', 'pillow', 'pyyaml', 'packaging', 'python-dateutil']);
      await py.runPythonAsync("import micropip\nawait micropip.install(['requests', 'rich'])");
      labsReady = true;
    }
    py.globals.set('_request_json', JSON.stringify(data.payload || {}));
    py.globals.set('_request_path', data.path);
    const result = await py.runPythonAsync("json.dumps(dispatch(_request_path, json.loads(_request_json)), ensure_ascii=True)");
    const bytes = py.FS.readFile('/home/pyodide/course/data/progreso.db');
    let binary = ''; for (const byte of bytes) binary += String.fromCharCode(byte);
    self.postMessage({id: data.id, result: JSON.parse(result), database: btoa(binary)});
  } catch (error) { self.postMessage({id: data.id, error: String(error)}); }
};
