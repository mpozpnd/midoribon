#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
#
# Author:   Graphium
# URL:      http://tehutehu.com
# License:  MIT License
# Created:  2016-06-28
#
import numpy as np
import pystan
from matplotlib import pyplot as plt

X = np.loadtxt("./data10.csv", dtype=np.int)

N = X.shape[0]

stan_data = {'N': N, 'Y': X}

fit = pystan.stan(file='model10.stan', data=stan_data, iter=10000, chains=1)


fit.plot()
plt.show()
