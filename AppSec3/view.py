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

import sys
import config
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
from App import controller as controller
assert config
from DISClib.ADT import map as mp
"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones y por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Ruta a los archivos
Casting = "AllMoviesCastingRaw.csv"
Details = "AllMoviesDetailsCleaned.csv"
# ___________________________________________________

#Casting = "themoviesdb/MoviesCastingRaw-small.csv"
#Details = "themoviesdb/SmallMoviesDetailsCleaned.csv"

# ___________________________________________________
#  Funciones para imprimir la inforamación de
#  respuesta.  La vista solo interactua con
#  el controlador.
# ___________________________________________________
def printElementData(element):
    """
    Imprime los datos de un elemento determinado
    """
    print('Promedio: ' + str(round(element['average_rating'],2)))
    print('Total de películas: ' + str(lt.size(element['movies'])))
    iterator = it.newIterator(element['movies'])
    while it.hasNext(iterator):
        movie = it.next(iterator)
        print('Película: ' + movie['title'])


def printCountryData (country):
    """
    Imprime los datos de un elemento determinado
    """
    print("Se econtraron "+ str(lt.size(country['movies']))+ " películas producidas en " +country["name"].title())
    print("Las películas producidas en "+country["name"].title()+", con su respectivo año de lanzamiento, y director, son: ")
    iterator1 = it.newIterator(country['movies'])
    iterator2 = it.newIterator(country['years'])
    iterator3=it.newIterator(country['directors'])
    while it.hasNext(iterator1) and it.hasNext(iterator2) and it.hasNext(iterator3) :
        movie = it.next(iterator1)
        year=it.next(iterator2)
        director=it.next(iterator3).title()
        print('\nPelícula: ' + movie['original_title'])
        print("Año de Estreno: "+ year )
        print("Director: "+director+"\n")
    print("Se econtraron "+ str(lt.size(country['movies']))+ " películas producidas en " +country["name"].title()+"\n")

def printMenu():
    print("\n0- Inicializar Catálogo")
    print("1- Cargar Archivos")
    print("2- Descubrir productoras de cine")
    print("3- Conocer a un director")
    print("4- Conocer a un actor")
    print("5- Entender un género cinematográfico")
    print("6- Encontrar películas por país")
    print("7- Salir")

# ___________________________________________________
#  Menu principal
# ___________________________________________________
while True:
    printMenu()
    inputs = input("Seleccione una opción para continuar:\n")
    if int(inputs[0]) == 0:
        print("Inicializando Catálogo ....")
        # cont es el controlador que se usará de acá en adelante
        cont = controller.initCatalog()  
    elif int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        controller.loadData(cont, Details, Casting)
        print('Películas cargadas: ' + str(controller.moviesSize(cont)))
        print('Directores cargados: ' + str(controller.directorsSize(cont)))    
        print(mp.size(cont['directors']))
        print(mp.size(cont['actors']))
        
    elif int(inputs[0]) == 2:
        production_company= (input("¿Qué productora de cine desea descubrir?:\n")).lower()
        productioncompanyinfo=controller.getMoviesByProductionCompany(cont,production_company)
        if productioncompanyinfo:
            print('\nProductora encontrada: ' + productioncompanyinfo['name'].title())
            printElementData(productioncompanyinfo)
        else:
            print('No se encontró la productora')
    elif int(inputs[0]) == 3:
        director_name = input("¿Qué director de cine desea conocer?:\n")
        director_name = director_name.lower()
        director_info = controller.getMoviesByDirector(cont, director_name)
        print("\nDirector encontrado: "+ director_name.title())
        printElementData(director_info)
    elif int(inputs[0]) == 4:    
        actor=input("¿Qué actor de cine desea conocer?:\n")
        actor = actor.lower()
        actorinfo=controller.getMoviesByActor(cont,actor)
        if actorinfo:
            print('\nActor encontrado: '+ actor.title())
            printElementData(actorinfo)
            if actorinfo["DirectorMaxCol"]!=None:
                print("El director con el que " + actor.title() + " más ha colaborado es: "+ actorinfo["DirectorMaxCol"])
            else:
                print("El actor " + actor.title() +" ha colaborado con varios directores en mismas cantidades, como: "+actorinfo["directors"][0])
        else:
            print('No se encontró el actor')
    elif int(inputs[0]) == 5:
        genre = input("¿Qué género desea consultar?: \n" ).lower()
        info = controller.moviesByGenre(cont,genre)
        print("\nGénero encontrado: " + genre.title())
        print("El género " + genre.title() + " tiene un total de "+ str(info[1]) + " películas")
        print("El promedio del número de votos es:  " + str(round(info[2],2))+ "\n")
        print("Algunas de las películas son: ") 
        for i in range(0,10):
            print("Titulo: "+ info[0][i])
    elif int(inputs[0]) == 6:
        country=input("¿Películas producidas en qué país desea encontrar?:\n")
        country=country.lower()
        countryinfo=controller.getMoviesByCountry(cont,country)
        if countryinfo:
            printCountryData(countryinfo)
        else:
            print('No se encontró el país')
    else:
        sys.exit(0)
