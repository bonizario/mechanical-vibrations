#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nome: Gabriel de Souza Bonizário
Matrícula: 2019.1037.9
Disciplina: Vibrações Mecânicas
Engenharia Mecânica
Universidade Federal do Triângulo Mineiro - UFTM

Created on Thu Mar 17 08:35:31 2022

@author: bonizario
"""

import numpy as np
from math import pi
import matplotlib.pyplot as plt

X = 0.01  # Amplitude [m]
m = 0.1   # Massa [kg]
f = 50    # Frequência [Hz]
T = 1 / f # Período [s]
fase = 0  # Fase [rad]

dt = T / 50                  # Intervalo de amostragem
t = np.arange(0, T, dt)      # Vetor de tempo
w = 2 * pi * f               # Frequência [rad/s]

x = X * np.sin(w * t + fase) # Função Senoidal
xc = X * np.exp(1j * w * t)  # Função Senoidal da Forma Complexa

plt.figure(1)

plt.title('Função Seno da Forma Complexa')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude [m]')

plt.plot(t, x, 'b.-', label='Função Seno')
plt.plot(t, np.imag(xc), 'r', label='Função Exponencial')
plt.legend(bbox_to_anchor=(1, 1))
plt.grid()
