"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
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


import pytest
import config as cf
from Sorting import insertionsort as sort
from DataStructures import listiterator as it
from DataStructures import singlelinkedlist as slt
from ADT import list as lt
import csv
from time import process_time 

list_type = 'ARRAY_LIST'
#list_type = 'SINGLE_LINKED'
moviesfile = "Data/theMoviesdb/SmallMoviesDetailsCleaned.csv"

def setUp():
    print('Loading movies')
    lst_movies = loadCSVFile(moviesfile)
    print(lst_movies['size'])

def tearDown():
       pass


def loadCSVFile (file, sep=";"):
    """
    Carga un archivo csv a una lista
    Args:
        file
            Archivo csv del cual se importaran los datos
        sep = ";"
            Separador utilizado para determinar cada objeto dentro del archivo
        Try:
        Intenta cargar el archivo CSV a la lista que se le pasa por parametro, si encuentra algun error
        Borra la lista e informa al usuario
    Returns: None  
    """
    lst = lt.newList(list_type) 
    print("Cargando archivo ....")
    dialect = csv.excel()
    dialect.delimiter=sep
    try:
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                lt.addLast(lst,row)
    except:
        print("Hubo un error con la carga del archivo")
    return lst

def printList(lst):
    iterator = it.newIterator(lst)
    while it.hasNext(iterator):
        element = it.next(iterator)
        print(element["vote_average"])

columna = "vote_average"

def less(element1, element2, column=columna): # Agregué "column" para poder escoger, por ejemplo, entre vote_average y vote_count
    if float(element1[column]) < float(element2[column]):
        return True
    return False

def greater(element1, element2, column=columna):
    if float(element1[column]) > float(element2[column]):
        return True
    return False  
def test_sort(criteria):
    """
    Lista con elementos en orden aleatorio
    Args:
        criteria
              Critero para ordenar (less o greater)  
    """
    print("sorting ....")
    lst_movies = loadCSVFile(moviesfile)
    t1_start = process_time() #tiempo inicial
    sort.insertionSort(lst_movies, criteria)
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")    


def test_loading_CSV_y_ordenamiento():
    """
    Prueba que se pueda leer el archivo y que despues de relizar el sort, el orden este correcto
    """
    setUp()
    sort.insertionSort(lst_movies,less)
    while not (lt.isEmpty(lst_movies)):
        x = float(lt.removeLast(lst_movies)['vote_average'])
        if not (lt.isEmpty(lst_movies)):
            y = float(lt.lastElement(lst_movies)['vote_average'])
        else:
            break
        assert x >= y       
##test_loading_CSV_y_ordenamiento()