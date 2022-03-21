#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nome: Gabriel de Souza Bonizário
Matrícula: 2019.1037.9
Disciplina: Vibrações Mecânicas
Engenharia Mecânica
Universidade Federal do Triângulo Mineiro - UFTM

Created on Thu Mar 17 08:06:46 2022

@author: bonizario
"""

import numpy as np
from math import pi
import matplotlib.pyplot as plt

X = 1     # Amplitude [m]
f = 10    # Frequência [Hz]
T = 1 / f # Período [s]
fase = 0  # Fase [rad]

dt = T / 100                      # Intervalo de amostragem
t = np.arange(0, T * 5, dt)       # Vetor de tempo
w = 2 * pi * f                    # Frequência [rad/seg]

x = X * np.sin(w * t + fase)      # Função Senoidal
x_f1 = X * np.sin(w * t + pi / 2) # Função Senoidal com fase 90 graus
x_f2 = X * np.sin(w * t + pi)     # Função Senoidal com fase 180 graus

plt.figure(1)

plt.title('Função Seno')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude [m]')

plt.plot(t, x, 'b', label='Fase = 0')
plt.plot(t, x_f1, 'r', label='Fase = pi/2')
plt.plot(t, x_f2, 'g', label='Fase = pi')
plt.legend(bbox_to_anchor=(1, 1))
plt.grid()
