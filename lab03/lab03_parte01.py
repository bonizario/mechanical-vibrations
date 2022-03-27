#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nome: Gabriel de Souza Bonizário
Matrícula: 2019.1037.9
Disciplina: Vibrações Mecânicas
Engenharia Mecânica
Universidade Federal do Triângulo Mineiro - UFTM

Created on Sun Mar 27 19:54:13 2022

@author: bonizario
"""

import numpy as np
from math import pi
import matplotlib.pyplot as plt

X = 0.01  # Amplitude [m]
m = 0.1   # Massa [kg]
f = 50    # Frequência [Hz]
T = 1 / f # Período [s]

dt = T / 50                 # Intervalo de amostragem
t = np.arange(0, T * 5, dt) # Vetor de tempo
w = 2 * pi * f              # Frequência [rad/s]

x = X * np.exp(1j * w * t)  # Função da Forma Complexa
x = np.imag(x)              # Deslocamento [m]

xp = 1j * w * X * np.exp(1j * w * t)
xp = np.imag(xp)            # Velocidade [m/s]

xpp = -w**2 * X * np.exp(1j * w * t)
xpp = np.imag(xpp)          # Aceleração [m/s^2]

Fi = m * xpp # Força partícula [N]

# Mola sob deflexão harmônica Fm = -K * x
K = 40000   # Coeficiente de rigidez [N/m]
F = K * x   # Força externa          [N]
Fm = -K * x # Força da mola          [N]

# Amortecedor Viscoso sob deflexão harmônica Fa = -C * x
C = 100 # Coeficiente de amortecimento [N*s/m]
Fa = -C * xp # Força do amortecedor    [N]

# Amortecedor Coulomb sob deflexão harmônica Fc = -u * N * sgn(xp)
uN = 1 # Coeficiente de atrito x Força normal [N]
Fc = -uN * np.sign(xp) # Força do amortecedor [N]


plt.figure(1)
plt.plot(t, x*1000*10, 'r-', label='x [mm]*10')
plt.plot(t, xp*100, 'b', label='v [cm/s]')
plt.plot(t, xpp, 'g', label='a [m/s^2]')
plt.plot(t, Fi, 'm', label='Fi [N]')
plt.title('Função Seno da Forma Complexa')
plt.xlabel('Tempo [s]')
plt.legend(bbox_to_anchor=(1, 1))
plt.grid()

plt.figure(2)
plt.plot(t, x*1000*10, label='x [mm]*10')
plt.plot(t, F, label='F [N]')
plt.plot(t, Fm, label='Fm [N]')
plt.title('Mola sob deflexão harmônica')
plt.xlabel('Tempo [s]')
plt.legend(bbox_to_anchor=(1, 1))
plt.grid()

plt.figure(3)
plt.plot(t, x*1000, label='x [mm]')
plt.plot(t, xp*10, label='v [m/s]*10')
plt.plot(t, Fa, label='Fa [N]')
plt.title('Amortecedor Viscoso sob deflexão harmônica')
plt.xlabel('Tempo [s]')
plt.legend(bbox_to_anchor=(1, 1))
plt.grid()

plt.figure(4)
plt.plot(t, x*1000, label='x [mm]')
plt.plot(t, xp, label='v [m/s]')
plt.plot(t, Fc, label='Fc [N]')
plt.title('Amortecedor Coulomb sob deflexão harmônica')
plt.xlabel('Tempo [s]')
plt.legend(bbox_to_anchor=(1, 1))
plt.grid()
