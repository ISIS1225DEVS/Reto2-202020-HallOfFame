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
from DISClib.DataStructures import mapentry as me
from DISClib.DataStructures import liststructure as lt
from DISClib.DataStructures import listiterator as it
from App import controller
from time import perf_counter

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

def printMenu():
    print("Bienvenido")
    print("w-Inicializar Catálogo")
    print("q-Cargar información en el catálogo")
    print("1- Descubrir productoras de cine")
    print("2- Conocer a un director")
    print("3- Conocer a un actor")
    print("4- Entender un género")
    print("5-Encontrar películas por país")
    print("0- Salir")




def printMoviesbyIdk(movies, msg_f, print_list, var_prom, var_freq=None):
    """
    Imprime los libros de un autor determinado
    """
    if movies:
        name = movies["name"]
        print(msg_f + " " + name)
        l_movies = movies["movies"]
        n = movies["size"]
        info = controller.info_movies(movies, var_prom, var_freq)
        iterator = it.newIterator(l_movies)
        for i in range(n):
            movie = it.next(iterator)
            print_m = ""
            for el_print in print_list:
                print_m += movie[el_print] + ",  "
            print(print_m)
        print("Numero de peliculas: ", n)
        print(var_prom, ": ", round(info[0], 2))

        if var_freq:
            rep = info[1]
            print("para {} se encontro que {} mas frecuente fue: {} con {}".
                  format(name, var_freq, rep[var_freq], rep["times"]))

    else:
        print('No se encontro el elemento')


# ___________________________________________________
#  Menu principal
# ___________________________________________________


while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if inputs[0] == "w":
        C1 = input("desea usar el ADT map PROBE: 0, CHAINING: 1 :")
        map_type = "CHAINING" if int(C1) else "PROBE"
        C2 = input("Loadfactor por defecto: 1, Otro: 2")
        if C2 == "2":
            print("recuerde que para map PROBE el loadfactor no debe superar")
            C3 = input("Ingrese en valor de loadfactor")
            loadfactor = float(C3)

        else:
            loadfactor = None

        t1 = perf_counter()
        print("Inicializando Catálogo ....")
        # cont es el controlador que se usará de acá en adelante
        cont = controller.initCatalog(map_type, loadfactor)
        t2 = perf_counter()
        print(t2 - t1)

    elif inputs[0] == "q":
        C1 = input("numero de elementos que quiere cargar, enter si desea todos")
        t1 = perf_counter()
        movies_file1 = "GoodMovies/AllMoviesDetailsCleaned.csv"
        movies_file2 = "GoodMovies/AllMoviesCastingRaw.csv"
        if C1 == "":
            n = "ALL"
        else:
            try:
                n = int(C1)
            except ValueError:
                print("numero no valido")
                continue

        print("Cargando información de los archivos ....")
        controller.loadData(cont, movies_file1, movies_file2, n)


        t2 = perf_counter()
        print("tiempo de carga:", t2 - t1)

    elif int(inputs[0]) == 1:
        estudio = input("estudio que desea ver\n")
        t1 = perf_counter()
        print("Cargando...")
        msf = "Se he encontrado al estudio"
        print_1 = ["original_title", "vote_average"]
        movies = controller.get_name(cont, "producers", estudio)
        printMoviesbyIdk(movies, msf, print_1, "vote_average")
        t2 = perf_counter()
        print("tiempo req1:", t2 - t1)

    elif int(inputs[0]) == 2:
        director = input("director que desea ver\n")
        t1 = perf_counter()
        print("Cargando...")
        msf = "Se he encontrado al director"
        print_1 = ["original_title", "vote_average"]
        movies = controller.get_name(cont, 'directores', director)
        printMoviesbyIdk(movies, msf, print_1, "vote_average")
        t2 = perf_counter()
        print("tiempo req2:", t2 - t1)

    elif int(inputs[0]) == 3:
        actor = input("actor que quiere consultar\n")
        print("Cargando...")
        t1 = perf_counter()
        msf = "Se he encontrado al actor/actriz"
        print_1 = ["original_title", "vote_average"]
        movies = controller.get_name(cont, "actors", actor)
        printMoviesbyIdk(movies, msf, print_1, "vote_average", "director_name")
        t2 = perf_counter()
        print("tiempo req3:", t2 - t1)

    elif int(inputs[0]) == 4:
        genero = input("genero que quiere consultar\n")
        t1 = perf_counter()
        print("Cargando...")
        msf = "Se he encontrado el genero"
        print_1 = ["original_title", "vote_average"]
        movies = controller.get_name(cont, "genres", genero)
        printMoviesbyIdk(movies, msf, print_1, "vote_average")
        t2 = perf_counter()
        print("tiempo req4:", t2 - t1)

    elif int(inputs[0]) == 5:
        pais = input("pais que quiere consultar\n")
        t1 = perf_counter()
        print("Cargando...")
        msf = "Se he encontrado el pais"
        print_1 = ["original_title", "vote_average","release_date","director_name"]
        movies = controller.get_name(cont, "paises", pais)
        printMoviesbyIdk(movies, msf, print_1, "vote_average")
        t2 = perf_counter()
        print("tiempo req5:", t2 - t1)

    elif int(inputs[0]) == 0:
        break

    else:
        print("Opcion invalida")
        continue
