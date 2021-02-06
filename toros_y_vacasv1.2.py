import random
import sys

# La función sample() del modulo random devuelve de una lista de elementos, un
# determinado número de elementos (4) diferentes elegidos al azar.

def ImprimeEncabezado():
    titulo = "\nT O R O S  Y  V A C A S v-1.2"
    return titulo

def MuestraFechaAutor():
    fechaautor = "@ 2021 by NESTOR JAVIER HEVIA PAVON"
    return fechaautor

def Instrucciones():
    instrucciones = ("""\n----------------------INTRUCCIONES-----------------------\n
                     "El programa seleccionará un código secreto de cuatro dígitos, distintos y tú tienes que adivinar cuál es en la menor cantidad de intentos."
                     "No hay límite en cuanto al número de intentos. Después de cada uno de tus intentos el programa te dirá cuántos T O R O S y cuántas V A C A S obtuviste
                     "- Un T O R O indica que uno de los dígitos que ingresaste coincide exactamente con el valor y la posición de uno de los dígitos en el código secreto:
                     "- Una V A C A indica que uno de los dígitos que ingresaste coincide con el valor de uno de los dígitos en el código secreto, pero que está en una posición incorrecta.
                     "El juego termina cuando obtengas cuatro T O R O S, es decir, cuando hayas descubierto todos los dígitos y posiciones correctas del código secreto.\n""")
    return instrucciones

# Funtion No.1 que devuleve un numero secreto aleatorio
# de 4 digitos diferentes
numero_secreto = ''
def get_numero_secreto():
    global numero_secreto
    if len(numero_secreto) != 0:
        print("numero_secreto: ", numero_secreto)
        return numero_secreto
    else:
        lista = [1,2,3,4,5,6,7,8,9,0]
        listanew = random.sample(lista, 4)
        numero_secreto = "".join(map(str, listanew))
        return numero_secreto

# Funcion que hace salir del ciclo si codigo_ingresado = None
# O presiona x para rendirte.
def try_salir_funcion(codigo_ingresado=None):
    if codigo_ingresado == 'x':
        print("Te rendiste el código secreto es: ", get_numero_secreto())
        sys.exit()

# definiendo variables globales
toros = 0
vacas = 0
contador_intentos = 0

# Codigo ingresado por el jugador
def get_CodIngresado():
    global contador_intentos
    global toros
    global vacas
    while toros != 4:
        contador_intentos += 1
        print("\n")
        count = (f"INTENTO No. {str(contador_intentos)}")
        print(count.center(50, "="))
        toros = 0
        vacas = 0
        codigo_ingresado = input("Ingrese un código, (X) para rendirte: ")
        try_salir_funcion(codigo_ingresado)

        while len(codigo_ingresado) != 4 and codigo_ingresado != 'x' or codigo_ingresado.isdigit() != True or len(set(codigo_ingresado)) != 4:
            codigo_ingresado = input("Ingrese un código correctamente, (X) para rendirte: ")
            try_salir_funcion(codigo_ingresado)
        
        # Validar entrada
        if len(codigo_ingresado) == 4 and codigo_ingresado.isdigit() == True:
            cs = get_numero_secreto()
            for i in range(4):
                indice = cs.find(codigo_ingresado[i])
                if indice == -1:
                    continue
                if indice == i:
                    toros += 1
                    continue
                vacas += 1
            print('Calificacion: Vacas: ', vacas, ' Toros: ', toros)
            ganar_juego(contador_intentos, toros)

def ganar_juego(contador_intentos, toros):
    if toros == 4:
        print("Ganaste!! en", contador_intentos, "intentos")
        sys.exit()

# Aqui comienza la ejecucion del juego
print(ImprimeEncabezado())
print("==============================================")
print(MuestraFechaAutor())
print("\n----------------PRESIONE----------------\n")
print(" (1) Para ver las intrucciones")
print(" (2) Para jugar")
print(" (3) Salir del juego")


opcion = int(input("\nElija una opción: "))
while opcion >= 1 and opcion <= 3:
    if opcion == 1:
        print(Instrucciones())
        print("---------------PRESIONE--------------\n")
        print(" (2) Para jugar")
        print(" (3) Salir del juego")
        opcion = int(input("\nElija una opción: "))

    if opcion == 2:
        get_CodIngresado()
    if opcion == 3:
        print("Gracias por participar")
    if opcion >= 3:
        print("Ha ocurrido un error")
        opcion = int(input("\nElija una opción del 1 al 3: \n"))