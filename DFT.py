import numpy as np
import matplotlib.pyplot as plt
from numpy.core.function_base import linspace
from rutiza import p
from scipy import fftpack
def DFT(sig, N):

    N_min = - N / 2
    N_max = N / 2 - 1
    N_add = N_min

    muestreo_n = []

    while N_add < N_max + 1:
        muestreo_n.append(N_add)
        N_add += 1

    y = np.array(sig)
    Y = fftpack.fft(y)
    Y = fftpack.fftshift(Y)

    muestreo_k = []
    N_add = N_min
    while N_add < N_max + 1:
        muestreo_k.append(N_add)
        N_add += 1

    return Y

P = DFT(p, 64)