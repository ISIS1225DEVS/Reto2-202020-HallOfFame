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
def initCatalog(size,loadfactor):
    catalog=model.newCatalog(size,loadfactor)
    return catalog
# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________
def loadData(catalog,moviesCastingFile,moviesDetailsFile):
    loadmoviesDetailsCleaned(catalog,moviesDetailsFile)
    loadmoviesCastingRaw(catalog,moviesCastingFile)

def loadmoviesCastingRaw(catalog,moviesfile):
    moviesfile = cf.data_dir + moviesfile
    dialect = csv.excel()
    dialect.delimiter=";"
    input_file= csv.DictReader(open(moviesfile, encoding='utf-8-sig'),dialect=dialect)
    for movie in input_file:
        model.addMovieCasting(catalog,movie)
        actors1 = movie['actor1_name'].split(",")
        actors2 = movie['actor2_name'].split(",")
        actors3 = movie['actor3_name'].split(",")
        actors4 = movie['actor4_name'].split(",")
        actors5 = movie['actor5_name'].split(",")
        directors = movie['director_name'].split(",")
        for autor in actors1:
            model.addMovieByActor(catalog, autor.strip().lower(), movie)
        for autor in actors2:
            model.addMovieByActor(catalog, autor.strip().lower(), movie)
        for autor in actors3:
            model.addMovieByActor(catalog, autor.strip().lower(), movie)
        for autor in actors4:
            model.addMovieByActor(catalog, autor.strip().lower(), movie)
        for autor in actors5:
            model.addMovieByActor(catalog, autor.strip().lower(), movie)
        for director in directors:
            model.addMovieByDirector(catalog, director.strip().lower(), movie)
        
def loadmoviesDetailsCleaned(catalog,moviesfile):
    moviesfile = cf.data_dir + moviesfile
    dialect = csv.excel()
    dialect.delimiter=";"
    input_file = csv.DictReader(open(moviesfile,encoding='utf-8-sig'),dialect=dialect)
    for movie in input_file:
        model.addMovieDetails(catalog,movie)
        companies = movie['production_companies'].split(",")
        genres = movie['genres'].split(",")
        countries = movie['production_countries'].split(",")
        for company in companies:
            model.addMovieByProductionCompany(catalog, company.strip().lower(), movie)
        for genre in genres:
            model.addMovieByGenre(catalog, genre.strip().lower(), movie)
        for productionCountry in countries:
            model.addMovieByProductionCountry(catalog, productionCountry.strip().lower(), movie)
# ___________________________________________________
#  Funciones para consultas
# ___________________________________________________
def moviesDetailsSize(catalog):
    return model.moviesDetailsSize(catalog)

def moviesCastingSize(catalog):
    return model.moviesCastingSize(catalog)

def moviesIdsSize(catalog):
    return model.MoviesIdsSize(catalog)

def actorsSize(catalog):
    return model.actorsSize(catalog)

def genresSize(catalog):
    return model.genresSize(catalog)

def productionCompaniesSize(catalog):
    return model.productionCompaniesSize(catalog)

def countriesSize(catalog):
    return model.countriesSize(catalog)

def voteAverageSize(catalog):
    return model.voteAverageSize(catalog)

def voteCountSize(catalog):
    return model.voteCountSize(catalog)

def getMoviesByDirector(catalog,directorName):
    return model.getmoviesByDirector(catalog,directorName)

def getMoviesByActor(catalog):
    return model.getmoviesByActor(catalog)

def getMoviesByProductionCompanies(catalog):
    return model.getmoviesByProductionCompany(catalog)

def getMoviesByCountry(catalog):
    return model.getmoviesByCountry(catalog)

def getMoviesByGenre(catalog):
    return model.getmoviesByGenre(catalog)

def descubrirProductorasDeCine(catalog, nameCompany):
    return model.descubrirProductorasDeCine(catalog, nameCompany)

def conocerUnActor(catalog, nameActor):
    return model.conocerUnActor(catalog,nameActor)

def entenderUnGenero(catalog, genre):
    return model.entenderUnGenero(catalog,genre)    

def encontrarPeliculasPorPais(catalog, country):
    return model.encontrarPeliculasPorPais(catalog, country)

def conocerUnDirector(catalog, name):
    return model.conocerUnDirector(catalog,name)