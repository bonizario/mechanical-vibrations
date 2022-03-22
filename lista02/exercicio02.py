#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nome: Gabriel de Souza Bonizário
Matrícula: 2019.1037.9
Disciplina: Vibrações Mecânicas
Engenharia Mecânica
Universidade Federal do Triângulo Mineiro - UFTM

Created on Mon Mar 21 14:08:52 2022

@author: bonizario
"""

import numpy as np
import matplotlib.pyplot as plt

g = 9.81 # Aceleração da gravidade [m/s^2]
K_ex1 = 5.9819 # Coeficiente de rigidez do exercício 1
dados3 = np.loadtxt('dados3.txt', skiprows=1) # Dados 150g, 225g, 300g

carga_mola = dados3[:, 0]    # Carga na mola (massa) [g]
deflexao_mola = dados3[:, 1] # Deflexão da mola      [cm]

carga_mola /= 1000           # Carga na mola (massa) [kg]
F = carga_mola * g           # Força aplicada (peso) [N]
x = deflexao_mola / 100      # Deflexão da mola      [m]

# Cálculo da constante de rigidez da mola
[K, b] = np.polyfit(x, F, 1) # Ajuste (regressão linear de grau 1)
y = np.polyval([K, b], x)    # Avalia o polinômio ajustado
erro = (1 - K_ex1 / K) * 100 # Erro entre ajuste com 3 pontos e ajuste ex 1

print()
print(f'x [m] = {x}\n')
print(f'F [N] = {F}\n')
print(f'K [N/m] (Exercício 1) = {K_ex1:.4f}\n')
print(f'K [N/m] (Exercício 2) = {K:.4f}\n')

print(f'Erro percentual = {erro:.4f} %')

plt.figure(1)
plt.plot(x, F, 'bo', label='Medida Experimental')
plt.plot(x, y, 'r', label='Ajuste linear')
plt.title('Lei de Hooke, F = kx')
plt.xlabel('x [m]')
plt.ylabel('F [N]')
plt.legend(loc='lower right')
plt.grid()
plt.text(0.45, 3.06, f'K = {K:.4f}')
