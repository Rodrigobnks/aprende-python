"""Retos intermedios y proyectos progresivos con archivos reales."""


def task(identifier, title, topic, goal, starter_files, solution_files, cases, hint,
         required_imports=(), project_id=None, project_title=None, stage=None):
    return {
        "id": identifier, "title": title, "topic": topic, "goal": goal,
        "starter_files": starter_files, "solution_files": solution_files,
        "cases": cases, "required_imports": list(required_imports),
        "project_id": project_id, "project_title": project_title, "stage": stage,
        "kind": "project" if project_id else "intermediate",
        "hints": [
            "Identifica la entrada, la salida y los archivos que intervienen. Prueba primero el caso visible.",
            f"Divide el trabajo en pasos pequeños. El tema principal de esta etapa es: {topic.lower()}.",
            hint,
        ],
    }


INTERMEDIATE = [
    task(
        "av-01-csv", "Sumar un CSV", "Archivos CSV",
        "Abre ventas.csv con csv.DictReader. Suma la columna monto como enteros y muestra 'Total: N'. El archivo cambia en cada prueba.",
        {"main.py": "# Lee ventas.csv y suma los montos.\nimport csv\n\n# Tu código aquí\n"},
        {"main.py": "import csv\n\nwith open('ventas.csv', newline='', encoding='utf-8') as archivo:\n    total = sum(int(fila['monto']) for fila in csv.DictReader(archivo))\nprint(f'Total: {total}')\n"},
        [
            {"files": {"ventas.csv": "producto,monto\nlibro,12\nlápiz,8\n"}, "expected_stdout": "Total: 20"},
            {"files": {"ventas.csv": "producto,monto\ncuaderno,7\n"}, "expected_stdout": "Total: 7"},
            {"files": {"ventas.csv": "producto,monto\n"}, "expected_stdout": "Total: 0"},
        ], "Usa open(..., newline='', encoding='utf-8') y recorre csv.DictReader(archivo).", ["csv"]),
    task(
        "av-02-json", "Leer configuración JSON", "Archivos JSON",
        "Lee config.json, que contiene nombre y limite. Muestra 'NOMBRE puede crear LIMITE tareas'. No fijes los datos del ejemplo en el código.",
        {"main.py": "import json\n\n# Lee config.json y forma el mensaje.\n"},
        {"main.py": "import json\n\nwith open('config.json', encoding='utf-8') as archivo:\n    config = json.load(archivo)\nprint(f\"{config['nombre']} puede crear {config['limite']} tareas\")\n"},
        [
            {"files": {"config.json": '{"nombre":"Ada","limite":3}'}, "expected_stdout": "Ada puede crear 3 tareas"},
            {"files": {"config.json": '{"nombre":"Luis","limite":8}'}, "expected_stdout": "Luis puede crear 8 tareas"},
        ], "json.load(archivo) devuelve un diccionario; consulta nombre y limite.", ["json"]),
    task(
        "av-03-escribir", "Crear un archivo de texto", "Escritura de archivos",
        "Lee un nombre de la entrada. Crea saludo.txt con una línea 'Hola, NOMBRE' y un salto final. Muestra 'Archivo creado'.",
        {"main.py": "# Lee un nombre y crea saludo.txt en esta carpeta.\n"},
        {"main.py": "nombre = input().strip()\nwith open('saludo.txt', 'w', encoding='utf-8') as archivo:\n    archivo.write(f'Hola, {nombre}\\n')\nprint('Archivo creado')\n"},
        [
            {"stdin": "Ana\n", "expected_stdout": "Archivo creado", "expected_files": {"saludo.txt": "Hola, Ana\n"}},
            {"stdin": "Mar\n", "expected_stdout": "Archivo creado", "expected_files": {"saludo.txt": "Hola, Mar\n"}},
        ], "Usa with open('saludo.txt', 'w', encoding='utf-8') y escribe el salto final con \\n."),
    task(
        "av-04-errores", "Ignorar entradas inválidas", "Excepciones",
        "Lee una línea con valores separados por comas. Suma los enteros válidos, cuenta los fragmentos inválidos y muestra 'Suma: N; inválidos: M'. Un campo vacío también es inválido.",
        {"main.py": "# Convierte cada fragmento y trata ValueError.\n"},
        {"main.py": "total = 0\nerrores = 0\nfor fragmento in input().split(','):\n    try:\n        total += int(fragmento.strip())\n    except ValueError:\n        errores += 1\nprint(f'Suma: {total}; inválidos: {errores}')\n"},
        [
            {"stdin": "5,abc,3\n", "expected_stdout": "Suma: 8; inválidos: 1"},
            {"stdin": "-2,4,,x\n", "expected_stdout": "Suma: 2; inválidos: 2"},
            {"stdin": "0\n", "expected_stdout": "Suma: 0; inválidos: 0"},
        ], "Coloca int(fragmento.strip()) dentro de try y aumenta el contador en except ValueError."),
    task(
        "av-05-modulos", "Separar lógica y programa", "Módulos propios",
        "En logica.py define precio_final(precio, descuento) que devuelva el precio tras aplicar un porcentaje. En main.py lee dos números e imprime el resultado. Conserva la importación entre archivos.",
        {"main.py": "import logica\n\nprecio = float(input())\ndescuento = float(input())\n# Usa logica.precio_final e imprime el resultado.\n", "logica.py": "def precio_final(precio, descuento):\n    pass\n"},
        {"main.py": "import logica\n\nprecio = float(input())\ndescuento = float(input())\nprint(logica.precio_final(precio, descuento))\n", "logica.py": "def precio_final(precio, descuento):\n    return precio * (1 - descuento / 100)\n"},
        [
            {"stdin": "100\n20\n", "expected_stdout": "80.0"},
            {"stdin": "50\n0\n", "expected_stdout": "50.0"},
            {"stdin": "200\n50\n", "expected_stdout": "100.0"},
        ], "Haz el cálculo en logica.py y desde main.py llama logica.precio_final(precio, descuento).", ["logica"]),
    task(
        "av-06-pruebas", "Reparar código con pruebas", "Pruebas unitarias",
        "Las pruebas en test_logica.py describen cuándo un número es primo. Corrige logica.py hasta que main.py muestre OK. Conserva los archivos de pruebas y comprueba también valores no incluidos en el ejemplo.",
        {"main.py": "import unittest\nfrom test_logica import Pruebas\n\nresultado = unittest.TestResult()\nunittest.defaultTestLoader.loadTestsFromTestCase(Pruebas).run(resultado)\nprint('OK' if resultado.wasSuccessful() else 'FALLO')\n", "logica.py": "def es_primo(n):\n    return n > 1 and n % 2 != 0\n", "test_logica.py": "import unittest\nfrom logica import es_primo\n\nclass Pruebas(unittest.TestCase):\n    def test_dos(self):\n        self.assertTrue(es_primo(2))\n    def test_nueve(self):\n        self.assertFalse(es_primo(9))\n    def test_diecisiete(self):\n        self.assertTrue(es_primo(17))\n"},
        {"main.py": "import unittest\nfrom test_logica import Pruebas\n\nresultado = unittest.TestResult()\nunittest.defaultTestLoader.loadTestsFromTestCase(Pruebas).run(resultado)\nprint('OK' if resultado.wasSuccessful() else 'FALLO')\n", "logica.py": "def es_primo(n):\n    if n < 2:\n        return False\n    for divisor in range(2, int(n ** 0.5) + 1):\n        if n % divisor == 0:\n            return False\n    return True\n", "test_logica.py": "import unittest\nfrom logica import es_primo\n\nclass Pruebas(unittest.TestCase):\n    def test_dos(self):\n        self.assertTrue(es_primo(2))\n    def test_nueve(self):\n        self.assertFalse(es_primo(9))\n    def test_diecisiete(self):\n        self.assertTrue(es_primo(17))\n"},
        [
            {"expected_stdout": "OK"},
            {"harness": "from logica import es_primo\nprint([es_primo(n) for n in [0, 1, 2, 3, 4, 9, 17]])\n", "expected_stdout": "[False, False, True, True, False, False, True]"},
        ], "Un número primo es mayor que 1 y no tiene divisores desde 2 hasta su raíz cuadrada.", ["unittest"]),
    task(
        "av-07-clase", "Cuenta con métodos", "Clases",
        "Crea una clase Cuenta con saldo, depositar(cantidad) y retirar(cantidad). Lee el saldo inicial y luego operaciones '+ N' o '- N', una por línea hasta fin de entrada. Muestra 'Saldo: N'. Todas las operaciones de este reto son válidas.",
        {"main.py": "class Cuenta:\n    def __init__(self, saldo):\n        self.saldo = saldo\n\n    def depositar(self, cantidad):\n        pass\n\n    def retirar(self, cantidad):\n        pass\n\n# Lee las operaciones e imprime el saldo.\n"},
        {"main.py": "import sys\n\nclass Cuenta:\n    def __init__(self, saldo):\n        self.saldo = saldo\n\n    def depositar(self, cantidad):\n        self.saldo += cantidad\n\n    def retirar(self, cantidad):\n        self.saldo -= cantidad\n\nlineas = sys.stdin.read().splitlines()\ncuenta = Cuenta(int(lineas[0]))\nfor linea in lineas[1:]:\n    operador, cantidad = linea.split()\n    if operador == '+':\n        cuenta.depositar(int(cantidad))\n    else:\n        cuenta.retirar(int(cantidad))\nprint(f'Saldo: {cuenta.saldo}')\n"},
        [
            {"stdin": "10\n+ 5\n- 3\n", "expected_stdout": "Saldo: 12"},
            {"stdin": "0\n+ 7\n", "expected_stdout": "Saldo: 7"},
            {"stdin": "20\n- 8\n+ 2\n", "expected_stdout": "Saldo: 14"},
        ], "Cada método cambia self.saldo; recorre las líneas después del saldo inicial.", ["sys"]),
    task(
        "av-08-sqlite", "Registrar movimientos", "SQLite",
        "Lee movimientos 'nombre,monto', uno por línea hasta fin de entrada. Crea movimientos.db, inserta cada fila con parámetros SQL y muestra 'Total: N' consultando SUM(monto).",
        {"main.py": "import sqlite3\nimport sys\n\n# Crea la tabla, inserta filas y consulta la suma.\n"},
        {"main.py": "import sqlite3\nimport sys\n\nwith sqlite3.connect('movimientos.db') as db:\n    db.execute('CREATE TABLE movimientos (nombre TEXT, monto INTEGER)')\n    for linea in sys.stdin.read().splitlines():\n        nombre, monto = linea.split(',')\n        db.execute('INSERT INTO movimientos VALUES (?, ?)', (nombre, int(monto)))\n    total = db.execute('SELECT COALESCE(SUM(monto), 0) FROM movimientos').fetchone()[0]\nprint(f'Total: {total}')\n"},
        [
            {"stdin": "Ana,5\nLuis,7\n", "expected_stdout": "Total: 12", "expected_db": {"movimientos.db": {"query": "SELECT nombre,monto FROM movimientos ORDER BY rowid", "rows": [["Ana", 5], ["Luis", 7]]}}},
            {"stdin": "Mar,-2\nSol,6\n", "expected_stdout": "Total: 4", "expected_db": {"movimientos.db": {"query": "SELECT nombre,monto FROM movimientos ORDER BY rowid", "rows": [["Mar", -2], ["Sol", 6]]}}},
            {"stdin": "", "expected_stdout": "Total: 0", "expected_db": {"movimientos.db": {"query": "SELECT nombre,monto FROM movimientos ORDER BY rowid", "rows": []}}},
        ], "Usa sqlite3.connect, CREATE TABLE, INSERT con signos ? y una consulta SUM.", ["sqlite3"]),
    task(
        "av-09-cli", "Argumentos de terminal", "argparse",
        "Acepta --nombre y --veces desde la línea de comandos. Imprime 'Hola, NOMBRE' tantas veces como indique --veces. El corrector pasará argumentos diferentes.",
        {"main.py": "import argparse\n\n# Define --nombre (texto) y --veces (entero).\n"},
        {"main.py": "import argparse\n\nparser = argparse.ArgumentParser()\nparser.add_argument('--nombre', required=True)\nparser.add_argument('--veces', type=int, required=True)\nargs = parser.parse_args()\nfor _ in range(args.veces):\n    print(f'Hola, {args.nombre}')\n"},
        [
            {"argv": ["--nombre", "Ana", "--veces", "2"], "expected_stdout": "Hola, Ana\nHola, Ana"},
            {"argv": ["--nombre", "Luis", "--veces", "1"], "expected_stdout": "Hola, Luis"},
            {"argv": ["--nombre", "Mar", "--veces", "0"], "expected_stdout": ""},
        ], "argparse.ArgumentParser().add_argument permite definir texto y type=int.", ["argparse"]),
    task(
        "av-10-logging", "Registrar un aviso", "Registros de ejecución",
        "Lee un aviso por entrada. Regístralo en app.log con formato 'WARNING:MENSAJE' y muestra 'Aviso guardado'. El archivo debe contener solo ese aviso y un salto final.",
        {"main.py": "import logging\n\n# Configura app.log y registra el aviso.\n"},
        {"main.py": "import logging\n\nlogging.basicConfig(filename='app.log', level=logging.WARNING, format='%(levelname)s:%(message)s', encoding='utf-8', force=True)\nlogging.warning(input())\nprint('Aviso guardado')\n"},
        [
            {"stdin": "Conexión lenta\n", "expected_stdout": "Aviso guardado", "expected_files": {"app.log": "WARNING:Conexión lenta\n"}},
            {"stdin": "Sin datos\n", "expected_stdout": "Aviso guardado", "expected_files": {"app.log": "WARNING:Sin datos\n"}},
        ], "Configura logging.basicConfig con filename, level y format antes de llamar logging.warning.", ["logging"]),
    task(
        "av-11-fechas", "Calcular una fecha futura", "Fechas",
        "Lee una fecha ISO YYYY-MM-DD y una cantidad entera de días. Muestra la fecha resultante en el mismo formato. Prueba un cambio de mes y un año bisiesto.",
        {"main.py": "from datetime import date, timedelta\n\n# Lee la fecha y los días.\n"},
        {"main.py": "from datetime import date, timedelta\n\nfecha = date.fromisoformat(input().strip())\ndias = int(input())\nprint((fecha + timedelta(days=dias)).isoformat())\n"},
        [
            {"stdin": "2024-02-28\n2\n", "expected_stdout": "2024-03-01"},
            {"stdin": "2025-12-31\n1\n", "expected_stdout": "2026-01-01"},
            {"stdin": "2024-03-01\n-1\n", "expected_stdout": "2024-02-29"},
        ], "date.fromisoformat lee la fecha; timedelta(days=dias) representa el desplazamiento.", ["datetime"]),
    task(
        "av-12-informe", "Generar un informe JSON", "CSV y JSON",
        "Lee ventas.csv con categoria y monto. Agrupa los montos por categoría y guarda un objeto JSON en resumen.json. Muestra 'Categorías: N'. El corrector compara el contenido JSON, sin importar espacios u orden de claves.",
        {"main.py": "import csv\nimport json\n\n# Lee, agrupa y crea resumen.json.\n"},
        {"main.py": "import csv\nimport json\n\ntotales = {}\nwith open('ventas.csv', newline='', encoding='utf-8') as archivo:\n    for fila in csv.DictReader(archivo):\n        categoria = fila['categoria']\n        totales[categoria] = totales.get(categoria, 0) + int(fila['monto'])\nwith open('resumen.json', 'w', encoding='utf-8') as archivo:\n    json.dump(totales, archivo, ensure_ascii=False)\nprint(f'Categorías: {len(totales)}')\n"},
        [
            {"files": {"ventas.csv": "categoria,monto\nlibros,12\njuegos,5\nlibros,8\n"}, "expected_stdout": "Categorías: 2", "expected_files": {"resumen.json": {"libros": 20, "juegos": 5}}},
            {"files": {"ventas.csv": "categoria,monto\ncomida,4\n"}, "expected_stdout": "Categorías: 1", "expected_files": {"resumen.json": {"comida": 4}}},
        ], "Usa csv.DictReader, un diccionario acumulador y json.dump.", ["csv", "json"]),
]


# Los archivos de solución de cada etapa contienen también las funciones anteriores.
# El alumno conserva su propio trabajo en un borrador del proyecto al avanzar.
GASTOS_STARTER = {
    "main.py": "import logica\n\naccion = input().strip()\nif accion == 'total':\n    print(f\"Total: {logica.total('gastos.csv')}\")\n",
    "logica.py": "import csv\n\ndef total(ruta):\n    return 0\n",
}
GASTOS_MAIN_1 = GASTOS_STARTER["main.py"]
GASTOS_LOGICA_1 = "import csv\n\ndef total(ruta):\n    with open(ruta, newline='', encoding='utf-8') as archivo:\n        return sum(int(fila['monto']) for fila in csv.DictReader(archivo))\n"
GASTOS_MAIN_2 = "import logica\n\naccion = input().strip()\nif accion == 'total':\n    print(f\"Total: {logica.total('gastos.csv')}\")\nelif accion == 'agregar':\n    categoria = input().strip()\n    monto = int(input())\n    logica.agregar('gastos.csv', categoria, monto)\n    print('Registrado')\n"
GASTOS_LOGICA_2 = GASTOS_LOGICA_1 + "\ndef agregar(ruta, categoria, monto):\n    with open(ruta, 'a', newline='', encoding='utf-8') as archivo:\n        csv.writer(archivo).writerow([categoria, monto])\n"
GASTOS_MAIN_3 = GASTOS_MAIN_2 + "elif accion == 'resumen':\n    for categoria, monto in sorted(logica.resumen('gastos.csv').items()):\n        print(f'{categoria}={monto}')\n"
GASTOS_LOGICA_3 = GASTOS_LOGICA_2 + "\ndef resumen(ruta):\n    totales = {}\n    with open(ruta, newline='', encoding='utf-8') as archivo:\n        for fila in csv.DictReader(archivo):\n            categoria = fila['categoria']\n            totales[categoria] = totales.get(categoria, 0) + int(fila['monto'])\n    return totales\n"
GASTOS_SEED = "categoria,monto\ncomida,12\ntransporte,8\n"

INVENTARIO_STARTER = {
    "main.py": "import logica\n\naccion = input().strip()\nif accion == 'total':\n    print(f\"Unidades: {logica.total('productos.json')}\")\n",
    "logica.py": "import json\n\ndef total(ruta):\n    return 0\n",
}
INVENTARIO_MAIN_1 = INVENTARIO_STARTER["main.py"]
INVENTARIO_LOGICA_1 = "import json\n\ndef cargar(ruta):\n    with open(ruta, encoding='utf-8') as archivo:\n        return json.load(archivo)\n\ndef guardar(ruta, productos):\n    with open(ruta, 'w', encoding='utf-8') as archivo:\n        json.dump(productos, archivo, ensure_ascii=False)\n\ndef total(ruta):\n    return sum(producto['stock'] for producto in cargar(ruta))\n"
INVENTARIO_MAIN_2 = INVENTARIO_MAIN_1 + "elif accion == 'vender':\n    sku = input().strip()\n    cantidad = int(input())\n    print('Venta registrada' if logica.vender('productos.json', sku, cantidad) else 'Sin existencias')\n"
INVENTARIO_LOGICA_2 = INVENTARIO_LOGICA_1 + "\ndef vender(ruta, sku, cantidad):\n    productos = cargar(ruta)\n    for producto in productos:\n        if producto['sku'] == sku and producto['stock'] >= cantidad:\n            producto['stock'] -= cantidad\n            guardar(ruta, productos)\n            return True\n    return False\n"
INVENTARIO_MAIN_3 = INVENTARIO_MAIN_2 + "elif accion == 'bajos':\n    limite = int(input())\n    bajos = logica.bajos('productos.json', limite)\n    print('\\n'.join(f\"{p['sku']}:{p['stock']}\" for p in bajos) if bajos else '(ninguno)')\n"
INVENTARIO_LOGICA_3 = INVENTARIO_LOGICA_2 + "\ndef bajos(ruta, limite):\n    return sorted((p for p in cargar(ruta) if p['stock'] <= limite), key=lambda p: p['sku'])\n"
INVENTARIO_SEED = '[{"sku":"A","nombre":"Lápiz","stock":3},{"sku":"B","nombre":"Libro","stock":5}]'

TAREAS_STARTER = {
    "main.py": "import logica\n\naccion = input().strip()\nif accion == 'pendientes':\n    titulos = logica.pendientes('tareas.json')\n    print('\\n'.join(titulos) if titulos else '(ninguna)')\n",
    "logica.py": "import json\n\ndef pendientes(ruta):\n    return []\n",
}
TAREAS_MAIN_1 = TAREAS_STARTER["main.py"]
TAREAS_LOGICA_1 = "import json\n\ndef cargar(ruta):\n    with open(ruta, encoding='utf-8') as archivo:\n        return json.load(archivo)\n\ndef guardar(ruta, tareas):\n    with open(ruta, 'w', encoding='utf-8') as archivo:\n        json.dump(tareas, archivo, ensure_ascii=False)\n\ndef pendientes(ruta):\n    return [tarea['titulo'] for tarea in cargar(ruta) if not tarea['hecha']]\n"
TAREAS_MAIN_2 = TAREAS_MAIN_1 + "elif accion == 'agregar':\n    titulo = input().strip()\n    numero = logica.agregar('tareas.json', titulo)\n    print(f'Creada #{numero}')\n"
TAREAS_LOGICA_2 = TAREAS_LOGICA_1 + "\ndef agregar(ruta, titulo):\n    tareas = cargar(ruta)\n    numero = max((t['id'] for t in tareas), default=0) + 1\n    tareas.append({'id': numero, 'titulo': titulo, 'hecha': False})\n    guardar(ruta, tareas)\n    return numero\n"
TAREAS_MAIN_3 = TAREAS_MAIN_2 + "elif accion == 'completar':\n    numero = int(input())\n    print('Completada' if logica.completar('tareas.json', numero) else 'No encontrada')\n"
TAREAS_LOGICA_3 = TAREAS_LOGICA_2 + "\ndef completar(ruta, numero):\n    tareas = cargar(ruta)\n    for tarea in tareas:\n        if tarea['id'] == numero:\n            tarea['hecha'] = True\n            guardar(ruta, tareas)\n            return True\n    return False\n"
TAREAS_SEED = '[{"id":1,"titulo":"Leer","hecha":false},{"id":2,"titulo":"Practicar","hecha":false}]'

PROJECTS = [
    task("pr-gastos-1", "Leer y sumar gastos", "CSV y módulos",
         "Proyecto Gestor de gastos, etapa 1/3. Mantén main.py como entrada y programa total(ruta) en logica.py. Con el comando total, lee gastos.csv y muestra la suma de monto. Prueba también un archivo con solo cabecera.",
         GASTOS_STARTER, {"main.py": GASTOS_MAIN_1, "logica.py": GASTOS_LOGICA_1},
         [{"stdin": "total\n", "files": {"gastos.csv": GASTOS_SEED}, "expected_stdout": "Total: 20"},
          {"stdin": "total\n", "files": {"gastos.csv": "categoria,monto\n"}, "expected_stdout": "Total: 0"}],
         "DictReader lee cada gasto como diccionario; convierte monto a entero antes de sumar.", ["csv", "logica"], "gastos", "Gestor de gastos", 1),
    task("pr-gastos-2", "Registrar un gasto", "CSV y persistencia",
         "Gestor de gastos, etapa 2/3. Conserva total y añade el comando agregar: recibe categoría y monto en las dos líneas siguientes, añade una fila a gastos.csv y muestra 'Registrado'. El archivo debe conservar sus filas anteriores.",
         GASTOS_STARTER, {"main.py": GASTOS_MAIN_2, "logica.py": GASTOS_LOGICA_2},
         [{"stdin": "agregar\ncomida\n7\n", "files": {"gastos.csv": GASTOS_SEED}, "expected_stdout": "Registrado", "expected_files": {"gastos.csv": [{"categoria": "comida", "monto": "12"}, {"categoria": "transporte", "monto": "8"}, {"categoria": "comida", "monto": "7"}]}},
          {"stdin": "total\n", "files": {"gastos.csv": GASTOS_SEED}, "expected_stdout": "Total: 20"}],
         "Abre el CSV en modo a con newline='' y usa csv.writer para una nueva fila.", ["csv", "logica"], "gastos", "Gestor de gastos", 2),
    task("pr-gastos-3", "Resumen por categoría", "Acumuladores y archivos",
         "Gestor de gastos, etapa 3/3. Conserva total y agregar. Añade el comando resumen: muestra 'categoria=monto' por línea, ordenado alfabéticamente por categoría. Una categoría puede aparecer varias veces.",
         GASTOS_STARTER, {"main.py": GASTOS_MAIN_3, "logica.py": GASTOS_LOGICA_3},
         [{"stdin": "resumen\n", "files": {"gastos.csv": "categoria,monto\ncomida,12\ntransporte,8\ncomida,7\n"}, "expected_stdout": "comida=19\ntransporte=8"},
          {"stdin": "agregar\ncomida\n7\n", "files": {"gastos.csv": GASTOS_SEED}, "expected_stdout": "Registrado", "expected_files": {"gastos.csv": [{"categoria": "comida", "monto": "12"}, {"categoria": "transporte", "monto": "8"}, {"categoria": "comida", "monto": "7"}]}},
          {"stdin": "total\n", "files": {"gastos.csv": GASTOS_SEED}, "expected_stdout": "Total: 20"}],
         "Acumula totales en un diccionario y usa sorted(...) para imprimir en orden.", ["csv", "logica"], "gastos", "Gestor de gastos", 3),
    task("pr-inventario-1", "Contar unidades", "JSON y módulos",
         "Proyecto Inventario de tienda, etapa 1/3. productos.json contiene una lista de objetos con sku, nombre y stock. Con el comando total, muestra la suma de unidades. Organiza la lectura en logica.py.",
         INVENTARIO_STARTER, {"main.py": INVENTARIO_MAIN_1, "logica.py": INVENTARIO_LOGICA_1},
         [{"stdin": "total\n", "files": {"productos.json": INVENTARIO_SEED}, "expected_stdout": "Unidades: 8"},
          {"stdin": "total\n", "files": {"productos.json": "[]"}, "expected_stdout": "Unidades: 0"}],
         "json.load devuelve la lista; suma producto['stock'] para cada producto.", ["json", "logica"], "inventario", "Inventario de tienda", 1),
    task("pr-inventario-2", "Registrar una venta", "JSON y actualización",
         "Inventario de tienda, etapa 2/3. Conserva total. Añade vender: lee SKU y cantidad; si hay suficientes unidades, reduce stock, guarda productos.json y muestra 'Venta registrada'. Si no alcanza o no existe el SKU, muestra 'Sin existencias' y conserva el archivo.",
         INVENTARIO_STARTER, {"main.py": INVENTARIO_MAIN_2, "logica.py": INVENTARIO_LOGICA_2},
         [{"stdin": "vender\nA\n2\n", "files": {"productos.json": INVENTARIO_SEED}, "expected_stdout": "Venta registrada", "expected_files": {"productos.json": [{"sku": "A", "nombre": "Lápiz", "stock": 1}, {"sku": "B", "nombre": "Libro", "stock": 5}]}},
          {"stdin": "vender\nA\n4\n", "files": {"productos.json": INVENTARIO_SEED}, "expected_stdout": "Sin existencias", "expected_files": {"productos.json": [{"sku": "A", "nombre": "Lápiz", "stock": 3}, {"sku": "B", "nombre": "Libro", "stock": 5}]}},
          {"stdin": "total\n", "files": {"productos.json": INVENTARIO_SEED}, "expected_stdout": "Unidades: 8"}],
         "Modifica el objeto correcto solo cuando stock >= cantidad; luego escribe la lista con json.dump.", ["json", "logica"], "inventario", "Inventario de tienda", 2),
    task("pr-inventario-3", "Detectar productos bajos", "Filtros y JSON",
         "Inventario de tienda, etapa 3/3. Conserva total y vender. Añade bajos: lee un límite y muestra 'SKU:stock' de los productos con stock menor o igual al límite, ordenados por SKU. Si no hay ninguno, muestra '(ninguno)'.",
         INVENTARIO_STARTER, {"main.py": INVENTARIO_MAIN_3, "logica.py": INVENTARIO_LOGICA_3},
         [{"stdin": "bajos\n3\n", "files": {"productos.json": INVENTARIO_SEED}, "expected_stdout": "A:3"},
          {"stdin": "bajos\n0\n", "files": {"productos.json": INVENTARIO_SEED}, "expected_stdout": "(ninguno)"},
          {"stdin": "vender\nA\n2\n", "files": {"productos.json": INVENTARIO_SEED}, "expected_stdout": "Venta registrada", "expected_files": {"productos.json": [{"sku": "A", "nombre": "Lápiz", "stock": 1}, {"sku": "B", "nombre": "Libro", "stock": 5}]}},
          {"stdin": "total\n", "files": {"productos.json": INVENTARIO_SEED}, "expected_stdout": "Unidades: 8"}],
         "Filtra la lista y ordena los resultados con key=lambda p: p['sku'].", ["json", "logica"], "inventario", "Inventario de tienda", 3),
    task("pr-tareas-1", "Listar pendientes", "JSON y funciones",
         "Proyecto Organizador de tareas, etapa 1/3. tareas.json guarda id, titulo y hecha. Con el comando pendientes, muestra los títulos no completados en el orden del archivo, uno por línea. Si no hay, muestra '(ninguna)'.",
         TAREAS_STARTER, {"main.py": TAREAS_MAIN_1, "logica.py": TAREAS_LOGICA_1},
         [{"stdin": "pendientes\n", "files": {"tareas.json": TAREAS_SEED}, "expected_stdout": "Leer\nPracticar"},
          {"stdin": "pendientes\n", "files": {"tareas.json": '[{"id":1,"titulo":"Leer","hecha":true}]'}, "expected_stdout": "(ninguna)"}],
         "Carga el JSON y construye una lista con titulo de cada tarea donde hecha sea False.", ["json", "logica"], "tareas", "Organizador de tareas", 1),
    task("pr-tareas-2", "Añadir una tarea", "JSON y persistencia",
         "Organizador de tareas, etapa 2/3. Conserva pendientes. Añade agregar: lee un título, crea una tarea con el siguiente id disponible y hecha=False, guarda tareas.json y muestra 'Creada #N'.",
         TAREAS_STARTER, {"main.py": TAREAS_MAIN_2, "logica.py": TAREAS_LOGICA_2},
         [{"stdin": "agregar\nRepasar CSV\n", "files": {"tareas.json": TAREAS_SEED}, "expected_stdout": "Creada #3", "expected_files": {"tareas.json": [{"id": 1, "titulo": "Leer", "hecha": False}, {"id": 2, "titulo": "Practicar", "hecha": False}, {"id": 3, "titulo": "Repasar CSV", "hecha": False}]}},
          {"stdin": "agregar\nPrimera\n", "files": {"tareas.json": "[]"}, "expected_stdout": "Creada #1", "expected_files": {"tareas.json": [{"id": 1, "titulo": "Primera", "hecha": False}]}},
          {"stdin": "pendientes\n", "files": {"tareas.json": TAREAS_SEED}, "expected_stdout": "Leer\nPracticar"}],
         "Calcula max(id) con default=0, añade un diccionario y guarda con json.dump.", ["json", "logica"], "tareas", "Organizador de tareas", 2),
    task("pr-tareas-3", "Completar una tarea", "JSON y estado",
         "Organizador de tareas, etapa 3/3. Conserva pendientes y agregar. Añade completar: lee un id; si existe, cambia hecha a True, guarda y muestra 'Completada'. Si no existe, muestra 'No encontrada'.",
         TAREAS_STARTER, {"main.py": TAREAS_MAIN_3, "logica.py": TAREAS_LOGICA_3},
         [{"stdin": "completar\n2\n", "files": {"tareas.json": TAREAS_SEED}, "expected_stdout": "Completada", "expected_files": {"tareas.json": [{"id": 1, "titulo": "Leer", "hecha": False}, {"id": 2, "titulo": "Practicar", "hecha": True}]}},
          {"stdin": "completar\n9\n", "files": {"tareas.json": TAREAS_SEED}, "expected_stdout": "No encontrada", "expected_files": {"tareas.json": [{"id": 1, "titulo": "Leer", "hecha": False}, {"id": 2, "titulo": "Practicar", "hecha": False}]}},
          {"stdin": "agregar\nRepasar CSV\n", "files": {"tareas.json": TAREAS_SEED}, "expected_stdout": "Creada #3", "expected_files": {"tareas.json": [{"id": 1, "titulo": "Leer", "hecha": False}, {"id": 2, "titulo": "Practicar", "hecha": False}, {"id": 3, "titulo": "Repasar CSV", "hecha": False}]}},
          {"stdin": "pendientes\n", "files": {"tareas.json": TAREAS_SEED}, "expected_stdout": "Leer\nPracticar"}],
         "Busca el id, actualiza hecha y guarda solo si encontraste la tarea.", ["json", "logica"], "tareas", "Organizador de tareas", 3),
]

ADVANCED = INTERMEDIATE + PROJECTS
ADVANCED_BY_ID = {item["id"]: item for item in ADVANCED}


def workspace_id(item):
    """Las etapas de un proyecto comparten un borrador de varios archivos."""
    return item["project_id"] or item["id"]


def public_advanced():
    return [
        {key: value for key, value in item.items() if key not in {"cases", "solution_files"}}
        | {"sample": item["cases"][0], "workspace_id": workspace_id(item)}
        for item in ADVANCED
    ]
