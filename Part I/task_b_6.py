"""
title:          Task_b_6
version:        1.0.0
fileName:       Task_b_6.py 
author:         Joachim Nilsen Grimstad
description:    Just a small script to plot task a 3), semesterwork I, in
                TPK4450 - Data Driven Prognostics and Predictive Maintenance                               
license:        GNU General Public License v3.0 https://www.gnu.org/licenses/gpl-3.0.en.html 
                
disclaimer:     Author takes no responsibility for any use other than authors own evaluation in courses at NTNU.
""" 

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from math import sqrt, log

μ0 = 0
μ1 = 2
σ = 2
n = 10

alpha = np.zeros(1000)
beta = np.zeros(1000)
lambda_vector = np.linspace(1e-10, 4, 1000)

def integral_limit(i):
    return (1/5) * log(lambda_vector[i]) + 1

for i in range(len(alpha)):
    alpha[i] = 1 - norm.cdf(integral_limit(i), μ0, σ/sqrt(n))
    beta[i] = norm.cdf(integral_limit(i), μ1, σ/sqrt(n))

plt.plot(lambda_vector, alpha, color = 'blue', label = 'False alarm')
plt.plot(lambda_vector, beta, color = 'red', label = 'Non-detection')
plt.xlabel('$λ_{NP}$')
plt.ylabel('Probability')
plt.ylim(0, 0.2)
plt.legend()
plt.show()