#!/usr/bin/python3

import sys #modulo sys para comunicarnos con la shell

NUM_ARG = 4 #cte

#Comprobacion numero de argumentos
if len(sys.argv) != NUM_ARG:
     sys.exit("Error. Uso: python3 calculadora.py funcion operando1 operando2")

#Definimos las funciones suma, resta, mult y div mediante def.
def suma(op1, op2):
    return op1+op2

def resta(op1, op2):
    return op1-op2

def mult(op1, op2):
    return op1*op2

def div(op1, op2):
    try:
        return op1/op2
    except ZeroDivisionError:
        print("No intentes dividir entre 0")
        sys.exit()

#Casting argumentos a tipo float
#y Comprobacion argumentos no son tipo char
try:
    op1 = float(sys.argv[2])
    op2 = float(sys.argv[3])
except ValueError:
    print ("No es posible operar con chars")
    sys.exit()


funcion = sys.argv[1]

if funcion == "suma":
    print(suma(op1,op2))

elif funcion == "resta":
    print(resta(op1,op2))

elif funcion == "mult":
    print(mult(op1,op2))

elif funcion == "div":
    print(div(op1,op2))

else:
    sys.exit("Funcion no existente")
