"""
title:          Task_b_5
version:        1.0.0
fileName:       Task_b_5.py 
author:         Joachim Nilsen Grimstad
description:    Just a small script to plot task a 3), semesterwork I, in
                TPK4450 - Data Driven Prognostics and Predictive Maintenance                               
license:        GNU General Public License v3.0 https://www.gnu.org/licenses/gpl-3.0.en.html 
                
disclaimer:     Author takes no responsibility for any use other than authors own evaluation in courses at NTNU.
""" 

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm
from math import sqrt, log


μ0 = 0
μ1 = 2
σ = 2
n = 10
lambda_NP = 1.22378284

def integral_limit():
    return (1/5) * log(lambda_NP) + 1

# Numerical integration:
β = norm.cdf(integral_limit(), μ1, σ/sqrt(n))

#
print(f'β = {β}')
