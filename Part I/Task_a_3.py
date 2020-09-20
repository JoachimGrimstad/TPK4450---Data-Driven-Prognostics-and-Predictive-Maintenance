"""
title:          Task_a_3
version:        1.0.0
fileName:       Task_a_3.py 
author:         Joachim Nilsen Grimstad
description:    Just a small script to empirically count classifications for problem a 3), semesterwork I, in
                TPK4450 - Data Driven Prognostics and Predictive Maintenance                               
license:        GNU General Public License v3.0 https://www.gnu.org/licenses/gpl-3.0.en.html 
                
disclaimer:     Author takes no responsibility for any use other than authors own evaluation in courses at NTNU.
""" 

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from math import sqrt

# Seed
np.random.seed(4450)

# Parameters
μ = 0
σ = 2
n = 10
num_samples = 100
X_max = 1.04038935

# Samples
samples = np.random.normal(μ, σ / sqrt(n), num_samples)

# Counters
healthy = 0
false_alarms = 0

# Counter
for sample in samples:
    if sample >= X_max:
        false_alarms += 1
    else:
        healthy += 1

# Count
print(f'The number of healthy samples is {healthy}, while the number of false alarms is {false_alarms}')
print()
print(f'Prosentage wise, healthy = {healthy / num_samples} and false_alarms = {false_alarms / num_samples}')




