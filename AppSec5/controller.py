"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
from App import model
import csv
from DISClib.DataStructures import mapstructure as mp
from DISClib.DataStructures import listiterator as it
from time import perf_counter
from random import randint

"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta. Esta responsabilidad
recae sobre el controlador.
"""


# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________

def initCatalog(map_type, loadfactor):
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    # catalog es utilizado para interactuar con el modelo
    catalog = model.newCatalog(map_type, loadfactor)
    return catalog


# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________
# def loadData(catalog, file1, file2):
#     """
#     Carga los datos de los archivos en el modelo
#     """
#     loadMovies(catalog, file1, file2)


def loadData(catalog, movies_file1, movies_file2, n: int = "ALL"):
    """
    Carga cada una de las lineas del archivo de libros.
    - Se agrega cada libro al catalogo de libros
    - Por cada libro se encuentran sus autores y por cada
      autor, se crea una lista con sus libros>
    """
    dialect = csv.excel()
    dialect.delimiter = ";"
    movies_file1 = cf.data_dir + movies_file1
    movies_file2 = cf.data_dir + movies_file2

    input_file1 = csv.DictReader(open(movies_file1, encoding="utf-8-sig"), dialect=dialect)
    input_file2 = csv.DictReader(open(movies_file2, encoding="utf-8-sig"), dialect=dialect)

    count = 0
    for movie1, movie2 in zip(input_file1, input_file2):
        if (n != "ALL") and (count > n):
            break
        movie1.update(movie2)  # se que es severo machetazo :V, lo sugirio  erich
        model.addMovie(catalog, movie1)
        count += 1


def get_name(catalog, tag, name):
    producer = model.getMoviesinTagbyName(catalog, tag, name)
    return producer


def info_movies(movies, var_prom, var_freq):
    return model.info_movies(movies, var_prom, var_freq)
