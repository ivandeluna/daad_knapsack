# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 12:54:55 2018

@author: josea
"""

import numpy as np
# El ejercicio contempla un modelo MCLP básico y optimiza una cadena de
# suministro resilente para un conjunto de plantas manufactureras y
# almacenes.

# La resilencia de este sistema de gestión de cadena de suministro es modelada
# en este ejercicio con una matriz A con el componente de tipo difuso a_ij

# Esta cadena de suministro conceptual incluye
l = 8 # Plantas manufactureras j
n = 5 # Almacenes i
k = 2 # nuevos almacenes considerados


# La matriz correspondiente esta definida de la siguiente manera:

A=np.array([[0.81286, 0.25123, 0.0,     0.54893, 1.0, 0.77105, 0.0,     0.64741],
            [0.0,     0.58108, 0.0,     0.90309, 0.0, 0.27081, 0.51569, 0.91733],
            [0.0,     0.32049, 0.64850, 0.74559, 0.0, 0.65833, 0.0,     0.60562],
            [0.62968, 0.89444, 0.91921, 0.50869, 0.0, 0.60434, 0.0,     0.63874],
            [0.0,     0.79300, 0.94740, 0.99279, 0.0, 0.23595, 0.57810, 0.71511]])

# Los pesos objetivo w_j indican una prioridad 
# y debe asumirse que son iguales a:    
    
w = np.array([32.0, 19.0, 41.0, 26.0, 37.0, 49.0, 50.0, 11.0])

# El quinto punto de demanda en este ejemplo no tiene un carácter resilente
# ya que solo una fabrica lo cubre.
# Asumimos que quien toma las decisiones está interesado en abrir otro punto.
# o de otra manera,

# Calculamos de la ecuación 12 en donde
# S_A_i := sum mu_j * a_i
# y
# A_i := (a_ij,..,a_in)'

# en donde a_ij es un componente de la matriz de elegibilidad

# Dado mu de la siguiente manera
mu = np.array([2,2,1,2,2,2,1,2])

# se calcula S
S = np.inner(mu,A)

# Se definen dos funciones que ayudan en la busqueda de la solución óptima

def z(n):
    ''' 
    Esta función calcula Z_h en base al parámetro n 
    que puede ser el número de almacenes o manufactureras
    Regresa un vector Z_h de tamaño [2**n-1, n] con valores
    booleanos {0,1}
    '''
    i = 2**n
    Z_h = np.zeros((i-1,n))
    p = 2**np.arange(n)
    for j in range(0,i):
        d = j * np.ones((1,n))
        Z_h[j-1,] = np.floor((d%(2*p))/p)
    return Z_h

def sol(XMn, fOptimEn, Zn):
    '''
    Función que devuelve la solución óptima a las ecuaciónes
    Usa los parámetros
    XMn - Matriz de tipo XM
    fOptimEn - valor máximo de la matriz XMn
    Zn - matriz de tipo Z o restricciones
    '''
    return Zn[np.where(XMn == fOptimEn),:]

Z1 = z(n)
Z2 = z(l)

D = np.ones(n)
I1 = np.zeros(2**n-1)

#I1 = Z1[np.where(np.dot(Z1, D) == k), :]

for i in range(0,2**n-1):
    if (np.dot(Z1[i,:],D) == k):
        I1[i] = 1

X1 = np.dot(Z1, S)
XM1 = X1.transpose()*I1
#XM1 = XM1.transpose()               
fOptimE2 = XM1.max()
solE2 = sol(XM1, fOptimE2, Z1)

D2 = np.inner(A.transpose(),solE2)
###########
I2 = np.zeros((2**l-1))

aux=np.ones((2**l-1))
for i in range(0, 2**l-1):
    for k in range(0,l-1):
        aux[k]=Z2[i,k] <= D2[k]
    if (np.all(aux)==True):
        I2[i] = 1
#    aux=[row[i] for row in Z2]
#    if (np.all(aux <= D2)==True):
#        I2[i]=1
#    if ((Z2[i,0] <= D2[0]) and
#        (Z2[i,1] <= D2[1]) and
#        (Z2[i,2] <= D2[2]) and
#        (Z2[i,3] <= D2[3]) and
#        (Z2[i,4] <= D2[4]) and
#        (Z2[i,5] <= D2[5]) and
#        (Z2[i,6] <= D2[6]) and
#        (Z2[i,7] <= D2[7])):
#        I2[i] = 1
'''
       
for i in range(0,2**l-1):
    if all(Z2[i,] <= D2.all()):
        I2[i] = 1
'''        
        
# Discriminar de vector de funcion objetivo X la combinacion que cumple la
# restriccion  
X2 = np.inner(w,Z2)
XM2 =X2*I2
fOptimE3 = XM2.max()
solE3 = sol(XM2, fOptimE3, Z2)

print(solE2)
print(fOptimE2)    
print(solE3)
print(fOptimE3)

#print(Z2)
#print(I2)