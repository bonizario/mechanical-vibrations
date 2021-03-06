#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nome: Gabriel de Souza Bonizário
Matrícula: 2019.1037.9
Disciplina: Vibrações Mecânicas
Engenharia Mecânica
Universidade Federal do Triângulo Mineiro - UFTM

Created on Mon Mar 21 08:56:37 2022

@author: bonizario
"""

import numpy as np
from math import pi
import matplotlib.pyplot as plt

X = 1     # Amplitude [m]
m = 0.9   # Massa [kg]
f = 79    # Frequência [Hz]
T = 1 / f # Período [s]

dt = T / 50                 # Intervalo de amostragem
t = np.arange(0, T * 5, dt) # Vetor de tempo
w = 2 * pi * f              # Frequência [rad/s]

x = X * np.exp(1j * w * t)  # Função da Forma Complexa
x = np.imag(x) * 1000 * 10  # Deslocamento [mm]*10
xp = 1j * w * X * np.exp(1j * w * t)
xp = np.imag(xp) * 100      # Velocidade [cm/s]
Ec = 0.5 * m / 10000 * np.power(xp, 2) # Energia Cinética [J]
plt.figure(1)

plt.title('Função Seno da Forma Complexa')
plt.xlabel('Tempo [s]')
plt.ylabel('')

plt.plot(t, x, 'r', label='x [m]')
plt.plot(t, xp, 'b', label='v [m/s]')
plt.plot(t, Ec, 'g', label='Ec [J]')

plt.legend(bbox_to_anchor=(1, 1))
plt.grid()
