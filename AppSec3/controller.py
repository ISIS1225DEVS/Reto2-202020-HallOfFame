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
    catalog = model.newCatalog()
    return catalog

# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________


def loadData(catalog, detailsfile, castingfile):
    """
    Carga cada una de las lineas del archivo de libros.
    - Se agrega cada libro al catalogo de libros
    - Por cada libro se encuentran sus autores y por cada
      autor, se crea una lista con sus libros
    """
    t1_start = process_time() #tiempo inicial
    dialect = csv.excel()
    dialect.delimiter = ";"
    detailsfile = cf.data_dir + detailsfile
    #input_file = #csv.DictReader(open(detailsfile,encoding="utf-8"), dialect=dialect)
    input_file = csv.DictReader(open(detailsfile,encoding="utf-8-sig"),dialect= dialect)
    castingfile = cf.data_dir + castingfile
    input_file2 = csv.DictReader(open(castingfile,encoding="utf-8"),dialect= dialect)
    #i = 0
    #j = 0
    for movie,casting in zip(input_file,input_file2):
      #i += 1
      model.addMovie(catalog,movie)
      model.addCasting(catalog,casting,movie)
      #print(i)
    t1_stop = process_time()
    #print(t1_stop)
    """for casting in input_file2:
      j += 1
      model.addCasting(catalog,casting)
      print(j)
    t1_stop = process_time() #tiempo final"""
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")


# ___________________________________________________
#  Funciones para consultas
# ___________________________________________________


def moviesSize(catalog):
  """Numero de libros leido
  """
  return model.moviesSize(catalog)


def directorsSize(catalog):
  """Numero de autores leido
  """
  return model.directorsSize(catalog)


def actorsSize(catalog):
  """Numero de tags leido
  """
  return model.actorsSize(catalog)


  
def getMoviesByProductionCompany(catalog,ProductionCompany):
  """
  Retorna las películas de un una productora de Cine
  """
  productioncompanyinfo = model.getMoviesByProductionCompany(catalog, ProductionCompany)
  return productioncompanyinfo


def getMoviesByDirector(catalog, directorname):
  """
    Retorna las películas de un director
  """
  directorinfo = model.getMoviesByDirector(catalog, directorname)
  return directorinfo


def getMoviesByActor(catalog, actorname):
  """
  Retorna las películas de un actor
  """
  actorinfo = model.getMoviesByActor(catalog, actorname)
  actorinfo["DirectorMaxCol"]=model.masrepetido(actorinfo["directors"]["elements"])
  return actorinfo

def getMoviesByCountry(catalog, country):
  """
  Retorna las películas de un país
  """
  model.addMovieDirectorsbyCountry(catalog, country)
  countryinfo = model.getMoviesByCountry(catalog, country)
  return countryinfo

def moviesByGenre(catalog,genre):
  info = model.getMoviesByGenre(catalog, genre)
  movies = info[0]
  count = model.listSize(movies)
  moviesReduced = model.getFifteenElements(movies)
  prom = info[1]/count
  return (moviesReduced,count,prom)
