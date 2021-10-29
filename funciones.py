import matplotlib.pyplot as plt
from math import cos, sin, exp, pi
import numpy as np
from numpy.core.function_base import linspace
import cmath

def fa(x):
    re = cos(np.pi * x)
    im = sin(np.pi * x)
    y = complex(re, im)
    return y

def fb(x):
    re = cos(np.pi * x)
    im = -sin(np.pi * x)
    y = complex(re, im)
    return y

# e^(-Pi*x^2)
def fc(x):
    # re = exp(-np.pi * (x ** 2))
    # y = complex(re, 0)
    y = cmath.exp(-np.pi * (x ** 2))
    return y

# e^(-Pi*(x^2+ix)) = e^(-Pi*x^2)*e^(-i*Pi*x) = e^(-Pi*x^2)*(cos(Pi*x)-i*sen(Pi*x))
def fd(x):
    # re = exp(-np.pi * (x ** 2)) * (cos(np.pi * x))
    # im = - exp(-np.pi * (x ** 2)) * sin(np.pi * x)
    # y = complex(re, im)
    y = cmath.exp(-np.pi * (x ** 2 + 1j * x))
    return y