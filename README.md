## Versión en línea para varias personas

La entrada de Streamlit es **streamlit_app.py**. Conserva la interfaz original. Streamlit sirve el contenido y cada visitante ejecuta Python mediante Pyodide 0.28.3 en un Web Worker de su navegador. El servidor no ejecuta el código de los alumnos ni guarda su progreso.

El progreso y los borradores se guardan por navegador. Usa **Descargar respaldo** y **Restaurar respaldo** para llevarlos a otro equipo. No existe sincronización automática ni cuentas de alumno. Si varias personas comparten un navegador y perfil, compartirán el progreso; usa perfiles separados.

La primera carga necesita Internet para descargar Python desde jsDelivr. El laboratorio descarga sus bibliotecas al usarlo; no necesitas instalar Python ni paquetes en tu computadora. Los proyectos usan archivos virtuales dentro del navegador. No permiten acceder a archivos del equipo. Las instrucciones de PowerShell del material original describen la versión local; en línea, las bibliotecas se preparan en el navegador.

### Publicar en Streamlit Community Cloud

- Repositorio: `Rodrigobnks/aprende-python`
- Rama: `main`
- Archivo principal: `streamlit_app.py`
- Dependencias: `requirements.txt`
- No se necesitan contraseñas ni secretos para la versión pública.

Para iniciar Streamlit localmente: `python -m pip install -r requirements.txt` y después `python -m streamlit run streamlit_app.py`.

La carpeta `data/`, las bases de progreso y los entornos virtuales locales están excluidos de GitHub. La plataforma local original sigue disponible mediante `python app.py`.

---
# Aprende Python · desde cero

Una plataforma local para aprender a programar en español. Incluye un **manual de 30 capítulos**, un **glosario consultable de 56 bibliotecas en 10 temas**, **100 ejercicios originales en 10 bloques**, **14 retos de bibliotecas externas y 3 mini proyectos**, además de **12 retos intermedios y 3 proyectos de tres etapas**. Hay editores de código, corrección automática, pistas escalonadas, ayuda para errores habituales y progreso guardado en el equipo.

## Iniciar

Necesitas Python 3.10 o posterior. El manual y los 100 ejercicios iniciales no requieren instalar paquetes adicionales. Los retos del laboratorio te enseñan a instalar los paquetes que uses.

En PowerShell, abre esta carpeta y ejecuta:

```powershell
python app.py
```

En Windows también puedes hacer doble clic en `iniciar.bat`.

La plataforma se abrirá en `http://127.0.0.1:8765`. Para detenerla, presiona `Ctrl+C` en la terminal. Si prefieres abrir el navegador manualmente, usa `python app.py --no-browser`. Si el puerto está ocupado, usa por ejemplo `python app.py --port 8766`.

## Cómo usarla

1. Abre **Manual** y lee los capítulos desde el inicio. Explican qué es Python, cómo funciona un programa, variables, tipos, control de flujo, funciones, bibliotecas, entornos y archivos. Los capítulos finales preparan paso a paso CSV, JSON, módulos propios, transformación de datos, clases, SQLite, argumentos de terminal, registros, fechas y proyectos.
2. Usa **Bibliotecas** para buscar por nombre, función o tarea; filtra por tema y distingue módulos de la biblioteca estándar de paquetes externos. Cada ficha indica cómo importar, funciones representativas y documentación oficial.
3. Desde un capítulo, pulsa **Practicar bloque** para ir a los ejercicios relacionados. También puedes entrar directamente por **Ejercicios**.
4. Completa el código del reto y presiona **Ejecutar** para ver qué hace con la entrada de ejemplo. En el editor, `Ctrl+Enter` también ejecuta el código. Si necesitas ayuda, abre las tres pistas una por una; la tercera es la más concreta.
5. Presiona **Comprobar reto** para evaluar uno o varios casos. Si falla, revisa la entrada del caso, el resultado esperado, el obtenido y la explicación de qué revisar.
6. Abre **Laboratorio** para practicar instalación, importación y uso de bibliotecas externas reales.
7. Abre **Proyectos** para resolver retos con archivos CSV y JSON, módulos, clases, pruebas y SQLite. Desde los capítulos relacionados del Manual puedes saltar al reto correspondiente. Después desarrolla programas de terminal en varias etapas.
8. Avanza al siguiente ejercicio o vuelve al manual con **Leer la teoría de este bloque**.

El progreso de las rutas se guarda en `data/progreso.db`. Los borradores de los 100 ejercicios y del laboratorio se guardan en el navegador; los borradores de **Proyectos** se guardan en la misma base local para retomarlos incluso si cambias de navegador. La plataforma escucha únicamente en `127.0.0.1` y está pensada para ejecutarse en tu propio equipo. Los ejecutores tienen límites de tiempo, pero **no son entornos aislados para ejecutar código de personas desconocidas**. Los ejemplos del manual y el glosario que usan archivos o `try` se ejecutan con Python normal fuera del editor inicial.

## Proyectos: programas con varios archivos

Los 12 retos intermedios cubren lectura y escritura de CSV y JSON, manejo de errores, módulos propios, pruebas unitarias, clases, SQLite, argumentos de terminal, registros, fechas y un informe que combina CSV y JSON.

Después hay tres proyectos independientes: **Gestor de gastos** (sumar, registrar y resumir gastos), **Inventario de tienda** (contar existencias, vender y detectar productos bajos) y **Organizador de tareas** (listar pendientes, añadir y completar tareas). Cada proyecto tiene tres etapas. El mismo borrador de `main.py` y `logica.py` se conserva al pasar de una etapa a la siguiente. Puedes añadir otros archivos `.py` con el editor. Las pruebas preparan archivos de datos temporales, ejecutan el programa con distintas entradas y comparan la salida y los archivos generados. También repiten comportamientos de etapas anteriores.

Estos retos usan la biblioteca estándar de Python, así que no necesitan instalar paquetes nuevos. Se definen en `advanced_curriculum.py` y se ejecutan desde `advanced_runner.py`.

## Laboratorio: instalar e importar bibliotecas

1. En **Laboratorio**, pulsa **Preparar entorno**. Esto crea `data/library_venv` con pip, separado del Python que inicia la plataforma. Solo se hace una vez.
2. Elige un reto y copia el comando que aparece bajo **Instala en PowerShell**. Pégalo en PowerShell. Por ejemplo, el reto de Pillow mostrará un comando como `& "C:\...\data\library_venv\Scripts\python.exe" -m pip install "Pillow"`. Necesitas acceso a Internet para descargar paquetes con pip. Ningún paquete se instala automáticamente al entrar en el reto.
3. Pulsa **Comprobar instalación**. La plataforma consulta la versión instalada *dentro de ese entorno* y prueba el `import`. Si pip o el import falla, pega el mensaje de PowerShell en **Diagnosticar error**: se clasifica localmente y se sugiere una comprobación. El texto pegado no se ejecuta.
4. Escribe el `import` solicitado y completa `solve(...)`. Debes usar la biblioteca importada dentro de la función. **Ejecutar ejemplo** muestra si resuelves el caso visible. **Comprobar reto** evalúa varios casos y guarda tu progreso.

Hay 14 retos sobre ocho paquetes: packaging, python-dateutil, PyYAML, requests, NumPy, pandas, Pillow y Rich. Los nombres de instalación e importación pueden ser distintos: `pip install Pillow` corresponde a `from PIL import Image`. Cuatro retos plantean el objetivo sin indicar la llamada exacta. Los tres proyectos finales combinan dos bibliotecas cada uno: informe de ventas desde YAML, analizador de paletas y construcción de una URL desde configuración. En los retos con requests solo se preparan URLs; no se envían peticiones de red. El progreso del laboratorio es independiente de los 100 ejercicios iniciales. Si mueves toda la carpeta de la plataforma a otra ubicación, recrea `data/library_venv` allí antes de usarlo, porque los entornos virtuales no son portátiles.

## Ruta de 100 ejercicios

Los bloques son: primer contacto; números y operaciones; texto y cadenas; entrada de datos; decisiones; bucles; listas; diccionarios; funciones; y retos integradores. Los ejercicios se definen en `curriculum.py` y `curriculum_more.py`. Los retos de bibliotecas se definen en `library_labs.py`.

## Libros y referencias

- Allen B. Downey, [*Think Python*, 3.ª edición](https://greenteapress.com/wp/think-python-3rd-edition/): guía para ordenar los conceptos desde las primeras instrucciones hasta funciones y estructuras más complejas.
- Al Sweigart, [*Automate the Boring Stuff with Python*, 3.ª edición](https://automatetheboringstuff.com/): inspiración para que cada concepto desemboque en ejercicios prácticos y, más adelante, automatizaciones.
- [Tutorial oficial de Python](https://docs.python.org/3.13/tutorial/): referencia de la sintaxis y el comportamiento del lenguaje. Sus autores indican que está orientado a personas que ya conocen algunos conceptos de programación, por eso aquí los explicamos desde cero.

La plataforma enlaza las fuentes como bibliografía y usa explicaciones y ejercicios propios; no reproduce capítulos de esos libros.

