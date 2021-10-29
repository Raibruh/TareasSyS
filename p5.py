from math import exp
import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack
import cmath
from rutiza import Rutiza
from simetra import Simetra

def intsinc(f, factor):
    N = len(f)