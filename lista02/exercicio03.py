#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lista 02 - Exercício 3
Nome: Gabriel de Souza Bonizário
Matrícula: 2019.1037.9
Disciplina: Vibrações Mecânicas
Engenharia Mecânica
Universidade Federal do Triângulo Mineiro - UFTM

Created on Sun Mar 27 19:04:49 2022

@author: bonizario
"""

# Material escolhido para mola: Liga de aço inoxidável 304
E = 193 * 10 ** 9      # Módulo de elasticidade [Pa]
v = 0.30               # Coeficiente de Poisson
G = E / (2 * (1 + v))  # Módulo de elasticidade transversal [Pa]
D = 16 * 10 ** (-3)    # Diâmetro da mola  [m]
k = 6.00               # Coeficiente de rigidez [N/m]
n = 12                 # Número de espiras

d = (8 * k * n * D**3 / G) ** (1/4)

print(f'd [mm] = {d * 10 ** 3}')
