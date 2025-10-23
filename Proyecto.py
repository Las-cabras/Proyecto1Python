
from genderize import Genderize
from Utils import Trabajos
def trabajo_en_10anios():


#Declaramos las variables que vamos a necesitar para poder realizar nuestro programa.
    nombre = input("Ingresa tu nombre: ")#Nombre del usuario, el cual usaremos para saludar y detectar si es hombre o mujer
    edad = int(input("Ingresa tu edad: "))#Edad del usuario, esta se le sumara 10 años y se mostrara para saber cuantos años tendria.
    edad += 10#Variable que contiene la edad del usuario dentro de 10 años
    genero = Genderize()#Llamamos a la funcion Genderize que la importamos desde una libreria, y la guardamos en una variable que se usara para detectar si el nombre es masc o fem
    resultado = genero.get([nombre])#Guardamos el resultado de si es masc o fem en una variable para despues comparar.

    #Importamos la libreria Faker de faker para poder obtener un trabajo aleatorio que se encuentre en esta.
    #Estos se pueden clasificar en generales, masc o fem dando opcion a realizar el programa como uno quiera.

    t= Trabajos()


    trabajo_en_20anios(resultado, nombre, edad,t)



    #Creamos una secuencia de if, elif, else para comprobar si el valor que se encuentra en dentro de resultado(male p female)
    #coundice con un género u otro.

    #NOTA --> Indicamos la posición 0, ya que ahora solo hay una persona a la que vamos a comprobar, si hubiesen mas personas
    #tendriamos que poner la posición exacta de esa persona. También ponermos entre corchetes la palabra gender para que
    #coja el valor de esa clave, ya que Genderize lo que hace es crear un diccionario con nombre, género,edad,etc...
    #haciendo que tengamos que indicar la clave de la que queremos el valor para poder compararla.

def genero(resultado):
    return resultado[0]["gender"]



def es_hombre(resultado):
    return genero(resultado) in ["male", "mostly_male"]


def es_mujer(resultado):
    return genero(resultado) in ["female", "mostly_female"]

def printerHombres(nombre, edad, t):
    return print(f"Hola  {nombre} dentro de 10 años cuando tengas  {edad} trabajaras de  {t.trabajos_hombres_aleatorios().lower()}")

def printerMujeres(nombre, edad, t):
    return print(f"Hola  {nombre} dentro de 10 años cuando tengas  {edad} trabajaras de  {t.trabajos_mujeres_aleatorios().lower()}")



def trabajo_en_20anios(resultado, nombre, edad, t):
    if es_hombre(resultado):#Comprobamos si el valor está entre las dos opciones.

        printerHombres(nombre,edad,t)#Printeamos el saludo junto a la edad y el trabajo que realizara

    elif es_mujer(resultado):#Comprobamos si el valor está entre las dos opciones.

        printerMujeres(nombre,edad,t)#Printeamos el saludo junto a la edad y el trabajo que realizara

    else: print("Genero no conocido")



trabajo_en_10anios()