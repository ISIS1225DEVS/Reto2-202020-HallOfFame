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
from App import controller as ctrl
assert config
from time import process_time
"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones y por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Ruta a los archivos
# ___________________________________________________

listDetails_s = "themoviesdb/SmallMoviesDetailsCleaned.csv"
listDetails_l = "themoviesdb/AllMoviesDetailsCleaned.csv"
listCasting_s = "themoviesdb/MoviesCastingRaw-small.csv"
listCasting_l = "themoviesdb/AllMoviesCastingRaw.csv"
 
# ___________________________________________________
#  Funciones para imprimir la inforamación de respuesta.  
#  La vista solo interactua con el controlador.
# ___________________________________________________


# ___________________________________________________
#  Menu principal
# ___________________________________________________
def menuData():
    print("Menú de opciones")
    print("1- Cargar archivos pequeños")
    print("2- Cargar archivos grandes")

def menuApp():
    print("\nBienvenido")
    print("1- Cargar información del catálogo")
    print("2- Descubrir productoras de cine")
    print("3- Conocer a un director")
    print("4- Conocer a un actor")
    print("5- Entender un género de cine")
    print("6- Encontrar películas por país")
    print("7- Salir de la aplicación") 

def main():
    cont = None
    while True:
        menuApp()
        opcion = input('Selecciona una opción para continuar: ')
        if len(opcion[0]) > 0:
            if int(opcion[0]) == 1:
                menuData()
                tamaño = int(input("Digite su selección para el tamaño de los archivos CSV: "))
                t1_start = process_time() #tiempo inicial
                if tamaño == 1:
                    size = 2001
                    loadfactor = 0.5
                    print("Inicializando Catálogo ....")
                    # cont es el controlador que se usará de acá en adelante
                    cont = ctrl.initCatalog(size,loadfactor)
                    print("Cargando información de los archivos .....")
                    ctrl.loadData(cont,listCasting_s, listDetails_s)
                    print('Películas (Detalles) cargadas: ' + str(ctrl.moviesDetailsSize(cont)))
                    print('Películas (Casting) cargadas: ' + str(ctrl.moviesCastingSize(cont)))
                elif tamaño == 2:
                    size = 329047
                    loadfactor = 3
                    print("Inicializando Catálogo ....")
                    # cont es el controlador que se usará de acá en adelante
                    cont = ctrl.initCatalog(size,loadfactor)
                    print("Cargando información de los archivos .....")
                    print('CALMASIÓN, SI ES CON ARCHIVOS GRANDES SE ESTÁ DEMORANDO 76 SEG EN PROMEDIO :(')
                    ctrl.loadData(cont,listCasting_l, listDetails_l)
                    print('Películas (Detalles) cargadas: ' + str(ctrl.moviesDetailsSize(cont)))
                    print('Películas (Casting) cargadas: ' + str(ctrl.moviesCastingSize(cont)))
                else:
                    print("Opción inválida.....")
                t1_stop = process_time() #tiempo final
                print("Tiempo de ejecución ",t1_stop-t1_start," segundos ")

            elif int(opcion[0]) == 2: #REQUERIMIENTO 1
                if cont == None:
                    print('¡KELLY CARGUE EL ARCHIVO PRIMERO!')
                else:
                    t1_start = process_time() #tiempo inicial
                    name = input('Digite el nombre de la productura: ').lower().strip()
                    data = ctrl.descubrirProductorasDeCine(cont,name)
                    if data == -1:
                        print('¿¿KELLY PERO QUÉ MONDÁ DE COMPAÑÍA ES ESA??')
                    else:
                        print('Nombres de peliculas para la compañia ',name,'...')
                        for i in range(data[2]):
                            print(i+1,'. ',lt.getElement(data[0],i)['original_title'])
                        print('El promedio para las peliculas para la compañia ',name.title(),' es de: ',round(data[1],2))
                        print('Para un total de ',data[2],' peliculas')
                    t1_stop = process_time() #tiempo final
                    print("Tiempo de ejecución ",t1_stop-t1_start," segundos ")

            elif int(opcion[0]) == 3: #REQUERIMIENTO 2
                if cont == None:
                    print('¡KELLY CARGUE EL ARCHIVO PRIMERO!')
                else:
                    t1_start=process_time()#Tiempo inicial
                    nombre=input('Digite el nombre del director :').lower().strip()
                    x =ctrl.conocerUnDirector(cont,nombre)
                    if x==-1:
                        print('¿¿KELLY PERO QUÉ MONDÁ DE DIRECTOR ES ESE??')
                    else:
                        print('Nombres de peliculas para el director', nombre.title(),'...')
                        for i in range(x[2]):
                            print(i+1,'. ',lt.getElement(x[0],i))
                        print('El promedio de peliculas para el director ',nombre,'es de: ',round(x[1],2))
                        print('Para un total de ', x[2], 'peliculas')
                    t1_stop = process_time() #tiempo final
                    print("Tiempo de ejecución  ",t1_stop-t1_start," segundos ")
            
            elif int(opcion[0]) == 4: #REQUERIMIENTO 3
                if cont == None:
                    print('¡KELLY CARGUE EL ARCHIVO PRIMERO!')
                else:
                    t1_start = process_time() #tiempo inicial
                    name = input('Digite el nombre del actor: ').lower().strip()
                    data = ctrl.conocerUnActor(cont,name)
                    if data == -1:
                        print('¿¿KELLY PERO QUÉ MONDÁ DE ACTOR ES ESE??')
                    else:
                        print('Nombres de peliculas para el actor ',name.title(),'...')
                        for i in range(data[2]):
                            print(i+1,'. ',lt.getElement(data[0],i))
                        print('El promedio para las peliculas para el actor ',name,' es de: ',round(data[1],2))
                        print('Para un total de ',data[2],' peliculas')
                        print('Este actor tuvo más colaboraciones con el director ',data[3])
                    t1_stop = process_time() #tiempo final
                    print("Tiempo de ejecución ",t1_stop-t1_start," segundos ")
                    
            elif int(opcion[0]) == 5: #REQUERIMIENTO 4
                if cont == None:
                    print('¡KELLY CARGUE EL ARCHIVO PRIMERO!')
                else:
                    t1_start = process_time() #tiempo inicial
                    genre = input('Digita un género cinematográfico: ').lower().strip()
                    data = ctrl.entenderUnGenero(cont,genre)
                    if data == -1:
                        print("¿¿KELLY PERO QUÉ MONDÁ DE GÉNERO ES ESE??")
                    else:
                        print("Lista de películas para el género ",genre," ...")
                        for i in range(data[2]):
                            print(i+1,'. ',lt.getElement(data[0],i)["original_title"])
                        print('El promedio para las peliculas para el género ',genre,' es de: ',round(data[1],2))
                        print('Para un total de ',data[2],' peliculas')
                    t1_stop = process_time() #tiempo final
                    print("Tiempo de ejecución ",t1_stop-t1_start," segundos ")
                
            elif int(opcion[0]) == 6: #REQUERIMIENTO 5
                if cont == None:
                    print('¡KELLY CARGUE EL ARCHIVO PRIMERO!')
                else:
                    t1_start = process_time() #tiempo inicial
                    country = input('Digita un país para consultar películas: ').lower().strip()
                    data = ctrl.encontrarPeliculasPorPais(cont,country)
                    if data == -1:
                        print("¿¿KELLY PERO QUÉ MONDÁ DE PAÍS ES ESE??")
                    else:
                        print("Lista de películas para el país ",country.title()," ...")
                        for i in range(lt.size(data[2])):
                            print(i+1,'. ',lt.getElement(data[0],i)["original_title"],'  - Fecha de estreno: ',lt.getElement(data[1],i),'  - Director: ',lt.getElement(data[2],i))
                    t1_stop = process_time() #tiempo final
                    print("Tiempo de ejecución ",t1_stop-t1_start," segundos ")    
            
            elif int(opcion[0]) == 7: #SALIR
                sys.exit(0)
            
            else:
                print('Elije una opción valida.....')
main()