from math import exp
import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack
import cmath
from rutiza import Rutiza
from simetra import Simetra

# Se define una función DFT, pero esta vez no hacemos el shift, ya que no es necesario
# el desplazamiento de la función...
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

    plt.figure(figsize=(9, 6))
    plt.stem(muestreo_k, Y.imag, 'b', markerfmt='bo', label="imag")
    plt.stem(muestreo_k, Y.real, 'g', markerfmt='go', label="real")
    plt.legend()
    plt.show()

    return Y

# Se realizan todas las funciones (rutiza + las distinas simetrías) y se saca su DFT:
rut = np.array([2, 0, 8, 0, 0, 3, 6, 3])
sig_rut = Rutiza(rut)
sig_sim_1 = Simetra(sig_rut, 1)
sig_sim_2 = Simetra(sig_rut, 2)
sig_sim_3 = Simetra(sig_rut, 3)
sig_sim_4 = Simetra(sig_rut, 4)
sig_sim_5 = Simetra(sig_rut, 5)
sig_sim_6 = Simetra(sig_rut, 6)
sig_sim_7 = Simetra(sig_rut, 7)
sig_sim_8 = Simetra(sig_rut, 8)
sig_sim_9 = Simetra(sig_rut, 9)
sig_sim_10 = Simetra(sig_rut, 10)
sig_sim_11 = Simetra(sig_rut, 11)
sig_sim_12 = Simetra(sig_rut, 12)
# Descomentar para ver cada una
# DFT(sig_rut, 64)
# DFT(sig_sim_1, len(sig_sim_1))
# DFT(sig_sim_2, len(sig_sim_2))
# DFT(sig_sim_3, len(sig_sim_3))
# DFT(sig_sim_4, len(sig_sim_4))
# DFT(sig_sim_5, len(sig_sim_5))
# DFT(sig_sim_6, len(sig_sim_6))
# DFT(sig_sim_7, len(sig_sim_7))
# DFT(sig_sim_8, len(sig_sim_8))
# DFT(sig_sim_9, len(sig_sim_9))
# DFT(sig_sim_10, len(sig_sim_10))
# DFT(sig_sim_11, len(sig_sim_11))
# DFT(sig_sim_12, len(sig_sim_12))
