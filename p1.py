import matplotlib.pyplot as plt
from math import cos, sin, exp, pi
import numpy as np
from numpy.core.function_base import linspace
import cmath
from funciones import fa, fb, fc, fd

# Se define la función plot, para graficar las distintas funciones importadas del módulo
# funciones
def plot(function, interval, N):
    xmin = interval[0]
    xmax = interval[1]
    T = (xmax - xmin) / N

    muestreo_x = []
    muestreo_n = []
    muestreo = []
    if (N % 2) == 0:
        N_min = - N / 2
        N_max = N / 2 - 1

    else:
        N_min = - (N - 1) / 2
        N_max = (N - 1) / 2

    N_add = N_min

    while N_add < N_max + 1:
        muestreo_x.append(N_add * T)
        muestreo_n.append(N_add)
        muestreo.append(function(N_add * T))
        N_add += 1

    data = np.array(muestreo)
    plt.figure(figsize=(8, 6))
    plt.stem(muestreo_n, data.imag, 'b', markerfmt='bo', label="imag")
    plt.stem(muestreo_n, data.real, 'g', markerfmt='go', label="real")
    plt.legend()
    plt.show()

# Descomentar para ver cada función
#plot(fa, [-1, 1], 64)
#plot(fb, [-1, 1], 64)
#plot(fc, [-2, 2], 64)
#plot(fd, [-2, 2], 64)
