#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nome: Gabriel de Souza Bonizário
Matrícula: 2019.1037.9
Disciplina: Vibrações Mecânicas
Engenharia Mecânica
Universidade Federal do Triângulo Mineiro - UFTM

Created on Thu Mar 17 08:48:55 2022

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

dt = T / 50                 # Intervalo de amostragem
t = np.arange(0, T * 5, dt) # Vetor de tempo
w = 2 * pi * f              # Frequência [rad/s]

x = X * np.exp(1j * w * t)  # Função da Forma Complexa
x = np.imag(x) * 1000 * 10  # Deslocamento [mm]*10
xp = 1j * w * X * np.exp(1j * w * t)
xp = np.imag(xp) * 100      # Velocidade [cm/s]
xpp = -w**2 * X * np.exp(1j * w * t)
xpp = np.imag(xpp)          # Aceleração [m/s^2]
Fi = m * xpp                # Força interna [N]

plt.figure(1)

plt.title('Função Seno da Forma Complexa')
plt.xlabel('Tempo [s]')
plt.ylabel('')

plt.plot(t, x, 'r', label='x [m]')
plt.plot(t, xp, 'b', label='v [m/s]')
plt.plot(t, xpp, 'g', label='a [m/s^2]')
plt.plot(t, Fi, 'm', label='Fi [N]')

plt.legend(bbox_to_anchor=(1, 1))
plt.grid()
