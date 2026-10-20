"""Glosario original de bibliotecas para consulta desde la plataforma."""


CATEGORIES = [
    {"id": "numeros", "title": "Matemáticas y ciencia", "description": "Cálculos, estadística y modelos."},
    {"id": "texto", "title": "Texto y estructuras", "description": "Buscar patrones, transformar texto y organizar datos."},
    {"id": "archivos", "title": "Archivos y sistema", "description": "Rutas, carpetas, copias y procesos."},
    {"id": "tiempo", "title": "Fechas y tiempo", "description": "Fechas, duraciones y zonas horarias."},
    {"id": "web", "title": "Web y redes", "description": "Pedir páginas, leer HTML y construir servicios."},
    {"id": "datos", "title": "Tablas y bases de datos", "description": "Consultar, limpiar y guardar información."},
    {"id": "visual", "title": "Gráficos e imágenes", "description": "Visualizar datos, editar imágenes y crear juegos."},
    {"id": "pruebas", "title": "Pruebas y calidad", "description": "Comprobar programas y describir su comportamiento."},
    {"id": "herramientas", "title": "Herramientas de programa", "description": "Crear comandos y presentar resultados."},
    {"id": "seguridad", "title": "Seguridad y concurrencia", "description": "Generar secretos, resumir datos y coordinar tareas."},
]


def library(name, category, purpose, import_code, apis, url, install=None, example=""):
    return {
        "name": name,
        "category": category,
        "purpose": purpose,
        "kind": "external" if install else "standard",
        "install": install or "",
        "import_code": import_code,
        "apis": [{"name": api, "purpose": explanation} for api, explanation in apis],
        "example": example,
        "url": url,
    }


LIBRARIES = [
    # Matemáticas y ciencia
    library("math", "numeros", "Funciones matemáticas para raíces, trigonometría, logaritmos y constantes.", "import math", [("math.sqrt(x)", "Calcula la raíz cuadrada de x."), ("math.isclose(a, b)", "Compara valores decimales con una tolerancia.")], "https://docs.python.org/3.13/library/math.html", example="import math\nprint(math.sqrt(81))  # 9.0"),
    library("statistics", "numeros", "Resumen estadístico de colecciones pequeñas de números.", "import statistics", [("statistics.mean(datos)", "Calcula la media aritmética."), ("statistics.median(datos)", "Encuentra el valor central ordenado.")], "https://docs.python.org/3.13/library/statistics.html"),
    library("decimal", "numeros", "Cálculos decimales con precisión y reglas de redondeo configurables.", "from decimal import Decimal", [("Decimal('0.1')", "Crea un decimal desde texto para evitar aproximaciones binarias iniciales."), ("valor.quantize(paso)", "Redondea un Decimal a la precisión indicada.")], "https://docs.python.org/3.13/library/decimal.html"),
    library("fractions", "numeros", "Fracciones exactas como 1/3 y operaciones con numerador y denominador.", "from fractions import Fraction", [("Fraction(1, 3)", "Crea una fracción exacta."), ("Fraction('0.5')", "Convierte un decimal escrito como texto en fracción.")], "https://docs.python.org/3.13/library/fractions.html"),
    library("random", "numeros", "Selección y simulaciones pseudoaleatorias; no sirve para contraseñas.", "import random", [("random.randint(a, b)", "Devuelve un entero entre a y b, incluidos."), ("random.choice(secuencia)", "Elige un elemento de una secuencia no vacía.")], "https://docs.python.org/3.13/library/random.html", example="import random\nprint(random.randint(1, 6))  # simula un dado"),
    library("NumPy", "numeros", "Arreglos numéricos y operaciones rápidas sobre muchos valores.", "import numpy as np", [("np.array(datos)", "Construye un arreglo a partir de valores."), ("np.mean(arreglo)", "Calcula la media de un arreglo o eje.")], "https://numpy.org/doc/stable/", install="numpy"),
    library("SciPy", "numeros", "Algoritmos científicos, optimización, integración y estadística avanzada.", "from scipy import optimize, stats", [("optimize.minimize(función, inicio)", "Busca un mínimo numérico."), ("stats.norm.cdf(x)", "Evalúa la distribución normal acumulada.")], "https://docs.scipy.org/doc/scipy/", install="scipy"),
    library("scikit-learn", "numeros", "Preparación de datos y modelos clásicos de aprendizaje automático.", "from sklearn.model_selection import train_test_split\nfrom sklearn.linear_model import LinearRegression", [("train_test_split(X, y)", "Separa datos de entrenamiento y prueba."), ("LinearRegression().fit(X, y)", "Ajusta un modelo de regresión lineal.")], "https://scikit-learn.org/stable/", install="scikit-learn"),

    # Texto y estructuras
    library("re", "texto", "Búsquedas y sustituciones mediante expresiones regulares.", "import re", [("re.search(patrón, texto)", "Busca la primera coincidencia."), ("re.sub(patrón, reemplazo, texto)", "Reemplaza coincidencias en una cadena.")], "https://docs.python.org/3.13/library/re.html", example="import re\nprint(bool(re.search(r'\\d+', 'Pedido 42')))"),
    library("string", "texto", "Constantes de caracteres y plantillas simples de texto.", "import string", [("string.ascii_letters", "Contiene las letras ASCII mayúsculas y minúsculas."), ("string.Template(texto)", "Prepara una plantilla con variables indicadas por $.")], "https://docs.python.org/3.13/library/string.html"),
    library("json", "texto", "Intercambio de datos entre programas usando el formato JSON.", "import json", [("json.loads(texto)", "Convierte texto JSON en valores Python."), ("json.dumps(datos)", "Convierte valores compatibles de Python en texto JSON.")], "https://docs.python.org/3.13/library/json.html", example="import json\ndatos = json.loads('{\"nivel\": 2}')\nprint(datos['nivel'])"),
    library("csv", "texto", "Lectura y escritura de tablas de texto con separadores.", "import csv", [("csv.DictReader(archivo)", "Lee filas como diccionarios usando los encabezados."), ("csv.writer(archivo)", "Crea un escritor de filas CSV.")], "https://docs.python.org/3.13/library/csv.html"),
    library("collections", "texto", "Contenedores especializados para contar, agrupar y mantener valores.", "from collections import Counter, defaultdict", [("Counter(datos)", "Cuenta cuántas veces aparece cada elemento."), ("defaultdict(list)", "Crea una lista vacía al consultar una clave nueva.")], "https://docs.python.org/3.13/library/collections.html"),
    library("itertools", "texto", "Herramientas para combinar y recorrer datos sin crear listas innecesarias.", "import itertools", [("itertools.chain(a, b)", "Recorre dos iterables uno después del otro."), ("itertools.combinations(datos, 2)", "Genera parejas sin repetir el orden.")], "https://docs.python.org/3.13/library/itertools.html"),
    library("Pydantic", "texto", "Modelos de datos con validación y mensajes de error detallados.", "from pydantic import BaseModel", [("BaseModel", "Clase base para definir campos de un modelo."), ("Modelo.model_validate(datos)", "Valida datos y crea una instancia del modelo.")], "https://docs.pydantic.dev/latest/", install="pydantic"),

    # Archivos y sistema
    library("pathlib", "archivos", "Rutas y operaciones comunes de archivos con objetos Path.", "from pathlib import Path", [("Path('nota.txt').read_text()", "Lee el contenido de un archivo de texto."), ("ruta.exists()", "Indica si existe un archivo o carpeta.")], "https://docs.python.org/3.13/library/pathlib.html", example="from pathlib import Path\nruta = Path('notas.txt')\nprint(ruta.exists())"),
    library("os", "archivos", "Información del entorno y operaciones cercanas al sistema operativo.", "import os", [("os.getenv('NOMBRE')", "Lee una variable de entorno."), ("os.listdir(ruta)", "Enumera nombres dentro de una carpeta.")], "https://docs.python.org/3.13/library/os.html"),
    library("shutil", "archivos", "Copiar, mover y trabajar con árboles de archivos.", "import shutil", [("shutil.copy2(origen, destino)", "Copia archivo y conserva metadatos habituales."), ("shutil.move(origen, destino)", "Mueve un archivo o carpeta.")], "https://docs.python.org/3.13/library/shutil.html"),
    library("glob", "archivos", "Buscar rutas que coincidan con patrones como *.csv.", "import glob", [("glob.glob('*.csv')", "Obtiene archivos CSV del directorio actual."), ("glob.iglob(patrón)", "Recorre coincidencias sin crear la lista completa.")], "https://docs.python.org/3.13/library/glob.html"),
    library("tempfile", "archivos", "Crear archivos y carpetas temporales que se limpian al terminar.", "import tempfile", [("tempfile.TemporaryDirectory()", "Crea una carpeta temporal administrada."), ("tempfile.NamedTemporaryFile()", "Crea un archivo temporal con nombre.")], "https://docs.python.org/3.13/library/tempfile.html"),
    library("zipfile", "archivos", "Leer y crear archivos ZIP.", "from zipfile import ZipFile", [("ZipFile(ruta)", "Abre un archivo ZIP."), ("archivo.write(ruta)", "Añade un archivo al ZIP abierto en modo escritura.")], "https://docs.python.org/3.13/library/zipfile.html"),
    library("subprocess", "archivos", "Ejecutar otros programas y recibir su resultado.", "import subprocess", [("subprocess.run(argumentos)", "Ejecuta un comando y espera a que termine."), ("subprocess.Popen(argumentos)", "Inicia un proceso y permite interactuar con él.")], "https://docs.python.org/3.13/library/subprocess.html"),

    # Fechas y tiempo
    library("datetime", "tiempo", "Fechas, horas y diferencias entre momentos.", "from datetime import datetime, timedelta", [("datetime.now()", "Obtiene la fecha y hora local actual."), ("timedelta(days=1)", "Representa una duración de un día.")], "https://docs.python.org/3.13/library/datetime.html", example="from datetime import date, timedelta\nprint(date.today() + timedelta(days=7))"),
    library("time", "tiempo", "Medición de intervalos y pausas en segundos.", "import time", [("time.perf_counter()", "Devuelve un reloj apropiado para medir duración."), ("time.sleep(segundos)", "Pausa el hilo actual.")], "https://docs.python.org/3.13/library/time.html"),
    library("zoneinfo", "tiempo", "Zonas horarias IANA para fechas conscientes de su zona; en Windows puede requerir datos tzdata.", "from zoneinfo import ZoneInfo", [("ZoneInfo('America/Mexico_City')", "Crea un objeto de zona horaria."), ("fecha.astimezone(zona)", "Convierte una fecha consciente a otra zona.")], "https://docs.python.org/3.13/library/zoneinfo.html"),

    # Web y redes
    library("urllib.request", "web", "Pedir recursos por URL con herramientas de la biblioteca estándar.", "from urllib.request import urlopen, Request", [("urlopen(url)", "Abre una URL y entrega una respuesta."), ("Request(url, headers=...)", "Prepara una solicitud con encabezados.")], "https://docs.python.org/3.13/library/urllib.request.html", example="from urllib.request import urlopen\nwith urlopen('https://example.com') as respuesta:\n    print(respuesta.status)"),
    library("Requests", "web", "Solicitudes HTTP con una interfaz sencilla y respuestas fáciles de consultar.", "import requests", [("requests.get(url)", "Realiza una solicitud GET."), ("respuesta.json()", "Interpreta el cuerpo de la respuesta como JSON.")], "https://requests.readthedocs.io/en/latest/", install="requests"),
    library("HTTPX", "web", "Cliente HTTP con APIs síncronas y asíncronas.", "import httpx", [("httpx.get(url)", "Realiza una solicitud GET síncrona."), ("httpx.AsyncClient()", "Crea un cliente para solicitudes asíncronas.")], "https://www.python-httpx.org/", install="httpx"),
    library("Beautiful Soup", "web", "Analizar HTML y localizar elementos de una página.", "from bs4 import BeautifulSoup", [("BeautifulSoup(html, 'html.parser')", "Construye un árbol a partir de HTML."), ("sopa.select('a')", "Encuentra elementos mediante un selector CSS.")], "https://www.crummy.com/software/BeautifulSoup/bs4/doc/", install="beautifulsoup4"),
    library("FastAPI", "web", "Crear APIs web con rutas y validación de datos.", "from fastapi import FastAPI", [("FastAPI()", "Crea la aplicación web."), ("@app.get('/ruta')", "Asocia una función con una ruta GET.")], "https://fastapi.tiangolo.com/", install="fastapi"),
    library("Flask", "web", "Crear aplicaciones y servicios web pequeños o ampliables.", "from flask import Flask", [("Flask(__name__)", "Crea una aplicación Flask."), ("@app.route('/')", "Vincula una función con una URL.")], "https://flask.palletsprojects.com/en/stable/", install="flask"),

    # Tablas y bases de datos
    library("sqlite3", "datos", "Guardar y consultar datos estructurados en una base SQLite local.", "import sqlite3", [("sqlite3.connect(ruta)", "Abre o crea una base de datos SQLite."), ("conexión.execute(sql, parámetros)", "Ejecuta una consulta con parámetros separados.")], "https://docs.python.org/3.13/library/sqlite3.html", example="import sqlite3\nwith sqlite3.connect(':memory:') as con:\n    print(con.execute('SELECT 2 + 3').fetchone()[0])"),
    library("pandas", "datos", "Leer, limpiar, agrupar y analizar tablas de datos.", "import pandas as pd", [("pd.read_csv(ruta)", "Carga un archivo CSV como DataFrame."), ("tabla.groupby(columna)", "Agrupa filas para calcular resúmenes.")], "https://pandas.pydata.org/docs/", install="pandas"),
    library("Polars", "datos", "Trabajar con tablas usando expresiones y ejecución eficiente.", "import polars as pl", [("pl.read_csv(ruta)", "Lee un archivo CSV como DataFrame."), ("tabla.select(expresiones)", "Selecciona o calcula columnas.")], "https://docs.pola.rs/", install="polars"),
    library("openpyxl", "datos", "Leer y escribir libros de Excel .xlsx.", "from openpyxl import Workbook, load_workbook", [("load_workbook(ruta)", "Abre un libro de Excel existente."), ("libro.save(ruta)", "Guarda los cambios en un archivo .xlsx.")], "https://openpyxl.readthedocs.io/en/stable/", install="openpyxl"),
    library("SQLAlchemy", "datos", "Construir consultas y organizar el acceso a bases de datos.", "from sqlalchemy import create_engine, select", [("create_engine(url)", "Configura una conexión a la base de datos."), ("select(Modelo)", "Construye una consulta SELECT.")], "https://docs.sqlalchemy.org/en/20/", install="sqlalchemy"),

    # Gráficos e imágenes
    library("Matplotlib", "visual", "Crear gráficos estáticos para explorar o presentar datos.", "import matplotlib.pyplot as plt", [("plt.plot(x, y)", "Dibuja una línea."), ("plt.scatter(x, y)", "Dibuja puntos para comparar dos variables.")], "https://matplotlib.org/stable/", install="matplotlib", example="import matplotlib.pyplot as plt\nplt.plot([1, 2, 3], [2, 4, 3])\nplt.show()"),
    library("Seaborn", "visual", "Gráficos estadísticos construidos sobre Matplotlib.", "import seaborn as sns", [("sns.histplot(data=tabla, x='edad')", "Muestra la distribución de una variable."), ("sns.scatterplot(data=tabla, x='x', y='y')", "Relaciona dos variables con puntos.")], "https://seaborn.pydata.org/", install="seaborn"),
    library("Plotly", "visual", "Gráficos interactivos que pueden verse en el navegador.", "import plotly.express as px", [("px.scatter(tabla, x='x', y='y')", "Crea un gráfico de dispersión interactivo."), ("fig.show()", "Muestra la figura en un entorno compatible.")], "https://plotly.com/python/", install="plotly"),
    library("Pillow", "visual", "Abrir, transformar y guardar imágenes rasterizadas.", "from PIL import Image", [("Image.open(ruta)", "Abre e identifica un archivo de imagen."), ("imagen.resize(tamaño)", "Devuelve una imagen con otro tamaño.")], "https://pillow.readthedocs.io/en/stable/", install="Pillow"),
    library("OpenCV", "visual", "Procesar imágenes y video mediante algoritmos de visión.", "import cv2", [("cv2.imread(ruta)", "Lee una imagen desde un archivo."), ("cv2.cvtColor(imagen, código)", "Convierte el espacio de color de una imagen.")], "https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html", install="opencv-python"),
    library("pygame", "visual", "Crear juegos y programas multimedia en una ventana.", "import pygame", [("pygame.init()", "Inicializa módulos de pygame."), ("pygame.display.set_mode(tamaño)", "Crea una ventana de dibujo.")], "https://www.pygame.org/docs/", install="pygame"),

    # Pruebas y calidad
    library("unittest", "pruebas", "Escribir pruebas automáticas con casos y aserciones.", "import unittest", [("unittest.TestCase", "Clase base para agrupar pruebas."), ("self.assertEqual(real, esperado)", "Comprueba que dos valores sean iguales.")], "https://docs.python.org/3.13/library/unittest.html", example="import unittest\n\nclass Prueba(unittest.TestCase):\n    def test_suma(self):\n        self.assertEqual(2 + 2, 4)"),
    library("doctest", "pruebas", "Comprobar ejemplos escritos en la documentación de funciones.", "import doctest", [("doctest.testmod()", "Ejecuta ejemplos del módulo actual."), ("doctest.run_docstring_examples(objeto, globals())", "Prueba ejemplos de un objeto concreto.")], "https://docs.python.org/3.13/library/doctest.html"),
    library("pytest", "pruebas", "Ejecutar pruebas con funciones simples, aserciones y utilidades.", "import pytest", [("pytest.raises(Error)", "Comprueba que una operación lance una excepción."), ("@pytest.mark.parametrize(...)", "Ejecuta la misma prueba con varios datos.")], "https://docs.pytest.org/en/stable/", install="pytest"),
    library("Hypothesis", "pruebas", "Generar muchos casos de prueba a partir de reglas de datos.", "from hypothesis import given, strategies as st", [("@given(st.integers())", "Entrega enteros generados a una prueba."), ("st.lists(st.integers())", "Describe listas de enteros para las pruebas.")], "https://hypothesis.readthedocs.io/en/latest/", install="hypothesis"),
    library("logging", "pruebas", "Registrar eventos, avisos y errores de un programa.", "import logging", [("logging.getLogger(nombre)", "Obtiene un registrador con nombre."), ("logger.warning(mensaje)", "Emite un aviso con nivel WARNING.")], "https://docs.python.org/3.13/library/logging.html"),
    library("typing", "pruebas", "Anotaciones para describir tipos y apoyar revisiones del código.", "from typing import Protocol, TypedDict", [("TypedDict", "Describe las claves y tipos esperados de un diccionario."), ("Protocol", "Describe operaciones que debe ofrecer un objeto.")], "https://docs.python.org/3.13/library/typing.html"),

    # Herramientas de programa
    library("argparse", "herramientas", "Leer argumentos de una herramienta ejecutada desde la terminal.", "import argparse", [("argparse.ArgumentParser()", "Crea un analizador de argumentos."), ("parser.add_argument('--ruta')", "Declara una opción que acepta el programa.")], "https://docs.python.org/3.13/library/argparse.html", example="import argparse\np = argparse.ArgumentParser()\np.add_argument('--nombre', default='mundo')\nprint(p.parse_args().nombre)"),
    library("configparser", "herramientas", "Leer archivos de configuración en formato INI.", "import configparser", [("configparser.ConfigParser()", "Crea un analizador de configuración."), ("config.read(ruta)", "Carga un archivo INI.")], "https://docs.python.org/3.13/library/configparser.html"),
    library("Rich", "herramientas", "Mostrar tablas, colores y mensajes legibles en la terminal.", "from rich.console import Console\nfrom rich.table import Table", [("Console().print(texto)", "Imprime texto con formato en la terminal."), ("Table.add_row(...)", "Añade una fila a una tabla Rich.")], "https://rich.readthedocs.io/en/stable/", install="rich"),
    library("Typer", "herramientas", "Construir comandos de terminal a partir de funciones y tipos.", "import typer", [("typer.Typer()", "Crea una aplicación de comandos."), ("@app.command()", "Expone una función como comando.")], "https://typer.tiangolo.com/", install="typer"),

    # Seguridad y concurrencia
    library("secrets", "seguridad", "Generar valores aleatorios adecuados para secretos y tokens.", "import secrets", [("secrets.token_urlsafe(n)", "Crea un token seguro para URL."), ("secrets.choice(secuencia)", "Elige un elemento con aleatoriedad criptográfica.")], "https://docs.python.org/3.13/library/secrets.html", example="import secrets\nprint(secrets.token_urlsafe(16))"),
    library("hashlib", "seguridad", "Calcular resúmenes de datos para verificar integridad; un hash no cifra el contenido.", "import hashlib", [("hashlib.sha256(datos)", "Crea un objeto hash SHA-256 para bytes."), ("hash.hexdigest()", "Devuelve el resumen como texto hexadecimal.")], "https://docs.python.org/3.13/library/hashlib.html"),
    library("asyncio", "seguridad", "Coordinar tareas de entrada y salida con programación asíncrona.", "import asyncio", [("asyncio.run(corutina)", "Ejecuta una corutina principal."), ("asyncio.gather(a, b)", "Espera varias operaciones asíncronas.")], "https://docs.python.org/3.13/library/asyncio.html"),
    library("concurrent.futures", "seguridad", "Enviar tareas a grupos de hilos o procesos.", "from concurrent.futures import ThreadPoolExecutor", [("ThreadPoolExecutor()", "Crea un grupo de hilos para tareas."), ("executor.submit(función, dato)", "Programa una tarea y devuelve un Future.")], "https://docs.python.org/3.13/library/concurrent.futures.html"),
]


def public_catalog():
    return {"categories": CATEGORIES, "libraries": LIBRARIES}
