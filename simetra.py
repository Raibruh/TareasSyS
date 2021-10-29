import numpy as np
import matplotlib.pyplot as plt
from numpy.core.function_base import linspace
from scipy import fftpack
from DFT import P

# función "simetra", recibe como parámetros p, que corresponde a la señal de entrada como
# array y tipo, que corresponde al tipo de simetría que se aplica
def Simetra(p, tipo):
    # f = (p 0 p(64:-1:2)), señal real par de largo 128
    if tipo == 1:
        largo = 128
        c = []
        for value in p:
            c.append(value)
        c.append(0)
        for value in p[::-1]:
            c.append(value)
        c = c[:-1]
        x = list(range(-64, 64))

    # f = (p 0 p(64:-1:2)) + i(p 0 -p(64:-1:2)), señal hermitiana de largo 128
    if tipo == 2:
        largo = 128
        c = []
        for value in p:
            c.append(value + 1j * value)
        c.append(0)
        for value in p[::-1]:
            c.append(value + 1j * -value)
        c = c[:-1]
        x = list(range(-64, 64))

    # f = i(p p p p), señal imaginaria periódica de largo 256
    if tipo == 3:
        largo = 256
        c = []
        for i in range(4):
            for value in p:
                c.append(1j * value)
        x = list(range(-128, 128))

    # f = (p 0 -p(64:-1:2)), señal real impar de largo 128
    if tipo == 4:
        largo = 128
        c = []
        for value in p:
            c.append(value)
        c.append(0)
        for value in p[::-1]:
            c.append(-value)
        c = c[:-1]

    # f = (ip 0 ip(64:-1:2)), señal imaginaria par de largo 128
    if tipo == 5:
        largo = 128
        c = []
        for value in p:
            c.append(1j * value)
        c.append(0)
        for value in p[::-1]:
            c.append(1j * value)
        c = c[:-1]
        x = list(range(-64, 64))

    # f = (ip 0 -ip(64:-1:2)), señal imaginaria impar de largo 128
    if tipo == 6:
        largo = 128
        c = []
        for value in p:
            c.append(1j * value)
        c.append(0)
        for value in p[::-1]:
            c.append(-1j * value)
        c = c[:-1]
        x = list(range(-64, 64))

    # f = (p 0 p(64:-1:2)) + i(p 0 p(64:-1:2)), señal compleja par de largo 128
    if tipo == 7:
        largo = 128
        c = []
        for value in p:
            c.append(value + 1j * value)
        c.append(0)
        for value in p[::-1]:
            c.append(value + 1j * value)
        c = c[:-1]
        x = list(range(-64, 64))

    # f = (p 0 p(64:-1:2)) + -i(p 0 p(64:-1:2)), señal compleja impar de largo 128
    if tipo == 8:
        largo = 128
        c = []
        for value in p:
            c.append(value - 1j * value)
        c.append(0)
        for value in p[::-1]:
            c.append(value - 1j * value)
        c = c[:-1]
        x = list(range(-64, 64))

    # P es la DFT de p importada de un módulo auxiliar para no tener errores de importación.
    # f = (P 0 P(64:-1:2)), señal real par de largo 128 (con P transformada de Fourier de p)
    if tipo == 9:
        largo = 128
        c = []
        for value in P:
            c.append(value)
        c.append(0)
        for value in P[::-1]:
            c.append(value)
        c = c[:-1]
        x = list(range(-64, 64))

    # f = (P 0 -P(64:-1:2)), señal real impar de largo 128
    if tipo == 10:
        largo = 128
        c = []
        for value in P:
            c.append(value)
        c.append(0)
        for value in P[::-1]:
            c.append(-value)
        c = c[:-1]

    # f = (iP 0 iP(64:-1:2)), señal imaginaria par de largo 128
    if tipo == 11:
        largo = 128
        c = []
        for value in P:
            c.append(1j * value)
        c.append(0)
        for value in P[::-1]:
            c.append(1j * value)
        c = c[:-1]
        x = list(range(-64, 64))

    # f = (iP 0 -iP(64:-1:2)), señal imaginaria impar de largo 128
    if tipo == 12:
        largo = 128
        c = []
        for value in P:
            c.append(1j * value)
        c.append(0)
        for value in P[::-1]:
            c.append(-1j * value)
        c = c[:-1]
        x = list(range(-64, 64))

    f = np.array(c)
    return f


def plotea(sig, tipo):

    f, x = Simetra(sig, tipo)
    plt.figure(figsize=(12, 4))

    for i in range(len(x)):
        x[i] = 0.1 * x[i]

    plt.plot(x, f.imag, label="imag")
    plt.plot(x, f.real, label="real", linestyle='dashed')
    plt.grid()
    plt.legend()
    plt.show()

