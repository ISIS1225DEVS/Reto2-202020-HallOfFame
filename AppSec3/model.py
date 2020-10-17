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
import config
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.DataStructures import listiterator as it
assert config

"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria

"""

# -----------------------------------------------------
# API del TAD Catalogo de peliculas
# -----------------------------------------------------
def newCatalog():
    """ Inicializa el catálogo de peliculas

    Crea una lista vacia para guardar todos los peliculas

    Se crean indices (Maps) por los siguientes criterios:
    Autores
    ID libros
    Tags
    Año de publicacion

    Retorna el catalogo inicializado.
    """
    catalog = {'Movies': None,
               'production_companies': None,
               'directors': None,
               'actors': None,
               'actor_director': None,
               'genres': None,
               'production_countries': None}

    catalog['Movies'] = lt.newList('ARRAY_LIST', compareMoviesIds)
    catalog["MoviesId"] = mp.newMap(329400,
                                    maptype='CHAINING', 
                                    loadfactor=0.5,  
                                    comparefunction=compareMapMoviesIds) 
    catalog["CastingId"]= mp.newMap(329400,
                                    maptype='CHAINING',
                                    loadfactor=0.5,  
                                    comparefunction=compareMapMoviesIds) 
    catalog['production_companies'] = mp.newMap(35894,
                                                maptype='CHAINING',  # Esto no lo entiendo
                                                loadfactor=0.5,    #Esto no lo entiendo
                                                comparefunction=compareMapCompanies) #Esto lo entiendo mas pero tampoco lo entiendo
    catalog['directors'] = mp.newMap(85908,
                                         maptype='CHAINING', #No lo entiendo
                                         loadfactor=0.5, #No entiendo
                                         comparefunction=compareMapDirectorsByName) #No entiendo
    catalog['actors'] = mp.newMap(260806,
                                      maptype='CHAINING', #No entiendo
                                      loadfactor=0.5, #No entiendo
                                      comparefunction=compareMapActorsByName) # No entiendo
    catalog['genres'] = mp.newMap(21,
                                 maptype='CHAINING',
                                 loadfactor=0.5,
                                 comparefunction=compareMapByGenre)
    catalog['production_countries'] = mp.newMap(235,
                                                maptype='CHAINING',
                                                loadfactor=0.5,
                                                comparefunction=compareMapCountries)
    return catalog

def newCompany(name):
    company = {"name": "", "movies": None, "average_rating": 0}
    company["name"] = name
    company["movies"] = lt.newList("ARRAY_LIST", compareElements)
    company["average_rating"]=0
    return company

def newDirector(name):
    """
    Crea una nueva estructura para modelar las películas 
    de un director y su promedio de ratings
    """
    director = {'name': "", "movies": None,  "average_rating": 0}
    director['name'] = name
    director['movies'] = lt.newList('ARRAY_LIST', compareElements)
    return director   

def newActor(actorname):
    actor = {"name": "", "movies": None, "average_rating": 0,"directors":"", "DirectorMaxCol":""}
    actor["name"] = actorname
    actor["movies"] = lt.newList("ARRAY_LIST", compareElements)
    actor["directors"]= lt.newList("ARRAY_LIST", compareElements)
    return actor

def newGenre(name):
    
    genre = {'name': "", "movies": None}
    genre['name'] = name
    genre["movies"] = lt.newList('ARRAY_LIST', compareElements)
    return genre

def newCountry(name):
    country = {"name": "", "movies": None,"years": None,"directors":None}
    country["name"] = name
    country["movies"] = lt.newList("ARRAY_LIST", compareElements)
    country["years"]=lt.newList("ARRAY_LIST", compareElements)
    country["directors"]=lt.newList("ARRAY_LIST", compareElements)
    return country

# Funciones para agregar informacion al catalogo
def addMovie(catalog, movie):
    lt.addLast(catalog["Movies"], movie)
    mp.put(catalog["MoviesId"], movie["id"], movie)
    addMovieGenre(catalog,movie)
    addMovieCompany(catalog, movie)
    addMovieCountry(catalog,movie)
    
def addCasting(catalog, casting, details):
    mp.put(catalog["CastingId"],casting["id"],casting)
    addMovieDirector(catalog,casting,details)
    addMovieActor(catalog, casting,details)

def addMovieCompany(catalog, movie):
    mapa = catalog["production_companies"]
    company = movie["production_companies"].lower()
    existcompany = mp.contains(mapa, company)
    if existcompany:
        entry = mp.get(mapa,company)
        comp = me.getValue(entry)
    else:
        comp = newCompany(company)
        mp.put(mapa, company, comp)
    lt.addLast(comp["movies"], movie)
    agregar_promedio(comp,movie['vote_average'])

def addMovieDirector(catalog,casting,details):
    mapa = catalog["directors"]
    #compareMap = catalog["MoviesId"]
    director = casting["director_name"].lower()
    #ide = casting["id"]
    #pair = mp.get(compareMap, ide)
    #details = me.getValue(pair)
    existdirector = mp.contains(mapa, director)
    if existdirector:
        entry = mp.get(mapa, director)
        comp = me.getValue(entry)
    else:
        comp = newDirector(director)
        mp.put(mapa, director, comp)
    lt.addLast(comp["movies"], details)
    movieavg = details['vote_average']
    agregar_promedio(comp,movieavg)
    
def addMovieActor(catalog,casting,details):
    mapa = catalog["actors"]
    #compareMap = catalog["MoviesId"]
    actors = [casting["actor1_name"],casting["actor2_name"],casting["actor3_name"],casting["actor4_name"],casting["actor5_name"]]
    #ide = casting["id"]
    #pair = mp.get(compareMap, ide)
    director= casting["director_name"]
    #details = me.getValue(pair)
    for actor in actors:
        existActor = mp.contains(mapa, actor.lower())
        if existActor:
            entry = mp.get(mapa,actor.lower())
            comp = me.getValue(entry)
        else:
            comp = newActor(actor.lower())
            mp.put(mapa,actor.lower(), comp)
        lt.addLast(comp["movies"], details)
        movieavg = details['vote_average']
        agregar_promedio(comp,movieavg)
        lt.addLast(comp["directors"],director)

def addMovieGenre(catalog, movie):
    """
    Esta funcion adiciona un libro a la lista de libros que
    fueron publicados en un año especifico.
    Los años se guardan en un Map, donde la llave es el año
    y el valor la lista de libros de ese año.
    """
    mapa = catalog['genres']
    genres = movie['genres'].split("|")
    for genre in genres:
        genre = genre.lower()
        existgenre = mp.contains(mapa, genre)
        if existgenre:
            entry = mp.get(mapa, genre)
            genero = me.getValue(entry)
        else:
            genero = newGenre(genre)
            mp.put(mapa, genre, genero)
        lt.addLast(genero["movies"], movie)
    

def addMovieCountry(catalog, movie):
    mapa = catalog["production_countries"]
    country = movie["production_countries"].lower()
    existcountry = mp.contains(mapa, country)
    if existcountry:
        entry = mp.get(mapa,country)
        comp = me.getValue(entry)
    else:
        comp = newCountry(country)
        mp.put(mapa, country, comp)
    lt.addLast(comp["movies"], movie)
    if movie["release_date"].find("/") == -1:
        year= movie["release_date"].split("-")[0]
    else:
        year= movie["release_date"].split("/")[2]
    lt.addLast(comp["years"],year)

def addMovieDirectorsbyCountry(catalog, country):
    compareMap = catalog["CastingId"]
    mapa=catalog['production_countries']
    country =mp.get(mapa,country)
    movies = country["value"]["movies"]
    iterator= it.newIterator(movies)
    while it.hasNext(iterator):
        movie = it.next(iterator)
        ide = movie["id"]
        pair = mp.get(compareMap, ide)
        casting = me.getValue(pair)
        director= casting["director_name"]
        lt.addLast(country["value"]["directors"],director)
    
# ==============================
# Funciones de consulta
# ==============================

def moviesSize(catalog):
    """Numero de películas
    """
    return lt.size(catalog["Movies"])

def listSize(lst):
    return lt.size(lst)

def directorsSize(catalog):
    """Numero de directores leido
    """
    return lt.size(catalog["directors"])


def actorsSize(catalog):
    """Numero de actores leido
    """
    return lt.size(catalog["actors"])

  
def getMoviesByProductionCompany(catalog,ProductionCompanyName):
    productioncompany=mp.get(catalog["production_companies"],ProductionCompanyName)
    if productioncompany:
        return me.getValue(productioncompany)
    return None


def getMoviesByDirector(catalog, directorname):
    """
    Retorna las películas de un director
    """
    director=mp.get(catalog["directors"],directorname)
    if director:
        return me.getValue(director)

    return None


def getMoviesByActor(catalog, actorname):
    """
    Retorna las películas de un actor
    """
    actor=mp.get(catalog["actors"],actorname)
    if actor:
        return me.getValue(actor)
    return None


def getFifteenElements(lst):
    lst = lt.subList(lst,1,listSize(lst)//3)
    iterator = it.newIterator(lst)
    movies = []
    while it.hasNext(iterator):
        movie = it.next(iterator)
        movies.append(movie)
    return movies
        
        
def getMoviesByGenre(catalog,genre):
    mapa = catalog["genres"]
    entry = mp.get(mapa,genre)
    movies = (me.getValue(entry))["movies"]
    iterator = it.newIterator(movies)
    movieList = lt.newList("ARRAY_LIST")
    averageCount = 0
    while it.hasNext(iterator):
        movie = it.next(iterator)
        lt.addLast(movieList,movie["original_title"])
        averageCount += float(movie["vote_count"])
    return (movieList,averageCount)
    
        


def getMoviesByCountry(catalog, countryname):
    """
    Retorna las películas de un país
    """
    country=mp.get(catalog["production_countries"],countryname)
    if country:
        return me.getValue(country)
    return None

# ==============================
# Funciones de Comparacion
# ==============================

def compareMoviesIds(id1, id2):
    """
    Compara dos ids de películas
    """
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1
def compareMapMoviesIds(id, entry):
    """
    Compara dos ids de pelícalas, id es un identificador
    y entry una pareja llave-valor
    """
    identry = me.getKey(entry)
    if (int(id) == int(identry)):
        return 0
    elif (int(id) > int(identry)):
        return 1
    else:
        return -1
def compareMapCompanies(keyname,company):
    companyentry=me.getKey(company)
    if keyname==companyentry:
        return 0
    elif keyname > companyentry:
        return 1
    else:
        return -1
def compareElements(element1, element2):
    if (element1 == element2):
        return 0
    elif (element1 > element2):
        return 1
    else:
        return 0
def compareMapDirectorsByName(keyname,director):
    directorentry=me.getKey(director)
    if keyname==directorentry:
        return 0
    elif keyname > directorentry:
        return 1
    else:
        return -1

def compareMapActorsByName(keyname,actor):
    actorentry=me.getKey(actor)
    if keyname==actorentry:
        return 0
    elif keyname > actorentry:
        return 1
    else:
        return -1
    return 0     


def compareMapByGenre(keyname,genre):
    genreentry=me.getKey(genre)
    if keyname==genreentry:
        return 0
    elif keyname > genreentry:
        return 1
    else:
        return -1

    
def compareMapCountries(keyname,country):
    countryentry=me.getKey(country)
    if keyname==countryentry:
        return 0
    elif keyname > countryentry:
        return 1
    else:
        return -1
def compareMapActorsDirectors(id,tag):
    entry = me.getKey(tag)
    if (id == entry):
        return 0
    elif (id > entry):
        return 1
    else:
        return -1

def agregar_promedio(comp,movieavg):
    compavg = comp['average_rating']
    comp['average_rating'] = (compavg*(lt.size(comp["movies"])-1) + float(movieavg)) / (lt.size(comp["movies"])) 
    
def masrepetido(lista):
    mas_repetido=""
    mayor=0
    for cada_elemento in lista:
        if mayor< lista.count(cada_elemento):
            mayor = lista.count(cada_elemento)
            mas_repetido = cada_elemento
    return mas_repetido

#===============================
def newList():
    a = lt.newList()
    return a

def addLast(lst, element):
    lt.addLast(lst, element)



