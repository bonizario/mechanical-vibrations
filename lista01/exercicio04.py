#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nome: Gabriel de Souza Bonizário
Matrícula: 2019.1037.9
Disciplina: Vibrações Mecânicas
Engenharia Mecânica
Universidade Federal do Triângulo Mineiro - UFTM

Created on Mon Mar 21 07:59:05 2022

@author: bonizario
"""

import numpy as np
from math import pi
import matplotlib.pyplot as plt

X = 1     # Amplitude [m]
m = 0.1   # Massa [kg]
f = 79    # Frequência [Hz]
T = 1 / f # Período [s]
fase = 0  # Fase [rad]

dt = T / 80                  # Intervalo de amostragem
t = np.arange(0, T * 5, dt)      # Vetor de tempo
w = 2 * pi * f               # Frequência [rad/s]

x = X * np.exp(1j * w * t)               # Função Senoidal (fase = 0)
x_f1 = X * np.exp(1j * (pi / 2 + w * t)) # Função Senoidal (fase = pi / 2)
x_f2 = X * np.exp(1j * (pi + w * t))     # Função Senoidal (fase = pi)

plt.figure(1)

plt.title('Função Seno')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude [m]')

plt.plot(t, np.imag(x), 'b-', label='Fase = 0')
plt.plot(t, np.imag(x_f1), 'r-', label='Fase = pi/2')
plt.plot(t, np.imag(x_f2), 'g-', label='Fase = pi')
plt.legend(bbox_to_anchor=(1, 1))
plt.grid()
