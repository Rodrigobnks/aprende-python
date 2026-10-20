"""Capítulos originales que conectan el manual básico con los proyectos."""


def advanced_chapters(chapter, section):
    return [
        chapter(
            "csv-practico", "CSV: leer y escribir tablas",
            "De una fila de texto a datos que puedes calcular.", 10,
            [
                section("Qué guarda un CSV", """
                    CSV es un formato de texto para datos en filas y columnas. En `categoria,monto`, la primera línea suele ser una cabecera que da nombre a las columnas; las siguientes líneas aportan valores. Un archivo puede verse simple, pero un campo puede contener comas entre comillas. Por eso no conviene separar cada línea con `split(",")`: usa el módulo `csv`, que entiende las reglas de comillas y delimitadores.

                    Observa que `12` escrito en un CSV llega al programa como la cadena `"12"`. Si quieres sumar, conviértelo a `int`. Antes de programar, identifica la cabecera exacta y escribe una fila de ejemplo. En el reto «Sumar un CSV», la entrada es `ventas.csv`, la transformación es sumar `monto` y la salida es `Total: N`.
                """, """\
                    categoria,monto
                    comida,12
                    transporte,8
                """),
                section("Leer con DictReader paso a paso", """
                    Abre el archivo con `encoding="utf-8"` para interpretar acentos y `newline=""` para que `csv` gestione correctamente los finales de línea. `csv.DictReader(archivo)` usa la cabecera como claves: la primera fila de datos se parece a `{"categoria": "comida", "monto": "12"}`. En cada vuelta del bucle eliges `fila["monto"]`, lo conviertes y lo añades al acumulador.

                    Para probar el ejemplo completo, el código de abajo crea primero un archivo pequeño y luego lo lee. En el reto, elimina la parte que crea el archivo: el corrector prepara `ventas.csv` con datos diferentes en cada prueba. Si el archivo tiene solo cabecera, el bucle no realiza vueltas y el total queda en cero.
                """, """\
                    import csv

                    with open("ventas.csv", "w", newline="", encoding="utf-8") as archivo:
                        escritor = csv.writer(archivo)
                        escritor.writerow(["categoria", "monto"])
                        escritor.writerow(["comida", 12])
                        escritor.writerow(["transporte", 8])

                    total = 0
                    with open("ventas.csv", newline="", encoding="utf-8") as archivo:
                        for fila in csv.DictReader(archivo):
                            total += int(fila["monto"])
                    print(f"Total: {total}")  # Total: 20
                """),
                section("Añadir filas sin borrar las anteriores", """
                    Para el gestor de gastos, `"a"` abre un archivo en modo añadir. `csv.writer(archivo).writerow([categoria, monto])` escribe una fila con dos columnas. Usa también `newline=""`. Si abres en modo `"w"`, se pierde el contenido previo: ese error puede hacer que la etapa de registrar un gasto pase un ejemplo trivial y falle la prueba que comprueba las filas antiguas.

                    Distingue el archivo de datos del código. `main.py` recibe el comando; `logica.py` abre `gastos.csv`. En las pruebas, cada caso recibe una copia temporal del archivo, así que una prueba no depende de lo que escribió otra. En un programa propio, haz una copia de un CSV importante antes de experimentar con escritura.
                """, """\
                    import csv

                    with open("gastos.csv", "a", newline="", encoding="utf-8") as archivo:
                        csv.writer(archivo).writerow(["comida", 7])
                """),
                section("Errores frecuentes y comprobación", """
                    Un `KeyError` puede indicar que escribiste mal el nombre de la columna o que la cabecera no coincide. `ValueError` al convertir suele significar que `monto` estaba vacío o no era un entero. No conviertas automáticamente cualquier valor inválido en cero: decide primero qué exige el enunciado. Si ves una línea en blanco extra en Windows, comprueba `newline=""` al abrir el archivo para escribir.

                    Prueba mentalmente las filas `comida,12` y `comida,7`: el total general es 19 y el resumen por categoría tiene una entrada `comida=19`. Después entra en Proyectos y resuelve «Sumar un CSV». Más adelante reutilizarás esta idea en «Generar un informe JSON» y en las tres etapas del gestor de gastos.
                """, note="Antes de ejecutar: ¿qué imprime el ejemplo si quitas las dos filas de datos y dejas solo la cabecera? Respuesta: Total: 0."),
            ],
            ["DictReader entrega cadenas bajo los nombres de la cabecera.",
             "Convierte los valores antes de sumar y conserva newline='' al abrir CSV.",
             "El modo a añade; el modo w sobrescribe."],
            [("Módulo csv", "https://docs.python.org/3.13/library/csv.html")],
        ),
        chapter(
            "json-practico", "JSON: estructuras que sobreviven",
            "Guardar listas y diccionarios sin confundir texto con objetos.", 10,
            [
                section("Texto JSON frente a objetos de Python", """
                    JSON es texto con una estructura definida. Un objeto JSON se convierte normalmente en un diccionario; una lista JSON en una lista; `true` y `false` en `True` y `False`; `null` en `None`. La cadena `'{"nombre": "Ana"}'` no es por sí misma un diccionario: sigue siendo `str` hasta que `json.loads` la interpreta. `json.load` hace lo mismo leyendo desde un archivo abierto.

                    Esta distinción importa en «Leer configuración JSON»: el programa debe abrir `config.json` y usar los valores reales. Imprimir siempre el nombre y límite del ejemplo no funcionará cuando el corrector cambie el archivo. Dibuja la estructura antes de codificar: ¿hay un objeto único, una lista de objetos o una lista dentro de un objeto?
                """, """\
                    import json

                    texto = '{"nombre": "Ana", "limite": 3}'
                    datos = json.loads(texto)
                    print(type(texto).__name__)   # str
                    print(type(datos).__name__)   # dict
                    print(datos["limite"])         # 3
                """),
                section("Guardar y recuperar datos", """
                    `json.dump(datos, archivo)` escribe una estructura compatible; `json.load(archivo)` la reconstruye. La letra final marca la diferencia: `dump/load` trabajan con archivos y `dumps/loads` con cadenas. Abre archivos de texto con UTF-8. `ensure_ascii=False` mantiene los acentos legibles en el archivo; no cambia la estructura de los datos.

                    El ejemplo crea `productos.json`, lo lee, cambia el stock en memoria y vuelve a guardarlo. Si omitieras el segundo `json.dump`, verías el cambio mientras corre Python, pero al abrir el archivo mañana seguiría el valor antiguo. El modo `"w"` reemplaza el documento completo: conserva en la lista los elementos que no quieres perder.
                """, """\
                    import json

                    productos = [{"sku": "A", "nombre": "Lápiz", "stock": 3}]
                    with open("productos.json", "w", encoding="utf-8") as archivo:
                        json.dump(productos, archivo, ensure_ascii=False)

                    with open("productos.json", encoding="utf-8") as archivo:
                        guardados = json.load(archivo)
                    guardados[0]["stock"] -= 1

                    with open("productos.json", "w", encoding="utf-8") as archivo:
                        json.dump(guardados, archivo, ensure_ascii=False)
                    print(guardados[0]["stock"])  # 2
                """),
                section("Validar antes de usar", """
                    Un JSON válido puede tener una forma inesperada: una lista cuando esperabas un diccionario, o un producto sin clave `stock`. Si controlas el formato, define cuáles claves son obligatorias y qué tipos deben tener. `json.JSONDecodeError` señala texto mal formado; `FileNotFoundError` señala que no se encontró el archivo; `KeyError` señala una clave ausente. Son problemas diferentes y requieren mensajes o decisiones diferentes.

                    En los retos se entregan archivos con el formato descrito por el enunciado. En un programa para otras personas, no supongas que cualquier archivo recibido cumple el contrato. Captura solo errores que puedas explicar o corregir; no rodees todo el programa con `except:` para ocultar fallos.
                """, """\
                    import json

                    texto = '{"stock": 3}'
                    producto = json.loads(texto)
                    if not isinstance(producto, dict) or "stock" not in producto:
                        raise ValueError("Falta el stock del producto")
                    print(int(producto["stock"]))  # 3
                """),
                section("Elegir un formato y practicar", """
                    CSV resulta cómodo para una tabla donde cada fila tiene las mismas columnas. JSON permite representar listas y diccionarios anidados, como productos con nombres, identificadores y estados. Ninguno sustituye automáticamente a una base de datos: si necesitas consultas frecuentes y cambios de muchos registros, estudia SQLite.

                    En Proyectos, empieza con «Leer configuración JSON», luego «Generar un informe JSON». En el inventario y el organizador de tareas leerás una lista, modificarás uno de sus diccionarios y guardarás toda la lista. Antes de pulsar «Comprobar etapa», verifica también el contenido del archivo producido: imprimir «Venta registrada» no demuestra que el stock haya cambiado.
                """, note="Comprueba: si cambias solo la lista en memoria y no vuelves a llamar json.dump, ¿qué valor leerás en la siguiente ejecución? El valor anterior."),
            ],
            ["JSON en disco es texto; json.load lo convierte a objetos de Python.",
             "Tras cambiar datos en memoria, vuelve a guardarlos para que persistan.",
             "Valida estructura, claves y tipos cuando recibas datos externos."],
            [("Módulo json", "https://docs.python.org/3.13/library/json.html")],
        ),
        chapter(
            "modulos-propios", "Programas con varios archivos",
            "Separar la entrada de usuario de las reglas del problema.", 10,
            [
                section("Por qué separar main.py y logica.py", """
                    Cuando todo vive en un archivo, leer entradas, calcular y guardar datos se entremezclan. Un segundo archivo permite dar una responsabilidad clara a cada parte. En nuestros proyectos, `main.py` es el punto de entrada: lee un comando y presenta el resultado. `logica.py` contiene funciones que calculan o modifican datos. Si ambos están en la misma carpeta del proyecto, `import logica` permite usar `logica.precio_final(...)`.

                    El nombre del archivo es parte de la importación: `import logica` busca un módulo `logica.py` disponible. Evita llamar a un archivo propio `json.py` o `csv.py`, porque podría ocultar el módulo de la biblioteca estándar. Las pruebas de Proyectos preparan ambos archivos en una carpeta temporal y ejecutan `main.py`; tus borradores siguen guardados para la siguiente etapa.
                """),
                section("Primero, una función con contrato", """
                    Escribe en `logica.py` una función que reciba datos y devuelva un resultado. El contrato de `precio_final` es: recibe precio y descuento en porcentaje, devuelve el precio después del descuento. `return` permite que `main.py` decida si lo imprime, lo guarda o lo usa en otra operación. Evita llamar a `input()` dentro de la función: así puedes probarla directamente con valores conocidos.

                    Para 100 y 20, calcula 20 por ciento de descuento: el resultado esperado es 80.0. Para 50 y 0, es 50.0. Pensar en más de un caso impide escribir una respuesta fija que solo coincida con el ejemplo.
                """, """\
                    # Archivo: logica.py
                    def precio_final(precio, descuento):
                        return precio * (1 - descuento / 100)
                """),
                section("Luego, el programa que lo usa", """
                    En `main.py`, la importación hace disponible el nombre `logica`. Cada `input()` consume una línea y entrega texto; por eso se convierte con `float`. `print` es responsabilidad de la capa que se comunica con la persona. Guarda este código en `main.py` junto al `logica.py` anterior y ejecútalo con dos líneas de entrada. También puedes escribir ambos archivos en el editor del reto «Separar lógica y programa».

                    La condición `if __name__ == "__main__"` ejecuta la función `main` al iniciar el archivo directamente. Si otro módulo importa `main.py`, no pide datos por sorpresa. No necesitas esa condición para los ejercicios más cortos, pero ayuda a organizar programas que crecerán.
                """, """\
                    # Archivo: main.py
                    import logica

                    def main():
                        precio = float(input())
                        descuento = float(input())
                        print(logica.precio_final(precio, descuento))

                    if __name__ == "__main__":
                        main()
                """),
                section("Qué revisar si falla el import", """
                    `ModuleNotFoundError: No module named 'logica'` puede significar que el archivo no existe, está en otra carpeta o tiene un nombre diferente, por ejemplo `lógica.py` con tilde. Comprueba las pestañas del editor y la línea exacta del import. Si importas `from logica import precio_final`, podrás llamar `precio_final(...)` sin el prefijo; elige una forma y úsala de manera consistente.

                    Evita que `logica.py` importe `main.py` a su vez: un ciclo de importaciones complica entender qué se define primero. Piensa en una dirección sencilla: `main.py` depende de `logica.py`, pero la lógica no necesita conocer cómo se pide entrada. Para la etapa siguiente, añade una función a `logica.py` y llama a esa función desde `main.py` conservando la anterior.
                """, note="Prueba de comprensión: si main.py importa logica.py, ¿en cuál archivo debería estar input()? En main.py."),
            ],
            ["import permite usar funciones de otro archivo disponible.",
             "main.py coordina entrada y salida; logica.py calcula o guarda datos.",
             "Una función con parámetros y return se puede probar sin teclado."],
            [("Tutorial de módulos", "https://docs.python.org/3.13/tutorial/modules.html")],
        ),
        chapter(
            "transformar-datos", "Transformar, agrupar y ordenar datos",
            "Patrones que aparecen al pasar del ejercicio al proyecto.", 10,
            [
                section("Del bucle a sum y una comprensión", """
                    Un acumulador como `total = 0` seguido de `total += monto` es una buena primera solución. Cuando ya entiendes el bucle, `sum(...)` puede expresar la misma intención en una línea. Una comprensión de lista como `[n * 2 for n in numeros]` construye una lista nueva; una expresión generadora como `(n * 2 for n in numeros)` entrega valores a medida que se piden. `sum` acepta esa expresión sin crear una lista intermedia.

                    No comprimas una transformación que todavía no puedes explicar. Lee `sum(int(fila["monto"]) for fila in ventas)` de adentro hacia afuera: para cada fila, toma la cadena monto, conviértela a entero y suma los enteros. Una lista vacía suma cero.
                """, """\
                    ventas = [{"monto": "12"}, {"monto": "8"}]
                    importes = [int(fila["monto"]) for fila in ventas]
                    print(importes)  # [12, 8]
                    print(sum(int(fila["monto"]) for fila in ventas))  # 20
                """),
                section("Agrupar con un diccionario", """
                    Para obtener un total por categoría, un único número no basta: necesitas asociar cada categoría con su acumulado. Empieza con `totales = {}`. Si la categoría aún no apareció, `totales.get(categoria, 0)` aporta el cero inicial; después añades el monto. Si ya había 12 para comida y llega 7, el nuevo valor es 19. Este patrón se usa en «Generar un informe JSON» y en el resumen del gestor de gastos.

                    Dibuja el estado del diccionario tras cada fila antes de ejecutar: tras `comida,12` queda `{"comida": 12}`; tras `transporte,8` aparece otra clave; tras `comida,7` se actualiza la primera. Si creas un diccionario nuevo en cada vuelta, perderás el acumulado.
                """, """\
                    filas = [("comida", 12), ("transporte", 8), ("comida", 7)]
                    totales = {}
                    for categoria, monto in filas:
                        totales[categoria] = totales.get(categoria, 0) + monto
                    print(totales)  # {'comida': 19, 'transporte': 8}
                """),
                section("Ordenar y filtrar sin perder datos", """
                    `sorted(iterable)` crea una lista ordenada sin modificar el iterable original. `sorted(totales)` ordena las claves de un diccionario; después puedes consultar `totales[categoria]`. Para ordenar objetos por un campo, `key=lambda p: p["sku"]` describe qué valor se compara. La `lambda` es una función breve; podrías escribir una función `def clave(p): return p["sku"]` si eso te resulta más claro.

                    Una comprensión con `if` filtra: `[p for p in productos if p["stock"] <= limite]` conserva solo los productos bajos. En el inventario, prueba un límite que incluya alguno y otro que no incluya ninguno. Cuando el resultado esté vacío, el enunciado pide imprimir `(ninguno)`.
                """, """\
                    productos = [{"sku": "B", "stock": 5}, {"sku": "A", "stock": 3}]
                    bajos = [p for p in productos if p["stock"] <= 3]
                    for producto in sorted(bajos, key=lambda p: p["sku"]):
                        print(f"{producto['sku']}:{producto['stock']}")  # A:3
                """),
                section("Máximos y casos vacíos", """
                    Al añadir una tarea necesitas un identificador mayor que los existentes. `max(...)` obtiene el mayor, pero una secuencia vacía no tiene máximo y provocaría `ValueError`. `max((t["id"] for t in tareas), default=0) + 1` resuelve el caso inicial: si no hay tareas, la nueva recibe id 1. Si ya existen 1, 2 y 5, recibirá 6; contar elementos y sumar uno daría un identificador repetido.

                    Estas herramientas son formas compactas de patrones que ya conoces: recorrer, comparar, filtrar y acumular. Si una línea te resulta difícil, escríbela como un bucle explícito, comprueba su resultado y solo después decide si la forma compacta ayuda a leer el programa.
                """, """\
                    tareas = [{"id": 1}, {"id": 5}]
                    siguiente = max((t["id"] for t in tareas), default=0) + 1
                    print(siguiente)  # 6
                    print(max((t["id"] for t in []), default=0) + 1)  # 1
                """, "Predice el resultado si los identificadores son 2 y 9. Respuesta: 10."),
            ],
            ["sum acumula valores; una comprensión construye o filtra colecciones.",
             "Un diccionario acumulador agrupa por clave.",
             "sorted ordena; max(..., default=0) cubre el caso vacío."],
            [("Estructuras de datos", "https://docs.python.org/3.13/tutorial/datastructures.html"),
             ("Funciones incorporadas", "https://docs.python.org/3.13/library/functions.html")],
        ),
        chapter(
            "clases-objetos", "Clases y objetos con estado",
            "Organizar datos y operaciones que pertenecen a la misma entidad.", 10,
            [
                section("La idea de una clase", """
                    Una clase describe cómo serán los objetos de cierto tipo. La clase `Cuenta` puede indicar que cada cuenta tiene un saldo y sabe depositar o retirar. `Cuenta(10)` crea un objeto con saldo inicial 10; `Cuenta(50)` crea otro objeto independiente. La clase es la definición, mientras cada objeto es una instancia concreta. No necesitas clases para todo: una función suele bastar cuando solo transformas datos sin conservar estado.

                    En el reto «Cuenta con métodos», el programa lee un saldo inicial y varias operaciones. La clase guarda el saldo entre operaciones. Antes de escribir `class`, identifica qué dato pertenece a cada objeto y qué operaciones deberían modificarlo. Si el saldo es una variable global, dos cuentas terminarían compartiendo accidentalmente el mismo estado.
                """, """\
                    class Cuenta:
                        def __init__(self, saldo):
                            self.saldo = saldo

                    primera = Cuenta(10)
                    segunda = Cuenta(50)
                    print(primera.saldo, segunda.saldo)  # 10 50
                """),
                section("self, __init__ y métodos", """
                    `__init__` se ejecuta al crear la instancia y establece sus atributos iniciales. `self` representa la instancia con la que se está trabajando. Al llamar `cuenta.depositar(5)`, Python entrega `cuenta` como primer argumento del método y 5 como `cantidad`. Por eso la definición lleva `self`, aunque la llamada habitual no lo escribe.

                    `self.saldo += cantidad` modifica el objeto. En cambio, `saldo += cantidad` dentro del método intentaría cambiar un nombre local y no actualizaría el atributo. Un método puede también devolver un valor: podrías hacer que `retirar` devuelva `False` si no hay fondos. En el reto inicial todas las operaciones se consideran válidas, así que concéntrate en actualizar el estado correctamente.
                """, """\
                    class Cuenta:
                        def __init__(self, saldo):
                            self.saldo = saldo

                        def depositar(self, cantidad):
                            self.saldo += cantidad

                        def retirar(self, cantidad):
                            self.saldo -= cantidad

                    cuenta = Cuenta(10)
                    cuenta.depositar(5)
                    cuenta.retirar(3)
                    print(f"Saldo: {cuenta.saldo}")  # Saldo: 12
                """),
                section("Seguir el estado paso a paso", """
                    Para la secuencia saldo 10, `+ 5`, `- 3`, dibuja una tabla: antes de empezar 10, tras depositar 15 y tras retirar 12. Esa tabla es una predicción; ejecuta luego el programa y compárala. Prueba también una cuenta que comienza en cero y otra que solo recibe retiros. Si creas una nueva instancia dentro del bucle, perderás el saldo anterior en cada vuelta.

                    Los métodos de una clase no están obligados a imprimir. Suele ser más flexible que actualicen o devuelvan datos y que `main.py` imprima al final. Así puedes probar el estado después de cada operación sin depender de un texto exacto. En un proyecto grande, las clases son una opción de diseño; los proyectos de la plataforma también muestran cómo resolver problemas con funciones y diccionarios.
                """, note="Antes de ejecutar: con saldo inicial 20, retirar 8 y depositar 2, ¿cuál es el saldo final? 14."),
                section("Errores comunes", """
                    Un `AttributeError` puede indicar que olvidaste asignar `self.saldo` en `__init__` o que escribiste otro nombre. Un `TypeError` al crear la cuenta puede indicar que no pasaste el saldo requerido. Si ves un resultado correcto una sola vez pero incorrecto tras varias operaciones, revisa si el método modifica `self.saldo` y si conservas la misma instancia.

                    Haz primero que el ejemplo mínimo de dos operaciones funcione. Después añade lectura de líneas hasta fin de entrada y decide según el signo. El reto evalúa varias secuencias, así que imprimir siempre «Saldo: 12» no sirve. Si necesitas repasar por qué `self` apunta a un objeto, vuelve al capítulo de variables, objetos y referencias.
                """),
            ],
            ["Una clase define el comportamiento; cada instancia conserva su estado.",
             "self permite leer y cambiar atributos de la instancia.",
             "Comprueba la evolución del estado, no solo la última impresión."],
            [("Clases en el tutorial", "https://docs.python.org/3.13/tutorial/classes.html")],
        ),
        chapter(
            "sqlite-practico", "SQLite: guardar y consultar registros",
            "Una base local para datos que necesitan consultas.", 10,
            [
                section("Cuándo usar una base de datos", """
                    Un CSV sirve para filas y un JSON para estructuras pequeñas, pero consultar, actualizar o relacionar muchos registros puede volverse incómodo si reescribes un archivo entero. SQLite guarda tablas en un archivo local `.db` y permite pedir filas mediante SQL. El módulo estándar `sqlite3` conecta Python con esa base. No necesitas iniciar un servidor de base de datos para los ejercicios de este curso.

                    Una tabla tiene columnas y filas. En `movimientos`, cada fila puede tener `nombre` y `monto`. `CREATE TABLE` define la estructura, `INSERT` añade, `SELECT` consulta. Antes de programar, escribe en papel dos filas y la consulta que quieres responder; en «Registrar movimientos» la pregunta es «¿cuál es la suma de monto?».
                """),
                section("Conectar, crear, insertar y consultar", """
                    `sqlite3.connect("ejemplo.db")` abre o crea la base en la carpeta de trabajo. El ejemplo crea una tabla si no existe. `INSERT OR IGNORE` con un id fijo permite ejecutarlo otra vez sin duplicar la fila de demostración. En un programa de registro real, cada movimiento nuevo recibiría su propio id. Los signos `?` son marcadores de parámetros: la tupla de valores se pasa por separado, sin construir SQL mediante f-strings.

                    El bloque `with conexion:` confirma los cambios si todo sale bien o los revierte si ocurre una excepción; no cierra por sí mismo la conexión. Por eso el ejemplo la cierra en `finally`. `fetchone()[0]` toma la primera columna de la primera fila del resultado de `SUM`. `COALESCE(..., 0)` convierte la suma vacía en cero.
                """, """\
                    import sqlite3

                    conexion = sqlite3.connect("ejemplo.db")
                    try:
                        with conexion:
                            conexion.execute(
                                "CREATE TABLE IF NOT EXISTS movimientos "
                                "(id INTEGER PRIMARY KEY, nombre TEXT, monto INTEGER)"
                            )
                            conexion.execute(
                                "INSERT OR IGNORE INTO movimientos VALUES (?, ?, ?)",
                                (1, "Ana", 5),
                            )
                        total = conexion.execute(
                            "SELECT COALESCE(SUM(monto), 0) FROM movimientos"
                        ).fetchone()[0]
                        print(f"Total: {total}")  # Total: 5
                    finally:
                        conexion.close()
                """),
                section("Leer filas y evitar consultas inseguras", """
                    `SELECT nombre, monto FROM movimientos` devuelve filas; `fetchall()` las reúne en una lista. Si la consulta depende de un nombre escrito por una persona, usa `WHERE nombre = ?` y pasa el nombre en una tupla: `(nombre,)`. La coma distingue una tupla de un solo elemento de unos paréntesis de agrupación. Construir la consulta como `f"WHERE nombre = '{nombre}'"` es frágil y permite que la entrada altere el SQL.

                    Para el reto, lee cada línea `nombre,monto`, convierte el monto a entero, inserta con parámetros y calcula la suma con SQL. El corrector revisa también las filas guardadas en `movimientos.db`. Si imprimes el total correcto sin crear la tabla e insertar los movimientos, la etapa no pasa.
                """, """\
                    import sqlite3

                    conexion = sqlite3.connect("ejemplo.db")
                    try:
                        nombre = "Ana"
                        filas = conexion.execute(
                            "SELECT nombre, monto FROM movimientos WHERE nombre = ?",
                            (nombre,),
                        ).fetchall()
                        print(filas)  # [('Ana', 5)] después del ejemplo anterior
                    finally:
                        conexion.close()
                """),
                section("Errores y decisiones de diseño", """
                    Si ejecutas `CREATE TABLE movimientos (...)` sin `IF NOT EXISTS` por segunda vez sobre el mismo archivo, aparecerá un error porque la tabla ya existe. Si abres la base en otra carpeta, puedes crear por accidente otro archivo vacío con el mismo nombre. Comprueba la carpeta de trabajo y usa rutas claras en proyectos propios. Para pruebas automáticas, usa bases temporales independientes.

                    SQLite es útil cuando necesitas consultas o actualizaciones selectivas; JSON sigue siendo suficiente para configuraciones pequeñas o una lista simple. Elige por las operaciones que exige el programa. Cuando cambies datos, comprueba tanto la respuesta impresa como el estado persistido.
                """, note="Predice: ¿qué devuelve COALESCE(SUM(monto), 0) si no hay movimientos? 0."),
            ],
            ["sqlite3 conecta con un archivo .db y ejecuta SQL.",
             "Los valores variables se pasan con parámetros ?, nunca pegados al SQL.",
             "Comprueba las filas persistidas además del mensaje en consola."],
            [("Guía de sqlite3", "https://docs.python.org/3.13/library/sqlite3.html")],
        ),
        chapter(
            "terminal-argumentos", "Programas de terminal con argparse",
            "Recibir opciones al iniciar, además de leer líneas con input().", 10,
            [
                section("Dos formas de recibir datos", """
                    `input()` consume una línea cuando el programa ya está en ejecución. Los argumentos de terminal se entregan al iniciarlo: `python saludo.py --nombre Ana --veces 2`. Esto permite lanzar un programa desde una terminal, un archivo de comandos o una tarea programada sin responder preguntas interactivas. El módulo `sys` expone los argumentos en `sys.argv`, pero `argparse` facilita definirlos y genera ayuda y errores útiles.

                    Separa el nombre de la opción del valor. `--veces` es la opción; `2` es su valor. Si el programa recibe la opción en otro orden, debería comportarse igual. En «Argumentos de terminal», el corrector ejecuta el archivo con varios conjuntos de argumentos, incluido cero repeticiones.
                """),
                section("Definir y analizar opciones", """
                    Crea un `ArgumentParser`, añade `--nombre` como texto obligatorio y `--veces` como entero obligatorio. `parse_args()` lee los argumentos y devuelve un objeto con atributos `args.nombre` y `args.veces`. Si alguien escribe `--veces hola`, el analizador informa que se esperaba un entero; no necesitas convertirlo manualmente con `int`.

                    Guarda el ejemplo como `saludo.py` y ejecútalo en PowerShell con `python saludo.py --nombre Ana --veces 2`: deben salir dos líneas «Hola, Ana». Usa `python saludo.py --help` para ver las opciones. En el editor de Proyectos, la plataforma prepara esos argumentos automáticamente para cada prueba.
                """, """\
                    # Archivo: saludo.py
                    import argparse

                    def main():
                        parser = argparse.ArgumentParser(description="Repite un saludo")
                        parser.add_argument("--nombre", required=True)
                        parser.add_argument("--veces", type=int, required=True)
                        args = parser.parse_args()
                        for _ in range(args.veces):
                            print(f"Hola, {args.nombre}")

                    if __name__ == "__main__":
                        main()
                """),
                section("Opcionales, valores por defecto y ayuda", """
                    No todas las opciones deben ser obligatorias. `parser.add_argument("--veces", type=int, default=1)` permite omitirla y saludar una vez. `help="Número de saludos"` explica una opción en `--help`. Un argumento posicional se define sin guiones, por ejemplo `parser.add_argument("archivo")`; la persona deberá escribirlo en la posición esperada.

                    El diseño de la interfaz depende del contrato: si el enunciado exige `--veces`, usa `required=True` aunque un programa distinto pudiera tener un valor por defecto. Prueba un caso con cero y otro con más de una repetición; no imprimas un saludo de más por colocar `print` fuera o dentro del bucle equivocado.
                """, """\
                    import argparse

                    parser = argparse.ArgumentParser()
                    parser.add_argument("--veces", type=int, default=1)
                    opciones = parser.parse_args(["--veces", "3"])
                    print(opciones.veces)  # 3
                """),
                section("Errores frecuentes", """
                    Escribir `input()` en lugar de `parse_args()` hace que el programa espere una línea que el corrector no envía para este reto. Leer `sys.argv[1]` directamente funciona en casos mínimos, pero se rompe si falta la posición o cambian de orden las opciones. `argparse` se encarga del análisis y muestra una explicación cuando los argumentos no cumplen el formato.

                    Distingue el comando de PowerShell del código Python: `python saludo.py --nombre Ana --veces 2` se escribe en la terminal; las llamadas a `ArgumentParser` van dentro del archivo `.py`. Antes de ejecutar, predice cuántas líneas producirá `--veces 0`: ninguna.
                """, note="Prueba de comprensión: cambia el orden a --veces 2 --nombre Ana. El resultado debe ser el mismo."),
            ],
            ["input() lee durante la ejecución; argparse procesa opciones al iniciarla.",
             "type=int convierte y valida el valor de una opción.",
             "--help documenta cómo usar el programa."],
            [("Módulo argparse", "https://docs.python.org/3.13/library/argparse.html"),
             ("Tutorial de argparse", "https://docs.python.org/3.13/howto/argparse.html")],
        ),
        chapter(
            "registros-logging", "Registros: entender qué hizo el programa",
            "Guardar avisos y errores sin mezclar diagnóstico con la salida esperada.", 10,
            [
                section("print frente a logging", """
                    `print` es adecuado para el resultado que espera quien usa el programa. Un registro describe acontecimientos internos: una operación completada, un aviso o un error. El módulo `logging` permite asignar niveles como `DEBUG`, `INFO`, `WARNING` y `ERROR`. Así puedes conservar mensajes de diagnóstico sin llenar la salida principal ni alterar el formato que comprueba un reto.

                    En «Registrar un aviso», el programa debe leer un texto, escribir en `app.log` una línea `WARNING:MENSAJE` y mostrar «Aviso guardado». Son dos salidas distintas: un archivo de registro y la consola. Imprimir la palabra WARNING no crea el archivo pedido.
                """),
                section("Configurar un archivo de registro", """
                    `logging.basicConfig` fija el destino, el nivel mínimo y el formato. `filename="app.log"` elige el archivo. `level=logging.WARNING` deja pasar avisos y errores. `format="%(levelname)s:%(message)s"` produce exactamente el nivel y el mensaje separados por dos puntos. `encoding="utf-8"` conserva los acentos. Aquí `filemode="w"` inicia un registro nuevo al ejecutar de nuevo el ejemplo y `force=True` sustituye configuraciones previas del proceso.

                    El programa de abajo escribe «Sin datos» y luego lee el archivo para mostrar su contenido. `logging.shutdown()` vacía y cierra los manejadores antes de leerlo inmediatamente. En una aplicación normal el sistema de registros gestiona sus manejadores durante la vida del proceso; aquí lo hacemos explícito para que el ejemplo sea reproducible.
                """, """\
                    import logging

                    logging.basicConfig(
                        filename="app.log",
                        level=logging.WARNING,
                        format="%(levelname)s:%(message)s",
                        encoding="utf-8",
                        filemode="w",
                        force=True,
                    )
                    logging.warning("Sin datos")
                    logging.shutdown()
                    with open("app.log", encoding="utf-8") as archivo:
                        print(archivo.read().strip())  # WARNING:Sin datos
                """),
                section("Qué registrar y qué evitar", """
                    Registra el contexto que ayude a investigar: qué operación falló y con qué tipo de problema. No registres contraseñas, claves de acceso ni datos personales innecesarios. Un `logging.warning` no equivale a lanzar una excepción: el programa continúa a menos que tú decidas otro flujo. Para errores que deban detener una operación, primero diseña cómo se recuperará o notificará la situación.

                    En el reto, cada prueba empieza en una carpeta temporal limpia. Por eso se espera exactamente un aviso en `app.log`. Si usas `print` dentro de una función que el corrector espera silenciosa, puedes crear salida extra; usa el registro para diagnóstico y conserva el formato pedido de consola.
                """),
                section("Diagnosticar un registro incorrecto", """
                    Si el archivo no aparece, comprueba `filename` y la carpeta de trabajo. Si aparece vacío al leerlo inmediatamente, asegúrate de que el mensaje alcanzó el nivel configurado y de que el manejador escribió antes de leer. Si se añaden mensajes de ejecuciones anteriores en un programa propio, decide si quieres anexar o iniciar un archivo nuevo; documenta esa elección.

                    Para practicar, predice qué pasará si configuras el nivel en `ERROR` pero llamas `logging.warning`: ese aviso no se escribirá. Después cambia el nivel a `WARNING` y comprueba el archivo. Esta diferencia entre configurar y emitir un mensaje es la misma idea que separar definición y llamada en funciones.
                """, note="Reto breve: cambia el texto por «Conexión lenta». ¿Qué línea exacta debe quedar en app.log? WARNING:Conexión lenta"),
            ],
            ["print muestra el resultado; logging registra acontecimientos.",
             "El nivel y el formato determinan qué se guarda y cómo se ve.",
             "Comprueba el archivo generado, no solo la salida en consola."],
            [("Módulo logging", "https://docs.python.org/3.13/library/logging.html"),
             ("Guía básica de logging", "https://docs.python.org/3.13/howto/logging.html")],
        ),
        chapter(
            "fechas-datetime", "Fechas y desplazamientos de días",
            "De texto ISO a cálculos correctos al cruzar meses y años.", 10,
            [
                section("Una fecha no es una cadena cualquiera", """
                    `"2024-02-28"` es texto. Podrías separar sus partes y sumar 2 al día, pero obtendrías `2024-02-30`, una fecha imposible. El módulo `datetime` ofrece `date` para representar una fecha del calendario y `timedelta` para una duración. `date.fromisoformat(texto)` interpreta una fecha `YYYY-MM-DD`; `fecha.isoformat()` la convierte de nuevo a ese formato.

                    En «Calcular una fecha futura», la entrada trae una fecha y un número entero de días. La salida debe conservar el formato ISO. El corrector prueba cambios de mes y un año bisiesto para descubrir soluciones que tratan el día como un número aislado.
                """),
                section("Sumar o restar días", """
                    `timedelta(days=2)` representa dos días. La expresión `fecha + timedelta(days=2)` produce una fecha nueva; no cambia el objeto original. Para retroceder, usa un número negativo. El calendario decide automáticamente si febrero tiene 28 o 29 días y cuándo empieza el siguiente mes o año.

                    Antes de ejecutar el ejemplo, predice el resultado del 28 de febrero de 2024 más dos días. Como 2024 es bisiesto, se pasa por el 29 de febrero y se llega al 1 de marzo. Una prueba adicional con `2025-12-31` más un día debe producir `2026-01-01`.
                """, """\
                    from datetime import date, timedelta

                    fecha = date.fromisoformat("2024-02-28")
                    nueva = fecha + timedelta(days=2)
                    print(nueva.isoformat())  # 2024-03-01
                    print((nueva + timedelta(days=-1)).isoformat())  # 2024-02-29
                """),
                section("Convertir y validar entradas", """
                    `fromisoformat` espera una cadena con una fecha válida; una fecha como `2024-02-30` provoca `ValueError`. `int(input())` puede provocar también `ValueError` si la cantidad de días no es un entero. En el reto se entregan entradas que cumplen el formato descrito, pero un programa usado por otras personas debería explicar qué dato fue inválido y pedirlo de nuevo o terminar con un mensaje claro.

                    La fecha inicial y los días son tipos distintos. No concatenes `"2024-02-28" + "2"` ni modifiques solo los últimos dos caracteres del texto: esas operaciones no saben nada del calendario. Convierte primero, calcula con objetos de fecha y formatea al final.
                """, """\
                    from datetime import date, timedelta

                    texto_fecha = "2025-12-31"
                    texto_dias = "1"
                    resultado = date.fromisoformat(texto_fecha) + timedelta(days=int(texto_dias))
                    print(resultado.isoformat())  # 2026-01-01
                """),
                section("Fecha frente a fecha y hora", """
                    `date` representa año, mes y día. `datetime` representa además hora, minutos y otros componentes. Si una aplicación necesita instantes comparables entre lugares, debe considerar zonas horarias; una fecha sola no indica a qué hora ocurrió algo. El reto se limita a fechas y desplazamientos enteros de días, así que `date` es la herramienta más simple.

                    Haz tres comprobaciones antes de cerrar el reto: cambio de mes, cambio de año y desplazamiento negativo. Este patrón de probar límites se aplica también a inventario, descuentos y conteos: los errores suelen aparecer en fronteras que el ejemplo normal no cubre.
                """, note="Predice: 2024-03-01 más -1 día produce 2024-02-29."),
            ],
            ["date.fromisoformat convierte texto ISO a una fecha.",
             "timedelta(days=n) desplaza la fecha a través de meses y años.",
             "Prueba límites, incluidos bisiestos y días negativos."],
            [("Módulo datetime", "https://docs.python.org/3.13/library/datetime.html")],
        ),
    ]
