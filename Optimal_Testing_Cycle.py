import numpy as np
import matplotlib.pyplot as plt
import random
import time
import math
import sys
# sys.path.append(r"D:\Research\COVID-19 project\101920")
import closed_form_A2_approximate_10 as cf
import pool_simulation as ps
import Testing_cycle_simulation as tcs
import numpy.random as npr
import os

import copy
from scipy.stats import norm
from scipy.stats import binom

Gamma = np.load('F_N_d_round.npy')
Eta = np.load('Eta_N_d_round.npy')
Theta = np.load('Theta_N_d_round.npy')
Psi = np.load('Psi_N_d_round.npy')


class Individual(object):
    def __init__(self, ID=0, pos=0, tested=0):
        self.ID = ID
        self.pos = pos
        self.tested = tested


def CRN(N, p, iter_time=100, seed=123456):
    np.random.seed(seed)
    return [np.random.binomial(N, p) for a in range(iter_time)]

def OTCL(total_length, T_total, C, V_0, alpha, out_rate):
    t=0
    while(1):
        print('t=',t)
        t = t + 1
        fp, avgs, avgt, avgrq, avgwq, avgfn = tcs.TCS(total_length, t, T_total, C, V_0, alpha, out_rate)
        if fp != -1:
            opt_t = t
            return opt_t, fp, avgs, avgt, avgrq, avgwq, avgfn
        if t == 30:
            return -1,-1,-1,-1,-1,-1,-1

#x1,x2,x3,x4,x5,x6,x7 = OTCL(14,10000,300,0.001,0.2,0.0005)
#print(x1)

