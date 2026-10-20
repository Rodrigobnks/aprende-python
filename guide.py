"""Manual original en español para acompañar los 100 ejercicios."""

from textwrap import dedent


def section(title, body, code="", note=""):
    return {
        "title": title,
        "paragraphs": [part.strip() for part in dedent(body).strip().split("\n\n")],
        "code": dedent(code).strip(),
        "note": note,
    }


def chapter(slug, title, subtitle, unit, sections, takeaways, sources=()):
    return {
        "id": slug, "title": title, "subtitle": subtitle,
        "unit": unit, "sections": sections, "takeaways": takeaways,
        "sources": [{"label": label, "url": url} for label, url in sources],
    }


GUIDE = [
    chapter(
        "bienvenida", "Cómo aprender con esta plataforma", "Una ruta de lectura y práctica desde cero.", 1,
        [
            section("Qué vas a aprender", """
                Programar es expresar una solución como instrucciones que una computadora puede ejecutar. Aquí no necesitas experiencia previa: empezamos con una línea que muestra un mensaje y llegamos a programas que leen archivos, guardan datos y se reparten entre varios módulos. La ruta tiene 100 ejercicios iniciales en diez bloques, 12 retos intermedios y tres proyectos de tres etapas. Conviene avanzar en orden, aunque puedes volver cuando quieras.

                El manual explica la idea con palabras y ejemplos; los ejercicios te obligan a aplicarla. Leer sin escribir código crea una sensación engañosa de dominio. Después de cada sección, intenta predecir qué mostrará el ejemplo antes de ejecutarlo. Si la predicción falla, identifica la línea exacta donde cambió tu expectativa.
            """),
            section("Método para resolver un reto", """
                Lee primero qué datos entran y qué resultado debe salir. Escribe un ejemplo pequeño a mano. Luego divide el problema en pasos: leer o recibir datos, transformarlos y mostrar o devolver un resultado. Escribe la versión más simple que puedas comprobar. Ejecutar muestra lo que pasa con el caso de ejemplo; Comprobar reto evalúa otros casos para descubrir si tu solución funciona de manera general.

                Si te atoras, revisa el mensaje de error, compara la salida esperada con la tuya y usa la pista. Volver a escribir una solución después de verla funciona mejor que copiarla sin entenderla. Un error no indica falta de capacidad: indica que tu modelo mental y el comportamiento de Python aún no coinciden.
            """),
            section("Qué significa completar un ejercicio", """
                La plataforma marca un ejercicio como completado cuando tu código pasa todas sus pruebas. Una prueba da ciertos datos y verifica la salida. Eso confirma el comportamiento observado en esos casos; no demuestra por sí solo que cualquier programa sea perfecto. Por eso incluimos límites, entradas distintas y valores especiales. Más adelante aprenderás a escribir tus propias pruebas.

                El editor de los 100 ejercicios iniciales permite un subconjunto de Python. El Laboratorio enseña a instalar e importar paquetes externos. La pestaña Proyectos permite trabajar con varios archivos `.py`, importar módulos propios, leer y escribir archivos de datos, usar clases, excepciones y SQLite. Cada editor corresponde a una etapa distinta de la ruta.
            """),
            section("Libros y referencias de esta ruta", """
                La progresión de conceptos toma como orientación *Think Python*, 3.ª edición, de Allen B. Downey: empezar por instrucciones pequeñas, construir modelos mentales de los tipos y avanzar hacia funciones y estructuras de datos. *Automate the Boring Stuff with Python*, 3.ª edición, de Al Sweigart, inspira la conexión entre cada idea y tareas prácticas. La documentación oficial de Python es la referencia para el comportamiento concreto del lenguaje y la biblioteca estándar.

                Este manual está escrito especialmente para la plataforma y sus ejemplos y ejercicios son originales. Los libros no son requisitos para usarla. Si deseas profundizar, sus enlaces están al final de este capítulo y en el README. La documentación oficial suele suponer cierta familiaridad previa con programación; aquí desglosamos los conceptos para empezar sin ella.
            """),
        ],
        ["Lee una idea, predice, escribe y comprueba.", "Los errores son información para ajustar tu razonamiento.", "El avance de los ejercicios y proyectos se conserva en tu equipo."],
        [("Think Python, 3.ª edición", "https://greenteapress.com/wp/think-python-3rd-edition/"),
         ("Automate the Boring Stuff, 3.ª edición", "https://automatetheboringstuff.com/"),
         ("Tutorial oficial", "https://docs.python.org/3.13/tutorial/index.html")],
    ),
    chapter(
        "que-es-python", "Qué es Python", "Lenguaje, intérprete y ecosistema: tres cosas relacionadas.", 1,
        [
            section("Python como lenguaje", """
                Python es un lenguaje de programación: un conjunto de reglas para escribir programas. Define una sintaxis —cómo se forman instrucciones válidas— y una semántica —qué significan esas instrucciones—. Por ejemplo, `print("Hola")` usa la función incorporada `print` para enviar texto a la salida. Las comillas indican que `Hola` es una cadena de caracteres, y los paréntesis contienen el argumento de la llamada.

                Se considera un lenguaje de propósito general porque puede servir para automatización, análisis de datos, aplicaciones web, enseñanza y muchos otros problemas. Que una tarea sea posible no implica que Python sea siempre la mejor herramienta; la elección depende del entorno, rendimiento, bibliotecas disponibles y conocimientos del equipo. Para aprender conceptos de programación, su sintaxis legible resulta especialmente útil.
            """, 'print("Hola")\nprint(2 + 3)'),
            section("Python como intérprete", """
                También llamamos Python al programa que lee y ejecuta código escrito en ese lenguaje. La implementación más común se llama CPython. Puedes abrirla de forma interactiva para probar instrucciones una por una, o pedirle que ejecute un archivo con extensión `.py`. Otras implementaciones de Python pueden ejecutar el mismo lenguaje con detalles internos distintos.

                En términos prácticos, tu archivo es texto; el intérprete entiende ese texto y realiza operaciones en memoria, recibe datos y produce resultados. El archivo no cambia por ejecutarlo, salvo que tu programa incluya instrucciones para escribir en él o en otros archivos.
            """, "python --version\npython mi_programa.py"),
            section("Python como ecosistema", """
                El lenguaje incluye piezas incorporadas, como `print`, `len`, `int` y tipos como listas o diccionarios. Además, una instalación normal contiene una biblioteca estándar: módulos para fechas, archivos, matemáticas, JSON y muchas tareas habituales. También existen bibliotecas de terceros que otras personas publican para problemas concretos. Estas capas explican por qué dos programas Python pueden tener necesidades de instalación diferentes.

                Esta plataforma utiliza Python en el servidor local, HTML y CSS para la pantalla, y JavaScript para los botones y el editor. Cuando presionas Comprobar reto, la página envía tu código al servidor local; este ejecuta el ejercicio y devuelve el resultado. Así puedes practicar Python desde el navegador sin instalar paquetes adicionales.
            """),
            section("Lo que Python no adivina", """
                El intérprete sigue instrucciones y reglas precisas. No conoce tu intención ni corrige automáticamente una variable mal escrita. `nombre`, `Nombre` y `nombres` son nombres diferentes. Tampoco interpreta una cadena como si fuera un número: `"2" + "3"` produce `"23"`, mientras `2 + 3` produce `5`. Buena parte del aprendizaje consiste en reconocer qué tipo de dato tienes y qué operación necesitas.
            """, 'print("2" + "3")  # 23\nprint(2 + 3)      # 5'),
        ],
        ["Python nombra al lenguaje y, en muchos contextos, a su intérprete.", "CPython es una implementación; la biblioteca estándar y las bibliotecas externas amplían lo disponible.", "El tipo de cada valor determina cómo se comportan las operaciones."],
        [("Tutorial oficial", "https://docs.python.org/3.13/tutorial/index.html"),
         ("Biblioteca estándar", "https://docs.python.org/3.13/library/index.html")],
    ),
    chapter(
        "como-funciona", "Cómo funciona un programa", "Del texto del archivo a un resultado visible.", 1,
        [
            section("Entrada, proceso y salida", """
                Un programa recibe información, hace operaciones con ella y produce algún efecto. La entrada puede venir del teclado, una función, un archivo o una red. El proceso puede calcular, comparar, repetir y organizar valores. La salida puede ser texto en pantalla, un valor devuelto por una función o un archivo guardado. Esta división ayuda a planear: primero identifica la entrada y la salida; después decide qué transformación las conecta.

                En un reto con `input()`, la entrada llega como texto. Si esperas sumar números, conviértela con `int` o `float`. `print` muestra un valor al usuario; `return` entrega un valor al código que llamó a una función. Son acciones distintas y muchas fallas iniciales vienen de confundirlas.
            """, 'edad = int(input())\nproxima = edad + 1\nprint(proxima)'),
            section("Qué ocurre al ejecutar un archivo", """
                Cuando invocas `python programa.py`, el sistema operativo inicia un proceso de Python. El intérprete lee el código fuente y comprueba su estructura. En CPython se transforma en una representación interna llamada código de bytes, que luego ejecuta la máquina virtual de CPython. Este detalle de implementación puede variar entre versiones e intérpretes; para resolver ejercicios basta pensar que Python analiza tus instrucciones y las ejecuta según las reglas del lenguaje.

                La ejecución de un módulo empieza por las instrucciones de nivel superior. Una definición `def` crea una función, pero su cuerpo no se ejecuta hasta que la llamas. Un `if` puede saltarse un bloque; un `for` puede repetirlo. Por eso no siempre se ejecuta cada línea exactamente una vez ni en simple orden visual.
            """, 'print("A")\ndef saludar():\n    print("B")\nprint("C")\nsaludar()  # A, C, B'),
            section("Memoria y nombres", """
                Durante la ejecución, Python mantiene objetos en memoria: números, cadenas, listas, funciones y más. Un nombre como `precio` se asocia con un objeto; al escribir `precio = 20` estableces esa relación. Si después haces `precio = 25`, el nombre pasa a referirse al nuevo valor. En cambio, algunas operaciones modifican un objeto existente: `lista.append(3)` altera la lista. Esta diferencia entre reasignar un nombre y mutar un objeto es esencial cuando compartes listas o diccionarios entre funciones.

                La memoria de un proceso normalmente se libera cuando este termina. Si quieres que un dato sobreviva, debes guardarlo de forma persistente, por ejemplo en un archivo o una base de datos. La plataforma guarda tu progreso en una base SQLite local.
            """, 'precio = 20\nprecio = 25\nnumeros = [1, 2]\nnumeros.append(3)'),
            section("Errores y terminación", """
                Hay errores detectados antes de ejecutar, como una sintaxis incompleta, y errores que aparecen durante la ejecución, como dividir entre cero. Cuando ocurre una excepción no atendida, Python detiene el camino actual y muestra información para localizar el problema. Un programa también puede terminar normalmente tras la última instrucción. Para entender una falla, mira el tipo de error, la línea señalada y los valores que estaban presentes.

                El editor de esta plataforma ejecuta cada intento en un proceso breve con límites de tiempo y salida. Así un bucle infinito no se queda ejecutando sin fin dentro de la lección. Es una protección para la práctica local; no convierte el editor en un aislamiento seguro para código de desconocidos.
            """),
        ],
        ["Identifica entrada, transformación y salida antes de escribir código.", "Definir una función y llamarla son momentos distintos.", "Los nombres se asocian con objetos; algunas operaciones reasignan y otras mutan."],
        [("Modelo de ejecución", "https://docs.python.org/3.13/reference/executionmodel.html"),
         ("Uso del intérprete", "https://docs.python.org/3.13/tutorial/interpreter.html")],
    ),
    chapter(
        "entorno", "Archivos, terminal y editor", "Dónde se escribe Python y cómo ponerlo en marcha.", 1,
        [
            section("Archivo frente a consola interactiva", """
                Un archivo `.py` guarda texto que puedes editar, revisar y ejecutar varias veces. La consola interactiva, reconocible por el indicador `>>>`, ejecuta pequeños fragmentos al escribirlos: resulta útil para comprobar expresiones rápidas. Si una solución requiere varias líneas, un archivo es más fácil de mantener. El editor de la plataforma funciona como un espacio de práctica: escribe código y usa los botones para enviarlo al Python local.

                La terminal ejecuta comandos del sistema, como `python app.py`. El código Python vive dentro de un archivo, en el intérprete interactivo o en el editor de ejercicios; escribir `python app.py` dentro de tu programa provocaría un error. Esta distinción entre comando de terminal e instrucción Python evita muchas confusiones al comenzar.
            """, "python --version\npython app.py"),
            section("Carpetas y rutas", """
                Los archivos se organizan en carpetas. Una ruta indica dónde está un archivo. La ruta relativa `programa.py` se interpreta desde la carpeta de trabajo actual; una ruta absoluta identifica una ubicación completa. Si la terminal dice que no encuentra `app.py`, comprueba que abriste la carpeta descomprimida de la plataforma antes de ejecutar el comando.

                En proyectos reales conviene mantener juntos el código, las pruebas y la documentación. Esta plataforma contiene `app.py` para el servidor, `curriculum.py` y `curriculum_more.py` para los ejercicios, y `guide.py` para este manual. No necesitas modificar esos archivos para usarla.
            """),
            section("Cómo practicar fuera de la plataforma", """
                Abre un editor de texto de código, crea `hola.py`, escribe `print("Hola")`, guarda y ejecuta `python hola.py` desde la carpeta correspondiente. La extensión `.py` indica que el archivo contiene código Python. Si una orden no funciona, revisa el mensaje completo: puede faltar Python, estar mal la ruta o haber un error dentro del archivo.

                También puedes practicar archivos y módulos propios dentro de la pestaña Proyectos, e instalar bibliotecas externas para el Laboratorio. Trabajar desde la terminal sigue siendo útil para crear programas tuyos fuera de los retos, ejecutarlos con argumentos y aprender a reconocer en qué carpeta se guardan sus datos.
            """, 'print("Hola")'),
        ],
        ["Un comando de terminal y una línea de Python viven en lugares distintos.", "La carpeta de trabajo determina cómo se resuelven rutas relativas.", "Un archivo `.py` permite guardar y repetir un programa."],
        [("Uso del intérprete", "https://docs.python.org/3.13/tutorial/interpreter.html")],
    ),
    chapter(
        "sintaxis", "Sintaxis, sangría y comentarios", "Las reglas que hacen legible y ejecutable el código.", 1,
        [
            section("Expresiones e instrucciones", """
                Una expresión produce un valor: `2 + 3`, `nombre` o `len(texto)`. Una instrucción realiza una acción dentro del programa: asignar con `=`, definir una función con `def`, elegir con `if` o repetir con `for`. Una línea puede contener una expresión dentro de una instrucción, como `total = precio * cantidad`. Python evalúa la expresión de la derecha y asocia el resultado con el nombre de la izquierda.

                Los paréntesis pueden indicar una llamada, como `print(5)`, o agrupar operaciones, como `(2 + 3) * 4`. Los dos puntos al final de `if`, `for`, `while` y `def` anuncian un bloque. La puntuación en código tiene un significado preciso; no es decoración.
            """, 'total = (2 + 3) * 4\nprint(total)  # 20'),
            section("Sangría y bloques", """
                La sangría son los espacios al inicio de una línea. En Python, las líneas con la misma sangría pertenecen al mismo bloque. Una instrucción `if` ejecuta su bloque solo si la condición se cumple. Al volver a la sangría anterior, el bloque termina. Habitualmente se usan cuatro espacios por nivel. Mezclar cantidades de espacios sin cuidado produce errores o cambia el comportamiento.

                Mira el ejemplo: `print("Siempre")` está fuera del bloque y se ejecuta aunque la condición sea falsa. La posición horizontal de cada línea forma parte de la lógica. Una práctica útil es señalar el bloque con el dedo y decir cuándo entra y cuándo sale el flujo.
            """, 'edad = 17\nif edad >= 18:\n    print("Puede entrar")\nprint("Siempre")'),
            section("Comentarios y nombres", """
                `#` inicia un comentario hasta el final de la línea. Python no lo ejecuta; sirve para explicar una decisión o dejar una pista a otra persona. Un comentario útil dice por qué se hace algo poco obvio, no repite literalmente la instrucción. Los nombres de variables distinguen mayúsculas: `precio` y `Precio` son diferentes. Es preferible usar nombres descriptivos como `total_compra` antes que `x` cuando el propósito no es evidente.

                Los identificadores no pueden contener espacios ni empezar por un número. Algunas palabras, como `if` y `return`, son palabras reservadas del lenguaje. La plataforma limita los nombres que empiezan por guion bajo en los retos iniciales; más adelante verás que Python los utiliza en ciertos convenios internos.
            """, '# Impuesto de ejemplo para calcular el total\nimpuesto = 0.16\ntotal_compra = 100 * (1 + impuesto)'),
            section("Errores de sintaxis comunes", """
                Olvidar una comilla, paréntesis o dos puntos suele producir `SyntaxError`. Una sangría incorrecta puede producir `IndentationError`, que es un tipo de error de sintaxis. El mensaje indica una línea cercana al problema, aunque la causa real puede estar justo antes. Revisa siempre el fragmento completo, desde el inicio del bloque hasta la línea marcada.
            """),
        ],
        ["La sangría define bloques y cambia el comportamiento.", "Una expresión produce un valor; una instrucción organiza o realiza acciones.", "Lee los mensajes de sintaxis junto con las líneas anteriores."],
        [("Introducción a Python", "https://docs.python.org/3.13/tutorial/introduction.html"),
         ("Control de flujo", "https://docs.python.org/3.13/tutorial/controlflow.html")],
    ),
    chapter(
        "variables", "Variables, objetos y tipos", "Qué se guarda en memoria y cómo se usa.", 2,
        [
            section("Asignar un nombre", """
                En `edad = 20`, Python evalúa el valor de la derecha y vincula el nombre `edad` con ese objeto. Después puedes usar el nombre en otras expresiones. La asignación no declara que `edad` deba ser siempre entero: en Python el tipo pertenece al objeto, y un nombre puede vincularse más adelante con otro tipo. Esa flexibilidad es útil, pero exige atención para no mezclar valores incompatibles.

                `=` asigna; `==` compara. `edad = 20` cambia a qué se refiere el nombre. `edad == 20` produce `True` o `False`. Una variable debe tener un valor asignado antes de que puedas leerla; si escribes un nombre inexistente, obtendrás `NameError`.
            """, 'edad = 20\nprint(edad + 1)\nedad = 21\nprint(edad == 21)'),
            section("Tipos frecuentes", """
                `int` representa enteros de tamaño arbitrario dentro de la memoria disponible. `float` representa números de punto flotante, adecuados para cálculos aproximados. `str` representa texto Unicode. `bool` tiene los valores `True` y `False`. `None` expresa ausencia de valor y tiene un tipo propio. Una lista (`list`) guarda elementos en orden; un diccionario (`dict`) relaciona claves con valores.

                La operación válida depende del tipo: sumar dos enteros calcula; sumar dos cadenas concatena; sumar un entero y una cadena produce `TypeError`. Usa conversiones explícitas cuando corresponde: `int("12")`, `float("2.5")` o `str(12)`. La conversión puede fallar si el texto no tiene la forma esperada.
            """, 'numero = int("12")\nmensaje = "Edad: " + str(numero)\nprint(mensaje)'),
            section("Mutabilidad y referencias", """
                Una cadena o un número no cambia por dentro: operaciones como `texto.upper()` o `numero + 1` producen nuevos valores. Las listas y diccionarios sí pueden modificarse. Si dos nombres se refieren a la misma lista, un cambio hecho desde uno se observa desde el otro. Esto sorprende cuando suponemos que `b = a` crea una copia; en realidad, solo crea otro vínculo con el mismo objeto.

                Al escribir `a = [1, 2]; b = a; b.append(3)`, tanto `a` como `b` muestran `[1, 2, 3]`. Para crear una lista nueva puedes usar un corte `a[:]` u otra técnica apropiada. Al principio basta recordar la diferencia entre reasignar un nombre y modificar una colección.
            """, 'a = [1, 2]\nb = a\nb.append(3)\nprint(a)  # [1, 2, 3]'),
            section("Igualdad y ausencia", """
                `==` compara valores según las reglas de cada tipo. Dos listas distintas pueden ser iguales si contienen lo mismo. `is` pregunta si son el mismo objeto; normalmente no lo uses para comparar números o textos. La excepción común es `valor is None` cuando quieres comprobar específicamente la ausencia de valor.

                Elegir nombres claros y mantener un tipo consistente para cada concepto reduce errores. Si `precio` primero es texto y luego número sin aviso, la lectura se vuelve difícil. Convierte los datos en el borde de entrada y trabaja después con el tipo adecuado.
            """),
        ],
        ["Un nombre se vincula con un objeto; `=` asigna y `==` compara.", "`int`, `float`, `str`, `bool` y `None` tienen comportamientos distintos.", "Listas y diccionarios se pueden modificar; números y cadenas no."],
        [("Tipos incorporados", "https://docs.python.org/3.13/library/stdtypes.html"),
         ("Modelo de ejecución", "https://docs.python.org/3.13/reference/executionmodel.html")],
    ),
    chapter(
        "numeros", "Números y operaciones", "De la aritmética simple a los límites de precisión.", 2,
        [
            section("Operadores básicos", """
                Python usa `+` para suma, `-` para resta, `*` para multiplicación, `/` para división, `//` para cociente entero, `%` para residuo y `**` para potencia. `/` produce un `float` incluso cuando la división es exacta: `6 / 3` da `2.0`. `//` redondea hacia abajo, así que con números negativos puede diferir de simplemente quitar decimales. `%` sirve para saber si un número es múltiplo de otro: `n % 2 == 0` identifica los pares.

                Si el divisor es cero, Python produce `ZeroDivisionError`. No es un problema de sintaxis: la operación está bien escrita, pero no puede realizarse con ese dato. Más adelante aprenderás a validar entradas antes de dividir.
            """, 'print(7 / 2)   # 3.5\nprint(7 // 2)  # 3\nprint(7 % 2)   # 1\nprint(2 ** 3)  # 8'),
            section("Prioridad y paréntesis", """
                Python sigue reglas de precedencia: en `2 + 3 * 4` multiplica primero y el resultado es 14. Para obtener 20 escribe `(2 + 3) * 4`. Los paréntesis también comunican intención a quien lee el programa, aunque el resultado fuera el mismo sin ellos. Cuando una fórmula tiene varios pasos, conviene guardarlos en variables intermedias con nombres expresivos y comprobar resultados parciales.

                Las operaciones entre enteros pueden producir enteros o decimales según el operador. Si necesitas una cantidad de objetos completos, `//` puede ser adecuado; si necesitas una media, usa `/`. Elegir el operador depende del significado del problema, no solo de lo que acepte el intérprete.
            """, 'subtotal = 100\nimpuesto = subtotal * 16 / 100\ntotal = subtotal + impuesto\nprint(total)'),
            section("Punto flotante y dinero", """
                `float` almacena aproximaciones binarias. Algunas fracciones decimales, como 0.1, no se representan exactamente; por eso ciertas sumas pueden mostrar muchos decimales inesperados. `round(valor, 2)` es útil para presentar un resultado, pero no convierte los cálculos internos en aritmética decimal exacta. Para aplicaciones financieras reales se suele usar `decimal.Decimal` o representar unidades mínimas como enteros, según los requisitos.

                En los ejercicios usamos `float` para aprender fórmulas. Si la salida esperada es `4.0`, imprimir `4` no coincide: el valor numérico es equivalente en muchas comparaciones, pero la representación textual es distinta. Presta atención al contrato de salida del ejercicio.
            """, 'print(0.1 + 0.2)\nprint(round(0.1 + 0.2, 2))'),
            section("Conversión y validación", """
                `input()` siempre entrega texto. `int("5")` funciona, pero `int("5.5")` falla; para decimales usa `float("5.5")`. En un programa real conviene prever entradas vacías, caracteres inesperados y límites válidos. Los retos proporcionan entradas acordes con su enunciado para concentrarse en un concepto a la vez. A medida que avances, empieza a pensar qué harías si esa garantía no existiera.
            """),
        ],
        ["`/`, `//` y `%` responden preguntas distintas.", "Los paréntesis controlan el orden y aclaran la intención.", "Los `float` son aproximados; no supongas exactitud decimal."],
        [("Tipos numéricos", "https://docs.python.org/3.13/library/stdtypes.html#numeric-types-int-float-complex")],
    ),
    chapter(
        "cadenas", "Texto y cadenas", "Representar, recorrer y transformar caracteres.", 3,
        [
            section("Qué es una cadena", """
                Una cadena (`str`) contiene texto. Se escribe entre comillas simples o dobles; ambas formas sirven. Para incluir una comilla dentro, puedes usar el otro tipo de comilla o una secuencia de escape. `\n` representa un salto de línea dentro de una cadena. Python 3 trabaja con texto Unicode, lo que permite acentos y caracteres de muchos idiomas. Para guardar texto en archivos conviene elegir explícitamente una codificación, normalmente UTF-8.

                Las cadenas son inmutables. `texto.upper()` devuelve otra cadena; no cambia `texto` salvo que reasignes el resultado. La concatenación con `+` une cadenas y la multiplicación por un entero repite el contenido. Para unir un número con texto, usa `str(numero)` o una f-string.
            """, 'nombre = "Ana"\nprint("Hola, " + nombre)\nprint("ja" * 3)'),
            section("Índices y cortes", """
                Cada posición tiene un índice que empieza en 0. Para `texto = "gato"`, `texto[0]` es `g` y `texto[-1]` es `o`. Un corte `texto[1:3]` toma posiciones desde 1 hasta antes de 3, de modo que obtiene `at`. Omitir el inicio o fin permite tomar desde un extremo; `texto[::-1]` invierte el orden. Acceder a un índice inexistente provoca `IndexError`.

                `len(texto)` cuenta unidades de texto llamadas puntos de código Unicode, no siempre los símbolos que una persona percibe como una sola letra. Para la mayoría de ejercicios básicos esa diferencia no afecta, pero es útil saberlo al trabajar con emojis o letras combinadas.
            """, 'texto = "gato"\nprint(texto[0])    # g\nprint(texto[1:3])  # at\nprint(texto[-1])   # o'),
            section("Métodos habituales", """
                Un método es una operación asociada con un objeto y se llama con un punto. `.lower()` pasa a minúsculas, `.upper()` a mayúsculas, `.strip()` quita espacios de los extremos, `.replace(viejo, nuevo)` sustituye fragmentos y `.split()` separa palabras por espacios en blanco. Estos métodos devuelven un valor; si quieres conservarlo, asígnalo a un nombre.

                La plataforma permite los métodos usados en sus ejercicios. En Python normal existe una gran cantidad más. Aprende a consultar la documentación de un método: identifica qué recibe, qué devuelve, si modifica el objeto y qué hace con casos especiales como una cadena vacía.
            """, 'texto = "  Hola Mundo  "\nlimpio = texto.strip().lower()\nprint(limpio)  # hola mundo'),
            section("Formato con f-strings", """
                Una f-string antepone `f` a las comillas e inserta expresiones dentro de llaves. `f"Hola, {nombre}"` construye una cadena nueva con el valor actual de `nombre`. Es más legible que varias concatenaciones y convierte valores como enteros a texto automáticamente. Las llaves evalúan expresiones, así que usa fórmulas sencillas dentro; si la expresión es compleja, calcula antes en una variable.
            """, 'nombre = "Ada"\nedad = 20\nprint(f"{nombre} tiene {edad} años")'),
        ],
        ["Las posiciones empiezan en 0 y el final de un corte no se incluye.", "Los métodos de cadenas producen una nueva cadena.", "Una f-string inserta valores en texto de forma clara."],
        [("Secuencias de texto", "https://docs.python.org/3.13/library/stdtypes.html#text-sequence-type-str"),
         ("Formato de salida", "https://docs.python.org/3.13/tutorial/inputoutput.html")],
    ),
    chapter(
        "entrada-salida", "Entrada, salida y conversiones", "Cómo se comunica un programa con quien lo usa.", 4,
        [
            section("Mostrar información con print", """
                `print()` envía una representación de sus argumentos a la salida estándar. Por defecto separa varios argumentos con un espacio y termina con un salto de línea. En Python normal puedes ajustar esos comportamientos con `sep` y `end`. Mostrar un resultado permite observar el programa, pero no devuelve automáticamente un valor a otra función. Si escribes una función y necesitas reutilizar su cálculo, usa `return`.

                La salida visible es parte del contrato de muchos retos: espacios, saltos de línea y orden importan. Esta plataforma quita espacios exteriores al comparar, pero conserva el contenido interior. Si la consigna pide una línea por elemento, una sola línea con todos los números no satisface ese formato.
            """, 'print("uno", "dos")       # uno dos\nprint("uno", "dos", sep="-")  # uno-dos'),
            section("Leer con input", """
                `input()` pausa la ejecución hasta recibir una línea y la devuelve como `str`, sin el salto de línea final. Cada llamada consume una línea. Si el programa lee dos números, los datos se escriben en líneas separadas en el cuadro Entrada para probar. Un mensaje de ayuda puede pasarse como argumento a `input` en programas normales, pero en los retos se prefieren entradas sin mensaje para mantener exacta la salida evaluada.

                La entrada que envías con Ejecutar sirve para experimentar; Comprobar reto utiliza varios casos preparados. Si tu programa imprime una respuesta fija que funciona con el ejemplo, probablemente fallará con un dato distinto. Guarda la entrada en variables y calcula a partir de ellas.
            """, 'nombre = input()\nprint(f"Hola, {nombre}")'),
            section("Convertir y verificar", """
                Para usar una entrada como entero, escribe `int(input())`. Para decimales, usa `float(input())`. La conversión es explícita porque el texto `"12"` y el número `12` son valores distintos. Si la entrada no se puede convertir, Python produce `ValueError`. En programas dirigidos a personas, se puede pedir de nuevo la entrada o mostrar un mensaje claro; esto se estudia junto con las excepciones.

                Antes de escribir código, marca en el enunciado cuántas líneas de entrada hay, qué tipo representa cada una y cómo debe verse la salida. Ese pequeño análisis evita confundir el orden de lectura y el formato de impresión.
            """, 'ancho = int(input())\nalto = int(input())\nprint(ancho * alto)'),
            section("Datos de prueba y límites", """
                Un caso de prueba conecta una entrada con una salida esperada. Prueba valores normales, límites y casos especiales: cero, negativos, cadenas vacías o empates, cuando la consigna los permita. Si el problema dice que una lista nunca estará vacía, puedes apoyarte en esa condición; si no lo dice, piensa qué debería pasar con una lista vacía. Documentar las condiciones de entrada es parte de especificar un programa.
            """),
        ],
        ["`input()` entrega texto y consume una línea por llamada.", "`print()` muestra; `return` devuelve un valor a quien llamó.", "Comprueba tu solución con entradas distintas y límites."],
        [("Entrada y salida", "https://docs.python.org/3.13/tutorial/inputoutput.html")],
    ),
    chapter(
        "condiciones", "Condiciones y lógica", "Decidir qué camino ejecuta el programa.", 5,
        [
            section("if, elif y else", """
                Una condición produce un resultado verdadero o falso. `if` ejecuta su bloque cuando la condición es verdadera. `elif` añade otra pregunta si las anteriores fueron falsas, y `else` recoge el caso restante. Solo uno de los bloques de una cadena `if/elif/else` se ejecuta. El orden importa: si revisas primero una condición amplia, puedes impedir que una más específica llegue a evaluarse.

                Para una nota, primero comprueba `>= 90`, después `>= 80`. Si hicieras la comprobación de `>= 70` al principio, una nota de 95 entraría allí y nunca alcanzaría la categoría A. Revisa los valores exactamente en las fronteras: 69, 70, 79, 80 y 90.
            """, 'if nota >= 90:\n    print("A")\nelif nota >= 80:\n    print("B")\nelse:\n    print("Otra")'),
            section("Comparaciones", """
                `==` prueba igualdad, `!=` desigualdad, `<` y `>` comparan estrictamente, y `<=` y `>=` incluyen el límite. `=` es asignación y no se usa como comparación. Python permite expresiones encadenadas como `1 <= numero <= 10`, equivalentes a exigir ambos límites. En texto, las comparaciones siguen reglas de orden de caracteres que no siempre coinciden con el orden alfabético de una persona.

                Evita comprobar un `float` calculado con `==` cuando esperas una igualdad decimal exacta: las aproximaciones pueden diferir. En esta ruta usamos comparaciones principalmente con enteros y valores discretos, donde la intención resulta más clara.
            """, 'numero = 5\nprint(1 <= numero <= 10)  # True'),
            section("and, or y not", """
                `and` exige que ambas condiciones sean verdaderas; `or` exige al menos una; `not` invierte el resultado. Python evalúa estas expresiones de izquierda a derecha y puede omitir la parte restante cuando ya conoce el resultado. Esto se llama evaluación de cortocircuito. Por ejemplo, `divisor != 0 and numero / divisor > 2` evita dividir entre cero cuando el divisor vale 0.

                Usa paréntesis si una combinación de condiciones resulta difícil de leer. Para el año bisiesto, la regla completa es: divisible por 400, o divisible por 4 pero no por 100. Descomponer esa frase antes de escribir la expresión reduce errores.
            """, 'bisiesto = anio % 400 == 0 or (anio % 4 == 0 and anio % 100 != 0)'),
            section("Verdad de otros valores", """
                Las condiciones no se limitan a `True` y `False` literales. Python trata como falsos valores como 0, una cadena vacía, una lista vacía y `None`; muchos otros valores se consideran verdaderos. Esto permite escribir `if lista:` para saber si tiene elementos. Sin embargo, la comparación explícita suele enseñar mejor la intención al principio, especialmente cuando debes distinguir entre 0, vacío y ausencia.
            """, 'datos = []\nif datos:\n    print("Hay elementos")\nelse:\n    print("Está vacía")'),
        ],
        ["El orden de `if/elif` cambia qué caso se elige.", "Prueba los valores de frontera de cada condición.", "`and` y `or` pueden dejar de evaluar cuando el resultado ya está decidido."],
        [("Control de flujo", "https://docs.python.org/3.13/tutorial/controlflow.html"),
         ("Valores de verdad", "https://docs.python.org/3.13/library/stdtypes.html#truth-value-testing")],
    ),
    chapter(
        "bucles", "Bucles: repetir con intención", "Repetición, contadores y condiciones de parada.", 6,
        [
            section("Por qué repetir", """
                Si una tarea debe hacerse muchas veces, copiar diez líneas parecidas es frágil: cualquier corrección tendría que repetirse diez veces. Un bucle describe una sola vez el trabajo y determina cuándo se repite. Antes de escribirlo, responde tres preguntas: qué cambia en cada vuelta, cuándo termina y qué resultado se conserva entre vueltas.

                Cada ejecución del cuerpo se llama iteración. Un bucle que nunca cumple su condición de parada es infinito. En los retos el ejecutor detiene programas demasiado largos; en un programa real, un bucle infinito puede bloquear la tarea y consumir recursos.
            """),
            section("for y range", """
                `for` toma sucesivamente los elementos de un iterable. Una cadena entrega caracteres; una lista, sus elementos; `range(5)`, los enteros 0, 1, 2, 3 y 4. El límite final de `range` se excluye. `range(2, 6)` produce del 2 al 5 y `range(2, 10, 2)` avanza de dos en dos. El nombre del bucle recibe un valor distinto en cada vuelta.

                Usa `for` cuando conoces los valores que vas a recorrer. No necesitas modificar a mano el contador para que avance. En ejercicios de suma, inicializa el acumulador antes del bucle y actualízalo dentro; imprime al final si quieres un único total.
            """, 'total = 0\nfor numero in range(1, 4):\n    total += numero\nprint(total)  # 6'),
            section("while y condición de parada", """
                `while` repite mientras su condición sea verdadera. Es útil cuando aún no sabes cuántas veces se repetirá algo, por ejemplo, hasta que llegue una señal de salida. La condición se revisa antes de cada vuelta; si empieza siendo falsa, el cuerpo no se ejecuta ninguna vez. Asegúrate de que el cuerpo pueda acercarse a la salida.

                `break` termina un bucle antes de tiempo y `continue` pasa directamente a la siguiente iteración. Son herramientas útiles, pero demasiados saltos complican seguir el flujo. Al empezar, suele ser más claro expresar la condición de parada y el cambio de estado de forma visible.
            """, 'n = 3\nwhile n > 0:\n    print(n)\n    n -= 1'),
            section("Patrones y errores comunes", """
                Contar elementos que cumplen una condición, acumular un total y buscar el primer elemento válido son patrones distintos. Para contar, empieza en cero y suma uno por coincidencia. Para buscar, puedes guardar el resultado o terminar con `break`. La indentación decide qué acciones se repiten y cuáles ocurren al terminar.

                El error de uno ocurre al incluir o excluir un límite equivocado. Verifica un bucle con cero, una y varias vueltas. En `range(inicio, fin)` pregunta siempre si necesitas que `fin` aparezca; si sí, quizá debas usar `fin + 1`.
            """),
        ],
        ["`for` recorre valores; `while` repite según una condición.", "El final de `range` se excluye.", "Todo bucle necesita una razón clara para terminar."],
        [("Control de flujo", "https://docs.python.org/3.13/tutorial/controlflow.html")],
    ),
    chapter(
        "listas-tuplas", "Listas, tuplas y secuencias", "Guardar varios valores y recorrerlos.", 7,
        [
            section("Una colección en un solo nombre", """
                Una lista agrupa valores en un orden. `[]` crea una lista vacía y `[3, 5, 8]` crea una de tres enteros. Cada posición tiene un índice que empieza en cero; los índices negativos cuentan desde el final. `len(lista)` indica cuántos elementos hay. Acceder a una posición que no existe produce `IndexError`.

                Una lista puede contener tipos distintos, aunque mantener datos relacionados del mismo tipo suele simplificar el código. Una matriz básica puede representarse como lista de listas. En ese caso `tabla[fila][columna]` realiza dos accesos sucesivos.
            """, 'notas = [7, 9, 8]\nprint(notas[0])   # 7\nprint(len(notas)) # 3'),
            section("Mutabilidad y métodos", """
                Las listas son mutables: puedes cambiar un elemento, añadir con `.append(valor)` o quitar elementos. `lista[0] = 10` modifica la lista original. Si asignas `otra = lista`, ambos nombres se refieren al mismo objeto; cambiar mediante uno se ve desde el otro. Para una copia superficial de una lista simple, puedes usar `lista.copy()` o `lista[:]` en Python normal.

                `.append()` modifica la lista y devuelve `None`: escribir `lista = lista.append(4)` pierde la referencia a la lista. Una cadena funciona de otra manera: sus métodos crean cadenas nuevas porque las cadenas son inmutables. Entender qué cambia y qué se devuelve evita muchos errores.
            """, 'numeros = [1, 2]\nnumeros.append(3)\nprint(numeros)  # [1, 2, 3]'),
            section("Recorrer e indexar", """
                `for elemento in lista:` expresa directamente que necesitas cada valor. Si además necesitas la posición, en Python normal `enumerate(lista)` produce pares de índice y elemento. Un corte como `lista[1:3]` crea otra lista con las posiciones 1 y 2. Igual que en las cadenas, el extremo derecho queda fuera.

                Si modificas una lista mientras la recorres, puedes saltarte valores por accidente. Una solución es construir una lista nueva a partir de los elementos aceptados. Más adelante podrás aprender comprensiones de listas, que condensan ese patrón sin cambiar la idea fundamental.
            """, 'pares = []\nfor n in [1, 2, 3, 4]:\n    if n % 2 == 0:\n        pares.append(n)\nprint(pares)'),
            section("Tuplas y elección de estructura", """
                Una tupla, como `(10, 20)`, conserva un orden, pero no permite reemplazar elementos después de creada. Es útil para un grupo fijo de valores, por ejemplo coordenadas. Una tupla de un solo elemento se escribe `(5,)`: la coma evita que Python la interprete como una expresión entre paréntesis.

                Elige una lista cuando necesites agregar, eliminar o cambiar elementos; una tupla cuando el grupo debe mantenerse fijo. Ni lista ni tupla etiquetan cada campo con nombre; cuando necesitas consultar datos por clave, un diccionario suele ser mejor.
            """),
        ],
        ["La primera posición es 0.", "Las listas cambian; las tuplas mantienen sus elementos.", "Dos nombres pueden apuntar a la misma lista."],
        [("Estructuras de datos", "https://docs.python.org/3.13/tutorial/datastructures.html")],
    ),
    chapter(
        "diccionarios-conjuntos", "Diccionarios y conjuntos", "Elegir datos por clave y evitar duplicados.", 8,
        [
            section("Claves y valores", """
                Un diccionario relaciona una clave con un valor: `{"nombre": "Ana", "edad": 24}`. En vez de preguntar por la posición 0, preguntas por `persona["nombre"]`. Las claves deben ser hashables, como cadenas, enteros o tuplas adecuadas; una lista no sirve como clave. Una clave no aparece dos veces: asignarle otro valor reemplaza el anterior.

                Cuando una clave podría faltar, `diccionario.get(clave)` devuelve `None` por defecto o el segundo argumento que indiques. La expresión `clave in diccionario` comprueba existencia. Acceder con corchetes a una clave ausente produce `KeyError`; esto puede señalar un error real, así que no sustituyas siempre los corchetes por `.get()` sin pensar.
            """, 'persona = {"nombre": "Ana", "edad": 24}\nprint(persona["nombre"])\nprint(persona.get("ciudad", "desconocida"))'),
            section("Actualizar y recorrer", """
                `diccionario[clave] = valor` añade o actualiza una entrada. Recorrer directamente un diccionario entrega sus claves. `.values()` entrega valores y `.items()` pares de clave y valor. En esta primera ruta se usan principalmente consultas y `.values()`; los demás patrones se pueden practicar al avanzar hacia proyectos completos.

                Para contar frecuencias, empieza con un diccionario vacío y aumenta el contador de cada dato: `conteos[x] = conteos.get(x, 0) + 1`. El cero significa que aún no se había visto. Este patrón sirve para palabras, respuestas de encuestas o categorías.
            """, 'conteos = {}\nfor letra in "casa":\n    conteos[letra] = conteos.get(letra, 0) + 1\nprint(conteos["a"])  # 2'),
            section("Conjuntos", """
                Un conjunto (`set`) guarda valores únicos. `{1, 2, 2}` equivale a `{1, 2}`. Es adecuado para preguntar si un elemento ya apareció o para operaciones como unión e intersección. No uses la posición de un elemento: los conjuntos no son secuencias indexadas. Para crear un conjunto vacío, escribe `set()`; `{}` crea un diccionario vacío.

                La plataforma explica conjuntos aquí para que conozcas la herramienta, pero el editor de esta primera ruta restringe algunas funciones. Para experimentar con `set()` y operaciones de conjuntos, abre Python en la terminal. Esa diferencia es una limitación del entorno de ejercicios, no del lenguaje Python.
            """, 'colores = {"rojo", "azul", "rojo"}\nprint(len(colores))  # 2'),
            section("Qué estructura escoger", """
                Si importa el orden y puede haber repeticiones, piensa en una lista. Si necesitas asociar nombres o identificadores a valores, piensa en un diccionario. Si lo importante es saber pertenencia sin duplicados, piensa en un conjunto. No existe una estructura universalmente mejor: la elección depende de las operaciones que el programa debe hacer.

                Antes de escribir un bucle, describe los datos con palabras: «una lista de notas», «un diccionario que asocia producto y precio», «un conjunto de usuarios vistos». Después será más fácil decidir cómo acceder y cómo comprobar resultados.
            """),
        ],
        ["Un diccionario asocia claves con valores.", "`.get()` ayuda cuando una clave podría faltar.", "Un conjunto elimina duplicados y no se consulta por índice."],
        [("Estructuras de datos", "https://docs.python.org/3.13/tutorial/datastructures.html")],
    ),
    chapter(
        "funciones", "Funciones paso a paso", "Dividir un problema y reutilizar soluciones.", 9,
        [
            section("Definir y llamar", """
                Una función agrupa instrucciones bajo un nombre. `def saludar():` define la función; `saludar()` la ejecuta. Definir no ejecuta el cuerpo de inmediato. Los paréntesis al llamar son necesarios incluso si no hay argumentos. Una función bien elegida responde a una tarea concreta, con un nombre que exprese su propósito.

                Dividir un programa en funciones permite comprobar una parte por separado y reutilizarla. Si el mismo cálculo aparece varias veces, conviértelo en una función en lugar de copiarlo. No hace falta crear una función para cada línea: busca unidades de trabajo con significado.
            """, 'def saludar():\n    print("Hola")\n\nsaludar()'),
            section("Parámetros y argumentos", """
                Los parámetros son nombres escritos en la definición; los argumentos son valores enviados en la llamada. En `def doble(numero):`, `numero` es parámetro; en `doble(4)`, `4` es argumento. La función puede ejecutarse con distintos valores sin cambiar su código. Al empezar, usa llamadas simples con argumentos posicionales y verifica que entregas la cantidad esperada.

                Python también acepta argumentos con nombre y parámetros con valores por defecto. `def saludar(nombre="amiga"):` permite llamar con o sin nombre. En programas reales, evita usar una lista mutable como valor por defecto: se crea una vez y puede conservar cambios entre llamadas.
            """, 'def doble(numero):\n    return numero * 2\n\nprint(doble(4))  # 8'),
            section("return frente a print", """
                `return` entrega un valor a quien llamó la función y termina esa llamada. `print` solo muestra algo. Si escribes `resultado = funcion()`, necesitas que la función devuelva el cálculo; si únicamente imprime, `resultado` será `None`. Puedes imprimir el valor fuera para mostrarlo o pasarlo a otra función para seguir calculando.

                Una función sin `return` explícito devuelve `None`. Puedes devolver un solo objeto que sea una tupla si necesitas varios resultados. En retos que añaden una llamada de prueba después del código, respeta el nombre y los parámetros pedidos por el enunciado.
            """, 'def area(base, altura):\n    return base * altura\n\nresultado = area(3, 4)\nprint(resultado)'),
            section("Alcance y diseño", """
                Un nombre asignado dentro de una función es local, salvo reglas especiales que estudiarás más adelante. La función no debe depender de una variable externa oculta cuando puede recibirla como parámetro. Recibir datos y devolver resultados hace más fácil comprobarla con diferentes casos.

                Para diseñar una función, escribe su contrato: qué recibe, qué devuelve y qué ocurre con entradas límite. Ponle un nombre descriptivo y prueba un caso normal, uno extremo y uno inesperado cuando corresponda. Una función corta no es automáticamente correcta, pero suele ser más fácil de razonar.
            """),
        ],
        ["`def` define; una llamada ejecuta.", "Los parámetros reciben los argumentos.", "`return` entrega un valor; `print` lo muestra."],
        [("Definición de funciones", "https://docs.python.org/3.13/tutorial/controlflow.html#defining-functions")],
    ),
    chapter(
        "errores-depuracion", "Errores y depuración", "Leer lo que Python te está diciendo.", 9,
        [
            section("Tres clases de problemas", """
                Un error de sintaxis impide interpretar el programa, como olvidar `:` después de `if`. Una excepción ocurre durante la ejecución, como dividir entre cero o convertir `"hola"` con `int()`. Un error lógico es más silencioso: el programa termina, pero entrega un resultado equivocado. Cada tipo pide una estrategia distinta.

                El mensaje de excepción incluye una categoría y, normalmente, la línea implicada. `NameError` sugiere un nombre no definido; `TypeError`, una operación con tipos incompatibles; `IndexError`, un índice fuera de la secuencia; `KeyError`, una clave ausente. La línea señalada es el lugar donde Python detectó el problema; la causa puede estar en una asignación anterior.
            """),
            section("Leer una traza", """
                La traza o traceback muestra la secuencia de llamadas que condujo al error. En un programa con funciones, empieza leyendo la última línea para ver el tipo de excepción y luego revisa de abajo hacia arriba dónde se produjo. No corrijas a ciegas todas las líneas: reproduce el caso con datos pequeños y pregunta cuál fue el primer valor diferente del esperado.

                En los ejercicios, el panel Resultado presenta mensajes simplificados y, al comprobar, la primera prueba que falló. Si esperabas una salida y no aparece, comprueba si la función solo devuelve un valor cuando el reto pedía imprimir, o al revés.
            """),
            section("Depurar con pasos pequeños", """
                Reduce el ejemplo que falla a la entrada más pequeña posible. Anota el resultado esperado y el obtenido. Comprueba valores intermedios con `print`, después retira esos mensajes si la salida final debe tener un formato exacto. También puedes ejecutar una función aislada con datos conocidos.

                Cambia una cosa por vez y vuelve a probar. Si cambias varias condiciones simultáneamente, no sabrás cuál solucionó o empeoró el problema. Una hipótesis concreta —«el límite de range excluye el último número»— se puede verificar con una prueba corta.
            """),
            section("Excepciones en programas completos", """
                En Python normal, `try` y `except` permiten responder a errores que esperas, por ejemplo una entrada que no se puede convertir. Captura una excepción específica como `ValueError` y explica a la persona qué dato necesita corregir. Capturar todo con `except:` puede ocultar fallas de programación que deberías descubrir.

                Los 100 ejercicios iniciales restringen `try` en su editor. En Proyectos puedes usarlo: el reto «Ignorar entradas inválidas» pide contar los fragmentos que provocan `ValueError`. Conviene primero reconocer la excepción y después decidir si corresponde recuperarse o detener el programa.
            """, 'try:\n    edad = int(input("Edad: "))\nexcept ValueError:\n    print("Escribe un número entero")'),
            section("Práctica guiada: contar datos inválidos", """
                Supón que recibes `5,abc,3`. Divide el texto con `.split(",")`: obtienes tres fragmentos. Inicializa `total = 0` y `errores = 0`. En la primera vuelta, `int("5")` entrega 5; en la segunda, `int("abc")` provoca `ValueError` y se ejecuta `except`; en la tercera, `int("3")` entrega 3. El resultado es suma 8 y un dato inválido. Un campo vacío también falla al convertirlo con `int`.

                El `try` debe rodear solo la operación que esperas que falle. Si incluyes demasiado código, podrías ocultar otro problema. Prueba además `-2,4,,x`: la suma es 2 y hay dos fragmentos inválidos. Esto prepara el reto «Ignorar entradas inválidas» de Proyectos.
            """, 'total = 0\nerrores = 0\nfor texto in "5,abc,3".split(","):\n    try:\n        total += int(texto.strip())\n    except ValueError:\n        errores += 1\nprint(total, errores)  # 8 1',
            "Antes de ejecutar, señala qué instrucciones se saltan cuando ocurre ValueError."),
        ],
        ["Lee la última línea del traceback y localiza la llamada que falló.", "Prueba una hipótesis por vez.", "Captura excepciones concretas cuando sepas cómo recuperarte."],
        [("Errores y excepciones", "https://docs.python.org/3.13/tutorial/errors.html")],
    ),
    chapter(
        "modulos-bibliotecas", "Módulos, paquetes y bibliotecas", "Cómo usa Python código ya escrito.", 10,
        [
            section("La idea de reutilizar código", """
                Un módulo es un archivo de Python que define nombres como funciones, constantes y clases. `import math` carga el módulo `math`, y `math.sqrt(9)` llama una función de ese módulo. El prefijo `math.` indica de dónde viene el nombre y evita confundir funciones con el mismo nombre. También puedes importar un nombre concreto: `from math import sqrt`; úsalo cuando la procedencia siga siendo clara.

                Una biblioteca es un conjunto de código reutilizable; puede tener uno o muchos módulos. Un paquete organiza módulos bajo un nombre, a menudo en carpetas. Estos términos se relacionan, pero no son sinónimos exactos. El comando `import` busca módulos en rutas configuradas para la instalación de Python y el proyecto.
            """, 'import math\nprint(math.sqrt(9))  # 3.0'),
            section("Qué contiene una biblioteca", """
                Una biblioteca puede ofrecer funciones, clases, constantes y submódulos. Una función recibe argumentos y produce un resultado o un efecto: `math.sqrt(9)` devuelve `3.0`. Una clase permite crear objetos con datos y métodos propios: `Path("notas.txt")` crea una ruta, y `ruta.exists()` consulta si existe. Una constante es un valor con nombre, como `math.pi`. Un submódulo agrupa una parte de la biblioteca, como `urllib.request`.

                La documentación suele presentar cada elemento con su nombre, parámetros, valor de retorno, posibles errores y ejemplos. Distingue la instalación del paquete, el nombre usado en `import` y el nombre de la función. Por ejemplo, se instala `beautifulsoup4`, se importa `bs4` y se crea un objeto con `BeautifulSoup(...)`. La pestaña Bibliotecas de esta plataforma muestra estas diferencias en cada ficha.
            """, 'from pathlib import Path\nruta = Path("notas.txt")\nprint(ruta.exists())'),
            section("Biblioteca estándar", """
                Python trae una biblioteca estándar. `math` aporta operaciones matemáticas; `random`, generación pseudoaleatoria; `pathlib`, manejo de rutas; `json`, lectura y escritura de datos JSON; `datetime`, fechas y horas. Son herramientas disponibles con la instalación normal, sin instalar paquetes de terceros por cada uso.

                La sintaxis del lenguaje (`if`, `for`, `def`) se aprende primero; una biblioteca añade capacidades concretas. Para saber qué ofrece un módulo, consulta la documentación oficial, busca la función, comprueba argumentos, tipo de retorno y ejemplos. No necesitas memorizar todas las bibliotecas para programar.
            """, 'import random\nprint(random.randint(1, 6))  # entre 1 y 6'),
            section("Paquetes externos", """
                Hay paquetes que se instalan aparte, por ejemplo para web, ciencia o imágenes. Un paquete puede traer dependencias: otros paquetes necesarios para funcionar. La versión instalada puede cambiar el comportamiento o la API, por eso conviene registrar dependencias y leer documentación correspondiente a la versión que usas.

                No copies un `pip install` de una página desconocida sin identificar el paquete y su origen. Instala en un entorno virtual del proyecto y usa recursos oficiales o mantenidos. El servidor de esta plataforma usa solo la biblioteca estándar; los paquetes externos se instalan aparte en el entorno del Laboratorio.
            """),
            section("Cómo escoger y aprender una biblioteca", """
                Define primero la tarea: «leer una tabla CSV», «enviar una solicitud HTTP» o «dibujar un gráfico». Revisa si la biblioteca estándar ya resuelve el caso; `csv`, `urllib.request` y `tkinter`, por ejemplo, cubren necesidades concretas sin instalar paquetes externos. Cuando otra biblioteca facilite el trabajo, lee su documentación oficial para saber qué versiones de Python acepta, cómo se instala, cómo se importa y cuál es su ejemplo mínimo.

                Prueba una función pequeña antes de integrarla en un programa grande. Observa si devuelve un valor, modifica un objeto, crea un archivo o hace una solicitud de red. Consulta qué excepciones puede producir. El glosario por temas sirve para descubrir nombres y funciones frecuentes; no sustituye la documentación completa ni significa que debas aprender todas las bibliotecas de memoria.
            """),
            section("El editor de ejercicios y los imports", """
                Los 100 ejercicios iniciales aceptan un subconjunto de Python y bloquean `import` para que las pruebas sean consistentes. Esta restricción pertenece solo a esa ruta; Python sí permite importar. Los ejemplos de esta sección también se pueden ejecutar en la terminal guardándolos en `prueba.py` y usando `python prueba.py`.

                En la pestaña Laboratorio hay retos específicos de instalación e importación. Preparas un entorno virtual, instalas paquetes reales y escribes código que los importa. En Proyectos, el editor de varios archivos te permite crear `main.py` y `logica.py`, importar uno desde el otro y usar módulos de la biblioteca estándar. Son dos formas complementarias de practicar bibliotecas y módulos.
            """),
        ],
        ["Un módulo suele ser un archivo importable; un paquete organiza módulos.", "La biblioteca estándar viene con Python.", "El editor inicial restringe imports; Python normal los admite."],
        [("Módulos", "https://docs.python.org/3.13/tutorial/modules.html"), ("Biblioteca estándar", "https://docs.python.org/3.13/library/index.html")],
    ),
    chapter(
        "pip-venv", "Instalación, pip y entornos virtuales", "Preparar un proyecto sin mezclar dependencias.", 10,
        [
            section("Python, el intérprete y pip", """
                El intérprete ejecuta tu código. Puedes comprobar su versión con `python --version` en Windows, o con el comando equivalente de tu sistema. `pip` es el instalador habitual de paquetes de Python. Usar `python -m pip` ayuda a dirigir la instalación al mismo intérprete que ejecutará el programa.

                Si un comando falla, comprueba qué intérprete y qué entorno estás usando antes de reinstalar todo. Es común tener más de una versión de Python. El archivo `.py` no contiene por sí solo paquetes de terceros: cada entorno necesita las dependencias correspondientes.
            """, 'python --version\npython -m pip --version'),
            section("Crear un entorno virtual", """
                `venv` crea una instalación aislada para las dependencias de un proyecto. Dentro de la carpeta del proyecto, `python -m venv .venv` crea el entorno. En Windows PowerShell suele activarse con `.\\.venv\\Scripts\\Activate.ps1`; en otros sistemas con `source .venv/bin/activate`. Las políticas del equipo pueden impedir la activación en PowerShell: también puedes llamar directamente al ejecutable Python del entorno.

                La activación cambia qué `python` y `pip` usa la terminal actual; no modifica mágicamente todos los proyectos. Al abrir otra terminal, revisa si el entorno sigue activo. Mantén la carpeta `.venv` fuera del control de versiones: los demás recrearán el entorno desde la lista de dependencias.
            """, 'python -m venv .venv\n& ".\\.venv\\Scripts\\python.exe" -m pip --version'),
            section("Instalar y registrar dependencias", """
                Una vez elegido el intérprete del entorno, instala un paquete con `python -m pip install nombre_paquete`. La documentación del paquete indica qué nombre instalar y cómo importarlo; a veces no son iguales. `python -m pip list` muestra paquetes instalados. Un archivo `requirements.txt` puede registrar nombres y versiones; `python -m pip install -r requirements.txt` los instala en otro entorno.

                Fijar versiones favorece la reproducibilidad, pero también requiere actualizar dependencias cuando sea necesario. No instales paquetes únicamente por si acaso. Empieza con la biblioteca estándar; añade una dependencia cuando resuelva una necesidad concreta.
            """),
            section("Resolver el clásico 'no module named'", """
                `ModuleNotFoundError` suele indicar que el módulo no está instalado en el intérprete actual, que el entorno virtual no está activo, o que el nombre escrito no coincide. Comprueba la ruta del Python usado, ejecuta `python -m pip show nombre_paquete` y confirma el nombre documentado para `import`.

                También puedes causar confusión si llamas a tu archivo `json.py` o `random.py`: tu archivo puede ocultar el módulo de la biblioteca estándar. Usa nombres propios para tus scripts. Esta plataforma no necesita instalar paquetes adicionales para abrirse.
            """),
            section("Diagnosticar un fallo de instalación paso a paso", """
                En el Laboratorio, copia el comando que se muestra: contiene la ruta completa al Python del entorno. Si pip dice que instaló un paquete pero el import falla, comprueba la versión de ese Python, la versión de pip para ese mismo Python y luego ejecuta `-m pip show` con el nombre de instalación. Por ejemplo, para Pillow instalas `Pillow` pero en el código usas `PIL`.

                Lee la primera línea útil del error y clasifícala: «comando no reconocido» apunta a la ruta o a la sintaxis de PowerShell; «no matching distribution» puede indicar un nombre mal escrito o una versión de Python incompatible; un error de certificado o de conexión apunta a la red. No desactives la verificación de certificados para ocultar el problema. Puedes pegar el mensaje en el diagnóstico local del laboratorio: te propondrá una comprobación, sin ejecutar el texto pegado.
            """, '& ".\\.venv\\Scripts\\python.exe" -V\n& ".\\.venv\\Scripts\\python.exe" -m pip --version\n& ".\\.venv\\Scripts\\python.exe" -m pip show Pillow'),
            section("Guardar dependencias de un proyecto", """
                Cuando un proyecto ya funciona, anota las dependencias directas y las versiones que probaste. `python -m pip freeze` lista todo lo instalado en el entorno, incluidas dependencias indirectas; si lo guardas en `requirements.txt`, otra persona podrá reconstruir ese conjunto con `python -m pip install -r requirements.txt`. Revisa el archivo antes de compartirlo para distinguir lo que elegiste de lo que llegó como dependencia.

                El entorno virtual en sí no se copia entre equipos. Comparte tu código, las instrucciones y la lista de dependencias; crea un entorno nuevo en el otro equipo. En los proyectos del Laboratorio, explica en un comentario qué paquete instalaste, con qué nombre lo importas y para qué lo usas.
            """, 'python -m pip freeze > requirements.txt\npython -m pip install -r requirements.txt'),
        ],
        ["Usa `python -m pip` con el intérprete del proyecto.", "Un entorno virtual separa dependencias.", "La plataforma funciona sin paquetes externos."],
        [("Entornos virtuales y paquetes", "https://docs.python.org/3.13/tutorial/venv.html"), ("venv", "https://docs.python.org/3.13/library/venv.html")],
    ),
    chapter(
        "archivos-datos", "Archivos y datos persistentes", "Conservar información después de cerrar el programa.", 10,
        [
            section("Memoria frente a archivo", """
                Una variable existe durante la ejecución del programa. Si necesitas recuperar datos mañana, guárdalos en un archivo o una base de datos. La ruta indica dónde está el archivo; una ruta relativa se interpreta desde el directorio de trabajo, que no siempre coincide con la carpeta del script. Por eso conviene comprobar desde dónde ejecutas y usar `pathlib` para construir rutas en proyectos completos.

                Leer y escribir archivos puede fallar si la ruta no existe, no tienes permiso o el disco está lleno. Diseña qué hacer ante esas condiciones. El editor de los 100 ejercicios iniciales no admite acceso a archivos; la pestaña Proyectos sí prepara archivos de ejemplo en una carpeta temporal para cada prueba y verifica los que crea tu programa.
            """),
            section("Abrir y cerrar correctamente", """
                `with open(ruta, modo, encoding="utf-8") as archivo:` abre un archivo y lo cierra al salir del bloque, incluso si ocurre una excepción. El modo `"r"` lee; `"w"` crea o sobrescribe; `"a"` añade al final. Antes de usar `"w"`, verifica la ruta: sobrescribir el archivo equivocado puede borrar datos. UTF-8 permite guardar texto en español de forma predecible.

                `read()` devuelve todo el contenido; recorrer el archivo línea por línea evita cargar un archivo enorme de una vez. `write()` recibe una cadena y no añade un salto de línea automáticamente. Para probar, usa archivos de ejemplo que puedas volver a crear.
            """, 'with open("notas.txt", "w", encoding="utf-8") as archivo:\n    archivo.write("Primera nota\\n")\nwith open("notas.txt", "r", encoding="utf-8") as archivo:\n    print(archivo.read())'),
            section("JSON y datos estructurados", """
                JSON representa objetos, listas, cadenas, números, booleanos y `null`. En Python, `json.dump(datos, archivo)` guarda estructuras compatibles y `json.load(archivo)` las recupera. Los diccionarios se parecen a objetos JSON, aunque no son exactamente el mismo formato. Las claves de un objeto JSON son texto y algunos tipos de Python necesitan conversión antes de guardarse.

                JSON sirve para configuraciones pequeñas o intercambio de datos. Si necesitas muchas consultas y actualizaciones concurrentes, una base de datos puede ser más apropiada. Esta plataforma usa SQLite para el progreso y almacena el archivo `data/progreso.db` en el equipo.
            """, 'import json\nwith open("perfil.json", "w", encoding="utf-8") as archivo:\n    json.dump({"nombre": "Ana", "nivel": 1}, archivo, ensure_ascii=False)'),
            section("Cuidar los datos", """
                Define qué datos guardarás y evita guardar información sensible innecesaria. Haz una copia antes de cambiar un formato o sobrescribir archivos importantes. Trata el contenido leído como dato: comprueba tipos, claves esperadas y valores válidos antes de usarlo. Un archivo puede estar vacío, incompleto o modificado por otra herramienta.

                Si mueves la carpeta de esta plataforma, copia también `data/progreso.db`: contiene el progreso de todas las rutas y los borradores de Proyectos. Los borradores de los 100 ejercicios iniciales y del Laboratorio se guardan en el navegador, asociados a la dirección local. Por eso, si cambias de navegador, los borradores de esas dos rutas no viajan con la base de datos.
            """),
        ],
        ["`with` cierra el archivo automáticamente.", "El modo `w` sobrescribe: revisa la ruta.", "El progreso y los borradores de Proyectos están en `data/progreso.db`; los otros borradores están en el navegador."],
        [("Entrada y salida", "https://docs.python.org/3.13/tutorial/inputoutput.html"), ("json", "https://docs.python.org/3.13/library/json.html")],
    ),
    chapter(
        "pruebas-calidad", "Pruebas y calidad del código", "Comprobar resultados y hacer el programa legible.", 10,
        [
            section("De ejemplos a pruebas", """
                Una prueba reúne entrada, salida esperada y una comparación. Probar solo el ejemplo del enunciado puede ocultar fallas: intenta un valor pequeño, uno grande, cero, negativos o cadena vacía cuando tengan sentido. Para una condición con límite, prueba un valor debajo, uno exactamente en el límite y uno encima.

                Los 100 ejercicios se corrigen con casos preparados. Cuando uno falla, el panel muestra el primer caso que no coincidió. Usa esa información para formular una hipótesis, pero vuelve a pensar en la regla general; cambiar el código para un único caso puede romper los demás.
            """),
            section("Pruebas automáticas", """
                La biblioteca estándar incluye `unittest`. Una prueba típica llama una función y compara su resultado con el esperado. `assertEqual` comprueba igualdad. También hay comprobaciones para excepciones y otras condiciones. En un proyecto más grande, ejecutar una batería de pruebas después de cada cambio da confianza, aunque ninguna batería demuestra la ausencia total de defectos.

                Escribe pruebas para comportamiento observable, no para repetir cada línea de implementación. Si cambias internamente cómo calculas un resultado y el contrato sigue igual, las pruebas deberían continuar pasando.
            """, 'import unittest\n\ndef doble(n):\n    return n * 2\n\nclass Pruebas(unittest.TestCase):\n    def test_doble(self):\n        self.assertEqual(doble(4), 8)\n\nif __name__ == "__main__":\n    unittest.main()'),
            section("Ejecutar y leer una prueba", """
                Guarda el ejemplo anterior como `test_doble.py` y ejecútalo desde PowerShell con `python -m unittest -v test_doble.py`. La opción `-v` muestra el nombre de cada prueba y si pasó. También puedes ejecutar `python test_doble.py` porque el bloque `if __name__ == "__main__"` llama a `unittest.main()` al ejecutar el archivo directamente. Si importas el archivo desde otro programa, ese bloque no inicia pruebas por sorpresa.

                Cambia temporalmente `return n * 2` por `return n + 2` y vuelve a ejecutar: la prueba muestra el valor esperado y el recibido. Después restaura la función. En el reto «Reparar código con pruebas», `main.py` ejecuta pruebas de `test_logica.py` y una comprobación adicional valida `es_primo` con otros números. Cambiar las pruebas para que pasen no arregla la función.
            """, 'python -m unittest -v test_doble.py',
            "Predice qué verás al cambiar la función para que `doble(4)` devuelva 6."),
            section("Diseñar casos útiles", """
                Una prueba del caso feliz es un inicio. Para `es_primo`, conviene comprobar 0 y 1 (no primos), 2 (primo par), 9 (compuesto impar) y 17 (primo mayor). Cada caso ataca un posible error de razonamiento. Por ejemplo, la regla «es primo si es impar» falla con 2 y 9. Si una función escribe un archivo, la prueba también debe leerlo y comprobar contenido, no conformarse con un mensaje impreso.

                Mantén las pruebas independientes: una no debería depender de que otra haya modificado un archivo o variable antes. Para archivos y bases de datos, trabaja con datos temporales que puedas recrear. Una prueba de regresión conserva un caso que antes falló para descubrir si una modificación vuelve a romperlo. Las etapas 2 y 3 de los proyectos repiten pruebas de funciones anteriores.
            """),
            section("Leer y mantener", """
                Usa nombres que expliquen su papel: `total`, `precio`, `contador`. La indentación consistente expresa bloques. Separa partes del programa en funciones cuando tengan una responsabilidad clara. Un comentario útil explica por qué se tomó una decisión difícil; un comentario que solo repite `total += 1` añade ruido.

                La guía de estilo PEP 8 ofrece convenciones comunes para que otros puedan leer tu código. El formato ayuda, pero no reemplaza el razonamiento. Primero consigue una solución correcta y clara; después mejora nombres y organización sin alterar el comportamiento, comprobándolo de nuevo.
            """),
            section("Cuando una prueba falla", """
                Anota qué caso falló, qué esperabas y qué obtuviste. Si la salida contiene espacios o líneas extra, imprime una representación como `repr(texto)` en Python normal para ver caracteres invisibles. Si el problema está en una función, compruébala con entradas directas antes de revisar el programa completo.

                Añade una prueba para el error corregido. Así, si reaparece más adelante, tendrás una señal automática. En esta plataforma puedes volver a cualquier ejercicio: repetir uno días después sin mirar la respuesta es una prueba útil de aprendizaje.
            """),
        ],
        ["Prueba valores normales y límites.", "Las pruebas verifican comportamiento observable.", "Nombres y funciones claras facilitan detectar errores."],
        [("unittest", "https://docs.python.org/3.13/library/unittest.html"), ("PEP 8", "https://peps.python.org/pep-0008/")],
    ),
    chapter(
        "proyecto", "De ejercicios a proyectos", "Unir ideas y planear la siguiente etapa.", 10,
        [
            section("Convertir una idea en pasos", """
                Un proyecto empieza con una necesidad concreta: llevar gastos, organizar tareas o transformar un archivo. Escribe quién lo usará, qué datos recibe y qué resultado espera. Después divide el problema en pasos pequeños que puedas comprobar. Para una libreta de gastos: leer una cantidad, validarla, guardarla, sumar gastos y mostrar un informe.

                Construye primero una versión mínima que funcione de principio a fin. Añade una característica cada vez y conserva pruebas para los casos importantes. Ese ciclo —definir, implementar, probar y mejorar— es más manejable que escribir cientos de líneas antes de ejecutar.
            """),
            section("Arquitectura sencilla", """
                Una función puede encargarse de calcular, otra de leer o escribir y otra de presentar resultados. Separar cálculos de entrada y salida permite probar la lógica con datos fijos. Un archivo pequeño puede bastar al principio; si crece, puedes mover funciones relacionadas a módulos y usar `import`.

                Anota las dependencias y cómo iniciar el proyecto en un README. Guarda ejemplos de entrada y salida. Si manejas datos personales, evita incluirlos en ejemplos compartidos. Cuando el proyecto necesite paquetes externos, usa un entorno virtual y registra las versiones que probaste.
            """),
            section("Ruta después de los 100 ejercicios", """
                Después de los fundamentos, entra en Proyectos y avanza por los 12 retos intermedios: leer CSV y JSON, escribir un archivo, manejar errores, separar módulos, reparar código con pruebas, crear una clase, guardar datos en SQLite, recibir argumentos, registrar avisos, calcular fechas y combinar CSV con JSON. Cada reto tiene un ejemplo visible y más casos al pulsar «Comprobar etapa». Los capítulos nuevos de este manual preparan esas herramientas.

                Luego elige uno de los tres proyectos. En el gestor de gastos primero lees y sumas, después registras y por último agrupas por categoría. En el inventario primero cuentas existencias, después vendes y finalmente detectas faltantes. En el organizador de tareas primero listas pendientes, después agregas y al final completas. Cada etapa conserva el mismo borrador de `main.py` y `logica.py`; modifica tu propio trabajo en lugar de empezar otra vez.
            """),
            section("Cómo trabajar cada etapa", """
                Lee el objetivo y anota el contrato: entrada, archivos disponibles, salida en consola y archivos que deben cambiar. Ejecuta primero el ejemplo. Si falla, compara exactamente lo esperado con lo recibido; incluye espacios, tipos y estructura de los datos. Después pulsa «Comprobar etapa» para probar otros casos. Si la etapa 2 pasa el caso nuevo pero falla el comportamiento de la etapa 1, repara la regresión antes de seguir.

                Mantén `main.py` para leer comandos y presentar resultados; mueve las operaciones con datos a `logica.py`. Si necesitas otra pieza, puedes añadir un archivo `.py`. Los archivos de datos de cada prueba se crean temporalmente; tus cambios de código se guardan como borrador en la base local. Un proyecto terminado no es solo el que imprime el ejemplo: también resiste entradas distintas y conserva los datos correctos.
            """, note="Antes de pasar de etapa, explica con tus palabras qué archivo lee cada función, qué devuelve y qué modifica."),
            section("Cómo seguir aprendiendo", """
                Alterna lectura y práctica. Explica con tus palabras una idea antes de copiar el ejemplo. Cambia un dato y predice el resultado. Si un ejercicio resulta fácil, intenta una variante: acepta otra entrada, trata un caso límite o mueve el cálculo a una función. Si resulta difícil, vuelve al capítulo relacionado y construye una versión de tres líneas.

                El objetivo es poder razonar sobre un programa: saber qué datos tiene, qué cambia, cuándo termina y cómo comprobar que resuelve el problema. Esas preguntas seguirán sirviendo incluso cuando uses bibliotecas y herramientas más grandes.
            """),
        ],
        ["Parte de una necesidad y un resultado verificable.", "Divide el trabajo en funciones y pasos pequeños.", "Tras los 100 ejercicios siguen 12 retos intermedios y tres proyectos de tres etapas."],
        [("Tutorial oficial", "https://docs.python.org/3.13/tutorial/index.html")],
    ),
    chapter(
        "glosario", "Glosario esencial", "Palabras para entender la documentación y los errores.", 1,
        [
            section("Código y ejecución", """
                **Programa**: instrucciones organizadas para resolver una tarea. **Código fuente**: texto que escribes en archivos `.py`. **Intérprete**: programa que ejecuta código Python. **Sintaxis**: reglas de escritura; una violación produce un error de sintaxis. **Expresión**: fragmento que produce un valor, como `2 + 3`. **Sentencia**: instrucción, como una asignación o un `if`. **Bloque**: conjunto de líneas indentadas que pertenecen a una estructura.

                **Variable**: nombre que se refiere a un objeto. **Asignación**: operación `=` que vincula un nombre con un valor. **Tipo**: categoría de un objeto, como `int` o `str`. **Valor**: dato concreto. **Conversión**: crear un valor de otro tipo, por ejemplo `int("5")`. **Booleano**: `True` o `False`.
            """),
            section("Flujo y funciones", """
                **Condición**: expresión que decide si se ejecuta un bloque. **Iteración**: una vuelta de un bucle. **Iterable**: objeto que puede recorrerse con `for`. **Índice**: posición de un elemento, empezando en cero. **Función**: bloque definido con nombre que puedes llamar. **Parámetro**: nombre que recibe datos en la definición; **argumento**: valor suministrado en una llamada. **Retorno**: valor entregado por `return`. **Alcance**: región del programa donde un nombre está disponible.

                **Mutabilidad**: posibilidad de cambiar un objeto existente. **Método**: función asociada con un objeto, llamada mediante un punto. **Excepción**: señal de un problema durante la ejecución. **Traceback**: secuencia de llamadas que muestra cómo se llegó a una excepción.
            """),
            section("Organización y práctica", """
                **Módulo**: unidad importable, normalmente un archivo `.py`. **Paquete**: organización de módulos bajo un nombre. **Biblioteca estándar**: colección que acompaña a Python. **Dependencia**: paquete que un proyecto necesita. **Entorno virtual**: entorno separado para un proyecto. **Prueba**: comparación de comportamiento real con el esperado. **Depuración**: proceso de localizar y corregir un problema. **Persistencia**: conservar datos después de que termina una ejecución.

                Si una palabra sigue siendo confusa, vuelve al capítulo que la presenta y modifica su ejemplo. Un glosario sirve como mapa, pero la comprensión llega al usar cada término para explicar lo que hace tu propio programa.
            """),
        ],
        ["Vuelve a los ejemplos para dar significado a cada palabra.", "Usa la documentación oficial para ampliar un concepto."],
        [("Glosario de Python", "https://docs.python.org/3.13/glossary.html")],
    ),
]


from guide_advanced import advanced_chapters

GUIDE[19:19] = advanced_chapters(chapter, section)
RELATED_ADVANCED = {
    "errores-depuracion": "av-04-errores",
    "archivos-datos": "av-03-escribir",
    "pruebas-calidad": "av-06-pruebas",
    "csv-practico": "av-01-csv",
    "json-practico": "av-02-json",
    "modulos-propios": "av-05-modulos",
    "transformar-datos": "av-12-informe",
    "clases-objetos": "av-07-clase",
    "sqlite-practico": "av-08-sqlite",
    "terminal-argumentos": "av-09-cli",
    "registros-logging": "av-10-logging",
    "fechas-datetime": "av-11-fechas",
    "proyecto": "pr-gastos-1",
}
for item in GUIDE:
    item["advanced_id"] = RELATED_ADVANCED.get(item["id"])


def public_guide():
    return GUIDE
