# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 15:27:03 2017
Francisco Salas
Resuelve Ec. (2) en (Azhmyakov et al. 2016, A Novel Numerical Approach to
 the MCLP Based Resilent Supply Chain Optimization)
@author: admin/Francisco Salas

Nota: se ejecuta antes de Optimization_MCLP_FSalas_Num2.py

Instrucciones: introducir datos de matriz A y vector Mu, en lineas 15 y 16,
 así como valor de k, en línea 26
"""
#from numpy import *
import numpy as np

A=np.array([[0.81286,0.25123,0,0.54893,1,0.77105,0,0.64741],
            [0,0.58108,0,0.90309,0,0.27081,0.51569,0.91733],
            [0,0.32049,0.64850,0.74559,0,0.65833,0,0.60562],
            [0.62968,0.89444,0.91921,0.50869,0,0.60434,0,0.63874],
            [0,0.79300,0.94740,0.99279,0,0.23595,0.57810,0.71511]])
Mu = np.array([2,2,1,2,2,2,1,2])

#% D es el producto de  \mu por a_{ij}, dada  
#% (obtenido en Datos_vadim2016_v1)
# Son los coeficientes de la funcion objetivo de "y" 
S=np.inner(Mu,A)
#S = np.array([[8.06295],[5.86033],[5.30955],[7.47098],[6.99921]])
#% D son los coeficientes del lado izquierdo de la restriccion
[n,m]=A.shape
#D=np.ones((1,n))
D=np.ones(n)
#D = np.array([1,1,1,1,1])
# Es la restricción o lado derecho de la funcion objetivo
k = 2
#[n,] = D.shape;
#n=8 # Tamanio del vector                   
tam = 2**(n)

#elementos = tam-1 # numero de combinaciones
# salida = np.zeros((elementos,n)) este ya no es necesario
Z1 = np.zeros((tam-1,n))

for numero in range(0,tam): # se cambió la variable elementos por tam
    #numero= # numero decimal 
    # d = np.array(numero) no es necesaria esta instrucción 
    power = 2**np.arange(n)
    d = numero * np.ones((1,n)) # se sustituyo de la linea 45 por numero.
    #b = np.floor((d%(2*power))/power)
    #salida[0,]=b
    Z1[numero-1,] = np.floor((d%(2*power))/power)
    #Z[numero-1,]=b  # matriz con los elementos en binario 
    # se quitó la linea en donde se crea la variable Z igual a la variable Salida

#% Se realiza la multiplicación para comprobar la restricción 
#% con cada combinacion 
#X = np.inner(Z,W)
X = np.dot(Z1,S)
# En Indice se guarda la combinacion (vector z) que cumple la restriccion
Indice = np.zeros((tam-1))

for i in range(0,tam-1):
    if (np.dot(Z1[i,:],D) == k):
        Indice[i] = 1
# Discriminar de vector de funcion objetivo X la combinacion que cumple la
# restriccion  
XM =X.transpose()*Indice
XM=XM.transpose()               
fOptim = XM.max()
for j in range(0,tam-1):
    if (XM[j]==fOptim):
        sol = Z1[j,:]
print(sol)
print(fOptim)
D2 = np.inner(A.transpose(),sol)
"""
D2 es el producto de A por sol (y), para el programa Optimization_MCLP_FSalas_Num2.py
La combinacion solucion es sol (revisar el orden de los elementos, parece que
es un orden inverso) que corresponde al vector solucion y de la optimizacion de la ec. (2)
El valor optimo de la funcion es fOptim         
""" 
