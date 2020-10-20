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



import config
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from time import process_time
assert config

"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria

"""

# -----------------------------------------------------
# API del TAD Catalogo de Libros
# -----------------------------------------------------
def newCatalog():
    catalogo={
        "movies":None,
        "producers":None,
        "directors":None,
        "actors":None,
        "genres":None,
        "countries":None,
        "ids":None
    }

    catalogo['movies'] = lt.newList("ARRAY_LIST",None)
    catalogo["ids"] = mp.newMap(2000,
                                   maptype='CHAINING',
                                   loadfactor=1,
                                   comparefunction=compareMapMovieIds)
    catalogo['producers'] = mp.newMap(200,
                                   maptype='CHAINING',
                                   loadfactor=1,
                                   comparefunction=compareProducersByName)
    catalogo["directors"] = mp.newMap(200,
                                   maptype='CHAINING',
                                   loadfactor=1,
                                   comparefunction=compareDirectorsByName)
    catalogo["actors"] = mp.newMap(200,
                                   maptype='CHAINING',
                                   loadfactor=1,
                                   comparefunction=compareActorsByName)
    catalogo["genres"] = mp.newMap(200,
                                   maptype='CHAINING',
                                   loadfactor=1,
                                   comparefunction=compareGenreByName)

    catalogo["countries"] = mp.newMap(200,
                                   maptype='CHAINING',
                                   loadfactor=1,
                                   comparefunction=compareCountryByName)

    


    return catalogo

def newProducer(name):
    """
    Crea una nueva estructura para modelar los libros de un autor
    y su promedio de ratings
    """
    producer = {'name': "", "movies": None,  "average_voting": 0}
    producer['name'] = name
    producer['movies'] = lt.newList('ARRAY_LIST', compareMoviesIds)
    return producer

def newDirector(name):
    director = {'name': "", "movies": None,  "average_voting": 0}
    director['name'] = name
    director['movies'] = lt.newList('ARRAY_LIST', compareMoviesIds)
    return director

def newActor(name):
    actor = {'name': "", "movies": None,  "average_voting": 0,"directores":None}
    actor['name'] = name
    actor['movies'] = lt.newList('ARRAY_LIST', compareMoviesIds)
    actor["directores"] = mp.newMap(200,
                                   maptype='CHAINING',
                                   loadfactor=0.4,
                                   comparefunction=compareDirectorsByName)
    return actor

def newGenre(name):
    genre = {'name': "", "movies": None,  "average_voting": 0}
    genre['name'] = name
    genre['movies'] = lt.newList('ARRAY_LIST', compareMoviesIds)
    return genre

def newCountry(name):
    country = {'name': "", "movies": None}
    country['name'] = name
    country['movies'] = lt.newList('ARRAY_LIST', compareMoviesIds)
    return country

def newId(name):
    id = {'name': "", "movie": None,"casting":None}
    id['name'] = name
    return id


# Funciones para agregar informacion al catalogo

def addMovie(catalog, movie):
    """
    Esta funcion adiciona un libro a la lista de libros,
    adicionalmente lo guarda en un Map usando como llave su Id.
    Finalmente crea una entrada en el Map de años, para indicar que este
    libro fue publicaco en ese año.
    """
    lt.addLast(catalog['movies'], movie)
    ids = catalog['ids']
    idName=movie["id"]
    existid = mp.contains(ids, idName)
    if existid:
        entry = mp.get(ids, idName)
        id = me.getValue(entry)
    else:
        id = newId(idName)
        mp.put(ids, idName, id)
    id['movie']= movie


def addCasting (catalog,casting):
    ids = catalog['ids']
    idName=casting["id"]
    existid = mp.contains(ids, idName)
    if existid:
        entry = mp.get(ids, idName)
        id = me.getValue(entry)
    else:
        id = newId(idName)
        mp.put(ids, idName, id)
    id['casting']= casting




def addMovieProducer(catalog, producerName, movie):
    producers = catalog['producers']
    existproducer = mp.contains(producers, producerName)
    if existproducer:
        entry = mp.get(producers, producerName)
        producer = me.getValue(entry)
    else:
        producer = newProducer(producerName)
        mp.put(producers, producerName, producer)
    lt.addLast(producer['movies'], movie)
    
    prodavg = producer['average_voting']
    movavg = movie['vote_average']
    if (prodavg != 0):
        producer['average_voting'] = round((prodavg*(getMoviesByElementSize(catalog,"producers",producerName)-1) + float(movavg)) / getMoviesByElementSize(catalog,"producers",producerName),2)
    else:
        producer['average_voting'] = float(movavg)

def addMovieDirector(catalog, directorName, movie):
    directors = catalog['directors']
    existDirector = mp.contains(directors, directorName)
    if existDirector:
        entry = mp.get(directors, directorName)
        director = me.getValue(entry)
    else:
        director = newDirector(directorName)
        mp.put(directors, directorName, director)
    lt.addLast(director['movies'], movie)
    diravg = director['average_voting']
    movavg = movie['vote_average']
    if (diravg != 0):
        director['average_voting'] = round((diravg*(getMoviesByElementSize(catalog,"directors",directorName)-1) + float(movavg)) / getMoviesByElementSize(catalog,"directors",directorName),2)
    else:
        director['average_voting'] = float(movavg)

def addMovieActor(catalog, actorName, movie):
    actors = catalog['actors']
    existActor = mp.contains(actors, actorName)
    if existActor:
        entry = mp.get(actors, actorName)
        actor = me.getValue(entry)
    else:
        actor = newActor(actorName)
        mp.put(actors, actorName, actor)
    lt.addLast(actor['movies'], movie)
    actavg = actor['average_voting']
    movavg = movie['vote_average']
    if (actavg != 0):
        actor['average_voting'] = round((actavg*(getMoviesByElementSize(catalog,"actors",actorName)-1) + float(movavg)) / getMoviesByElementSize(catalog,"actors",actorName),2)
    else:
        actor['average_voting'] = float(movavg)


def addDirectorActor(actor, directorName):
    directors = actor['directores']
    existDirector = mp.contains(directors, directorName)
    if existDirector:
        entry = mp.get(directors, directorName)
        contador = me.getValue(entry)
        me.setValue(entry,contador+1)
    else:
        mp.put(directors, directorName, 1)

def addMovieGenre(catalog, genreName, movie):
    genres = catalog['genres']
    existGenre = mp.contains(genres, genreName)
    if existGenre:
        entry = mp.get(genres, genreName)
        genre = me.getValue(entry)
    else:
        genre = newGenre(genreName)
        mp.put(genres, genreName, genre)
    lt.addLast(genre['movies'], movie)
    genavg = genre['average_voting']
    movavg = movie['vote_count']
    if (genavg != 0):
        genre['average_voting'] = round((genavg*(getMoviesByElementSize(catalog,"genres",genreName)-1) + float(movavg)) / getMoviesByElementSize(catalog,"genres",genreName),2)
    else:
        genre['average_voting'] = float(movavg)

def addMovieCountry (catalog,countryName,movie):
    countries = catalog['countries']
    existcountry= mp.contains(countries, countryName)
    if existcountry:
        entry = mp.get(countries, countryName)
        country = me.getValue(entry)
    else:
        country = newCountry(countryName)
        mp.put(countries, countryName, country)
    lt.addLast(country['movies'], movie)




# ==============================
# Funciones de consulta
# ==============================

def firstMovie(catalog):
    return lt.firstElement(catalog["movies"])

def lastMovie(catalog):
    return lt.lastElement(catalog["movies"])

def getElement(catalog,element,elementName):
    elemento = mp.get(catalog[element], elementName)
    if elemento:
        return me.getValue(elemento)
    return None

def getMoviesByElement(catalog,element, elementName):
    elemento = getElement(catalog,element,elementName)
    if element=="ids":
        return elemento["movie"]
    elif elemento:
        return elemento["movies"]
    return None

def getMoviesByElementSize(catalog,element,elementName):
    elemento = getElement(catalog,element,elementName)
    if elemento:
        return lt.size(elemento["movies"])
    return None

def getMejorDirector(catalog,actorName):
    actor = getElement(catalog,"actors",actorName)
    directores = actor["directores"]
    llaves = mp.keySet(directores)
    mejor_director = None
    maximo=0
    # directorName= ""
    # tupla = None
    # valor = 0
    for i in range(1,lt.size(llaves)+1):
        directorName = lt.getElement(llaves,i)
        valor = getElement(actor,"directores",directorName)
        if valor>maximo:
            maximo = valor
            mejor_director = directorName
    return mejor_director

def getDirectorMovie (catalog,id):
    movie=getElement(catalog,"ids",id)
    casting=movie["casting"]
    director=casting["director_name"]
    return director


# def getMoviesById(catalog, id):
#     movie = mp.get(catalog["moviesId"],id)
#     if movie:
#         return me.getValue(movie)
#     return None

def moviesSize(catalog):
    """
    Número de libros en el catago
    """
    return lt.size(catalog['movies'])

def elementsSize(catalog, element):
    """
    Numero de autores en el catalogo
    """
    return mp.size(catalog[element])
# ==============================
# Funciones de Comparacion
# ==============================


def compareMoviesIds(id1, id2):
    """
    Compara dos ids de libros
    """
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1

def compareProducersByName(keyname, producer):
    """
    Compara dos nombres de autor. El primero es una cadena
    y el segundo un entry de un map
    """
    prodentry = me.getKey(producer)
    if (keyname == prodentry):
        return 0
    elif (keyname > prodentry):
        return 1
    else:
        return -1


def compareDirectorsByName(keyname, director):
    """
    Compara dos nombres de autor. El primero es una cadena
    y el segundo un entry de un map
    """
    direntry = me.getKey(director)
    if (keyname == direntry):
        return 0
    elif (keyname > direntry):
        return 1
    else:
        return -1

def compareActorsByName(keyname, actor):
    """
    Compara dos nombres de actor. El primero es una cadena
    y el segundo un entry de un map
    """
    actentry = me.getKey(actor)
    if (keyname == actentry):
        return 0
    elif (keyname > actentry):
        return 1
    else:
        return -1

def compareGenreByName(keyname, genre):
    genentry = me.getKey(genre)
    if (keyname == genentry):
        return 0
    elif (keyname > genentry):
        return 1
    else:
        return -1

def compareCountryByName(keyname, country):
    couentry = me.getKey(country)
    if (keyname == couentry):
        return 0
    elif (keyname > couentry):
        return 1
    else:
        return -1


def compareMapMovieIds(id, entry):

    identry = me.getKey(entry)
    if (int(id) == int(identry)):
        return 0
    elif (int(id) > int(identry)):
        return 1
    else:
        return -1