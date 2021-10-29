from scipy.interpolate import interpolate
import numpy as np
from scipy import fftpack
def Rutiza(d):
    # d vector de 8 dígitos
    d = np.sort(d)[::-1]
    y0 = np.linspace(d[0], d[1], 9)
    y0 = y0[1:8]
    y1 = np.linspace(d[1], d[2], 9)
    y1 = y1[1:8]
    y2 = np.linspace(d[2], d[3], 9)
    y2 = y2[1:8]
    y3 = np.linspace(d[3], d[4], 9)
    y3 = y3[1:8]
    y4 = np.linspace(d[4], d[5], 9)
    y4 = y4[1:8]
    y5 = np.linspace(d[5], d[6], 9)
    y5 = y5[1:8]
    y6 = np.linspace(d[6], d[7], 9)
    y6 = y6[1:8]
    y7 = np.array([d[7], d[7], d[7], d[7], d[7], d[7], d[7]])

    y = np.concatenate((np.array([d[0]]), y0, np.array([d[1]]), y1, np.array([d[2]]),
                        y2, np.array([d[3]]), y3, np.array([d[4]]), y4, np.array([d[5]]),
                        y5, np.array([d[6]]), y6, np.array([d[7]]), y7))

    return y

vector = np.array([2, 0, 8, 0, 0, 3, 6, 3])
p = Rutiza(vector)
# print(p)
# print(len(p))
