"""Ejercicios 9-100. Cada solución se usa solo para verificar el banco de retos."""

from textwrap import indent


UNIT_NAMES = {
    1: "Primer contacto",
    2: "Números y operaciones",
    3: "Texto y cadenas",
    4: "Entrada de datos",
    5: "Decisiones",
    6: "Bucles",
    7: "Listas",
    8: "Diccionarios",
    9: "Funciones",
    10: "Retos integradores",
}

MORE = []


def P(number, unit, title, concept, example, task, hint, starter, solution, cases):
    """Add a complete-program exercise. cases are (input, expected output)."""
    MORE.append({
        "id": f"{number:02d}-programa", "number": number, "unit": unit,
        "unit_title": UNIT_NAMES[unit], "title": title,
        "subtitle": UNIT_NAMES[unit], "minutes": min(5 + unit, 12),
        "concept": concept, "example": example, "task": task,
        "hint": hint, "starter": starter, "solution": solution,
        "sample_input": cases[0][0], "sample_output": cases[0][1],
        "tests": [{"input": data, "expected": expected} for data, expected in cases],
    })


def F(number, unit, signature, title, concept, example, task, hint, body, cases):
    """Add a function exercise. cases are (argument expression, expected output)."""
    name = signature.split("(", 1)[0]
    source = f"def {signature}:\n" + indent(body, "    ")
    tests = [
        {"input": "", "suffix": f"\nprint({name}({args}))", "expected": expected}
        for args, expected in cases
    ]
    MORE.append({
        "id": f"{number:02d}-{name}", "number": number, "unit": unit,
        "unit_title": UNIT_NAMES[unit], "title": title,
        "subtitle": UNIT_NAMES[unit], "minutes": min(5 + unit, 12),
        "concept": concept, "example": example, "task": task,
        "hint": hint, "starter": f"def {signature}:\n    pass",
        "solution": source, "sample_input": "",
        "sample_output": cases[0][1], "preview_suffix": tests[0]["suffix"],
        "tests": tests,
    })


# Unidad 1: dos retos adicionales tras el recorrido inicial de ocho pasos.
P(9, 1, "Varias líneas", "Cada llamada a print() empieza una línea nueva.",
  'print("uno")\nprint("dos")', "Muestra Sol, Luna y Tierra, cada palabra en su propia línea.",
  "Usa tres instrucciones print().", 'print("Sol")\n# Sigue aquí',
  'print("Sol")\nprint("Luna")\nprint("Tierra")', [("", "Sol\nLuna\nTierra")])
P(10, 1, "Orden de ejecución", "Python ejecuta el programa de arriba hacia abajo.",
  'paso = "primero"\nprint(paso)', "Guarda inicio = 'Listo' y final = 'Vamos'. Muestra ambos valores en ese orden.",
  "Asigna las dos variables antes de imprimirlas.", 'inicio = "Listo"\nfinal = "Vamos"\n# Muestra ambos valores',
  'inicio = "Listo"\nfinal = "Vamos"\nprint(inicio)\nprint(final)', [("", "Listo\nVamos")])


# Unidad 2: operaciones con datos variables y casos de prueba distintos.
P(11, 2, "Suma dos números", "int(input()) convierte una entrada de texto en entero.",
  'a = int(input())\nprint(a + 1)', "Lee dos enteros, uno por línea, y muestra su suma.",
  "Convierte cada entrada con int().", 'a = int(input())\nb = int(input())\n# Muestra la suma',
  'a = int(input())\nb = int(input())\nprint(a + b)', [("3\n4", "7"), ("-2\n5", "3"), ("0\n0", "0")])
P(12, 2, "Resta dos números", "La resta conserva el orden de sus operandos: a - b.",
  'print(10 - 3)', "Lee a y b; muestra a menos b.", "Usa a - b, no b - a.",
  'a = int(input())\nb = int(input())\n# Resta',
  'a = int(input())\nb = int(input())\nprint(a - b)', [("9\n4", "5"), ("3\n8", "-5"), ("0\n0", "0")])
P(13, 2, "Multiplica", "El asterisco * representa la multiplicación.",
  'print(4 * 3)', "Lee dos enteros y muestra su producto.", "Escribe a * b.",
  'a = int(input())\nb = int(input())\n# Multiplica',
  'a = int(input())\nb = int(input())\nprint(a * b)', [("6\n7", "42"), ("-3\n5", "-15"), ("0\n8", "0")])
P(14, 2, "División entera", "El operador // da el cociente entero de una división.",
  'print(14 // 3)  # 4', "Lee dos enteros positivos y muestra el cociente entero de a entre b.",
  "Usa a // b.", 'a = int(input())\nb = int(input())\n# Cociente',
  'a = int(input())\nb = int(input())\nprint(a // b)', [("17\n5", "3"), ("20\n4", "5"), ("2\n3", "0")])
P(15, 2, "Residuo", "El operador % devuelve lo que sobra al dividir.",
  'print(14 % 3)  # 2', "Lee dos enteros positivos y muestra el residuo de a entre b.",
  "Usa a % b.", 'a = int(input())\nb = int(input())\n# Residuo',
  'a = int(input())\nb = int(input())\nprint(a % b)', [("17\n5", "2"), ("20\n4", "0"), ("2\n3", "2")])
P(16, 2, "Potencias", "El operador ** eleva un número a una potencia.",
  'print(2 ** 3)  # 8', "Lee base y exponente; muestra base elevada a exponente.",
  "Prueba base ** exponente.", 'base = int(input())\nexponente = int(input())\n# Potencia',
  'base = int(input())\nexponente = int(input())\nprint(base ** exponente)', [("2\n4", "16"), ("3\n2", "9"), ("5\n0", "1")])
P(17, 2, "Prioridad de operaciones", "Python multiplica antes de sumar; los paréntesis cambian el orden.",
  'print(2 + 3 * 4)  # 14', "Lee a, b y c; muestra a + b * c.",
  "Escribe la expresión tal como aparece.", 'a = int(input())\nb = int(input())\nc = int(input())\n# Calcula',
  'a = int(input())\nb = int(input())\nc = int(input())\nprint(a + b * c)', [("2\n3\n4", "14"), ("5\n2\n6", "17")])
P(18, 2, "Promedio de tres", "El operador / produce una división con decimales.",
  'print((2 + 4) / 2)  # 3.0', "Lee tres enteros y muestra su promedio como número decimal.",
  "Suma primero los tres valores entre paréntesis y divide entre 3.",
  'a = int(input())\nb = int(input())\nc = int(input())\n# Promedio',
  'a = int(input())\nb = int(input())\nc = int(input())\nprint((a + b + c) / 3)', [("3\n4\n5", "4.0"), ("1\n2\n3", "2.0")])
P(19, 2, "Precio con descuento", "Un descuento de 10 % deja el 90 % del precio original.",
  'print(100 * 90 / 100)  # 90.0', "Lee un precio entero y muestra su precio tras descontar 10 %.",
  "Multiplica el precio por 90 y divide entre 100.", 'precio = int(input())\n# Aplica el descuento',
  'precio = int(input())\nprint(precio * 90 / 100)', [("100", "90.0"), ("50", "45.0"), ("200", "180.0")])
P(20, 2, "Minutos a segundos", "Una conversión combina una cantidad con un factor fijo.",
  'print(2 * 60)  # 120', "Lee un número entero de minutos y muestra cuántos segundos son.",
  "Multiplica por 60.", 'minutos = int(input())\n# Convierte',
  'minutos = int(input())\nprint(minutos * 60)', [("3", "180"), ("0", "0"), ("12", "720")])


# Unidad 3: funciones pequeñas para comprobar distintos textos.
F(21, 3, "longitud(texto)", "Mide un texto", "len() devuelve la cantidad de caracteres, incluidos los espacios.",
  'print(len("sol"))  # 3', "Define longitud(texto) y devuelve cuántos caracteres tiene.",
  "Devuelve len(texto).", 'return len(texto)', [('"Python"', "6"), ('"hola mundo"', "10"), ('""', "0")])
F(22, 3, "primera_letra(texto)", "Primera letra", "Los índices de una cadena empiezan en 0.",
  'print("gato"[0])  # g', "Define primera_letra(texto) y devuelve su primer carácter. Las pruebas usan textos no vacíos.",
  "Usa texto[0].", 'return texto[0]', [('"Python"', "P"), ('"sol"', "s")])
F(23, 3, "ultima_letra(texto)", "Última letra", "El índice -1 señala el último elemento.",
  'print("gato"[-1])  # o', "Define ultima_letra(texto) y devuelve su último carácter. Las pruebas usan textos no vacíos.",
  "Usa texto[-1].", 'return texto[-1]', [('"Python"', "n"), ('"sol"', "l")])
F(24, 3, "en_mayusculas(texto)", "Todo en mayúsculas", "El método .upper() crea una versión en mayúsculas.",
  'print("sol".upper())  # SOL', "Define en_mayusculas(texto) y devuelve el texto en mayúsculas.",
  "Usa texto.upper().", 'return texto.upper()', [('"Hola"', "HOLA"), ('"Python 3"', "PYTHON 3")])
F(25, 3, "en_minusculas(texto)", "Todo en minúsculas", "El método .lower() crea una versión en minúsculas.",
  'print("SOL".lower())  # sol', "Define en_minusculas(texto) y devuelve el texto en minúsculas.",
  "Usa texto.lower().", 'return texto.lower()', [('"HOLA"', "hola"), ('"PyThOn"', "python")])
F(26, 3, "sin_espacios(texto)", "Limpia los extremos", "El método .strip() elimina espacios al principio y al final.",
  'print("  hola  ".strip())', "Define sin_espacios(texto) y devuelve el texto sin espacios en sus extremos.",
  "Usa texto.strip().", 'return texto.strip()', [('"  hola  "', "hola"), ('"  dos palabras "', "dos palabras")])
F(27, 3, "cambiar_guiones(texto)", "Reemplaza caracteres", "El método .replace(viejo, nuevo) sustituye apariciones de un fragmento.",
  'print("a-b".replace("-", " "))', "Define cambiar_guiones(texto) y reemplaza cada guion por un espacio.",
  'Usa texto.replace("-", " ").', 'return texto.replace("-", " ")', [('"hola-mundo"', "hola mundo"), ('"a-b-c"', "a b c")])
F(28, 3, "etiqueta(nombre)", "Forma una etiqueta", "Una f-string inserta valores dentro de un texto.",
  'nombre = "Ana"\nprint(f"[{nombre}]")', "Define etiqueta(nombre) y devuelve el nombre entre corchetes, por ejemplo [Ana].",
  'Devuelve f"[{nombre}]".', 'return f"[{nombre}]"', [('"Ana"', "[Ana]"), ('"Sol"', "[Sol]")])
F(29, 3, "repetir(texto, veces)", "Repite texto", "Una cadena multiplicada por un entero se repite esa cantidad de veces.",
  'print("ja" * 3)  # jajaja', "Define repetir(texto, veces) y devuelve el texto repetido.",
  "Usa texto * veces.", 'return texto * veces', [('"ja", 3', "jajaja"), ('"x", 0', ""), ('"ab", 2', "abab")])
F(30, 3, "contar_palabras(texto)", "Cuenta palabras", "El método .split() separa un texto por espacios y devuelve una lista.",
  'print("uno dos".split())', "Define contar_palabras(texto) y devuelve la cantidad de palabras.",
  "Combina len() con texto.split().", 'return len(texto.split())', [('"uno dos tres"', "3"), ('"  hola   mundo "', "2"), ('""', "0")])


# Unidad 4: programas que reciben una o varias entradas.
P(31, 4, "Saluda a dos personas", "Cada llamada a input() consume una línea de entrada.",
  'primero = input()\nsegundo = input()\nprint(primero, segundo)', "Lee dos nombres y muestra 'Hola, NOMBRE1 y NOMBRE2'.",
  "Guarda cada nombre y usa una f-string.", 'nombre1 = input()\nnombre2 = input()\n# Saluda',
  'nombre1 = input()\nnombre2 = input()\nprint(f"Hola, {nombre1} y {nombre2}")',
  [("Ana\nLuis", "Hola, Ana y Luis"), ("Sol\nMar", "Hola, Sol y Mar")])
P(32, 4, "Presentación con edad", "La edad llega como texto; una f-string puede incluirla directamente.",
  'nombre = input()\nedad = input()\nprint(f"{nombre}: {edad}")', "Lee nombre y edad. Muestra 'NOMBRE tiene EDAD años'.",
  "Lee dos veces y construye una f-string.", 'nombre = input()\nedad = input()\n# Preséntate',
  'nombre = input()\nedad = input()\nprint(f"{nombre} tiene {edad} años")',
  [("Ana\n20", "Ana tiene 20 años"), ("Leo\n8", "Leo tiene 8 años")])
P(33, 4, "Suma decimales", "float() convierte texto a número decimal.",
  'numero = float(input())\nprint(numero * 2)', "Lee dos números decimales y muestra su suma.",
  "Usa float(input()) para cada valor.", 'a = float(input())\nb = float(input())\n# Suma',
  'a = float(input())\nb = float(input())\nprint(a + b)',
  [("1.5\n2.0", "3.5"), ("0.25\n0.75", "1.0"), ("-1.5\n2.5", "1.0")])
P(34, 4, "Celsius a Fahrenheit", "La fórmula es Fahrenheit = Celsius × 9 / 5 + 32.",
  'print(0 * 9 / 5 + 32)  # 32.0', "Lee grados Celsius como entero y muestra su equivalente en Fahrenheit.",
  "Aplica la fórmula con la variable celsius.", 'celsius = int(input())\n# Convierte',
  'celsius = int(input())\nprint(celsius * 9 / 5 + 32)',
  [("0", "32.0"), ("100", "212.0"), ("-40", "-40.0")])
P(35, 4, "Área de un rectángulo", "El área es ancho por alto.",
  'print(3 * 4)  # 12', "Lee ancho y alto como enteros; muestra el área.",
  "Multiplica ancho * alto.", 'ancho = int(input())\nalto = int(input())\n# Área',
  'ancho = int(input())\nalto = int(input())\nprint(ancho * alto)',
  [("3\n5", "15"), ("10\n2", "20")])
P(36, 4, "Perímetro de un rectángulo", "El perímetro suma los cuatro lados: 2 × (ancho + alto).",
  'print(2 * (3 + 4))  # 14', "Lee ancho y alto como enteros; muestra el perímetro.",
  "Usa 2 * (ancho + alto).", 'ancho = int(input())\nalto = int(input())\n# Perímetro',
  'ancho = int(input())\nalto = int(input())\nprint(2 * (ancho + alto))',
  [("3\n5", "16"), ("10\n2", "24")])
P(37, 4, "Kilogramos a gramos", "Un kilogramo equivale a 1000 gramos.",
  'print(2 * 1000)', "Lee una cantidad decimal de kilogramos y muestra los gramos.",
  "Convierte con float(input()) y multiplica por 1000.", 'kilos = float(input())\n# Convierte',
  'kilos = float(input())\nprint(kilos * 1000)',
  [("1.5", "1500.0"), ("0.25", "250.0"), ("2", "2000.0")])
P(38, 4, "Segundos a minutos", "// obtiene los minutos completos y % los segundos sobrantes.",
  'print(125 // 60, 125 % 60)  # 2 5', "Lee segundos enteros. Muestra 'M min S s', por ejemplo '2 min 5 s'.",
  "Calcula segundos // 60 y segundos % 60.", 'segundos = int(input())\n# Descompón el tiempo',
  'segundos = int(input())\nprint(f"{segundos // 60} min {segundos % 60} s")',
  [("125", "2 min 5 s"), ("60", "1 min 0 s"), ("45", "0 min 45 s")])
P(39, 4, "Invierte el orden", "Las variables permiten guardar dos entradas antes de mostrarlas.",
  'a = input()\nb = input()\nprint(b, a)', "Lee dos palabras. Muéstralas en orden inverso, una por línea.",
  "Imprime primero la segunda variable.", 'primera = input()\nsegunda = input()\n# Invierte',
  'primera = input()\nsegunda = input()\nprint(segunda)\nprint(primera)',
  [("sol\nluna", "luna\nsol"), ("rojo\nazul", "azul\nrojo")])
P(40, 4, "Costo de entradas", "Un precio unitario multiplicado por la cantidad da el costo total.",
  'precio = 10\ncantidad = 3\nprint(precio * cantidad)', "Lee precio unitario y cantidad como enteros; muestra el costo total.",
  "Multiplica las dos entradas.", 'precio = int(input())\ncantidad = int(input())\n# Total',
  'precio = int(input())\ncantidad = int(input())\nprint(precio * cantidad)',
  [("25\n3", "75"), ("12\n0", "0"), ("7\n10", "70")])


# Unidad 5: decisiones con varias entradas de prueba.
F(41, 5, "signo(numero)", "Positivo, negativo o cero", "if, elif y else cubren tres posibilidades.",
  'if x > 0:\n    print("positivo")', "Define signo(numero) y devuelve 'positivo', 'negativo' o 'cero'.",
  "Compara con 0 usando > y <.", 'if numero > 0:\n    return "positivo"\nif numero < 0:\n    return "negativo"\nreturn "cero"',
  [('5', "positivo"), ('-3', "negativo"), ('0', "cero")])
F(42, 5, "paridad(numero)", "Par o impar", "Un número es par cuando su residuo al dividir entre 2 es 0.",
  'print(8 % 2)  # 0', "Define paridad(numero) y devuelve 'par' o 'impar'.",
  "Comprueba numero % 2 == 0.", 'if numero % 2 == 0:\n    return "par"\nreturn "impar"',
  [('8', "par"), ('7', "impar"), ('0', "par")])
F(43, 5, "mayor(a, b)", "El mayor de dos", "Una comparación permite escoger entre dos valores.",
  'print(9 > 4)  # True', "Define mayor(a, b) y devuelve el mayor de ambos números.",
  "Usa if a >= b.", 'if a >= b:\n    return a\nreturn b',
  [('8, 3', "8"), ('2, 9', "9"), ('4, 4', "4")])
F(44, 5, "menor(a, b)", "El menor de dos", "El operador <= incluye el caso en que los valores son iguales.",
  'print(2 <= 3)  # True', "Define menor(a, b) y devuelve el menor de ambos números.",
  "Usa if a <= b.", 'if a <= b:\n    return a\nreturn b',
  [('8, 3', "3"), ('2, 9', "2"), ('4, 4', "4")])
F(45, 5, "es_adulto(edad)", "Mayoría de edad", "Una función puede devolver un booleano: True o False.",
  'print(20 >= 18)  # True', "Define es_adulto(edad) y devuelve True si edad es al menos 18.",
  "Devuelve directamente la comparación edad >= 18.", 'return edad >= 18',
  [('20', "True"), ('17', "False"), ('18', "True")])
F(46, 5, "aprobado(nota)", "Calificación aprobatoria", "El límite también debe funcionar exactamente en la frontera.",
  'print(6 >= 6)  # True', "Define aprobado(nota) y devuelve True cuando nota es 6 o más.",
  "Usa nota >= 6.", 'return nota >= 6',
  [('7', "True"), ('5', "False"), ('6', "True")])
F(47, 5, "en_rango(numero)", "Dentro de un rango", "and exige que se cumplan dos condiciones a la vez.",
  'print(1 <= 5 and 5 <= 10)', "Define en_rango(numero) y devuelve True si está entre 1 y 10, incluidos ambos límites.",
  "Comprueba numero >= 1 and numero <= 10.", 'return 1 <= numero and numero <= 10',
  [('1', "True"), ('10', "True"), ('0', "False"), ('11', "False")])
F(48, 5, "comparar(a, b)", "Compara dos números", "Tres resultados posibles requieren revisar mayor, menor e igualdad.",
  'print(4 == 4)  # True', "Define comparar(a, b) y devuelve 'mayor', 'menor' o 'igual' según a frente a b.",
  "Revisa a > b, luego a < b y finalmente la igualdad.", 'if a > b:\n    return "mayor"\nif a < b:\n    return "menor"\nreturn "igual"',
  [('5, 2', "mayor"), ('2, 5', "menor"), ('4, 4', "igual")])
F(49, 5, "bisiesto(anio)", "Año bisiesto", "Un año divisible por 4 es bisiesto, salvo los siglos que no son divisibles por 400.",
  'print(2024 % 4 == 0)  # True', "Define bisiesto(anio) y devuelve True o False según esa regla.",
  "Usa % con 4, 100 y 400.", 'return anio % 400 == 0 or (anio % 4 == 0 and anio % 100 != 0)',
  [('2024', "True"), ('1900', "False"), ('2000', "True"), ('2023', "False")])
F(50, 5, "envio(total)", "Costo de envío", "Las condiciones pueden determinar un precio adicional.",
  'if total >= 500:\n    print(0)', "Define envio(total): devuelve 0 si total es 500 o más; en otro caso devuelve 50.",
  "Comprueba el umbral 500.", 'if total >= 500:\n    return 0\nreturn 50',
  [('600', "0"), ('499', "50"), ('500', "0")])


# Unidad 6: acumuladores, contadores y repeticiones.
F(51, 6, "suma_hasta(n)", "Suma del 1 al n", "Un acumulador conserva el resultado parcial de un bucle.",
  'total = 0\nfor x in range(1, 4):\n    total += x', "Define suma_hasta(n) y devuelve 1 + 2 + ... + n. Para n=0 devuelve 0.",
  "Empieza con total = 0 y recorre range(1, n + 1).", 'total = 0\nfor numero in range(1, n + 1):\n    total += numero\nreturn total',
  [('5', "15"), ('1', "1"), ('0', "0")])
F(52, 6, "factorial(n)", "Producto acumulado", "Para multiplicar en un bucle, el acumulador empieza en 1.",
  'producto = 1\nproducto *= 3', "Define factorial(n) y devuelve 1 × 2 × ... × n. Para 0 devuelve 1.",
  "Multiplica los números de range(1, n + 1).", 'producto = 1\nfor numero in range(1, n + 1):\n    producto *= numero\nreturn producto',
  [('4', "24"), ('0', "1"), ('1', "1"), ('6', "720")])
F(53, 6, "contar_pares(n)", "Cuenta pares", "Un contador aumenta solo cuando se cumple una condición.",
  'if 4 % 2 == 0:\n    cuenta += 1', "Define contar_pares(n) y cuenta los pares desde 1 hasta n, incluido n.",
  "Recorre el rango y suma 1 cuando numero % 2 == 0.", 'cuenta = 0\nfor numero in range(1, n + 1):\n    if numero % 2 == 0:\n        cuenta += 1\nreturn cuenta',
  [('6', "3"), ('5', "2"), ('1', "0"), ('0', "0")])
F(54, 6, "sumar_pares(n)", "Suma los pares", "Puedes filtrar dentro del bucle con if.",
  'for x in range(1, 5):\n    if x % 2 == 0:\n        print(x)', "Define sumar_pares(n) y suma los pares desde 1 hasta n.",
  "Usa un acumulador y añade solamente números pares.", 'total = 0\nfor numero in range(1, n + 1):\n    if numero % 2 == 0:\n        total += numero\nreturn total',
  [('6', "12"), ('5', "6"), ('1', "0")])
F(55, 6, "contar_digitos(n)", "Cuenta dígitos", "Un while repite mientras su condición sea verdadera.",
  'while n >= 10:\n    n //= 10', "Define contar_digitos(n) para enteros no negativos; devuelve cuántos dígitos tiene. El 0 tiene uno.",
  "Empieza en 1 y divide n entre 10 mientras n >= 10.", 'cuenta = 1\nwhile n >= 10:\n    n //= 10\n    cuenta += 1\nreturn cuenta',
  [('0', "1"), ('7', "1"), ('1234', "4")])
F(56, 6, "cuenta_atras(n)", "Cuenta regresiva", "range(inicio, fin, paso) admite un paso negativo.",
  'print(list(range(3, 0, -1)))', "Define cuenta_atras(n) y devuelve una lista de n hasta 1. Para 0 devuelve [].",
  "Recorre range(n, 0, -1) y añade cada número a una lista.", 'resultado = []\nfor numero in range(n, 0, -1):\n    resultado.append(numero)\nreturn resultado',
  [('4', "[4, 3, 2, 1]"), ('1', "[1]"), ('0', "[]")])
F(57, 6, "sumar_digitos(n)", "Suma de dígitos", "% 10 obtiene el último dígito y // 10 lo elimina.",
  'print(123 % 10)  # 3', "Define sumar_digitos(n) para enteros no negativos y suma sus dígitos.",
  "Repite mientras n > 0 y acumula n % 10.", 'total = 0\nwhile n > 0:\n    total += n % 10\n    n //= 10\nreturn total',
  [('123', "6"), ('90', "9"), ('0', "0")])
F(58, 6, "primer_multiplo(numero, minimo)", "Busca un múltiplo", "Un while puede avanzar hasta encontrar el primer valor que cumple una regla.",
  'x = 10\nwhile x % 3 != 0:\n    x += 1', "Define primer_multiplo(numero, minimo). Devuelve el primer múltiplo de numero que sea al menos minimo. numero será positivo.",
  "Empieza en minimo y aumenta hasta que valor % numero sea 0.", 'valor = minimo\nwhile valor % numero != 0:\n    valor += 1\nreturn valor',
  [('3, 10', "12"), ('5, 20', "20"), ('4, 1', "4")])
F(59, 6, "apariciones(texto, letra)", "Cuenta apariciones", "Un for también puede recorrer cada carácter de un texto.",
  'for letra in "sol":\n    print(letra)', "Define apariciones(texto, letra) y cuenta cuántas veces aparece esa letra.",
  "Aumenta un contador cuando carácter == letra.", 'cuenta = 0\nfor caracter in texto:\n    if caracter == letra:\n        cuenta += 1\nreturn cuenta',
  [('"banana", "a"', "3"), ('"Python", "x"', "0"), ('"aaa", "a"', "3")])
F(60, 6, "potencia_repetida(base, exponente)", "Potencia con un bucle", "La multiplicación repetida permite construir una potencia.",
  'resultado = 1\nfor paso in range(3):\n    resultado *= 2', "Define potencia_repetida(base, exponente) con un bucle. El exponente será no negativo.",
  "Empieza resultado en 1 y multiplica por base tantas veces como indique exponente.", 'resultado = 1\nfor paso in range(exponente):\n    resultado *= base\nreturn resultado',
  [('2, 5', "32"), ('3, 0', "1"), ('4, 2', "16")])


# Unidad 7: colecciones ordenadas.
F(61, 7, "tamano_lista(datos)", "Longitud de una lista", "len() sirve tanto para textos como para listas.",
  'print(len([2, 4, 6]))  # 3', "Define tamano_lista(datos) y devuelve el número de elementos.",
  "Devuelve len(datos).", 'return len(datos)', [('[2, 4, 6]', "3"), ('[]', "0"), ('["x"]', "1")])
F(62, 7, "total_lista(datos)", "Suma una lista", "sum() suma números dentro de una lista.",
  'print(sum([1, 2, 3]))  # 6', "Define total_lista(datos) y devuelve la suma de sus números.",
  "Usa sum(datos) o un acumulador.", 'return sum(datos)', [('[2, 4, 6]', "12"), ('[]', "0"), ('[-2, 5]', "3")])
F(63, 7, "mayor_lista(datos)", "Máximo de una lista", "max() devuelve el mayor elemento. Aquí las listas nunca están vacías.",
  'print(max([3, 8, 2]))  # 8', "Define mayor_lista(datos) y devuelve su número mayor.",
  "Usa max(datos).", 'return max(datos)', [('[3, 8, 2]', "8"), ('[-5, -2, -9]', "-2")])
F(64, 7, "menor_lista(datos)", "Mínimo de una lista", "min() devuelve el menor elemento. Aquí las listas nunca están vacías.",
  'print(min([3, 8, 2]))  # 2', "Define menor_lista(datos) y devuelve su número menor.",
  "Usa min(datos).", 'return min(datos)', [('[3, 8, 2]', "2"), ('[-5, -2, -9]', "-9")])
F(65, 7, "extremos(datos)", "Primer y último elemento", "Los índices 0 y -1 toman los extremos de una lista.",
  'print([4, 5, 6][0])  # 4', "Define extremos(datos) y devuelve una lista con el primer y el último elemento. La lista de entrada no estará vacía.",
  "Devuelve [datos[0], datos[-1]].", 'return [datos[0], datos[-1]]', [('[1, 2, 3]', "[1, 3]"), ('[9]', "[9, 9]")])
F(66, 7, "invertir_lista(datos)", "Lista al revés", "El corte [::-1] crea una copia en orden inverso.",
  'print([1, 2, 3][::-1])', "Define invertir_lista(datos) y devuelve los elementos en orden inverso.",
  "Prueba datos[::-1].", 'return datos[::-1]', [('[1, 2, 3]', "[3, 2, 1]"), ('[]', "[]"), ('["a", "b"]', "['b', 'a']")])
F(67, 7, "veces_en_lista(datos, valor)", "Cuenta un valor", "El método .count() cuenta coincidencias exactas.",
  'print([1, 1, 2].count(1))  # 2', "Define veces_en_lista(datos, valor) y devuelve cuántas veces aparece valor.",
  "Usa datos.count(valor).", 'return datos.count(valor)', [('[1, 2, 1, 3], 1', "2"), ('[4, 5], 2', "0")])
F(68, 7, "agregar(datos, valor)", "Agrega al final", "El método .append() modifica una lista añadiendo un elemento al final.",
  'lista = [1]\nlista.append(2)\nprint(lista)', "Define agregar(datos, valor), añade valor al final y devuelve la lista.",
  "Llama datos.append(valor) antes de devolver datos.", 'datos.append(valor)\nreturn datos', [('[1, 2], 3', "[1, 2, 3]"), ('[], "a"', "['a']")])
F(69, 7, "solo_positivos(datos)", "Filtra números", "Un bucle puede construir una nueva lista que cumpla una condición.",
  'nuevos = []\nfor n in [1, -2]:\n    if n > 0:\n        nuevos.append(n)', "Define solo_positivos(datos) y devuelve una nueva lista con los números mayores que 0.",
  "Crea resultado = [] y añade n cuando n > 0.", 'resultado = []\nfor numero in datos:\n    if numero > 0:\n        resultado.append(numero)\nreturn resultado',
  [('[2, -1, 0, 5]', "[2, 5]"), ('[-3, 0]', "[]"), ('[1, 2]', "[1, 2]")])
F(70, 7, "promedio_lista(datos)", "Promedio de una lista", "El promedio es la suma dividida por la cantidad de elementos.",
  'print(sum([2, 4]) / len([2, 4]))', "Define promedio_lista(datos) y devuelve el promedio decimal. Las listas no estarán vacías.",
  "Usa sum(datos) / len(datos).", 'return sum(datos) / len(datos)',
  [('[2, 4, 6]', "4.0"), ('[1, 2]', "1.5"), ('[10]', "10.0")])


# Unidad 8: pares clave-valor y conteos.
F(71, 8, "buscar_precio(precios, producto)", "Busca por clave", "Un diccionario relaciona claves con valores.",
  'precios = {"pan": 12}\nprint(precios["pan"])', "Define buscar_precio(precios, producto) y devuelve su precio. La clave existirá.",
  "Accede a precios[producto].", 'return precios[producto]',
  [('{"pan": 12, "leche": 25}, "pan"', "12"), ('{"pan": 12, "leche": 25}, "leche"', "25")])
F(72, 8, "precio_o_cero(precios, producto)", "Clave opcional", "El método .get(clave, valor) evita un error cuando falta la clave.",
  'print({"pan": 12}.get("agua", 0))', "Define precio_o_cero(precios, producto): devuelve su precio o 0 si no existe.",
  "Usa precios.get(producto, 0).", 'return precios.get(producto, 0)',
  [('{"pan": 12}, "pan"', "12"), ('{"pan": 12}, "agua"', "0")])
F(73, 8, "cantidad_claves(datos)", "Cuenta claves", "len() sobre un diccionario cuenta sus pares clave-valor.",
  'print(len({"a": 1, "b": 2}))', "Define cantidad_claves(datos) y devuelve cuántas claves contiene.",
  "Usa len(datos).", 'return len(datos)',
  [('{"a": 1, "b": 2}', "2"), ('{}', "0")])
F(74, 8, "sumar_valores(datos)", "Suma valores", "El método .values() permite recorrer los valores de un diccionario.",
  'print(sum({"a": 2, "b": 3}.values()))', "Define sumar_valores(datos) y suma sus valores numéricos.",
  "Combina sum() y datos.values().", 'return sum(datos.values())',
  [('{"a": 2, "b": 3}', "5"), ('{}', "0"), ('{"x": -2, "y": 6}', "4")])
F(75, 8, "lista_claves(datos)", "Lista de claves", "Al recorrer un diccionario obtienes sus claves.",
  'for clave in {"a": 1}:\n    print(clave)', "Define lista_claves(datos) y devuelve una lista con las claves en su orden de inserción.",
  "Usa list(datos).", 'return list(datos)',
  [('{"a": 1, "b": 2}', "['a', 'b']"), ('{}', "[]")])
F(76, 8, "guardar_puntaje(datos, nombre, puntos)", "Actualiza un valor", "Asignar datos[clave] = valor crea o reemplaza un par.",
  'puntos = {}\npuntos["Ana"] = 5', "Define guardar_puntaje(datos, nombre, puntos). Guarda ese puntaje y devuelve el diccionario.",
  "Asigna datos[nombre] = puntos y devuelve datos.", 'datos[nombre] = puntos\nreturn datos',
  [('{"Ana": 3}, "Ana", 5', "{'Ana': 5}"), ('{}, "Sol", 2', "{'Sol': 2}")])
F(77, 8, "frecuencias(datos)", "Frecuencias", "Un diccionario sirve para contar cuántas veces aparece cada elemento.",
  'cuenta = {}\ncuenta["a"] = cuenta.get("a", 0) + 1', "Define frecuencias(datos) y devuelve un diccionario con el conteo de cada elemento, en orden de primera aparición.",
  "Usa resultado.get(elemento, 0) + 1 en un bucle.", 'resultado = {}\nfor elemento in datos:\n    resultado[elemento] = resultado.get(elemento, 0) + 1\nreturn resultado',
  [('["a", "b", "a"]', "{'a': 2, 'b': 1}"), ('[]', "{}"), ('[1, 1, 2]', "{1: 2, 2: 1}")])
F(78, 8, "invertir_mapa(datos)", "Invierte claves y valores", "Si los valores son únicos, pueden convertirse en claves de otro diccionario.",
  'nuevo = {}\nnuevo[1] = "a"', "Define invertir_mapa(datos). Devuelve un nuevo diccionario con valores como claves y claves como valores. Los valores serán únicos.",
  "Recorre las claves y asigna nuevo[datos[clave]] = clave.", 'nuevo = {}\nfor clave in datos:\n    nuevo[datos[clave]] = clave\nreturn nuevo',
  [('{"a": 1, "b": 2}', "{1: 'a', 2: 'b'}"), ('{}', "{}")])
F(79, 8, "combinar_mapas(primero, segundo)", "Combina diccionarios", "Puedes copiar un diccionario y añadir las claves del segundo.",
  'nuevo = {"a": 1}\nnuevo["b"] = 2', "Define combinar_mapas(primero, segundo). Devuelve un nuevo diccionario; si una clave se repite, gana el valor de segundo.",
  "Copia las claves de primero y luego las de segundo en resultado.", 'resultado = {}\nfor clave in primero:\n    resultado[clave] = primero[clave]\nfor clave in segundo:\n    resultado[clave] = segundo[clave]\nreturn resultado',
  [('{"a": 1}, {"b": 2}', "{'a': 1, 'b': 2}"), ('{"x": 1}, {"x": 9}', "{'x': 9}")])
F(80, 8, "mejor_alumno(puntajes)", "Busca el puntaje mayor", "Puedes guardar la mejor clave encontrada mientras recorres el diccionario.",
  'for nombre in {"Ana": 8}:\n    print(nombre)', "Define mejor_alumno(puntajes) y devuelve el nombre con mayor puntaje. Si hay empate, conserva el primero. El diccionario no estará vacío.",
  "Guarda mejor y compara cada puntaje con el de mejor.", 'mejor = ""\nfor nombre in puntajes:\n    if mejor == "" or puntajes[nombre] > puntajes[mejor]:\n        mejor = nombre\nreturn mejor',
  [('{"Ana": 8, "Luis": 9}', "Luis"), ('{"Ana": 9, "Luis": 9}', "Ana"), ('{"Sol": 7}', "Sol")])


# Unidad 9: funciones reutilizables, parámetros y resultados.
F(81, 9, "cuadrado(numero)", "Función cuadrado", "Una función pequeña encapsula una operación reutilizable.",
  'def doble(x):\n    return x * 2', "Define cuadrado(numero) y devuelve numero al cuadrado.",
  "Puedes usar numero * numero.", 'return numero * numero',
  [('4', "16"), ('-3', "9"), ('0', "0")])
F(82, 9, "area_rectangulo(ancho, alto)", "Dos parámetros", "Cada parámetro representa un dato que recibe la función.",
  'def suma(a, b):\n    return a + b', "Define area_rectangulo(ancho, alto) y devuelve el área.",
  "Devuelve ancho * alto.", 'return ancho * alto',
  [('3, 5', "15"), ('10, 2', "20")])
F(83, 9, 'saludo_personalizado(nombre, prefijo="Hola")', "Valor predeterminado", "Un parámetro con valor predeterminado es opcional al llamar la función.",
  'def sumar(a, b=1):\n    return a + b', "Define saludo_personalizado(nombre, prefijo='Hola'). Devuelve 'PREFIJO, NOMBRE' usando el valor predeterminado cuando falte prefijo.",
  "Usa una f-string con prefijo y nombre.", 'return f"{prefijo}, {nombre}"',
  [('"Ana"', "Hola, Ana"), ('"Ana", "Buen día"', "Buen día, Ana")])
F(84, 9, "limitar(numero, minimo, maximo)", "Límite inferior y superior", "Una función puede devolver temprano si encuentra un caso especial.",
  'if x < 0:\n    return 0', "Define limitar(numero, minimo, maximo): devuelve minimo si número es menor, maximo si lo supera o el número en otro caso.",
  "Comprueba primero los dos extremos.", 'if numero < minimo:\n    return minimo\nif numero > maximo:\n    return maximo\nreturn numero',
  [('5, 0, 10', "5"), ('-2, 0, 10', "0"), ('15, 0, 10', "10")])
F(85, 9, "es_divisible(numero, divisor)", "Función booleana", "Una función puede devolver el resultado de una comparación directamente.",
  'def es_par(n):\n    return n % 2 == 0', "Define es_divisible(numero, divisor) y devuelve True si la división no tiene residuo. divisor será distinto de 0.",
  "Comprueba numero % divisor == 0.", 'return numero % divisor == 0',
  [('12, 3', "True"), ('13, 3', "False"), ('0, 5', "True")])
F(86, 9, "area_triangulo(base, altura)", "Resultado decimal", "La fórmula del área triangular es base × altura / 2.",
  'print(4 * 3 / 2)  # 6.0', "Define area_triangulo(base, altura) y devuelve el área como número decimal.",
  "Devuelve base * altura / 2.", 'return base * altura / 2',
  [('4, 3', "6.0"), ('5, 2', "5.0"), ('3, 3', "4.5")])
F(87, 9, "fibonacci(n)", "Secuencia de Fibonacci", "Cada término es la suma de los dos anteriores: 0, 1, 1, 2, 3...",
  'a, b = 0, 1\na, b = b, a + b', "Define fibonacci(n) y devuelve el término de índice n, empezando con índice 0 igual a 0. n será no negativo.",
  "Repite n veces el cambio a, b = b, a + b.", 'a, b = 0, 1\nfor paso in range(n):\n    a, b = b, a + b\nreturn a',
  [('0', "0"), ('1', "1"), ('7', "13"), ('10', "55")])
F(88, 9, "suma_cuadrados(datos)", "Combina funciones y bucles", "Puedes transformar cada dato antes de sumarlo.",
  'total = 0\nfor n in [1, 2]:\n    total += n * n', "Define suma_cuadrados(datos) y devuelve la suma de los cuadrados de todos los números.",
  "Recorre datos y suma numero * numero.", 'total = 0\nfor numero in datos:\n    total += numero * numero\nreturn total',
  [('[1, 2, 3]', "14"), ('[]', "0"), ('[-2, 3]', "13")])
F(89, 9, "es_palindromo(texto)", "Palíndromo", "Un palíndromo se lee igual de ambos lados; aquí ignoramos las diferencias entre mayúsculas y minúsculas.",
  'print("oso" == "oso"[::-1])', "Define es_palindromo(texto). Devuelve True si el texto es palíndromo sin distinguir mayúsculas, pero conservando espacios y signos.",
  "Pasa a minúsculas y compara con [::-1].", 'limpio = texto.lower()\nreturn limpio == limpio[::-1]',
  [('"Oso"', "True"), ('"Python"', "False"), ('"Ana"', "True")])
F(90, 9, "letra_nota(nota)", "Transforma una nota", "Varias condiciones ordenadas permiten clasificar rangos.",
  'if nota >= 90:\n    return "A"', "Define letra_nota(nota): A para 90-100, B para 80-89, C para 70-79 y D para menos de 70.",
  "Revisa los límites de mayor a menor.", 'if nota >= 90:\n    return "A"\nif nota >= 80:\n    return "B"\nif nota >= 70:\n    return "C"\nreturn "D"',
  [('95', "A"), ('80', "B"), ('75', "C"), ('69', "D")])


# Unidad 10: problemas que combinan temas anteriores.
F(91, 10, "calcular_propina(total, porcentaje)", "Propina", "Un porcentaje es una fracción de 100.",
  'print(50 * 10 / 100)  # 5.0', "Define calcular_propina(total, porcentaje) y devuelve la propina como decimal.",
  "Multiplica total * porcentaje / 100.", 'return total * porcentaje / 100',
  [('100, 15', "15.0"), ('80, 10', "8.0"), ('50, 0', "0.0")])
F(92, 10, "indice_masa(peso, altura)", "Índice de masa corporal", "El IMC se calcula como peso / altura². round(valor, 2) redondea a dos decimales.",
  'print(round(10 / 3, 2))  # 3.33', "Define indice_masa(peso, altura) y devuelve el IMC redondeado a dos decimales. altura será positiva.",
  "Usa round(peso / (altura * altura), 2).", 'return round(peso / (altura * altura), 2)',
  [('72, 1.8', "22.22"), ('80, 2.0', "20.0"), ('50, 1.6', "19.53")])
F(93, 10, "calculadora(a, b, operador)", "Mini calculadora", "Una cadena puede indicar qué operación realizar.",
  'if signo == "+":\n    return a + b', "Define calculadora(a, b, operador) para '+', '-', '*' y '/'. Devuelve el resultado. En división, b no será 0.",
  "Usa if/elif para los cuatro operadores.", 'if operador == "+":\n    return a + b\nif operador == "-":\n    return a - b\nif operador == "*":\n    return a * b\nreturn a / b',
  [('8, 3, "+"', "11"), ('8, 3, "-"', "5"), ('8, 3, "*"', "24"), ('8, 2, "/"', "4.0")])
F(94, 10, "clave_valida(clave)", "Comprueba una clave", "Una regla puede combinar longitud y presencia de un dígito.",
  'for caracter in "abc1":\n    if caracter in "0123456789":\n        print("dígito")', "Define clave_valida(clave): devuelve True si tiene al menos 8 caracteres y algún dígito.",
  "Si len(clave) < 8 devuelve False; luego recorre los caracteres.", 'if len(clave) < 8:\n    return False\nfor caracter in clave:\n    if caracter in "0123456789":\n        return True\nreturn False',
  [('"clave123"', "True"), ('"claveabc"', "False"), ('"a1"', "False")])
F(95, 10, "total_carrito(precios, cantidades)", "Total de carrito", "Dos listas paralelas guardan el precio y la cantidad de cada producto.",
  'print(10 * 2 + 5 * 3)', "Define total_carrito(precios, cantidades). Multiplica cada precio por su cantidad y suma. Las listas tendrán la misma longitud.",
  "Recorre range(len(precios)) y suma precios[i] * cantidades[i].", 'total = 0\nfor indice in range(len(precios)):\n    total += precios[indice] * cantidades[indice]\nreturn total',
  [('[10, 5], [2, 3]', "35"), ('[], []', "0"), ('[7], [4]', "28")])
F(96, 10, "resumen_notas(notas)", "Resumen de calificaciones", "Un diccionario puede reunir varios resultados calculados.",
  'print({"promedio": 8.0, "aprobados": 2})', "Define resumen_notas(notas). Devuelve {'promedio': promedio decimal, 'aprobados': cantidad de notas >= 6}. La lista no estará vacía.",
  "Usa sum(notas) / len(notas) y cuenta las aprobadas en un bucle.", 'aprobados = 0\nfor nota in notas:\n    if nota >= 6:\n        aprobados += 1\nreturn {"promedio": sum(notas) / len(notas), "aprobados": aprobados}',
  [('[5, 7, 9]', "{'promedio': 7.0, 'aprobados': 2}"), ('[6, 6]', "{'promedio': 6.0, 'aprobados': 2}")])
F(97, 10, "stock_restante(inventario, producto, vendidos)", "Control de inventario", "get() permite tratar los productos inexistentes como stock 0.",
  'print(max(0, 3 - 5))  # 0', "Define stock_restante(inventario, producto, vendidos). Devuelve el stock tras vender, sin bajar de 0. Si no existe el producto, usa 0.",
  "Calcula max(0, inventario.get(producto, 0) - vendidos).", 'return max(0, inventario.get(producto, 0) - vendidos)',
  [('{"pan": 10}, "pan", 3', "7"), ('{"pan": 2}, "pan", 5', "0"), ('{}, "leche", 1', "0")])
F(98, 10, "palabras_frecuentes(texto)", "Frecuencia de palabras", "Convierte a minúsculas antes de separar palabras para un conteo uniforme.",
  'print("Hola hola".lower().split())', "Define palabras_frecuentes(texto) y devuelve un diccionario con la frecuencia de cada palabra, en orden de primera aparición.",
  "Recorre texto.lower().split() y usa get(palabra, 0).", 'resultado = {}\nfor palabra in texto.lower().split():\n    resultado[palabra] = resultado.get(palabra, 0) + 1\nreturn resultado',
  [('"Hola hola mundo"', "{'hola': 2, 'mundo': 1}"), ('"Sol LUNA sol"', "{'sol': 2, 'luna': 1}"), ('""', "{}")])
F(99, 10, "mas_frecuente(datos)", "El valor más frecuente", "Cuenta elementos y conserva el primer valor si hay empate.",
  'print(["a", "b", "a"].count("a"))', "Define mas_frecuente(datos) y devuelve el elemento más repetido. En empate, devuelve el que apareció primero. La lista no estará vacía.",
  "Cuenta en un diccionario; luego cambia el mejor solo si la cuenta es mayor.", 'cuentas = {}\nfor valor in datos:\n    cuentas[valor] = cuentas.get(valor, 0) + 1\nmejor = datos[0]\nfor valor in datos:\n    if cuentas[valor] > cuentas[mejor]:\n        mejor = valor\nreturn mejor',
  [('["a", "b", "a"]', "a"), ('[1, 2, 2, 1]', "1"), ('[7]', "7")])
F(100, 10, "total_pedido(productos)", "Proyecto final: pedido", "Combina una lista de pares (precio, cantidad), un acumulador y una decisión.",
  'for precio, cantidad in [(10, 2)]:\n    print(precio * cantidad)', "Define total_pedido(productos). Cada elemento es (precio, cantidad). Suma el subtotal. Si llega a 100, aplica 10 % de descuento; si es menor, suma 15 de envío. Devuelve el total decimal.",
  "Recorre los pares; al final decide con if subtotal >= 100.", 'subtotal = 0\nfor precio, cantidad in productos:\n    subtotal += precio * cantidad\nif subtotal >= 100:\n    return subtotal * 0.9\nreturn subtotal + 15.0',
  [('[(20, 2), (30, 2)]', "90.0"), ('[(10, 2)]', "35.0"), ('[(50, 1)]', "65.0")])


assert len(MORE) == 92, f"Se esperaban 92 ejercicios adicionales, hay {len(MORE)}"
assert [exercise["number"] for exercise in MORE] == list(range(9, 101))
