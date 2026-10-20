"""Proyectos integradores: el alumno elige las funciones de cada biblioteca."""

PROJECTS = [
    {
        "id": "lab-15-ventas-yaml", "title": "Informe de ventas desde YAML", "kind": "project",
        "packages": ["PyYAML", "pandas"], "import_roots": ["yaml", "pandas"],
        "concept": "Una configuración puede llegar como YAML y convertirse en datos tabulares. Tu trabajo es conectar la lectura con el análisis.",
        "task": "Una tienda recibe un texto YAML con una lista llamada ventas. Cada venta tiene categoria y monto. Escribe solve(texto_yaml) para devolver un diccionario con el monto total por categoría. Investiga qué funciones de PyYAML y pandas necesitas; el reto no te indica las llamadas exactas.",
        "starter": "# Investiga cómo leer YAML y agrupar datos con pandas.\n# Importa las bibliotecas que decidas usar.\n\ndef solve(texto_yaml):\n    pass\n",
        "hint": "Combina una lectura segura de YAML con una agrupación por categoria y la suma de monto.",
        "cases": [
            {"args": ["ventas:\n  - categoria: libros\n    monto: 12\n  - categoria: juegos\n    monto: 5\n  - categoria: libros\n    monto: 8"], "expected": {"juegos": 5, "libros": 20}},
            {"args": ["ventas:\n  - categoria: comida\n    monto: 10\n  - categoria: comida\n    monto: 4\n  - categoria: transporte\n    monto: 7"], "expected": {"comida": 14, "transporte": 7}},
            {"args": ["ventas:\n  - categoria: A\n    monto: 0\n  - categoria: B\n    monto: 3"], "expected": {"A": 0, "B": 3}},
        ],
        "solution": "import yaml\nimport pandas as pd\n\ndef solve(texto_yaml):\n    ventas = yaml.safe_load(texto_yaml)['ventas']\n    return pd.DataFrame(ventas).groupby('categoria')['monto'].sum().to_dict()\n",
    },
    {
        "id": "lab-16-paleta", "title": "Analizador de paletas", "kind": "project",
        "packages": ["Pillow", "numpy"], "import_roots": ["PIL", "numpy"],
        "concept": "Pillow entiende colores en formato hexadecimal; NumPy permite analizar los canales rojo, verde y azul por separado.",
        "task": "Un diseñador te entrega una lista no vacía de colores como '#ff0000'. Escribe solve(colores) para devolver una lista de tres números: el promedio de rojo, verde y azul, en ese orden. Puede haber promedios con .5; consérvalos. Investiga cómo combinar Pillow y NumPy.",
        "starter": "# Investiga cómo convertir colores hexadecimales y promediar canales.\n# Importa las bibliotecas necesarias.\n\ndef solve(colores):\n    pass\n",
        "hint": "Convierte cada color en tres canales, forma un arreglo y promedia cada columna.",
        "cases": [
            {"args": [["#ff0000", "#0000ff"]], "expected": [127.5, 0.0, 127.5]},
            {"args": [["#ffffff", "#000000"]], "expected": [127.5, 127.5, 127.5]},
            {"args": [["#123456"]], "expected": [18.0, 52.0, 86.0]},
        ],
        "solution": "from PIL import ImageColor\nimport numpy as np\n\ndef solve(colores):\n    canales = [ImageColor.getrgb(color) for color in colores]\n    return np.array(canales).mean(axis=0).tolist()\n",
    },
    {
        "id": "lab-17-api-config", "title": "Preparar una búsqueda configurable", "kind": "project",
        "packages": ["PyYAML", "requests"], "import_roots": ["yaml", "requests"],
        "concept": "Una aplicación puede guardar su URL y parámetros en YAML. requests puede construir la URL codificada sin enviarla por Internet.",
        "task": "Recibes texto YAML con url y un mapa parametros. Escribe solve(texto_yaml) para devolver la URL de una petición GET preparada con esos parámetros. No realices ninguna conexión. Investiga cómo leer la configuración y preparar la petición.",
        "starter": "# Investiga cómo leer la configuración y preparar un GET sin enviarlo.\n# Importa las bibliotecas necesarias.\n\ndef solve(texto_yaml):\n    pass\n",
        "hint": "Extrae url y parametros de YAML; deja que requests codifique los parámetros.",
        "cases": [
            {"args": ["url: https://ejemplo.com/buscar\nparametros:\n  q: python\n  pagina: 2"], "expected": "https://ejemplo.com/buscar?q=python&pagina=2"},
            {"args": ["url: https://ejemplo.com/buscar\nparametros:\n  q: dos palabras"], "expected": "https://ejemplo.com/buscar?q=dos+palabras"},
            {"args": ["url: https://ejemplo.com/buscar\nparametros:\n  q: a+b"], "expected": "https://ejemplo.com/buscar?q=a%2Bb"},
        ],
        "solution": "import yaml\nimport requests\n\ndef solve(texto_yaml):\n    config = yaml.safe_load(texto_yaml)\n    return requests.Request('GET', config['url'], params=config['parametros']).prepare().url\n",
    },
]
