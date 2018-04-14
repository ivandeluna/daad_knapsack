# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 15:27:03 2017
Francisco Salas
Resuelve Ec. (3) en (Azhmyakov et al. 2016, A Novel Numerical Approach to the MCLP Based Resilent Supply Chain Optimization)
@author: admin/Francisco Salas

Nota: Ejecutar después de Optimization_MCLP_FSalas_Num2.py
Del resultado de dicho programa se toma la variable D2, que es el valor del producto de la matriz A por y 

Instrucciones : Introducir valores del vector W en linea 23

"""
#from numpy import *
import numpy as np

#% D2 es el producto A'*y, dada una y de 5*1 arbitraria (u optima) 
#% (obtenido en Datos_vadim2016_v1)
# Son los coeficientes de la restricciones para cada uno de los elementos del
# vector z
#D = np.array([[1.4425],[1.1457],[0.9192],[1.0576],[1],[1.3754],[0],[1.2862]])
#% W son los pesos o los coeficientes de la funcion objetivo
W = np.array([32,19,41,26,37,49,50,11])
# D2 es una variable producida en Fuerza_bruta_03_Mlb
#[l,] = D2.shape; #se convierte en l = 8
#n=8 # Tamanio del vector                   
cl = 2**(l) # usar l = 8

elementos = cl-1 # numero de combinaciones
salida = np.zeros((cl-1,l))

for numero in range(0,cl):
    #numero= # numero decimal 
    #d = np.array(numero)
    power = 2**np.arange(l)
    d = numero * np.ones((1,l))
    b = np.floor((d%(2*power))/power)
    #salida[0,]=b
    salida[numero-1,]=b  # matriz con los elementos en binario
Z2=salida  

#% Se realiza la multiplicación para comprobar la restricción 
#% con cada combinacion 
X = np.inner(W,Z2)
# En Indice se guarda la combinacion (vector z) que cumple la restriccion
Indice = np.zeros((cl-1))
for i in range(0,cl-1):
    if ((Z2[i,0] <= D2[0]) and
        (Z2[i,1] <= D2[1]) and
        (Z2[i,2] <= D2[2]) and
        (Z2[i,3] <= D2[3]) and
        (Z2[i,4] <= D2[4]) and
        (Z2[i,5] <= D2[5]) and
        (Z2[i,6] <= D2[6]) and
        (Z2[i,7] <= D2[7])):
        Indice[i] = 1
# Discriminar de vector de funcion objetivo X la combinacion que cumple la
# restriccion  
XM =X*Indice
fOptimE3 = max(XM)
for j in range(0, cl-1):
    if (XM[j]==fOptimE3):
        solE3 = Z2[j]
print(solE3)
print(fOptimE3)
"""
La combinacion solucion es solE3 
El valor optimo de la funcion es fOptimE3         
(Comparar con la solucion en ec. (16)) 
"""