# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 15:27:03 2017
Francisco Salas
Resuelve Ec. (2) en (Azhmyakov et al. 2016, A Novel Numerical Approach to the MCLP Based Resilent Supply Chain Optimization)
@author: admin/Francisco Salas

Nota: se ejecuta antes de Optimization_MCLP_FSalas_Num2.py

Instrucciones: introducir datos de matriz A y vector Mu, en lineas 15 y 16, así como valor de k, en línea 26
"""
#from numpy import*
import numpy as np

n=5
l=8

A=np.matrix([[0.81286,0.25123,0,0.54893,1,0.77105,0,0.64741],
            [0,0.58108,0,0.90309,0,0.27081,0.51569,0.91733],
            [0,0.32049,0.64850,0.74559,0,0.65833,0,0.60562],
            [0.62968,0.89444,0.91921,0.50869,0,0.60434,0,0.63874],
            [0,0.79300,0.94740,0.99279,0,0.23595,0.57810,0.71511]])

Mu = np.matrix([2,2,1,2,2,2,1,2])

y = np.matrix([1,1,0,0,0])

S = n*[n*[0]]

J = np.zeros(n-1)

JM = np.zeros(n-1)

nJM = np.zeros(n-1)

S[0][:] = y*A

J[0] = np.inner(Mu,S[0][:])

for i1 in range(0,n-1):
    y = np.matrix([0,0,0,0,0])
    y[0,i1] = 1
    J = np.zeros(n-1)
    for i2 in range(i1+1,n):
        y[0,i2] = 1
        S[i2-1][:] = y*A
        J[i2-1] = np.inner(Mu,S[i2-1][:])
        print(y)
        print(J)
        combinaciones = i1+1
        y[0,i2] = 0
    JM[i1] = np.amax(J)
    nJ=np.argmax(J,axis=0)
    nJM[i1]=nJ
    print(JM)
    print(nJM)
    input("Press Enter to continue...")

JMAX=np.amax(JM)

nJ1=np.argmax(JM,axis=0)

nJMAX=nJ1

yopt=np.array([0,0,0,0,0])

yopt[int(nJM[nJ1]+1)]=1

yopt[int(nJ1)]=1

print(JMAX)

print(nJMAX)

print(yopt)

input("Press Enter to continue...")

