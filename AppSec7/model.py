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
assert config

"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria

"""

# -----------------------------------------------------
# API del TAD Catalogo de Libros
# -----------------------------------------------------

def newCatalog():
    catalog={'Movies':None,
             'Casting':None,
             'Producers':None,
             'Directors':None,
             'Actors':None,
             'generos': None,
             'Countries':None}
    catalog['Movies'] = lt.newList('ARRAY_LIST', compareMovieIds)
    catalog['Casting'] =lt.newList('ARRAY_LIST', compareMovieIds)
    catalog['Producers']=mp.newMap(1,maptype='PROBING',loadfactor=0.5,comparefunction=CompareProducersByName)
    catalog['Directors']=mp.newMap(1,maptype='CHAINING',loadfactor=10,comparefunction=CompareProducersByName)
    catalog['Actors']=mp.newMap(1,maptype='CHAINING',loadfactor=0.5,comparefunction=CompareProducersByName)
    catalog['generos']=mp.newMap(1,maptype='CHAINING',loadfactor=2,comparefunction=CompareProducersByName)
    catalog['Countries']=mp.newMap(30011,maptype='PROBING',loadfactor=0.5,comparefunction=CompareProducersByName)
    return catalog

def newProducer(nom_movies,tot_movies,prom_movies): 
    producer={'Peliculas':None,
              'Total películas':None,
              'Promedio':None}
    producer['Peliculas']=nom_movies
    producer['Total películas']=tot_movies
    producer['Promedio']=prom_movies
    return producer
   
def newActor(nom_movies,tot_movies,prom_movies,nom_director): 
    actor={'Peliculas':None,
            'Total películas':None,
            'Promedio':None,
            'Nombre director':None}
    actor['Peliculas']=nom_movies
    actor['Total películas']=tot_movies
    actor['Promedio']=prom_movies
    actor['Nombre director']=nom_director
    return actor
  
# Funciones para agregar informacion al catalogo

def addMovie (catalog,movie):
    lt.addLast(catalog['Movies'],movie)
    
def addCasting (catalog,movie):
    lt.addLast(catalog['Casting'],movie)
  
def addProducer (catalog, producer):
    tamaño=sizeMovies(catalog)
    acum=0
    titulo=[]
    tupla=()
    for i in range(1,tamaño+1):
        pelicula=lt.getElement(catalog['Movies'],i)
        if pelicula['production_companies'].lower()==producer.lower():
            productora=pelicula['production_companies']
            titulo.append(getTitulo(catalog,i))
            acum=acum+float(getPromedio(catalog,i))
    tamaño_peliculas=len(titulo)
    promedio=acum/tamaño_peliculas
    nuevos_productores=newProducer(titulo,tamaño_peliculas,promedio)
    mp.put(catalog['Producers'],productora,nuevos_productores)
    return mp.get(catalog['Producers'],productora)

def addDirector (catalog, director):
    tamaño=sizeMovies(catalog)
    suma=0
    titulo=[]
    tupla=()
    for i in range(1,tamaño+1):
        pelicula=lt.getElement(catalog['Casting'],i)
        if pelicula['director_name'].lower()==director.lower():
            directores=pelicula['director_name']
            titulo.append(getTitulo(catalog,i))
            suma+=float(getPromedio(catalog,i))
    tamaño_peliculas=len(titulo)
    promedio=suma/tamaño_peliculas
    nuevos_directores=newProducer(titulo,tamaño_peliculas,promedio)
    mp.put(catalog['Directors'],directores,nuevos_directores)
    return mp.get(catalog['Directors'],directores)
   
def addActor (catalog, nombre_actor):
    tamaño=sizeCasting(catalog)
    acum=0
    directores={}
    titulo=[]
    lista_directores=[]
    for i in range(1,tamaño+1):
        pelicula=lt.getElement(catalog['Movies'],i)
        nombre=lt.getElement(catalog['Casting'],i)
        if nombre_actor.lower()==nombre['actor1_name'].lower() or nombre_actor.lower()==nombre['actor2_name'].lower() or nombre_actor.lower()==nombre['actor3_name'].lower() or nombre_actor.lower()==nombre['actor4_name'].lower() or nombre_actor.lower()==nombre['actor5_name'].lower():
            actor=nombre_actor
            titulo.append(getTitulo(catalog,i))
            acum=acum+float(getPromedio(catalog,i))
            if not((nombre["director_name"]) in directores):
                directores[nombre["director_name"]]=1
            elif nombre["director_name"] in directores:
                directores[nombre["director_name"]]+=1
    nom_dic=list(directores.keys())
    num_dic=list(directores.values())
    max_dic=max(num_dic)
    i=0
    while i<len(nom_dic):
        if max_dic==directores[nom_dic[i]]:
            lista_directores.append(nom_dic[i])
        i=i+1
    tamaño_peliculas=len(titulo)
    promedio=acum/tamaño_peliculas
    nuevos_actores=newActor(titulo,tamaño_peliculas,promedio,lista_directores)
    mp.put(catalog['Actors'],actor,nuevos_actores)
    return mp.get(catalog['Actors'],actor) 
   
def addGenero (catalog, genero):
    l_peliculas = []
    contador = 0
    valoracion = 0
    tamaño = sizeMovies(catalog)
    for n in range(1,tamaño+1):
        pelicula = lt.getElement(catalog['Movies'], n)
        if genero.lower()==pelicula["genres"].lower() or genero.lower() in pelicula["genres"].lower():
            l_peliculas.append(pelicula["title"])
            contador += 1
            valoracion += float(pelicula["vote_average"])
    promedio = valoracion/contador
    nuevo_genero = newProducer(l_peliculas,contador, promedio)
    mp.put(catalog['generos'], genero, nuevo_genero)
    return mp.get(catalog['generos'], genero)

def addPais (catalog,pais):
    tamaño=sizeCasting(catalog)
    for i in range(1,tamaño+1):
        pelicula=lt.getElement(catalog['Movies'],i)
        nombre=lt.getElement(catalog['Casting'],i)
        if pais.lower()==pelicula['production_countries'].lower():
            mp.put(catalog['Countries'],getTitulo(catalog,i),[getFecha(catalog,i),nombre['director_name']])
    return catalog['Countries']

# ==============================
# Funciones de consulta
# ==============================

def sizeMovies(catalog):
    return lt.size(catalog['Movies'])
 
def sizeCasting(catalog):
    return lt.size(catalog['Casting'])

def getTitulo(catalog,pos):
    pelicula=lt.getElement(catalog['Movies'],pos)
    titulo=pelicula['original_title']
    return titulo

def getFecha(catalog,pos):
    pelicula=lt.getElement(catalog['Movies'],pos)
    fecha=pelicula['release_date']
    return fecha
    
def getPromedio(catalog,pos):
    pelicula=lt.getElement(catalog['Movies'],pos)
    promedio=pelicula['vote_average']
    return promedio

def getVotos(catalog,pos):
    pelicula=lt.getElement(catalog['Movies'],pos)
    votos=pelicula['vote_count']
    return votos

def getIdioma(catalog,pos):
    pelicula=lt.getElement(catalog['Movies'],pos)
    idioma=pelicula['original_language']
    return idioma

def getFirstandLastElementsNTFPVI(catalog,titulo,fecha,promedio,votos,idioma,tamaño,pos):
    Lf=lt.newList('ARRAY_LIST',compareMovieIds)
    pelicula=lt.getElement(catalog['Movies'],pos)
    if pos==1:
        lt.addLast(Lf,"Primera película")
        lt.addLast(Lf,"Número de películas cargadas:"+str(tamaño))
    else:
        lt.addLast(Lf,"Última película")
        lt.addLast(Lf,"Número de películas cargadas:"+str(tamaño))
    lt.addLast(Lf,"Título:"+titulo)
    lt.addLast(Lf,"Fecha de estreno:"+fecha)
    lt.addLast(Lf,"Promedio de la votación:"+promedio)
    lt.addLast(Lf,"Número de votos:"+votos)
    lt.addLast(Lf,"Idioma original:"+idioma)
    return Lf['elements']

# ==============================
# Funciones de Comparacion
# ==============================

def compareMovieIds(id1,id2):
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1

def CompareProducersByName(name, Producers):
    producerentry = me.getKey(Producers)
    if (name == producerentry):
        return 0
    elif (name > producerentry):
        return 1
    else:
        return -1
