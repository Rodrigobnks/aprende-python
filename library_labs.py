"""Retos prácticos de instalación e importación de bibliotecas externas."""

from learning_support import lab_hints
from project_labs import PROJECTS

LABS = [
    {
        "id": "lab-01-versiones", "title": "Comparar versiones", "package": "packaging", "import_root": "packaging",
        "concept": "packaging.version.Version interpreta versiones como 1.10 y 1.9 correctamente. Compararlas como texto daría un resultado equivocado.",
        "task": "Instala packaging. Importa Version desde packaging.version. Escribe solve(a, b): devuelve 'mayor', 'menor' o 'igual' según la comparación de a con b.",
        "starter": "# Instala packaging en el entorno del laboratorio.\n# Importa Version desde packaging.version.\n\ndef solve(a, b):\n    pass\n",
        "hint": "from packaging.version import Version; compara Version(a) con Version(b).",
        "cases": [{"args": ["1.10", "1.9"], "expected": "mayor"}, {"args": ["2.0", "2.0"], "expected": "igual"}, {"args": ["1.0rc1", "1.0"], "expected": "menor"}],
        "solution": "from packaging.version import Version\n\ndef solve(a, b):\n    if Version(a) > Version(b):\n        return 'mayor'\n    if Version(a) < Version(b):\n        return 'menor'\n    return 'igual'\n",
    },
    {
        "id": "lab-02-rangos", "title": "Versiones permitidas", "package": "packaging", "import_root": "packaging",
        "concept": "Un requisito de dependencias puede contener límites como >=2,<3. Debes interpretar la versión y el rango antes de compararlos.",
        "task": "Instala packaging. Escribe solve(version, rango): devuelve True si la versión cumple el rango y False en caso contrario. Investiga qué objetos de packaging representan versiones y rangos.",
        "starter": "# Importa Version y SpecifierSet desde packaging.\n\ndef solve(version, rango):\n    pass\n",
        "hint": "Usa Version(version) in SpecifierSet(rango).",
        "cases": [{"args": ["2.4", ">=2,<3"], "expected": True}, {"args": ["3.0", ">=2,<3"], "expected": False}, {"args": ["1.0", "==1.0"], "expected": True}],
        "solution": "from packaging.version import Version\nfrom packaging.specifiers import SpecifierSet\n\ndef solve(version, rango):\n    return Version(version) in SpecifierSet(rango)\n",
    },
    {
        "id": "lab-03-fechas", "title": "Interpretar fechas", "package": "python-dateutil", "import_root": "dateutil",
        "concept": "El nombre que usa pip puede diferir del import: instalas python-dateutil, pero importas dateutil.",
        "task": "Instala python-dateutil. Importa parser desde dateutil. Escribe solve(texto): interpreta una fecha con dayfirst=True y devuelve YYYY-MM-DD.",
        "starter": "# Instala python-dateutil e importa dateutil.parser.\n\ndef solve(texto):\n    pass\n",
        "hint": "parser.parse(texto, dayfirst=True).strftime('%Y-%m-%d').",
        "cases": [{"args": ["25/12/2025"], "expected": "2025-12-25"}, {"args": ["01/02/2024"], "expected": "2024-02-01"}, {"args": ["15 March 2023"], "expected": "2023-03-15"}],
        "solution": "from dateutil import parser\n\ndef solve(texto):\n    return parser.parse(texto, dayfirst=True).strftime('%Y-%m-%d')\n",
    },
    {
        "id": "lab-04-meses", "title": "Sumar meses reales", "package": "python-dateutil", "import_root": "dateutil",
        "concept": "Un mes no tiene una duración fija. relativedelta ajusta fechas de calendario, incluso al final del mes.",
        "task": "Instala python-dateutil. Importa parser y relativedelta. Escribe solve(fecha_iso, meses): suma esa cantidad de meses y devuelve la nueva fecha ISO.",
        "starter": "# Importa parser y relativedelta desde dateutil.\n\ndef solve(fecha_iso, meses):\n    pass\n",
        "hint": "(parser.parse(fecha_iso) + relativedelta(months=meses)).date().isoformat().",
        "cases": [{"args": ["2024-01-31", 1], "expected": "2024-02-29"}, {"args": ["2023-01-31", 1], "expected": "2023-02-28"}, {"args": ["2024-11-15", 3], "expected": "2025-02-15"}],
        "solution": "from dateutil import parser\nfrom dateutil.relativedelta import relativedelta\n\ndef solve(fecha_iso, meses):\n    return (parser.parse(fecha_iso) + relativedelta(months=meses)).date().isoformat()\n",
    },
    {
        "id": "lab-05-yaml-usuario", "title": "Leer configuración YAML", "package": "PyYAML", "import_root": "yaml",
        "concept": "YAML representa datos estructurados legibles. safe_load lee datos sin activar la carga de objetos arbitrarios.",
        "task": "Instala PyYAML. Importa yaml. Escribe solve(texto): usa yaml.safe_load y devuelve el valor de la clave 'usuario'.",
        "starter": "# Instala PyYAML e importa yaml.\n\ndef solve(texto):\n    pass\n",
        "hint": "datos = yaml.safe_load(texto); devuelve datos['usuario'].",
        "cases": [{"args": ["usuario: Ana\nactivo: true"], "expected": "Ana"}, {"args": ["usuario: Luis\nactivo: false"], "expected": "Luis"}, {"args": ["usuario: 'María López'"], "expected": "María López"}],
        "solution": "import yaml\n\ndef solve(texto):\n    datos = yaml.safe_load(texto)\n    return datos['usuario']\n",
    },
    {
        "id": "lab-06-yaml-pedidos", "title": "Sumar datos YAML", "package": "PyYAML", "import_root": "yaml",
        "concept": "Una lista YAML se convierte en lista de Python y un mapa YAML en diccionario.",
        "task": "Instala PyYAML e importa yaml. Escribe solve(texto): carga los datos con safe_load y devuelve la suma de la lista 'pedidos'.",
        "starter": "# Importa yaml y utiliza safe_load.\n\ndef solve(texto):\n    pass\n",
        "hint": "sum(yaml.safe_load(texto)['pedidos']).",
        "cases": [{"args": ["pedidos: [4, 7, 2]"], "expected": 13}, {"args": ["pedidos:\n  - 10\n  - 5"], "expected": 15}, {"args": ["pedidos: []"], "expected": 0}],
        "solution": "import yaml\n\ndef solve(texto):\n    return sum(yaml.safe_load(texto)['pedidos'])\n",
    },
    {
        "id": "lab-07-requests", "title": "Preparar una URL", "package": "requests", "import_root": "requests",
        "concept": "requests puede preparar una petición y codificar sus parámetros sin conectarse a Internet. Este reto funciona sin enviar nada.",
        "task": "Instala requests e impórtala. Escribe solve(base, termino): devuelve la URL que tendría una petición GET con q=termino. Investiga cómo construirla sin enviar la petición; no llames a get.",
        "starter": "# Instala e importa requests. No hagas ninguna conexión.\n\ndef solve(base, termino):\n    pass\n",
        "hint": "requests.Request('GET', base, params={'q': termino}).prepare().url.",
        "cases": [{"args": ["https://ejemplo.com/buscar", "python"], "expected": "https://ejemplo.com/buscar?q=python"}, {"args": ["https://ejemplo.com/buscar", "dos palabras"], "expected": "https://ejemplo.com/buscar?q=dos+palabras"}, {"args": ["https://ejemplo.com/buscar", "a+b"], "expected": "https://ejemplo.com/buscar?q=a%2Bb"}],
        "solution": "import requests\n\ndef solve(base, termino):\n    return requests.Request('GET', base, params={'q': termino}).prepare().url\n",
    },
    {
        "id": "lab-08-numpy-media", "title": "Promedio con NumPy", "package": "numpy", "import_root": "numpy",
        "concept": "NumPy trabaja con arreglos numéricos y ofrece operaciones agregadas como mean.",
        "task": "Instala numpy. Impórtala como np. Escribe solve(valores): devuelve float(np.mean(valores)).",
        "starter": "# Instala numpy e impórtala como np.\n\ndef solve(valores):\n    pass\n",
        "hint": "Convierte el resultado de np.mean(valores) a float.",
        "cases": [{"args": [[2, 4, 6]], "expected": 4.0}, {"args": [[1, 2]], "expected": 1.5}, {"args": [[10, -2, 1]], "expected": 3.0}],
        "solution": "import numpy as np\n\ndef solve(valores):\n    return float(np.mean(valores))\n",
    },
    {
        "id": "lab-09-numpy-forma", "title": "Cambiar forma de un arreglo", "package": "numpy", "import_root": "numpy",
        "concept": "reshape organiza una secuencia en filas y columnas sin cambiar sus valores.",
        "task": "Instala numpy e impórtala como np. Escribe solve(valores): convierte exactamente cuatro números en una matriz 2 × 2 y devuelve una lista de listas.",
        "starter": "# Importa numpy como np.\n\ndef solve(valores):\n    pass\n",
        "hint": "np.array(valores).reshape(2, 2).tolist().",
        "cases": [{"args": [[1, 2, 3, 4]], "expected": [[1, 2], [3, 4]]}, {"args": [[9, 8, 7, 6]], "expected": [[9, 8], [7, 6]]}, {"args": [[0, -1, 5, 2]], "expected": [[0, -1], [5, 2]]}],
        "solution": "import numpy as np\n\ndef solve(valores):\n    return np.array(valores).reshape(2, 2).tolist()\n",
    },
    {
        "id": "lab-10-pandas-grupos", "title": "Agrupar ventas", "package": "pandas", "import_root": "pandas",
        "concept": "DataFrame guarda datos tabulares. Las filas pueden repetirse por categoría y necesitan resumirse.",
        "task": "Instala pandas. Escribe solve(filas): cada fila tiene 'categoria' y 'monto'. Devuelve un diccionario con la suma por categoría. Investiga cómo agrupar y resumir datos con pandas.",
        "starter": "# Instala pandas e impórtala como pd.\n\ndef solve(filas):\n    pass\n",
        "hint": "pd.DataFrame(filas).groupby('categoria')['monto'].sum().to_dict().",
        "cases": [{"args": [[{"categoria": "A", "monto": 2}, {"categoria": "B", "monto": 5}, {"categoria": "A", "monto": 3}]], "expected": {"A": 5, "B": 5}}, {"args": [[{"categoria": "X", "monto": 10}, {"categoria": "X", "monto": 4}]], "expected": {"X": 14}}, {"args": [[{"categoria": "B", "monto": 1}, {"categoria": "A", "monto": 7}]], "expected": {"A": 7, "B": 1}}],
        "solution": "import pandas as pd\n\ndef solve(filas):\n    return pd.DataFrame(filas).groupby('categoria')['monto'].sum().to_dict()\n",
    },
    {
        "id": "lab-11-pandas-faltantes", "title": "Promedio con datos faltantes", "package": "pandas", "import_root": "pandas",
        "concept": "Una Series de pandas omite valores faltantes al calcular mean.",
        "task": "Instala pandas e impórtala como pd. Escribe solve(valores): devuelve como float el promedio, ignorando los None.",
        "starter": "# Importa pandas como pd.\n\ndef solve(valores):\n    pass\n",
        "hint": "float(pd.Series(valores).mean()).",
        "cases": [{"args": [[2, None, 4]], "expected": 3.0}, {"args": [[1, 2, None, 6]], "expected": 3.0}, {"args": [[None, 10]], "expected": 10.0}],
        "solution": "import pandas as pd\n\ndef solve(valores):\n    return float(pd.Series(valores).mean())\n",
    },
    {
        "id": "lab-12-pillow-color", "title": "Crear un píxel", "package": "Pillow", "import_root": "PIL",
        "concept": "Instalas Pillow, pero importas PIL. Image.new crea imágenes en memoria; no hace falta guardar archivos.",
        "task": "Instala Pillow. Importa Image desde PIL. Escribe solve(ancho, alto, color_hex): crea una imagen RGB de ese tamaño y color; devuelve [rojo, verde, azul] del píxel (0, 0).",
        "starter": "# Instala Pillow e importa Image desde PIL.\n\ndef solve(ancho, alto, color_hex):\n    pass\n",
        "hint": "Image.new('RGB', (ancho, alto), color_hex).getpixel((0, 0)); convierte la tupla en lista.",
        "cases": [{"args": [2, 3, "#ff0000"], "expected": [255, 0, 0]}, {"args": [1, 1, "#00ff80"], "expected": [0, 255, 128]}, {"args": [4, 2, "#000000"], "expected": [0, 0, 0]}],
        "solution": "from PIL import Image\n\ndef solve(ancho, alto, color_hex):\n    return list(Image.new('RGB', (ancho, alto), color_hex).getpixel((0, 0)))\n",
    },
    {
        "id": "lab-13-pillow-gris", "title": "Convertir a gris", "package": "Pillow", "import_root": "PIL",
        "concept": "ImageOps.grayscale convierte una imagen RGB en luminancia. El resultado es un entero de 0 a 255.",
        "task": "Instala Pillow. Importa Image e ImageOps desde PIL. Escribe solve(color_hex): crea una imagen RGB de 1 × 1, pásala a escala de grises y devuelve el valor del píxel.",
        "starter": "# Importa Image e ImageOps desde PIL.\n\ndef solve(color_hex):\n    pass\n",
        "hint": "ImageOps.grayscale(Image.new('RGB', (1, 1), color_hex)).getpixel((0, 0)).",
        "cases": [{"args": ["#000000"], "expected": 0}, {"args": ["#ffffff"], "expected": 255}, {"args": ["#808080"], "expected": 128}],
        "solution": "from PIL import Image, ImageOps\n\ndef solve(color_hex):\n    return ImageOps.grayscale(Image.new('RGB', (1, 1), color_hex)).getpixel((0, 0))\n",
    },
    {
        "id": "lab-14-rich", "title": "Leer texto con formato", "package": "rich", "import_root": "rich",
        "concept": "Rich interpreta etiquetas de formato para la terminal. A veces necesitas recuperar solo el texto visible.",
        "task": "Instala rich. Escribe solve(texto): interpreta el marcado y devuelve solo el texto visible, sin etiquetas. Investiga qué función de rich.markup y qué propiedad del resultado necesitas.",
        "starter": "# Instala rich e importa render desde rich.markup.\n\ndef solve(texto):\n    pass\n",
        "hint": "render(texto).plain.",
        "cases": [{"args": ["[bold]Hola[/bold]"], "expected": "Hola"}, {"args": ["[red]Error[/red]: revisa"], "expected": "Error: revisa"}, {"args": ["Python [green]listo[/green]"], "expected": "Python listo"}],
        "solution": "from rich.markup import render\n\ndef solve(texto):\n    return render(texto).plain\n",
    },
]

LABS.extend(PROJECTS)
LAB_BY_ID = {lab["id"]: lab for lab in LABS}


def lab_packages(lab):
    return lab.get("packages", [lab["package"]] if "package" in lab else [])


def lab_import_roots(lab):
    return lab.get("import_roots", [lab["import_root"]] if "import_root" in lab else [])


def public_labs():
    """Los casos de validación adicionales y las soluciones quedan en el servidor."""
    return [
        {key: value for key, value in lab.items() if key not in {"cases", "solution"}}
        | {"sample": lab["cases"][0], "hints": lab_hints(lab), "packages": lab_packages(lab), "import_roots": lab_import_roots(lab)}
        for lab in LABS
    ]
