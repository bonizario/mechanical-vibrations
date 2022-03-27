#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lista 02 - Exercício 1
Nome: Gabriel de Souza Bonizário
Matrícula: 2019.1037.9
Disciplina: Vibrações Mecânicas
Engenharia Mecânica
Universidade Federal do Triângulo Mineiro - UFTM

Created on Mon Mar 21 09:11:21 2022

@author: bonizario
"""

import numpy as np
import matplotlib.pyplot as plt

g = 9.81 # Aceleração da gravidade [m/s^2]
dados1 = np.loadtxt('dados1.txt', skiprows=1) # Dados 150g - 300g (step=5g)

carga_mola = dados1[:, 0]    # Carga na mola (massa) [g]
deflexao_mola = dados1[:, 1] # Deflexão da mola      [cm]

carga_mola /= 1000           # Carga na mola (massa) [kg]
F = carga_mola * g           # Força aplicada (peso) [N]
x = deflexao_mola / 100      # Deflexão da mola      [m]

# Cálculo da constante de rigidez da mola
[K, b] = np.polyfit(x, F, 1) # Ajuste (regressão linear de grau 1)
y = np.polyval([K, b], x)    # Avalia o polinômio ajustado

print()
print(f'x [m] = {x}\n')
print(f'F [N] = {F}\n')
print(f'K [N/m] = {K:.4f}\n')

plt.figure(1)
plt.plot(x, F, 'bo', label='Medida Experimental')
plt.plot(x, y, 'r', label='Ajuste linear')
plt.title('Lei de Hooke, F = kx')
plt.xlabel('x [m]')
plt.ylabel('F [N]')
plt.legend(loc='lower right')
plt.grid()
plt.text(0.45, 3.065, f'K = {K:.4f}')
