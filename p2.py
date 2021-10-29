from math import exp
from funciones import fa, fb, fc, fd
import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack
import cmath

# Se define la función DFT, que recibe como parámetros la función de interés, el intervalo de
# muestreo y la cantidad N de muestras, adecuados para obtener un buen gráfico
def DFT(function, interval, N):
    xmin = interval[0]
    xmax = interval[1]
    T = (xmax - xmin) / N

    muestreo_n = []
    muestreo = []

    N_min = - N / 2
    N_max = N / 2 - 1
    N_add = N_min

    while N_add < N_max + 1:
        muestreo_n.append(N_add)
        muestreo.append(function(N_add * T))
        N_add += 1

    u = muestreo_n
    aux = list(range(0, N))
    k_shift = np.array(aux)
    # Por propiedad de desplazamiento en Fourier hay que multiplicar por un exp
    # (f = 1 / T)
    phase_shift = []
    for elem in k_shift:
        phase_shift.append(cmath.exp(-1j * 2 * np.pi * (1 / T) * (xmax) * elem / N))
    phase_shift = np.array(phase_shift)

    y = np.array(muestreo)
    Y = fftpack.fft(y) / N
    Y = Y / phase_shift
    Y = fftpack.fftshift(Y)

    # NUT = 1
    # U = 1 / (N * T)
    u = np.array(u)
    u = u / (N * T)

    muestreo_k = []
    N_add = N_min
    while N_add < N_max + 1:
        muestreo_k.append(N_add)
        N_add += 1

    plt.figure(figsize=(9, 6))
    plt.stem(muestreo_k, Y.imag, 'b', markerfmt='bo', label="imag")
    plt.stem(muestreo_k, Y.real, 'g', markerfmt='go', label="real")
    plt.legend()
    plt.show()

    return Y

# Los siguientes parámetros resultan en una bastante buena representación gráfica:
# Descomentar para ver cada uno...
# DFT(fa, [-1, 1], 64)
# DFT(fb, [-1, 1], 64)
# DFT(fc, [-2, 2], 64)
# DFT(fd, [-2, 2], 64)
