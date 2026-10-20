"""Ayuda pedagógica y diagnósticos locales. No envía código ni errores fuera del equipo."""

LESSON_HINTS = {
    1: ("Identifica el valor exacto que debe aparecer y en qué orden se ejecutan las líneas.", "Completa una línea del código inicial y ejecútala antes de añadir más."),
    2: ("Calcula a mano el resultado del ejemplo antes de escribir la operación.", "Revisa qué datos son enteros, qué operación necesitas y dónde mostrar el resultado."),
    3: ("Separa las partes fijas del mensaje de las partes que cambian.", "Prueba una operación de cadenas con un ejemplo pequeño; después aplícala a la entrada del reto."),
    4: ("Piensa qué recibe cada llamada a input() y qué tipo de dato devuelve.", "Prueba con una segunda entrada distinta para confirmar que no escribiste la respuesta fija."),
    5: ("Enumera los casos posibles y decide qué condición distingue uno de otro.", "Prueba un valor menor, uno igual y uno mayor que el límite del enunciado."),
    6: ("Identifica qué debe repetirse y cuándo debe terminar el bucle.", "Revisa el inicio y el límite de range() o la condición de parada."),
    7: ("Piensa en una lista pequeña y sigue el valor de cada elemento paso a paso.", "Comprueba índices, acumuladores y qué ocurre con una lista vacía si el reto la permite."),
    8: ("Dibuja las claves y los valores que necesitas conservar.", "Prueba primero con un diccionario de dos elementos y revisa el caso de una clave ausente."),
    9: ("Distingue los parámetros que entran de lo que la función debe devolver.", "Llama mentalmente a la función con dos argumentos diferentes; evita fijar el resultado del ejemplo."),
    10: ("Divide el problema en entrada, transformación y salida.", "Prueba cada paso con pocos datos antes de combinarlo todo."),
}

LAB_HINTS = {
    "lab-01-versiones": ("Compara 1.10 y 1.9 como texto: ¿por qué sale mal?", "Busca en packaging el objeto que interpreta versiones antes de compararlas."),
    "lab-02-rangos": ("El rango es una regla; la versión es un valor que debes contrastar con ella.", "La documentación de packaging distingue objetos para versiones y para especificadores."),
    "lab-03-fechas": ("Primero convierte el texto en una fecha; después cambia su formato.", "Configura la lectura de fechas numéricas para que el día vaya primero."),
    "lab-04-meses": ("Sumar 30 días no equivale a sumar un mes de calendario.", "Busca una diferencia de calendario en dateutil y pruébala con el 31 de enero."),
    "lab-05-yaml-usuario": ("El texto YAML representa un mapa con claves y valores.", "Carga el YAML de forma segura y consulta la clave solicitada."),
    "lab-06-yaml-pedidos": ("Tras cargar el YAML, la clave pedidos contiene una lista de números.", "Usa una suma de Python sobre la lista ya convertida."),
    "lab-07-requests": ("Solo necesitas la URL final. No hagas una conexión HTTP.", "Busca cómo preparar un objeto Request con params y leer su URL."),
    "lab-08-numpy-media": ("Piensa qué operación agrega todos los valores en un solo número.", "NumPy devuelve un escalar propio; conviértelo a float para devolverlo."),
    "lab-09-numpy-forma": ("Cuatro valores se pueden distribuir en dos filas y dos columnas.", "Convierte la entrada a arreglo, cambia su forma y al final conviértela a listas."),
    "lab-10-pandas-grupos": ("Varias filas comparten categoría; sus montos deben reunirse.", "Construye una tabla, agrupa por categoria y suma la columna monto."),
    "lab-11-pandas-faltantes": ("None representa un dato ausente; no debe contar en el promedio.", "La serie de pandas sabe omitir faltantes al calcular la media."),
    "lab-12-pillow-color": ("Una imagen RGB guarda tres canales por píxel.", "Crea una imagen en memoria y consulta el píxel de la esquina superior izquierda."),
    "lab-13-pillow-gris": ("La salida es un solo valor, aunque el color de entrada tenga tres canales.", "Busca en ImageOps la conversión a escala de grises."),
    "lab-14-rich": ("Las etiquetas de estilo no forman parte del texto visible.", "Interpreta el marcado con Rich y consulta la propiedad del texto sin formato."),
    "lab-15-ventas-yaml": ("Separa el proyecto en lectura de datos y cálculo por categoría.", "Carga el YAML, crea una tabla con ventas y agrupa los montos por categoria."),
    "lab-16-paleta": ("Cada color hexadecimal representa tres canales RGB.", "Convierte los colores con Pillow y calcula la media por columna con NumPy."),
    "lab-17-api-config": ("El YAML guarda la base y los parámetros de una petición.", "Carga la configuración y prepara un GET con requests sin enviarlo."),
}

LAB_FINAL_HINTS = {
    "lab-15-ventas-yaml": "Usa yaml.safe_load(texto)['ventas'] y luego un DataFrame para agrupar 'categoria' y sumar 'monto'. Devuelve un dict.",
    "lab-16-paleta": "Convierte cada hexadecimal con PIL.ImageColor.getrgb; np.array(...).mean(axis=0).tolist() devuelve tres promedios.",
    "lab-17-api-config": "Lee url y parametros con yaml.safe_load; prepara requests.Request('GET', url, params=parametros) y devuelve .prepare().url.",
}

LAB_DEBUG = {
    "lab-01-versiones": "Una comparación de texto falla en 1.10 frente a 1.9. Convierte ambas cadenas a Version.",
    "lab-02-rangos": "Prueba los límites del rango: una versión dentro y otra justo fuera.",
    "lab-03-fechas": "Comprueba si 01/02 significa 1 de febrero; dayfirst cambia esa interpretación.",
    "lab-04-meses": "Comprueba qué ocurre al sumar un mes al 31 de enero en un año bisiesto.",
    "lab-05-yaml-usuario": "safe_load devuelve datos de Python; aquí necesitas el valor de la clave usuario.",
    "lab-06-yaml-pedidos": "Prueba también pedidos: []; la suma debe ser cero.",
    "lab-07-requests": "No unas la URL y la consulta a mano: params debe codificar espacios y signos +.",
    "lab-08-numpy-media": "Comprueba que estás calculando la media, no la suma, y devuelve float.",
    "lab-09-numpy-forma": "La salida debe ser una lista de listas de 2 × 2, no un ndarray.",
    "lab-10-pandas-grupos": "Suma los montos de categorías repetidas y devuelve un diccionario de Python.",
    "lab-11-pandas-faltantes": "None no debe contarse como cero ni aumentar el divisor de la media.",
    "lab-12-pillow-color": "getpixel devuelve una tupla RGB; el contrato pide una lista.",
    "lab-13-pillow-gris": "La salida es un entero de luminancia; comprueba negro, blanco y gris medio.",
    "lab-14-rich": "El resultado no debe contener etiquetas [bold] ni [red].",
    "lab-15-ventas-yaml": "Agrupa las filas después de cargar el YAML; la misma categoría puede aparecer varias veces.",
    "lab-16-paleta": "Calcula la media de cada canal por separado; no redondees los valores 127.5 a enteros.",
    "lab-17-api-config": "Deja que requests codifique los parámetros; un espacio en q debe aparecer como + en la URL.",
}


def lesson_hints(lesson):
    first, second = LESSON_HINTS[lesson["unit"]]
    return [first, second, lesson["hint"]]


def lab_hints(lab):
    first, second = LAB_HINTS[lab["id"]]
    return [first, second, LAB_FINAL_HINTS.get(lab["id"], lab["hint"])]


def runtime_diagnosis(error):
    """Traduce errores habituales en una comprobación que el alumno pueda hacer."""
    if "ModuleNotFoundError" in error:
        return "Python no encontró un módulo. Comprueba que instalaste el paquete en el entorno del laboratorio y que el nombre del import es el indicado; el nombre de pip puede ser distinto."
    if "ImportError" in error:
        return "El paquete existe, pero esa importación no funcionó. Revisa el nombre del módulo y del elemento en su documentación."
    if "IndentationError" in error or "unexpected indent" in error:
        return "Revisa los espacios al principio de las líneas. Después de def, if o for, el bloque debe ir indentado de forma consistente."
    if "SyntaxError" in error:
        return "Revisa la línea señalada y la anterior: comillas, paréntesis y dos puntos al final de def, if o for."
    if "NameError" in error:
        return "Hay un nombre que Python no conoce. Revisa mayúsculas, alias del import y si definiste la variable antes de usarla."
    if "TypeError" in error:
        return "Una operación recibió un tipo o número de argumentos distinto del esperado. Mira qué tipo entra a solve y qué devuelve cada paso."
    if "KeyError" in error:
        return "La clave consultada no existe en ese diccionario. Comprueba la estructura de los datos recibidos y el nombre exacto de la clave."
    if "IndexError" in error:
        return "Intentaste acceder a una posición fuera de la lista. Revisa su longitud y recuerda que el primer índice es 0."
    if "AttributeError" in error:
        return "Ese objeto no tiene el método o atributo escrito. Comprueba el tipo del objeto y el nombre en la documentación."
    if "ValueError" in error:
        return "El valor tiene una forma que esa función no admite. Revisa el ejemplo de entrada y la conversión que haces."
    if "ZeroDivisionError" in error:
        return "Hay una división entre cero. Revisa el divisor antes de calcular."
    return "Localiza la primera línea de tu código mencionada por el error y comprueba sus datos de entrada."


def mismatch_diagnosis(lab_id=None, unit=None):
    if lab_id:
        return LAB_DEBUG[lab_id]
    by_unit = {
        1: "Compara letras, espacios y saltos de línea con la salida esperada.",
        2: "Calcula el caso a mano; revisa el orden de operaciones y el tipo de número.",
        3: "Revisa mayúsculas, espacios y signos; la salida debe coincidir exactamente.",
        4: "Tu programa debe funcionar con entradas distintas del ejemplo, no con un texto fijo.",
        5: "Prueba los valores justo antes, en y después del límite de la condición.",
        6: "Revisa el número de vueltas y si el último valor del rango se incluye.",
        7: "Comprueba el orden de los elementos y qué ocurre en listas pequeñas.",
        8: "Revisa las claves, los valores y si una clave aparece más de una vez.",
        9: "Comprueba que la función devuelve el resultado para cualquier argumento.",
        10: "Divide el programa en pasos y prueba cada transformación por separado.",
    }
    return by_unit.get(unit, "Prueba un caso pequeño y compara cada paso.")


def installation_diagnosis(output, lab, command):
    """Clasifica texto pegado desde PowerShell sin ejecutar lo que contiene."""
    line = output.casefold()
    if not output.strip():
        return "Pega el error completo que mostró PowerShell para poder identificar la causa."
    if "no module named pip" in line:
        return "Este Python no encuentra pip. Pulsa Preparar entorno y comprueba que el comando usa data/library_venv/Scripts/python.exe. Después ejecuta de nuevo el comando de instalación."
    if "modulenotfounderror" in line or "no module named" in line:
        return f"El módulo no está disponible para el Python que ejecutó tu código. Instala en el entorno del curso con este comando y vuelve a comprobar: {command}"
    if "not recognized" in line or "no se reconoce" in line or "commandnotfoundexception" in line:
        return f"PowerShell no encontró el comando. Copia la línea completa, incluido el símbolo & y las comillas de la ruta: {command}"
    if "externally-managed-environment" in line:
        return f"Estás usando un Python gestionado por el sistema. Usa el entorno virtual del curso: {command}"
    if "could not find a version that satisfies" in line or "no matching distribution found" in line:
        return "pip no encontró una versión compatible. Comprueba que copiaste el nombre del paquete y consulta la versión de Python del entorno; algunos paquetes no admiten todas las versiones de Python."
    if "certificate_verify_failed" in line or "ssl" in line:
        return "La descarga falló al verificar la conexión segura. Comprueba fecha y hora del equipo y la configuración de red o proxy; después vuelve a intentarlo."
    if "readtimeout" in line or "connectionerror" in line or "connection refused" in line or "failed to establish a new connection" in line:
        return "pip no pudo conectarse al índice de paquetes. Comprueba tu conexión a Internet y vuelve a ejecutar el comando."
    if "permissionerror" in line or "access is denied" in line or "acceso denegado" in line:
        return "El entorno no pudo escribir archivos. Comprueba que la carpeta de la plataforma sea editable y que no haya otro proceso instalando el mismo paquete."
    if "no space left" in line or "espacio insuficiente" in line:
        return "No hay suficiente espacio para descargar o instalar la biblioteca. Libera espacio y vuelve a intentar."
    return f"No reconozco todavía este error. Comprueba que preparaste el entorno y ejecutaste exactamente: {command}. Conserva el mensaje completo para revisarlo."
