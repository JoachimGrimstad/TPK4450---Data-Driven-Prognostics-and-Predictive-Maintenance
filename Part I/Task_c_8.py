"""
title:          Task_c_8
version:        1.0.0
fileName:       Task_c_8.py 
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
import seaborn as sns

np.random.seed(4450)

samples = []
μ0 = 0
σ = 2
n = 10
X_max = 1.04038935
μ_i = np.linspace(μ0,σ,21)
for μ in μ_i:
    samples.append(np.random.normal(μ, σ, n).mean())

# Classifications
classification = []

#Classification
for sample in samples:
    if sample >= X_max:
        classification.append(1)
    else:
        classification.append(0)
shift = np.linspace(0,20,21)

color_palatte = {1: 'red', 0: 'blue'}
sns.scatterplot(x = shift, y = classification, hue = classification, palette = color_palatte)
plt.legend([],[], frameon=False)
plt.xlabel('Shift (time)')
plt.ylabel('Classification')
plt.show()