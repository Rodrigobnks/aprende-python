const $ = (id) => document.getElementById(id);
let lessons = [];
let guide = [];
let catalog = { categories: [], libraries: [] };
let progress = { lessons: {}, completed: 0, total: 100 };
let labs = [];
let labProgress = { labs: {}, completed: 0, total: 17 };
let labIndex = 0;
let labEnvironmentReady = false;
let labHintLevel = 0;
let advanced = [];
let advancedProgress = { items: {}, completed: 0, total: 21 };
let advancedDrafts = {};
let advancedIndex = 0;
let advancedFiles = null;
let advancedFileName = 'main.py';
let advancedHintLevel = 0;
let advancedSaveTimer = null;
let advancedSaveQueue = Promise.resolve();
let lessonHintLevel = 0;
let currentIndex = 0;
let chapterIndex = 0;
let catalogCategory = 'all';
let activeView = 'guide';
let busy = false;
const chapterByUnit = { 1: 'que-es-python', 2: 'numeros', 3: 'cadenas', 4: 'entrada-salida', 5: 'condiciones', 6: 'bucles', 7: 'listas-tuplas', 8: 'diccionarios-conjuntos', 9: 'funciones', 10: 'proyecto' };

function escapeHtml(value) {
  return String(value).replace(/[&<>"']/g, (character) => ({
    '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'
  })[character]);
}

function draftKey(lesson) { return `aprende-python:draft:${lesson.id}`; }

function inlineText(value) {
  return escapeHtml(value).replace(/`([^`]+)`/g, '<code>$1</code>').replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');
}

function setView(view) {
  activeView = view;
  $('guideView').hidden = view !== 'guide';
  $('catalogView').hidden = view !== 'catalog';
  $('exerciseView').hidden = view !== 'practice';
  $('labView').hidden = view !== 'lab';
  $('advancedView').hidden = view !== 'advanced';
  $('guideSidebar').hidden = view !== 'guide';
  $('catalogSidebar').hidden = view !== 'catalog';
  $('practiceSidebar').hidden = view !== 'practice';
  $('labSidebar').hidden = view !== 'lab';
  $('advancedSidebar').hidden = view !== 'advanced';
  $('guideTab').classList.toggle('active', view === 'guide');
  $('catalogTab').classList.toggle('active', view === 'catalog');
  $('practiceTab').classList.toggle('active', view === 'practice');
  $('labTab').classList.toggle('active', view === 'lab');
  $('advancedTab').classList.toggle('active', view === 'advanced');
  $('guideTab').setAttribute('aria-pressed', String(view === 'guide'));
  $('catalogTab').setAttribute('aria-pressed', String(view === 'catalog'));
  $('practiceTab').setAttribute('aria-pressed', String(view === 'practice'));
  $('labTab').setAttribute('aria-pressed', String(view === 'lab'));
  $('advancedTab').setAttribute('aria-pressed', String(view === 'advanced'));
  localStorage.setItem('aprende-python:view', view);
  $('breadcrumbUnit').textContent = view === 'guide' ? guide[chapterIndex]?.title.toUpperCase() ?? 'MANUAL' : view === 'catalog' ? 'BIBLIOTECAS' : view === 'lab' ? 'LABORATORIO' : view === 'advanced' ? 'PROYECTOS' : lessons[currentIndex]?.unit_title.toUpperCase() ?? 'EJERCICIOS';
}

function advancedWorkspace(item) { return item?.workspace_id; }

function storeAdvancedEditor() {
  if (advancedFiles && advancedFileName) advancedFiles[advancedFileName] = $('advancedEditor').value;
}

function saveAdvancedCurrent() {
  const item = advanced[advancedIndex];
  if (!item || !advancedFiles) return advancedSaveQueue;
  storeAdvancedEditor();
  const files = { ...advancedFiles };
  const key = advancedWorkspace(item);
  advancedDrafts[key] = files;
  $('advancedSaveStatus').textContent = 'Guardando...';
  advancedSaveQueue = advancedSaveQueue.catch(() => {}).then(() => post('/api/advanced/save', { item_id: item.id, files }));
  advancedSaveQueue.then(() => {
    if (advancedWorkspace(advanced[advancedIndex]) === key) $('advancedSaveStatus').textContent = 'Guardado local';
  }).catch((error) => {
    if (advancedWorkspace(advanced[advancedIndex]) === key) $('advancedSaveStatus').textContent = `Error al guardar: ${error.message}`;
  });
  return advancedSaveQueue;
}

function queueAdvancedSave() {
  clearTimeout(advancedSaveTimer);
  $('advancedSaveStatus').textContent = 'Cambios sin guardar';
  advancedSaveTimer = setTimeout(() => saveAdvancedCurrent(), 700);
}

function renderAdvancedNav() {
  $('advancedProgressLabel').textContent = `${advancedProgress.completed}/${advancedProgress.total} etapas completadas`;
  $('advancedNav').innerHTML = advanced.map((item, index) => {
    const done = !!advancedProgress.items[item.id]?.completed_at;
    const heading = index === 0 ? '<div class="lab-nav-heading">12 RETOS INTERMEDIOS</div>'
      : index === 12 || (item.project_id && advanced[index - 1]?.project_id !== item.project_id)
        ? `<div class="lab-nav-heading">${escapeHtml(item.project_title.toUpperCase())}</div>` : '';
    return `${heading}<button class="nav-item ${index === advancedIndex ? 'active' : ''} ${done ? 'completed' : ''}" type="button" data-advanced="${index}" ${index === advancedIndex ? 'aria-current="step"' : ''}><span class="nav-number">${item.project_id ? item.stage : String(index + 1).padStart(2, '0')}</span><span>${escapeHtml(item.title)}</span>${done ? '<span class="nav-check">✓</span>' : ''}</button>`;
  }).join('');
  $('advancedNav').querySelectorAll('button').forEach((button) => button.addEventListener('click', () => showAdvanced(Number(button.dataset.advanced))));
}

function renderAdvancedFiles() {
  $('advancedFiles').innerHTML = Object.keys(advancedFiles).map((name) => `<button class="advanced-file ${name === advancedFileName ? 'active' : ''}" role="tab" type="button" aria-selected="${name === advancedFileName}" data-file="${escapeHtml(name)}">${escapeHtml(name)}</button>`).join('');
  $('advancedFiles').querySelectorAll('button').forEach((button) => button.addEventListener('click', () => {
    storeAdvancedEditor();
    advancedFileName = button.dataset.file;
    $('advancedEditor').value = advancedFiles[advancedFileName];
    renderAdvancedFiles();
    $('advancedEditor').focus();
  }));
}

function showAdvanced(index) {
  if (index < 0 || index >= advanced.length) return;
  const previous = advanced[advancedIndex];
  const next = advanced[index];
  if (advancedFiles) {
    storeAdvancedEditor();
    if (advancedWorkspace(previous) !== advancedWorkspace(next)) {
      clearTimeout(advancedSaveTimer);
      saveAdvancedCurrent();
    }
  }
  if (!advancedFiles || advancedWorkspace(previous) !== advancedWorkspace(next)) {
    advancedFiles = { ...(advancedDrafts[advancedWorkspace(next)] || next.starter_files) };
    advancedFileName = 'main.py';
  }
  advancedIndex = index;
  $('advancedNumber').textContent = next.project_id ? `${next.project_title.toUpperCase()} · ETAPA ${next.stage} DE 3` : `RETO INTERMEDIO ${index + 1} DE 12`;
  $('advancedTitle').textContent = next.title;
  $('advancedTopic').textContent = next.topic;
  $('advancedGoal').textContent = next.goal;
  const sample = next.sample;
  $('advancedSampleInput').textContent = [sample.stdin !== undefined ? `Entrada:\n${sample.stdin || '(vacía)'}` : '', sample.argv ? `Argumentos: ${sample.argv.join(' ')}` : '', sample.files ? `Archivos de datos:\n${Object.entries(sample.files).map(([name, content]) => `${name}:\n${content}`).join('\n')}` : ''].filter(Boolean).join('\n');
  $('advancedSampleOutput').textContent = `Consola: ${sample.expected_stdout || '(sin salida)'}${sample.expected_files ? `\nArchivos esperados:\n${JSON.stringify(sample.expected_files, null, 2)}` : ''}${sample.expected_db ? `\nFilas esperadas en SQLite:\n${JSON.stringify(sample.expected_db, null, 2)}` : ''}`;
  advancedHintLevel = 0;
  $('advancedHint').hidden = true;
  $('advancedHintButton').disabled = false;
  $('advancedHintButton').textContent = 'Ver pista 1 de 3 ↓';
  $('advancedHintButton').setAttribute('aria-expanded', 'false');
  $('advancedEditor').value = advancedFiles[advancedFileName] || '';
  $('advancedSaveStatus').textContent = 'Guardado local';
  $('advancedConsole').textContent = 'Aquí aparecerá la salida del programa.';
  $('advancedRunStatus').textContent = 'Listo';
  $('advancedDiagnosis').hidden = true;
  $('advancedFeedback').hidden = true;
  renderAdvancedFiles();
  renderAdvancedNav();
  setView('advanced');
  $('advancedView').scrollIntoView({ behavior: 'smooth', block: 'start' });
}

async function runAdvanced(check) {
  if (busy || !advanced[advancedIndex]) return;
  const item = advanced[advancedIndex];
  clearTimeout(advancedSaveTimer);
  storeAdvancedEditor();
  const files = { ...advancedFiles };
  busy = true;
  $('advancedRunButton').disabled = true;
  $('advancedCheckButton').disabled = true;
  $('advancedRunStatus').textContent = 'Ejecutando...';
  $('advancedFeedback').hidden = true;
  try {
    await saveAdvancedCurrent();
    const result = await post(check ? '/api/advanced/check' : '/api/advanced/run', { item_id: item.id, files });
    if (advanced[advancedIndex]?.id !== item.id) return;
    if (check && result.progress) {
      advancedProgress = result.progress;
      renderAdvancedNav();
    }
    $('advancedRunStatus').textContent = result.passed ? 'Correcto' : 'Revisa tu código';
    $('advancedConsole').textContent = result.message
      + (result.case_input ? `\nDatos de la prueba: ${JSON.stringify(result.case_input, null, 2)}` : '')
      + (result.expected !== undefined ? `\nEsperado: ${JSON.stringify(result.expected)}\nObtenido: ${JSON.stringify(result.received)}` : '')
      + (result.error ? `\n${result.error}` : '');
    $('advancedDiagnosis').hidden = !result.diagnosis;
    $('advancedDiagnosisText').textContent = result.diagnosis || '';
    $('advancedFeedback').hidden = !check;
    $('advancedFeedback').classList.toggle('fail', !result.passed);
    $('advancedFeedbackTitle').textContent = result.passed ? '¡Etapa superada!' : 'Sigue intentándolo';
    $('advancedFeedbackMessage').textContent = result.message;
    $('advancedNextButton').hidden = !result.passed || advancedIndex === advanced.length - 1;
  } catch (error) {
    $('advancedRunStatus').textContent = 'Error';
    $('advancedConsole').textContent = error.message;
  } finally {
    busy = false;
    $('advancedRunButton').disabled = false;
    $('advancedCheckButton').disabled = false;
  }
}

function renderLabNav() {
  $('labProgressLabel').textContent = `${labProgress.completed}/${labProgress.total} completados`;
  $('labNav').innerHTML = labs.map((lab, index) => {
    const done = !!labProgress.labs[lab.id]?.completed_at;
    const heading = index === 0 ? '<div class="lab-nav-heading">RETOS GUIADOS</div>' : lab.kind === 'project' && labs[index - 1]?.kind !== 'project' ? '<div class="lab-nav-heading">PROYECTOS INTEGRADORES</div>' : '';
    return `${heading}<button class="nav-item ${index === labIndex ? 'active' : ''} ${done ? 'completed' : ''}" type="button" data-lab="${index}" ${index === labIndex ? 'aria-current="step"' : ''}><span class="nav-number">${String(index + 1).padStart(2, '0')}</span><span>${escapeHtml(lab.title)}</span>${done ? '<span class="nav-check">✓</span>' : ''}</button>`;
  }).join('');
  $('labNav').querySelectorAll('button').forEach((button) => button.addEventListener('click', () => showLab(Number(button.dataset.lab))));
}

async function refreshLabStatus() {
  const lab = labs[labIndex];
  if (!lab) return;
  $('labInstallStatus').textContent = 'Comprobando instalación...';
  try {
    const status = await post('/api/labs/status', { lab_id: lab.id });
    if (labs[labIndex]?.id !== lab.id) return;
    labEnvironmentReady = status.ready;
    $('labEnvironmentStatus').textContent = status.ready ? 'Entorno listo para instalar bibliotecas.' : 'Primero prepara el entorno.';
    $('labSetupButton').hidden = status.ready;
    $('labInstallCommand').textContent = status.command;
    $('labInstallStatus').textContent = status.message;
    $('labInstallStatus').classList.toggle('installed', status.installed);
  } catch (error) {
    $('labInstallStatus').textContent = error.message;
  }
}

function showLab(index) {
  if (index < 0 || index >= labs.length) return;
  labIndex = index;
  const lab = labs[index];
  $('labNumber').textContent = lab.kind === 'project' ? `PROYECTO ${index - 13} DE 3` : `RETO ${String(index + 1).padStart(2, '0')} DE 14`;
  $('labTitle').textContent = lab.title;
  $('labPackage').textContent = `Instalar: ${lab.packages.join(' + ')} · Importar: ${lab.import_roots.join(' + ')}`;
  $('labConcept').textContent = lab.concept;
  $('labTask').textContent = lab.task;
  $('labSampleInput').textContent = JSON.stringify(lab.sample.args, null, 2);
  $('labSampleOutput').textContent = JSON.stringify(lab.sample.expected, null, 2);
  labHintLevel = 0;
  $('labHint').hidden = true;
  $('labHintButton').disabled = false;
  $('labHintButton').textContent = 'Ver pista 1 de 3 ↓';
  $('labHintButton').setAttribute('aria-expanded', 'false');
  $('labCodeEditor').value = localStorage.getItem(`aprende-python:lab:${lab.id}`) ?? lab.starter;
  $('labConsole').textContent = 'Aquí aparecerá el resultado.';
  $('labRunStatus').textContent = 'Listo';
  $('labFeedback').hidden = true;
  $('labDiagnosis').hidden = true;
  $('labErrorInput').value = '';
  $('labErrorDiagnosis').textContent = '';
  renderLabNav();
  setView('lab');
  refreshLabStatus();
  $('labView').scrollIntoView({ behavior: 'smooth', block: 'start' });
}

async function runLab(check) {
  if (busy) return;
  const lab = labs[labIndex];
  const code = $('labCodeEditor').value;
  localStorage.setItem(`aprende-python:lab:${lab.id}`, code);
  busy = true;
  $('labRunButton').disabled = true;
  $('labCheckButton').disabled = true;
  $('labRunStatus').textContent = 'Ejecutando...';
  $('labFeedback').hidden = true;
  try {
    const result = await post(check ? '/api/labs/check' : '/api/labs/run', { lab_id: lab.id, code });
    if (check && result.progress) {
      labProgress = result.progress;
      renderLabNav();
    }
    $('labRunStatus').textContent = result.passed ? 'Correcto' : 'Revisa tu código';
    $('labConsole').textContent = result.message + (result.case_input !== undefined ? `\nEntrada: ${JSON.stringify(result.case_input)}` : '') + (result.expected !== undefined ? `\nEsperado: ${JSON.stringify(result.expected)}\nObtenido: ${JSON.stringify(result.received)}` : '');
    $('labDiagnosis').hidden = !result.diagnosis;
    $('labDiagnosisText').textContent = result.diagnosis || '';
    $('labFeedback').hidden = !check;
    $('labFeedback').classList.toggle('fail', !result.passed);
    $('labFeedbackTitle').textContent = result.passed ? '¡Reto superado!' : 'Sigue intentándolo';
    $('labFeedbackMessage').textContent = result.message;
    $('labNextButton').hidden = !result.passed || labIndex === labs.length - 1;
  } catch (error) {
    $('labRunStatus').textContent = 'Error';
    $('labConsole').textContent = error.message;
  } finally {
    busy = false;
    $('labRunButton').disabled = false;
    $('labCheckButton').disabled = false;
  }
}

function renderGuideNav() {
  $('guideNav').innerHTML = guide.map((chapter, index) => `<button class="nav-item ${index === chapterIndex ? 'active' : ''}" type="button" data-chapter="${index}" ${index === chapterIndex ? 'aria-current="page"' : ''}><span class="nav-number">${String(index + 1).padStart(2, '0')}</span><span>${escapeHtml(chapter.title)}</span></button>`).join('');
  $('guideNav').querySelectorAll('button').forEach((button) => button.addEventListener('click', () => showChapter(Number(button.dataset.chapter))));
}

function normalizeSearch(value) {
  return String(value).normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
}

function renderCatalogNav() {
  const all = `<button class="nav-item ${catalogCategory === 'all' ? 'active' : ''}" type="button" data-category="all"><span class="nav-number">✳</span><span>Todos los temas</span><small>${catalog.libraries.length}</small></button>`;
  $('catalogNav').innerHTML = all + catalog.categories.map((category, index) => {
    const count = catalog.libraries.filter((entry) => entry.category === category.id).length;
    return `<button class="nav-item ${catalogCategory === category.id ? 'active' : ''}" type="button" data-category="${escapeHtml(category.id)}"><span class="nav-number">${String(index + 1).padStart(2, '0')}</span><span>${escapeHtml(category.title)}</span><small>${count}</small></button>`;
  }).join('');
  $('catalogNav').querySelectorAll('button').forEach((button) => button.addEventListener('click', () => {
    catalogCategory = button.dataset.category;
    $('catalogCategory').value = catalogCategory;
    renderCatalog();
    setView('catalog');
  }));
}

function renderCatalog() {
  const query = normalizeSearch($('catalogSearch').value.trim());
  const kind = $('catalogKind').value;
  const categoryNames = new Map(catalog.categories.map((category) => [category.id, category.title]));
  const visible = catalog.libraries.filter((entry) => {
    if (catalogCategory !== 'all' && entry.category !== catalogCategory) return false;
    if (kind !== 'all' && entry.kind !== kind) return false;
    const searchable = [entry.name, entry.purpose, categoryNames.get(entry.category), entry.import_code, ...entry.apis.flatMap((api) => [api.name, api.purpose])].join(' ');
    return normalizeSearch(searchable).includes(query);
  });
  $('catalogCount').textContent = `${visible.length} de ${catalog.libraries.length} bibliotecas`;
  $('catalogEmpty').hidden = visible.length !== 0;
  $('catalogGrid').innerHTML = visible.map((entry) => `<article class="library-card"><div class="library-card-top"><div><h3>${escapeHtml(entry.name)}</h3><div class="library-topic">${escapeHtml(categoryNames.get(entry.category) || '')}</div></div><span class="library-kind ${entry.kind === 'external' ? 'external' : ''}">${entry.kind === 'external' ? 'Paquete externo' : 'Estándar'}</span></div><p class="library-purpose">${escapeHtml(entry.purpose)}</p>${entry.install ? `<div class="library-install"><span>INSTALAR</span><code>python -m pip install ${escapeHtml(entry.install)}</code></div>` : ''}<div class="library-import"><span>IMPORTAR</span><code>${escapeHtml(entry.import_code)}</code></div><div class="library-apis"><strong>FUNCIONES Y ELEMENTOS CLAVE</strong>${entry.apis.map((api) => `<div class="library-api"><code>${escapeHtml(api.name)}</code><span>${escapeHtml(api.purpose)}</span></div>`).join('')}</div>${entry.example ? `<pre class="library-example"><code>${escapeHtml(entry.example)}</code></pre>` : ''}<a class="library-docs" href="${escapeHtml(entry.url)}" target="_blank" rel="noopener noreferrer">Documentación oficial ↗</a></article>`).join('');
  renderCatalogNav();
}

function showChapter(index) {
  if (index < 0 || index >= guide.length) return;
  chapterIndex = index;
  const chapter = guide[index];
  $('chapterNumber').textContent = `CAPÍTULO ${String(index + 1).padStart(2, '0')} DE ${guide.length}`;
  $('guideTitle').textContent = chapter.title;
  $('guideSubtitle').textContent = chapter.subtitle;
  $('guideSections').innerHTML = chapter.sections.map((section) => `<article class="guide-section"><h3>${escapeHtml(section.title)}</h3>${section.paragraphs.map((paragraph) => `<p>${inlineText(paragraph)}</p>`).join('')}${section.code ? `<pre><code>${escapeHtml(section.code)}</code></pre>` : ''}${section.note ? `<div class="guide-note">${inlineText(section.note)}</div>` : ''}</article>`).join('');
  $('guideTakeaways').innerHTML = chapter.takeaways.map((item) => `<li>${inlineText(item)}</li>`).join('');
  $('guideSources').innerHTML = chapter.sources.map((source) => `<a href="${escapeHtml(source.url)}" target="_blank" rel="noopener noreferrer">${escapeHtml(source.label)} ↗</a>`).join('') || '<span>Aplica estas ideas en los ejercicios.</span>';
  $('previousChapter').disabled = index === 0;
  $('nextChapter').disabled = index === guide.length - 1;
  const related = lessons.filter((lesson) => lesson.unit === chapter.unit);
  $('practiceUnit').hidden = !chapter.advanced_id && related.length === 0;
  $('practiceUnit').textContent = chapter.advanced_id ? 'Abrir reto relacionado →' : `Practicar bloque ${chapter.unit} →`;
  renderGuideNav();
  setView('guide');
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

function renderProgress() {
  $('progressCount').textContent = progress.completed;
  $('progressTotal').textContent = progress.total;
  $('progressBar').style.width = `${Math.round((progress.completed / progress.total) * 100)}%`;
  $('progressNote').textContent = progress.completed === progress.total
    ? '¡Terminaste esta primera ruta!'
    : progress.completed === 0 ? 'Tu camino comienza aquí.' : 'Un paso más en cada lección.';
  const groups = new Map();
  lessons.forEach((lesson, index) => {
    if (!groups.has(lesson.unit)) groups.set(lesson.unit, []);
    groups.get(lesson.unit).push({ lesson, index });
  });
  $('lessonNav').innerHTML = [...groups].map(([unit, items]) => {
    const completed = items.filter(({ lesson }) => progress.lessons[lesson.id]?.completed_at).length;
    const buttons = items.map(({ lesson, index }) => {
      const done = !!progress.lessons[lesson.id]?.completed_at;
      return `<button class="nav-item ${index === currentIndex ? 'active' : ''} ${done ? 'completed' : ''}" type="button" data-index="${index}" ${index === currentIndex ? 'aria-current="step"' : ''}><span class="nav-number">${String(lesson.number).padStart(2, '0')}</span><span>${escapeHtml(lesson.title)}</span>${done ? '<span class="nav-check">✓</span>' : ''}</button>`;
    }).join('');
    return `<details class="unit-group" ${lessons[currentIndex]?.unit === unit ? 'open' : ''}><summary><span class="unit-index">${String(unit).padStart(2, '0')}</span><span class="unit-name">${escapeHtml(items[0].lesson.unit_title)}</span><small>${completed}/${items.length}</small></summary><div class="unit-exercises">${buttons}</div></details>`;
  }).join('');
  $('lessonNav').querySelectorAll('.nav-item').forEach((button) => {
    button.addEventListener('click', () => showLesson(Number(button.dataset.index)));
  });
}

function showLesson(index) {
  if (index < 0 || index >= lessons.length) return;
  currentIndex = index;
  const lesson = lessons[index];
  $('breadcrumbUnit').textContent = lesson.unit_title.toUpperCase();
  $('exerciseNumber').textContent = `EJERCICIO ${String(lesson.number).padStart(2, '0')} DE ${lessons.length}`;
  $('lessonTitle').textContent = lesson.title;
  $('lessonSubtitle').textContent = `Bloque ${String(lesson.unit).padStart(2, '0')} · ${lesson.unit_title}`;
  $('lessonMinutes').textContent = lesson.minutes;
  $('lessonConcept').textContent = lesson.concept;
  $('lessonExample').textContent = lesson.example;
  $('lessonTask').textContent = lesson.task;
  $('sampleOutput').textContent = lesson.sample_output;
  lessonHintLevel = 0;
  $('hintText').hidden = true;
  $('hintButton').disabled = false;
  $('hintButton').textContent = 'Ver pista 1 de 3 ↓';
  $('hintButton').setAttribute('aria-expanded', 'false');
  $('codeEditor').value = localStorage.getItem(draftKey(lesson)) ?? lesson.starter;
  $('inputWrap').hidden = !lesson.sample_input;
  $('inputData').value = lesson.sample_input;
  $('consoleOutput').textContent = 'Tu resultado aparecerá aquí cuando ejecutes el código.';
  $('runStatus').textContent = 'Listo para ejecutar';
  $('feedback').hidden = true;
  $('exerciseDiagnosis').hidden = true;
  $('feedbackCompare').hidden = true;
  $('nextButton').hidden = true;
  renderProgress();
  if (activeView === 'practice') document.querySelector('.section-heading').scrollIntoView({ behavior: 'smooth', block: 'start' });
}

function setBusy(value) {
  busy = value;
  $('runButton').disabled = value;
  $('checkButton').disabled = value;
  if (value) $('runStatus').textContent = 'Ejecutando...';
}

async function post(path, body) {
  const response = await fetch(path, {
    method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body)
  });
  const result = await response.json();
  if (!response.ok) throw new Error(result.error || 'No se pudo completar la solicitud.');
  return result;
}

function showFeedback(result) {
  const box = $('feedback');
  box.hidden = false;
  box.classList.toggle('fail', !result.passed);
  $('feedbackTitle').textContent = result.passed ? '¡Lo lograste!' : 'Casi lo tienes';
  $('feedbackMessage').textContent = result.message + (result.case_input ? ` Entrada que falló: ${JSON.stringify(result.case_input)}.` : '');
  $('exerciseDiagnosis').hidden = !result.diagnosis;
  $('exerciseDiagnosisText').textContent = result.diagnosis || '';
  const compare = !result.passed && result.expected !== undefined;
  $('feedbackCompare').hidden = !compare;
  if (compare) {
    $('expectedOutput').textContent = result.expected ?? '(sin salida)';
    $('receivedOutput').textContent = result.received ?? '(sin salida)';
  }
  $('nextButton').hidden = !result.passed || currentIndex === lessons.length - 1;
}

async function runCode(check) {
  if (busy) return;
  const lesson = lessons[currentIndex];
  const code = $('codeEditor').value;
  localStorage.setItem(draftKey(lesson), code);
  setBusy(true);
  $('feedback').hidden = true;
  try {
    if (check) {
      const result = await post('/api/check', { lesson_id: lesson.id, code });
      progress = result.progress;
      renderProgress();
      showFeedback(result);
      $('runStatus').textContent = result.passed ? 'Todas las pruebas correctas' : 'Revisa el resultado';
      $('consoleOutput').textContent = result.passed ? 'Tu programa pasó todas las pruebas.' : result.message;
    } else {
      const result = await post('/api/run', {
        lesson_id: lesson.id, code, input: $('inputWrap').hidden ? '' : $('inputData').value
      });
      $('runStatus').textContent = result.ok ? 'Ejecución terminada' : 'Revisa tu código';
      $('consoleOutput').textContent = [result.stdout, result.error].filter(Boolean).join('\n') || '(el programa no produjo salida)';
      $('exerciseDiagnosis').hidden = !result.diagnosis;
      $('exerciseDiagnosisText').textContent = result.diagnosis || '';
    }
  } catch (error) {
    $('runStatus').textContent = 'Error de conexión';
    $('consoleOutput').textContent = error.message;
  } finally {
    setBusy(false);
  }
}

async function start() {
  try {
    const response = await fetch('/api/state');
    if (!response.ok) throw new Error('No se pudo cargar la plataforma.');
    const state = await response.json();
    const preferredView = localStorage.getItem('aprende-python:view');
    lessons = state.lessons;
    guide = state.guide;
    $('guideCountIcon').textContent = guide.length;
    $('guideCountText').textContent = guide.length;
    catalog = state.catalog;
    progress = state.progress;
    labs = state.labs;
    labProgress = state.lab_progress;
    advanced = state.advanced;
    advancedProgress = state.advanced_progress;
    advancedDrafts = state.advanced_drafts;
    labEnvironmentReady = state.lab_environment_ready;
    $('labEnvironmentStatus').textContent = labEnvironmentReady ? 'Entorno listo para instalar bibliotecas.' : 'Primero prepara el entorno.';
    $('labSetupButton').hidden = labEnvironmentReady;
    renderLabNav();
    renderAdvancedNav();
    $('catalogTotal').textContent = catalog.libraries.length;
    $('catalogCategory').innerHTML = '<option value="all">Todos los temas</option>' + catalog.categories.map((category) => `<option value="${escapeHtml(category.id)}">${escapeHtml(category.title)}</option>`).join('');
    renderCatalog();
    const next = lessons.findIndex((lesson) => !progress.lessons[lesson.id]?.completed_at);
    showLesson(next < 0 ? 0 : next);
    showChapter(0);
    const nextAdvanced = advanced.findIndex((item) => !advancedProgress.items[item.id]?.completed_at);
    if (preferredView === 'advanced') showAdvanced(nextAdvanced < 0 ? 0 : nextAdvanced);
    if (preferredView === 'practice') setView('practice');
    if (preferredView === 'catalog') setView('catalog');
    if (preferredView === 'lab') showLab(labs.findIndex((lab) => !labProgress.labs[lab.id]?.completed_at) < 0 ? 0 : labs.findIndex((lab) => !labProgress.labs[lab.id]?.completed_at));
  } catch (error) {
    $('lessonTitle').textContent = 'No se pudo iniciar';
    $('lessonSubtitle').textContent = error.message;
  }
}

$('codeEditor').addEventListener('input', () => {
  if (lessons[currentIndex]) localStorage.setItem(draftKey(lessons[currentIndex]), $('codeEditor').value);
});
$('codeEditor').addEventListener('keydown', (event) => {
  if (event.key === 'Tab') {
    event.preventDefault();
    const editor = event.target;
    const start = editor.selectionStart;
    editor.setRangeText('    ', start, editor.selectionEnd, 'end');
    editor.dispatchEvent(new Event('input'));
  }
  if (event.key === 'Enter' && (event.ctrlKey || event.metaKey)) {
    event.preventDefault();
    runCode(false);
  }
});
$('hintButton').addEventListener('click', () => {
  const lesson = lessons[currentIndex];
  if (!lesson || lessonHintLevel >= lesson.hints.length) return;
  lessonHintLevel += 1;
  $('hintLevel').textContent = `PISTA ${lessonHintLevel} DE ${lesson.hints.length}`;
  $('hintBody').textContent = lesson.hints[lessonHintLevel - 1];
  $('hintText').hidden = false;
  $('hintButton').setAttribute('aria-expanded', 'true');
  $('hintButton').textContent = lessonHintLevel < lesson.hints.length ? `Ver pista ${lessonHintLevel + 1} de ${lesson.hints.length} ↓` : 'Ya viste las tres pistas';
  $('hintButton').disabled = lessonHintLevel === lesson.hints.length;
});
$('resetButton').addEventListener('click', () => {
  const lesson = lessons[currentIndex];
  $('codeEditor').value = lesson.starter;
  localStorage.removeItem(draftKey(lesson));
  $('codeEditor').focus();
});
$('runButton').addEventListener('click', () => runCode(false));
$('checkButton').addEventListener('click', () => runCode(true));
$('nextButton').addEventListener('click', () => showLesson(currentIndex + 1));
$('guideTab').addEventListener('click', () => setView('guide'));
$('catalogTab').addEventListener('click', () => setView('catalog'));
$('practiceTab').addEventListener('click', () => setView('practice'));
$('labTab').addEventListener('click', () => showLab(labIndex));
$('advancedTab').addEventListener('click', () => showAdvanced(advancedIndex));
$('advancedAddFile').addEventListener('click', () => {
  if (!advancedFiles) return;
  const name = $('advancedNewFileName').value.trim();
  if (!/^[a-z][a-z0-9_]*\.py$/.test(name) || name === '__prueba__.py') {
    $('advancedSaveStatus').textContent = 'Usa nombre_modulo.py';
    return;
  }
  if (Object.keys(advancedFiles).length >= 8 && !(name in advancedFiles)) {
    $('advancedSaveStatus').textContent = 'Máximo 8 archivos';
    return;
  }
  storeAdvancedEditor();
  if (!(name in advancedFiles)) advancedFiles[name] = '';
  advancedFileName = name;
  $('advancedEditor').value = advancedFiles[name];
  $('advancedNewFileName').value = '';
  renderAdvancedFiles();
  queueAdvancedSave();
  $('advancedEditor').focus();
});
$('advancedNewFileName').addEventListener('keydown', (event) => {
  if (event.key === 'Enter') {
    event.preventDefault();
    $('advancedAddFile').click();
  }
});
$('advancedEditor').addEventListener('input', () => {
  storeAdvancedEditor();
  queueAdvancedSave();
});
$('advancedEditor').addEventListener('keydown', (event) => {
  if (event.key === 'Tab') {
    event.preventDefault();
    event.target.setRangeText('    ', event.target.selectionStart, event.target.selectionEnd, 'end');
    event.target.dispatchEvent(new Event('input'));
  }
  if (event.key === 'Enter' && (event.ctrlKey || event.metaKey)) {
    event.preventDefault();
    runAdvanced(false);
  }
});
$('advancedRunButton').addEventListener('click', () => runAdvanced(false));
$('advancedCheckButton').addEventListener('click', () => runAdvanced(true));
$('advancedNextButton').addEventListener('click', () => showAdvanced(advancedIndex + 1));
$('advancedHintButton').addEventListener('click', () => {
  const item = advanced[advancedIndex];
  if (!item || advancedHintLevel >= item.hints.length) return;
  advancedHintLevel += 1;
  $('advancedHintLevel').textContent = `PISTA ${advancedHintLevel} DE ${item.hints.length}`;
  $('advancedHintBody').textContent = item.hints[advancedHintLevel - 1];
  $('advancedHint').hidden = false;
  $('advancedHintButton').setAttribute('aria-expanded', 'true');
  $('advancedHintButton').textContent = advancedHintLevel < item.hints.length ? `Ver pista ${advancedHintLevel + 1} de ${item.hints.length} ↓` : 'Ya viste las tres pistas';
  $('advancedHintButton').disabled = advancedHintLevel === item.hints.length;
});
$('labSetupButton').addEventListener('click', async () => {
  $('labSetupButton').disabled = true;
  $('labEnvironmentStatus').textContent = 'Creando el entorno virtual...';
  try {
    const result = await post('/api/labs/setup', {});
    labEnvironmentReady = result.ready;
    $('labEnvironmentStatus').textContent = result.message || result.error;
    $('labSetupButton').hidden = result.ready;
    if (result.ready) refreshLabStatus();
  } catch (error) {
    $('labEnvironmentStatus').textContent = error.message;
  } finally {
    $('labSetupButton').disabled = false;
  }
});
$('labStatusButton').addEventListener('click', refreshLabStatus);
$('labDiagnoseButton').addEventListener('click', async () => {
  const lab = labs[labIndex];
  if (!lab) return;
  $('labErrorDiagnosis').textContent = 'Analizando el mensaje...';
  try {
    const result = await post('/api/labs/diagnose', { lab_id: lab.id, output: $('labErrorInput').value });
    $('labErrorDiagnosis').textContent = result.diagnosis;
  } catch (error) {
    $('labErrorDiagnosis').textContent = error.message;
  }
});
$('labCatalogButton').addEventListener('click', () => {
  $('catalogSearch').value = labs[labIndex].packages[0];
  $('catalogKind').value = 'external';
  catalogCategory = 'all';
  $('catalogCategory').value = 'all';
  renderCatalog();
  setView('catalog');
});
$('labCodeEditor').addEventListener('input', () => {
  if (labs[labIndex]) localStorage.setItem(`aprende-python:lab:${labs[labIndex].id}`, $('labCodeEditor').value);
});
$('labCodeEditor').addEventListener('keydown', (event) => {
  if (event.key === 'Tab') {
    event.preventDefault();
    event.target.setRangeText('    ', event.target.selectionStart, event.target.selectionEnd, 'end');
    event.target.dispatchEvent(new Event('input'));
  }
  if (event.key === 'Enter' && (event.ctrlKey || event.metaKey)) {
    event.preventDefault();
    runLab(false);
  }
});
$('labHintButton').addEventListener('click', () => {
  const lab = labs[labIndex];
  if (!lab || labHintLevel >= lab.hints.length) return;
  labHintLevel += 1;
  $('labHintLevel').textContent = `PISTA ${labHintLevel} DE ${lab.hints.length}`;
  $('labHintBody').textContent = lab.hints[labHintLevel - 1];
  $('labHint').hidden = false;
  $('labHintButton').setAttribute('aria-expanded', 'true');
  $('labHintButton').textContent = labHintLevel < lab.hints.length ? `Ver pista ${labHintLevel + 1} de ${lab.hints.length} ↓` : 'Ya viste las tres pistas';
  $('labHintButton').disabled = labHintLevel === lab.hints.length;
});
$('labResetButton').addEventListener('click', () => {
  const lab = labs[labIndex];
  $('labCodeEditor').value = lab.starter;
  localStorage.removeItem(`aprende-python:lab:${lab.id}`);
  $('labCodeEditor').focus();
});
$('labRunButton').addEventListener('click', () => runLab(false));
$('labCheckButton').addEventListener('click', () => runLab(true));
$('labNextButton').addEventListener('click', () => showLab(labIndex + 1));
$('catalogSearch').addEventListener('input', renderCatalog);
$('catalogCategory').addEventListener('change', (event) => {
  catalogCategory = event.target.value;
  renderCatalog();
});
$('catalogKind').addEventListener('change', renderCatalog);
$('previousChapter').addEventListener('click', () => showChapter(chapterIndex - 1));
$('nextChapter').addEventListener('click', () => showChapter(chapterIndex + 1));
$('practiceUnit').addEventListener('click', () => {
  const relatedAdvanced = guide[chapterIndex].advanced_id;
  if (relatedAdvanced) {
    const index = advanced.findIndex((item) => item.id === relatedAdvanced);
    if (index >= 0) showAdvanced(index);
    return;
  }
  const unit = guide[chapterIndex].unit;
  const next = lessons.findIndex((lesson) => lesson.unit === unit && !progress.lessons[lesson.id]?.completed_at);
  const first = lessons.findIndex((lesson) => lesson.unit === unit);
  setView('practice');
  showLesson(next >= 0 ? next : first);
});
$('theoryButton').addEventListener('click', () => {
  const slug = chapterByUnit[lessons[currentIndex].unit];
  showChapter(guide.findIndex((chapter) => chapter.id === slug));
});
$('libraryTheoryButton').addEventListener('click', () => {
  showChapter(guide.findIndex((chapter) => chapter.id === 'modulos-bibliotecas'));
});
start();
