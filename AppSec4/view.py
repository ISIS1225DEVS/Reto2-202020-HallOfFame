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

import sys
import config
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
from AppSec4 import controller
from time import process_time
assert config

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones y por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Ruta a los archivos
# ___________________________________________________





# ___________________________________________________
#  Funciones para imprimir la inforamación de
#  respuesta.  La vista solo interactua con
#  el controlador.
# ___________________________________________________

def printLoadInfo(catalog):
    print('Peliculas cargadas: ' + str(controller.moviesSize(catalog)))
    print("PRIMERA PELICULA")
    print("\tTitulo: " + controller.firstMovie(catalog)["title"])
    print("\tFecha de estrenos: " + controller.firstMovie(catalog)["release_date"])
    print("\tPromedio de votación: "+controller.firstMovie(catalog)["vote_average"])
    print("\tNúmero de votos: "+controller.firstMovie(catalog)["vote_count"])
    print("\tIdioma: "+controller.firstMovie(catalog)["original_language"])
    print("ULTIMA PELICULA")
    print("\tTitulo: " + controller.lastMovie(catalog)["title"])
    print("\tFecha de estrenos: " + controller.lastMovie(catalog)["release_date"])
    print("\tPromedio de votación: "+controller.lastMovie(catalog)["vote_average"])
    print("\tNúmero de votos: "+controller.lastMovie(catalog)["vote_count"])
    print("\tIdioma: "+controller.lastMovie(catalog)["original_language"])
# ___________________________________________________
#  Menu principal
# ___________________________________________________

def printMenu():
    print("Bienvenido")
    print("1- Inicializar Catálogo")
    print("2- Cargar información en el catálogo de las peliculas")
    print("3- Descubrir productoras de cine")
    print("4- Conocer a un director")
    print("5- Conocer a un actor")
    print("6- Conocer género")
    print ("7-Encontrar películas por país")

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Inicializando Catálogo ....")
        catalog = controller.initCatalog()
    elif int(inputs[0]) == 2:
        print("Cargando información de las peliculas ....")
        controller.loadData(catalog,"SmallMoviesDetailsCleaned.csv","MoviesCastingRaw-small.csv")
        printLoadInfo(catalog)
    elif int(inputs[0]) == 3:
        producerName=input('Seleccione una productora\n')
        t1=process_time()
        productora=controller.getElement(catalog,"producers",producerName)
        peliculas=controller.getMoviesByElement(catalog,"producers",producerName)
        nPeliculas=controller.getMoviesByElementSize(catalog,"producers",producerName)
        t2=process_time()
        print("Tiempo de ejecución " + str(t2-t1) + "s")
        print("Peliculas de la productora "+producerName)
        if(peliculas):
            for pos in range(0,nPeliculas):
                actual = lt.getElement(peliculas,pos)
                print("\t"+actual["title"])
            print("Número de peliculas: " + str(nPeliculas))
            print("Promedio de calificación: " + str(productora["average_voting"]))
        else:
            print("No se encontro ninguna productora con ese nombre.")
    elif int(inputs[0])==4:
        directorName = input("Seleccione un director\n")
        t1=process_time()
        director=controller.getElement(catalog,"directors",directorName)
        peliculas=controller.getMoviesByElement(catalog,"directors",directorName)
        nPeliculas=controller.getMoviesByElementSize(catalog,"directors",directorName)
        t2=process_time()
        print("Tiempo de ejecución " + str(t2-t1) + "s")
        print("Peliculas del director  "+directorName)
        if(peliculas):
            for pos in range(0,nPeliculas):
                actual = lt.getElement(peliculas,pos)
                print("\t"+ actual["title"])
            print("Número de peliculas: " + str(nPeliculas))
            print("Promedio de calificación: " + str(director["average_voting"]))
        else:
            print("No se encontro ningún director con ese nombre.")
    elif int(inputs[0])==5:
        actorName = input("Seleccione un actor\n")
        t1=process_time()
        actor=controller.getElement(catalog,"actors",actorName)
        peliculas=controller.getMoviesByElement(catalog,"actors",actorName)
        nPeliculas=controller.getMoviesByElementSize(catalog,"actors",actorName)
        mejor_director = controller.getMejorDirector(catalog,actorName)
        t2=process_time()
        print("Tiempo de ejecución " + str(t2-t1) + "s")
        print("Peliculas del actor "+actorName)
        if(peliculas):
            for pos in range(0,nPeliculas):
                actual = lt.getElement(peliculas,pos)
                print("\t"+ actual["title"])
            print("Número de peliculas: " + str(nPeliculas))
            print("Promedio de calificación: " + str(actor["average_voting"]))
            print("El director con más colaboraciones es "+mejor_director)
        else:
            print("No se encontro ningún actor con ese nombre.")
    
    elif int(inputs[0])==6:
        genreName = input("Seleccione un genero\n")
        t1=process_time()
        genero=controller.getElement(catalog,"genres",genreName)
        peliculas=controller.getMoviesByElement(catalog,"genres",genreName)
        nPeliculas=controller.getMoviesByElementSize(catalog,"genres",genreName)
        t2=process_time()
        print("Tiempo de ejecución " + str(t2-t1) + "s")
        print("Peliculas del genero: "+genreName)
        if(peliculas):
            for pos in range(0,nPeliculas):
                actual = lt.getElement(peliculas,pos)
                print("\t"+ actual["title"])
            print("Número de peliculas: " + str(nPeliculas))

            print("Promedio de votos: " + str(genero["average_voting"]))
        else:
            print("No se encontro ningún genero con ese nombre.")

    elif int(inputs[0])==7:
        countryName = input("Seleccione un país\n")
        t1=process_time()
        country=controller.getElement(catalog,"countries",countryName)
        peliculas=controller.getMoviesByElement(catalog,"countries",countryName)
        nPeliculas=controller.getMoviesByElementSize(catalog,"countries",countryName)
        t2=process_time()
        print("Tiempo de ejecución " + str(t2-t1) + "s")
        print("Peliculas del país "+countryName)
        if(peliculas):
            for pos in range(0,nPeliculas):
                actual = lt.getElement(peliculas,pos)
                id=actual["id"]
                director= controller.getDirectorMovie(catalog,id)
                print (str(pos+1))
                print("\t"+ actual["title"])
                print("\t"+ actual["release_date"])
                print("\t"+ director)
            print("Número de peliculas: " + str(nPeliculas))
        else:
            print("No se encontro ningún país con ese nombre.")  

        
    else:


        sys.exit(0)
sys.exit(0)