# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 20:11:06 2018

@author: ivand

Ejercicios del documento
An introduction to pulp for Python Programmers
Stuart Mitchell
"""

import pulp

# A Linear Program consist of three main parts.
# Variable definitions
# Objective function
# Constraints

# Variable definitions

# initialise the model
whiskas_model = pulp.LpProblem('The Whiskas Problem', pulp.LpMinimize)

# make a list of ingredients
ingredients = ['chicken','beef','mutton','rice','wheat','gel']

# create a dictionary of pulp variables with keys from ingredients
# the default lower bound is -inf
x = pulp.LpVariable.dict('x_%s', ingredients, lowBound = 0)

# cost data
cost = dict(zip(ingredients,[0.013,0.008,0.010,0.002,0.005,0.001]))

# Objective function

# create the objective
whiskas_model += sum([cost[i] * x[i] for i in ingredients])

# Constraints

# ingredient parameters

protein = dict(zip(ingredients, [0.100,0.200,0.150,0.000,0.040,0.001]))
fat = dict(zip(ingredients,[0.080,0.100,0.110,0.010,0.010,0.000]))
fibre = dict(zip(ingredients,[0.001,0.005,0.003,0.100,0.150,0.000]))
salt = dict(zip(ingredients,[0.002,0.005,0.007,0.002,0.008,0.000]))

# these are constraints and not an objective as there is an equality/inequality
whiskas_model += sum([protein[i]*x[i] for i in ingredients]) >= 8.0
whiskas_model += sum([fat[i]*x[i] for i in ingredients]) >= 6.0
whiskas_model += sum([fibre[i]*x[i] for i in ingredients]) <= 2.0
whiskas_model += sum([salt[i]*x[i] for i in ingredients]) <= 0.4

# problem is then solved with the default solver
whiskas_model.solve()

# print the result
for ingredient in ingredients:
    print ('The mass of %s is %s grams per can'%(ingredient,
                                                x[ingredient].value()))





