#!/usr/bin/python
#!encoding: UTF-8

import sys

#def calcular_xi (n, i):
#  xi = (i - 1.0/2.0) / n
#  return xi

def calcular_pi (n):
  #  PI35 = 3.1415926535897931159979634685441852
  print "Valor correcto"
  sumatorio = 0.0
  ini = 0
  intervalos = 1.0 / float (n)
  for i in range(n):
    x_i = ((i+1) - 1.0/2.0) / n
#   x_i = calcular_xi (n, i+1)
    fx_i = 4.0 /(1.0 + x_i * x_i)
    ini += intervalos
    sumatorio += fx_i
  valor_pi = sumatorio / n
  return (valor_pi)
  
  
#Programa principal
#Ojo, para hacer uso de la funcion sys, debemos incluirla al principio deñ programa
argumentos = sys.argv[1:]
print argumentos
if (len(argumentos) == 2):
  n = int (argumentos[0])
  aproximaciones = int (argumentos[1])
else:
  print "Introduzca el nº de intervalos(n>0):"
  n = int (raw_input());
  print "Introduce el nº de aproximaciones:"
  aproximaciones = int (raw_input());
if(n>0):
  intervalo = n
  lista = []
  for i in range (aproximaciones):
    valor = calcular_pi (intervalo)
    lista.append (valor)
    intervalo += n
  print lista
  

else:
  print "El valor de los intervalos debe ser mayor que 0"