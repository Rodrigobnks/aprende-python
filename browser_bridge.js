// The app's HTTP calls stay inside this visitor's browser.
let pythonWorker, requestNumber = 0, queue = Promise.resolve();
const pending = new Map();
const DB_KEY = 'aprende-python:cloud-db:v1';
function createWorker() {
  const url = URL.createObjectURL(new Blob([WORKER_SOURCE], {type:'text/javascript'}));
  pythonWorker = new Worker(url); URL.revokeObjectURL(url);
  pythonWorker.onmessage = ({data}) => {
    const task = pending.get(data.id); if (!task) return;
    clearTimeout(task.timer); pending.delete(data.id);
    if (data.database) { try { localStorage.setItem(DB_KEY, data.database); } catch (_) {} }
    data.error ? task.reject(new Error(data.error)) : task.resolve({ok:true, json:async () => data.result});
  };
  pythonWorker.onerror = () => resetWorker('No se pudo cargar Python. Comprueba tu conexión y vuelve a intentarlo.');
}
function resetWorker(message) {
  if (pythonWorker) pythonWorker.terminate(); pythonWorker = null;
  for (const task of pending.values()) {clearTimeout(task.timer); task.reject(new Error(message));}
  pending.clear();
}
const originalFetch = window.fetch.bind(window);
window.fetch = (path, options={}) => {
  if (typeof path !== 'string' || !path.startsWith('/api/')) return originalFetch(path, options);
  const request = () => new Promise((resolve, reject) => {
    const cold = !pythonWorker; if (cold) createWorker();
    const id = ++requestNumber;
    const timer = setTimeout(() => resetWorker('La operación tardó demasiado. Puedes volver a intentarlo; tu progreso guardado se conserva.'), cold || path.startsWith('/api/labs/') ? 180000 : 10000);
    pending.set(id, {resolve,reject,timer});
    let database; try { database = localStorage.getItem(DB_KEY); } catch (_) {}
    pythonWorker.postMessage({id,path,payload:JSON.parse(options.body || '{}'), ...(cold ? {sources:PY_SOURCES,backend:PY_BACKEND,database} : {})});
  });
  const result = queue.then(request); queue = result.catch(() => {}); return result;
};
window.addEventListener('DOMContentLoaded', () => {
  const tools = document.createElement('div');
  tools.style.cssText = 'padding:12px;display:flex;gap:12px;align-items:center;flex-wrap:wrap;background:#edf4f7';
  tools.innerHTML = '<span>Progreso personal en este navegador</span><button id="exportCloud">Descargar respaldo</button><label>Restaurar respaldo <input id="importCloud" type="file" accept=".json"></label>';
  document.body.prepend(tools);
  document.getElementById('exportCloud').onclick = () => {
    const items = {}; for(let i=0;i<localStorage.length;i++){const k=localStorage.key(i);if(k.startsWith('aprende-python:'))items[k]=localStorage.getItem(k);}
    const url = URL.createObjectURL(new Blob([JSON.stringify({version:1,items})],{type:'application/json'}));
    const a = document.createElement('a');a.href=url;a.download='mi-progreso-python.json';a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);
  };
  document.getElementById('importCloud').onchange = async event => {
    try {
      const file = event.target.files[0]; if(!file || file.size>5000000)throw Error('Archivo demasiado grande.');
      const backup = JSON.parse(await file.text());if(backup.version!==1 || !backup.items)throw Error('Respaldo no válido.');
      for(const [k,v] of Object.entries(backup.items)){if(!k.startsWith('aprende-python:') || typeof v!=='string')throw Error('Respaldo no válido.');}
      if(!confirm('¿Restaurar el respaldo? Reemplazará las entradas incluidas del progreso de este navegador.'))return;
      for(const [k,v] of Object.entries(backup.items))localStorage.setItem(k,v);
      location.reload();
    } catch(error){alert(error.message);}
  };
});
