"""
title:          Normal Distribution Sample
version:        1.0.0
fileName:       Normalsample_mean.py 
author:         Joachim Nilsen Grimstad
description:    Just a small script to illustrate how the standard deviation decreases for sample means. Reflection during semesterwork I, problem a) in
                TPK4450 - Data Driven Prognostics and Predictive Maintenance                               
license:       GNU General Public License v3.0 https://www.gnu.org/licenses/gpl-3.0.en.html 
                
disclaimer:     Author takes no responsibility for any use other than authors own evaluation in courses at NTNU.
""" 

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(4450)

def generate_normal_data(sample_size, num_samples):
    data = []
    i = 0
    while i < num_samples:
        i += 1
        point = np.random.normal(0, 1, sample_size).mean()
        data.append(point)
    np.array(data)
    return data

# Figures
fig_a = plt.figure(figsize=(15,15)) # Creates a figure a
ax1 = fig_a.add_subplot(1, 2, 1) # Creates a subplot ax1 on first half of the figure fig_a
ax1.set_title('Histogram')
ax1.set_ylabel('Frequency')
ax1.set_xlabel('X')
ax2 = fig_a.add_subplot(1, 2, 2) # Creates a subplot ax2 on second half of the figure fig_a
ax2.set_title('Probability Density Function using Kernel Density Estimation')
ax2.set_ylabel('Probability Density')
ax2.set_xlabel('X')

# normal distribution plots
normal_data_n_1 = generate_normal_data(1, 100000)
normal_data_n_5 = generate_normal_data(5, 20000)
normal_data_n_10 = generate_normal_data(10, 10000)
sns.distplot(normal_data_n_1, ax = ax1, norm_hist = False, kde = False, color = 'blue', label = 'n = 1')
sns.distplot(normal_data_n_5, ax = ax1, norm_hist = False, kde = False, color = 'green', label = 'n = 5')
sns.distplot(normal_data_n_10, ax = ax1, norm_hist = False, kde = False, color = 'red', label = 'n = 10')
sns.kdeplot(normal_data_n_1, ax = ax2, color = 'blue', label = 'n = 1')
sns.kdeplot(normal_data_n_5, ax = ax2, color = 'green', label = 'n = 5')
sns.kdeplot(normal_data_n_10, ax = ax2, color = 'red', label = 'n = 10')
plt.show()
