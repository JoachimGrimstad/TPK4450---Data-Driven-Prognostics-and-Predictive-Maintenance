"""
title:          Task_b_4
version:        1.0.0
fileName:       Task_b_4.py 
author:         Joachim Nilsen Grimstad
description:    Just a small script to plot task a 3), semesterwork I, in
                TPK4450 - Data Driven Prognostics and Predictive Maintenance                               
license:        GNU General Public License v3.0 https://www.gnu.org/licenses/gpl-3.0.en.html 
                
disclaimer:     Author takes no responsibility for any use other than authors own evaluation in courses at NTNU.
""" 

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from math import sqrt
from scipy.stats import norm

# Seed
np.random.seed(4450)

# Parameters
μ0 = 0
μ1 = 2
σ = 2
n = 10
num_samples = 100
X_max = 1.04038935

# Samples
healthy_samples = np.random.normal(μ0, σ / sqrt(n), num_samples)
faulty_samples = np.random.normal(μ1, σ / sqrt(n), num_samples)

# Plot
sns.distplot(healthy_samples, hist = False, kde = True, label = 'Healthy', color = 'blue')
sns.distplot(faulty_samples, hist = False, kde = True, label = 'Faulty', color = 'green')
line_x = [1.04038935, 1.04038935] # x-coordinates for max limit
line_y = [0, 0.8] # y-coordinates for max limit
plt.plot(line_x, line_y, label = '$\overline{X}_{max}$', color = 'red') # plot limit
plt.xlabel('$\overline{X}_{i}$')
plt.ylabel('Probability Density')
plt.legend()
plt.show()

# Counters
false_alarms = 0
non_detected = 0

for index in range(len(healthy_samples)):
    if healthy_samples[index] >= X_max:
        false_alarms += 1
    if faulty_samples[index] < X_max:
        non_detected += 1

# Count
print(f'The number of false alarms is {false_alarms}, while the number if non detected faults is {non_detected}')
