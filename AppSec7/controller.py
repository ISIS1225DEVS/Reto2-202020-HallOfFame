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
 
def loadData(catalog, moviesfile, moviesfile2):
    """
    Carga los datos de los archivos en el modelo
    """
    loadMovie(catalog, moviesfile)
    loadMovie2(catalog, moviesfile2)
 
def loadMovie(catalog, moviesfile):
    moviesfile = cf.data_dir + moviesfile
    dialect = csv.excel()
    dialect.delimiter=";"
    input_file = csv.DictReader(open(moviesfile,encoding="utf-8"),dialect=dialect)
    for movie in input_file:
        model.addMovie(catalog,movie)

def loadMovie2(catalog, moviesfile2):
    moviesfile2 = cf.data_dir + moviesfile2
    dialect = csv.excel()
    dialect.delimiter=";"
    input_file = csv.DictReader(open(moviesfile2,encoding="utf-8"),dialect=dialect)
    for movie in input_file:
        model.addCasting(catalog,movie)
 
# ___________________________________________________
#  Funciones para consultas
# ___________________________________________________
def movieSize(catalog):
    retorno = model.sizeMovies(catalog)
    return retorno
  
def castingSize(catalog):
    retorno=model.sizeCasting(catalog)
    return retorno
  
def Titulo(catalog, pos):
    retorno = model.getTitulo(catalog, pos)
    return retorno
 
def Fecha(catalog, pos):
    retorno = model.getFecha(catalog, pos)
    return retorno
 
def Promedio(catalog, pos):
    retorno = model.getPromedio(catalog, pos)
    return retorno
 
def Votos(catalog, pos):
    retorno = model.getVotos(catalog,pos)
    return retorno
 
def Idioma(catalog, pos):
    retorno = model.getIdioma(catalog,pos)
    return retorno
 
def FirstandLastElementsNTFPVI(catalog,titulo,fecha,promedio,votos,idioma,tamaño,pos):
    retorno = model.getFirstandLastElementsNTFPVI(catalog,titulo,fecha,promedio,votos,idioma,tamaño,pos)
    return retorno

def infoProductor(catalog, producer):
    retorno = model.addProducer(catalog, producer)
    return retorno

def infoDirector(catalog, director):
    retorno = model.addDirector(catalog, director)
    return retorno

def infoActor (catalog, actor):
    retorno= model.addActor(catalog, actor)
    return retorno
  
def infoGenero(catalog, genero):
    retorno = model.addGenero(catalog, genero)
    return retorno

def infoPais(catalog, pais):
    retorno = model.addPais(catalog, pais)
    return retorno
