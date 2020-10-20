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

#-------------------------------------------------------------
#-------------------------------------------------------------
#               Tomado de grupo 2 - sec 4
#-------------------------------------------------------------
#-------------------------------------------------------------


import config as cf
from AppSec4 import model
from time import process_time
import csv


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

def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    # catalog es utilizado para interactuar con el modelo
    catalog = model.newCatalog()
    return catalog

# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________

def loadData(catalog, moviesFile, castingFile):
    """
    Carga los datos de los archivos en el modelo
    """
    t1=process_time()
    loadMovies(catalog, moviesFile)
    loadCasting(catalog, castingFile)
    t2=process_time()
    print("Tiempo de carga de datos " + str(t2-t1) +" s")

def loadMovies(catalog, moviesfile):
    """
    Carga cada una de las lineas del archivo de libros.
    - Se agrega cada libro al catalogo de libros
    - Por cada libro se encuentran sus autores y por cada
      autor, se crea una lista con sus libros
    """

    dialect = csv.excel()
    dialect.delimiter=";"
    try:
        with open(  "Data/" + moviesfile, encoding="utf-8") as csvfile:
            row = csv.DictReader(csvfile, dialect=dialect)
            for movie in row: 
                model.addMovie(catalog, movie)
                producer = movie['production_companies']
                country=movie["production_countries"]
                model.addMovieCountry(catalog,country,movie)
                model.addMovieProducer(catalog,producer,movie)
                genres = movie["genres"].split("|")
                for i in range(0,len(genres)):
                    model.addMovieGenre(catalog, genres[i],movie)
    except Exception as e:
        print(e)
        print("Hubo un error con la carga del archivo")

def loadCasting(catalog, castingFile):
    dialect = csv.excel()
    dialect.delimiter=";"
    try:
        with open(  "Data/" + castingFile, encoding="utf-8") as csvfile:
            row = csv.DictReader(csvfile, dialect=dialect)
            for movie in row: 
                director = movie['director_name']
                idActual = movie["id"]
                model.addCasting(catalog,movie)
                actual = model.getMoviesByElement(catalog,"ids", idActual)
                
                for i in range(1,6):
                    actor_name = movie["actor"+str(i)+"_name"]
                    model.addMovieActor(catalog,actor_name,actual)
                    actor = model.getElement(catalog,"actors",actor_name)
                    model.addDirectorActor(actor,director)
                model.addMovieDirector(catalog,director,actual)
    except:
        print("Hubo un error con la carga del archivo")

def firstMovie(catalog):
    return model.firstMovie(catalog)

def lastMovie(catalog):
    return model.lastMovie(catalog)

def getElement(catalog, element, elementName):
    return model.getElement(catalog, element, elementName)

def getMoviesByElement(catalog,element, elementName):
    return model.getMoviesByElement(catalog, element, elementName)

def getMoviesByElementSize(catalog,element, elementName):
    return model.getMoviesByElementSize(catalog,element,elementName)

def getMejorDirector(catalog,actorName):
    return model.getMejorDirector(catalog,actorName)

def getDirectorMovie (catalog,id):
    return model.getDirectorMovie(catalog,id)

def elementsSize(catalog):
    return model.elementsSize(catalog)

def moviesSize(catalog):
    return model.moviesSize(catalog)