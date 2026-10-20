"""Ruta progresiva con 100 ejercicios originales en español."""

from curriculum_more import MORE, UNIT_NAMES
from learning_support import lesson_hints

LESSONS = [
    {
        "id": "01-hola-mundo",
        "title": "Tu primera instrucción",
        "subtitle": "Haz que Python muestre un mensaje.",
        "minutes": 4,
        "concept": "Programar consiste en darle instrucciones precisas a una computadora. Python ejecuta esas instrucciones de arriba hacia abajo. La función print() muestra texto en pantalla; el texto va entre comillas.",
        "example": 'print("Estoy aprendiendo Python")',
        "task": 'Escribe un programa que muestre exactamente: Hola, mundo',
        "hint": 'Usa print() y escribe el mensaje entre comillas: print("...")',
        "starter": '# Escribe tu mensaje aquí\nprint()',
        "sample_input": "",
        "sample_output": "Hola, mundo",
        "tests": [{"input": "", "expected": "Hola, mundo"}],
    },
    {
        "id": "02-variables",
        "title": "Guarda información",
        "subtitle": "Ponle un nombre a un valor para usarlo después.",
        "minutes": 5,
        "concept": "Una variable guarda un valor. Escribe su nombre, el signo = y el valor. Puedes usar la variable en una instrucción posterior. El signo = asigna; no significa ‘es igual a’ como en matemáticas.",
        "example": 'nombre = "Ana"\nprint(nombre)',
        "task": 'Crea una variable llamada nombre con el valor "Ada" y muestra: Hola, Ada',
        "hint": 'Puedes juntar textos con +: print("Hola, " + nombre)',
        "starter": 'nombre = ""\nprint()',
        "sample_input": "",
        "sample_output": "Hola, Ada",
        "tests": [{"input": "", "expected": "Hola, Ada"}],
    },
    {
        "id": "03-numeros",
        "title": "Calcula con números",
        "subtitle": "Suma, resta y combina operaciones.",
        "minutes": 6,
        "concept": "Los números no llevan comillas. Python puede operar con +, -, * y /. Guarda resultados en variables y usa print() para verlos. Si usas comillas, Python tratará el valor como texto.",
        "example": 'precio = 12\ncantidad = 3\nprint(precio * cantidad)',
        "task": "Una libreta cuesta 18 y compras 3. Guarda precio y cantidad en variables; muestra el total 54.",
        "hint": "Multiplica precio * cantidad y muestra el resultado con print().",
        "starter": 'precio = 18\ncantidad = 3\n# Calcula y muestra el total\n',
        "sample_input": "",
        "sample_output": "54",
        "tests": [{"input": "", "expected": "54"}],
    },
    {
        "id": "04-texto",
        "title": "Construye mensajes",
        "subtitle": "Combina texto y valores.",
        "minutes": 6,
        "concept": "Una cadena de texto se llama str. Puedes insertar variables en un mensaje con una f-string: antepón f a las comillas y escribe el nombre de la variable entre llaves. Así puedes mezclar texto y números sin convertirlos a mano.",
        "example": 'nombre = "Luz"\nedad = 21\nprint(f"{nombre} tiene {edad} años")',
        "task": 'Guarda producto = "lápiz" y precio = 7. Muestra exactamente: El lápiz cuesta 7 pesos',
        "hint": 'Prueba: print(f"El {producto} cuesta {precio} pesos")',
        "starter": 'producto = "lápiz"\nprecio = 7\n# Construye el mensaje con una f-string\n',
        "sample_input": "",
        "sample_output": "El lápiz cuesta 7 pesos",
        "tests": [{"input": "", "expected": "El lápiz cuesta 7 pesos"}],
    },
    {
        "id": "05-entrada",
        "title": "Escucha al usuario",
        "subtitle": "Haz que tu programa responda a distintos nombres.",
        "minutes": 7,
        "concept": "input() espera una respuesta y la devuelve como texto. Guarda ese texto en una variable. Un buen programa funciona con distintos datos, no solo con un ejemplo.",
        "example": 'nombre = input()\nprint(f"Hola, {nombre}")',
        "task": 'Lee un nombre con input() y muestra: Bienvenido, NOMBRE. Por ejemplo, si se ingresa Ana, muestra Bienvenido, Ana.',
        "hint": 'Guarda input() en nombre. Luego imprime una f-string que incluya nombre.',
        "starter": 'nombre = input()\n# Muestra el saludo\n',
        "sample_input": "Ana",
        "sample_output": "Bienvenido, Ana",
        "tests": [
            {"input": "Ana", "expected": "Bienvenido, Ana"},
            {"input": "Luis", "expected": "Bienvenido, Luis"},
            {"input": "Mar", "expected": "Bienvenido, Mar"},
        ],
    },
    {
        "id": "06-condiciones",
        "title": "Toma decisiones",
        "subtitle": "Ejecuta instrucciones según una condición.",
        "minutes": 8,
        "concept": "if ejecuta un bloque cuando una condición es verdadera; else cubre el otro caso. Los dos puntos abren el bloque y los espacios al inicio de la siguiente línea indican qué instrucciones pertenecen a él. int() convierte texto a número entero.",
        "example": 'edad = int(input())\nif edad >= 18:\n    print("Mayor")\nelse:\n    print("Menor")',
        "task": 'Lee una edad. Si es 18 o más, muestra "Puede entrar"; si no, muestra "Aún no puede entrar".',
        "hint": 'Usa edad = int(input()), luego if edad >= 18: y else: con print() en cada bloque.',
        "starter": 'edad = int(input())\nif edad >= 18:\n    print()\nelse:\n    print()',
        "sample_input": "20",
        "sample_output": "Puede entrar",
        "tests": [
            {"input": "20", "expected": "Puede entrar"},
            {"input": "17", "expected": "Aún no puede entrar"},
            {"input": "18", "expected": "Puede entrar"},
        ],
    },
    {
        "id": "07-bucles",
        "title": "Repite sin copiar",
        "subtitle": "Usa un bucle para contar.",
        "minutes": 8,
        "concept": "for repite un bloque de instrucciones. range(1, 4) produce los números 1, 2 y 3: el segundo límite no se incluye. En cada vuelta, la variable toma el siguiente valor.",
        "example": 'for numero in range(1, 4):\n    print(numero)',
        "task": "Usa un bucle for para mostrar los números del 1 al 5, cada uno en una línea.",
        "hint": "Prueba for numero in range(1, 6): y dentro print(numero).",
        "starter": 'for numero in range(1, 6):\n    # Muestra el número de esta vuelta\n    pass',
        "sample_input": "",
        "sample_output": "1\n2\n3\n4\n5",
        "tests": [{"input": "", "expected": "1\n2\n3\n4\n5"}],
    },
    {
        "id": "08-funciones",
        "title": "Crea tu propia función",
        "subtitle": "Agrupa instrucciones que puedas reutilizar.",
        "minutes": 9,
        "concept": "def define una función con nombre. Los parámetros reciben datos cuando la llamas. return devuelve un resultado. Aquí la plataforma llamará a tu función con varios nombres para comprobar que funciona siempre.",
        "example": 'def doble(numero):\n    return numero * 2\n\nprint(doble(4))',
        "task": 'Define una función saludar(nombre) que devuelva "Hola, NOMBRE!". No necesitas llamarla: la plataforma lo hará por ti.',
        "hint": 'Dentro de def saludar(nombre): usa return f"Hola, {nombre}!"',
        "starter": 'def saludar(nombre):\n    # Devuelve el saludo\n    return ""',
        "sample_input": "",
        "sample_output": "Hola, Ana!",
        "preview_suffix": '\nprint(saludar("Ana"))',
        "tests": [
            {"input": "", "suffix": '\nprint(saludar("Ana"))', "expected": "Hola, Ana!"},
            {"input": "", "suffix": '\nprint(saludar("Luis"))', "expected": "Hola, Luis!"},
            {"input": "", "suffix": '\nprint(saludar("Mar"))', "expected": "Hola, Mar!"},
        ],
    },
]

BASE_SOLUTIONS = {
    "01-hola-mundo": 'print("Hola, mundo")',
    "02-variables": 'nombre = "Ada"\nprint("Hola, " + nombre)',
    "03-numeros": 'precio = 18\ncantidad = 3\nprint(precio * cantidad)',
    "04-texto": 'producto = "lápiz"\nprecio = 7\nprint(f"El {producto} cuesta {precio} pesos")',
    "05-entrada": 'nombre = input()\nprint(f"Bienvenido, {nombre}")',
    "06-condiciones": 'edad = int(input())\nif edad >= 18:\n    print("Puede entrar")\nelse:\n    print("Aún no puede entrar")',
    "07-bucles": 'for numero in range(1, 6):\n    print(numero)',
    "08-funciones": 'def saludar(nombre):\n    return f"Hola, {nombre}!"',
}

for number, lesson in enumerate(LESSONS, start=1):
    lesson.update(number=number, unit=1, unit_title=UNIT_NAMES[1],
                  solution=BASE_SOLUTIONS[lesson["id"]])

LESSONS.extend(MORE)
assert len(LESSONS) == 100
LESSON_BY_ID = {lesson["id"]: lesson for lesson in LESSONS}


def public_lessons():
    """Return lesson data without answer keys or hidden check cases."""
    return [
        {key: value for key, value in lesson.items() if key not in {"tests", "preview_suffix", "solution"}}
        | {"hints": lesson_hints(lesson)}
        for lesson in LESSONS
    ]
