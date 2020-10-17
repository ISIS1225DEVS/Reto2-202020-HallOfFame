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
from App import controller
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

moviesfile="AllMoviesDetailsCleaned.csv"
moviesfile2="AllMoviesCastingRaw.csv"


# ___________________________________________________
#  Funciones para imprimir la inforamación de
#  respuesta.  La vista solo interactua con
#  el controlador.
# ___________________________________________________

def printFirstandLast(catalog,titulo,fecha,promedio,votos,idioma,tamaño,pos):
    print(controller.FirstandLastElementsNTFPVI(catalog,titulo,fecha,promedio,votos,idioma,tamaño,pos))

def infoProductor(catalog, producer):
    print(controller.infoProductor(catalog, producer))
  
def infoActor(catalog, actor):
    print(controller.infoActor(catalog, actor))

def infoGenero(catalog, genero):
    print(controller.infoGenero(catalog, genero))
  
def infoPais(catalog, pais):
    print(controller.infoPais(catalog, pais))
  
# ___________________________________________________
#  Menu principal
# ___________________________________________________

def printMenu():
    print("Bienvenido")
    print("1 - Inicializar Catalogo")
    print("2 - Cargar informacion en el catalogo")
    print("3 - Imprimir primera y ultima pelicula")
    print("4 - Informacion de una productora")
    print("5 - Informacion de un director")
    print("6 - Información de un actor")
    print("7 - Informacion de un Genero")
    print("8 - Peliculas producidas en un pais")
    print("0 - Salir")


while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')

    if int(inputs[0]) == 1:
        print("Inicializando Catálogo ....")
        # cont es el controlador que se usará de acá en adelante
        cont = controller.initCatalog()

    elif int(inputs[0]) == 2:
        print("Cargando información de los archivos ....")
        controller.loadData(cont, moviesfile, moviesfile2)
        print('Películas cargadas: ' + str(controller.movieSize(cont)))
        print('Películas cargadas: ' + str(controller.castingSize(cont)))

    elif int(inputs[0]) == 3:
        Tamaño = controller.movieSize(cont)
        Titulo1 = controller.Titulo(cont, 1)
        Titulo2 = controller.Titulo(cont, Tamaño)
        Fecha1 = controller.Fecha(cont, 1)
        Fecha2 = controller.Fecha(cont,Tamaño)
        Promedio1 = controller.Promedio(cont, 1)
        Promedio2 = controller.Promedio(cont, Tamaño)
        Votos1 = controller.Votos(cont, 1)
        Votos2 = controller.Votos(cont, Tamaño)
        Idioma1 = controller.Idioma(cont, 1)
        Idioma2 = controller.Idioma(cont, Tamaño)
        printFirstandLast(cont,Titulo1, Fecha1, Promedio1, Votos1, Idioma1,Tamaño,1)
        printFirstandLast(cont,Titulo2, Fecha2, Promedio2, Votos2, Idioma2,Tamaño,Tamaño)
    
    elif int(inputs[0]) == 4:
        producer = input("Ingrese el nombre del productor:  ")
        print(infoProductor(cont, producer))
    
    elif int(inputs[0]) == 5:
        director = input("Ingrese el nombre del director:  ")
        print(controller.infoDirector(cont, director))
       
    elif int(inputs[0]) == 6:
        actor = input("Ingrese el nombre del actor:  ")
        print(infoActor(cont, actor))
       
    elif int(inputs[0]) == 7:
        genero = input("Ingrese el genero:  ")
        print(infoGenero(cont, genero))
       
    elif int(inputs[0]) == 8:
        pais = input("Ingrese el pais:  ")
        print(infoPais(cont, pais))
           
    else:
        sys.exit(0)
sys.exit(0)
