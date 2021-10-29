from math import exp
import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack
import cmath
from rutiza import Rutiza
from simetra import Simetra

def intsinc(f, factor):
    N = len(f)
    muestreo = []
    m_sinc = np.sinc(factor * f)
    for i in range(N):
        muestreo.append(np.convolve(f[i:N], m_sinc))

    g = []
    for lista in muestreo:
        for elem in lista:
            g.append(elem)

    return g
