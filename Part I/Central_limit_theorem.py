"""
title:          Central Limit Theorem
version:        1.0.0
fileName:       Central_limit_theorem.py 
author:         Joachim Nilsen Grimstad
description:    Just a small script to illustrate the central limit theorem for a reflection during semesterwork I, problem a) in
                TPK4450 - Data Driven Prognostics and Predictive Maintenance                               
license:       GNU General Public License v3.0 https://www.gnu.org/licenses/gpl-3.0.en.html 
                
disclaimer:     Author takes no responsibility for any use other than authors own evaluation in courses at NTNU.
""" 

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Seed
np.random.seed(4450)

# Data Generation
def generate_uniform_data(sample_size, num_samples):
    data = []
    i = 0
    while i < num_samples:
        i += 1
        point = (np.random.rand(sample_size) * 100).mean()
        data.append(point)
    np.array(data)
    return data

def generate_exponential_data(sample_size, num_samples):
    data = []
    i = 0
    Lambda = 0.05
    scale = 1 / Lambda 
    while i < num_samples:
        i += 1
        point = np.random.exponential(scale, sample_size).mean()
        data.append(point)
    np.array(data)
    return data

# Figure
fig_a = plt.figure(figsize=(15,15)) # Creates a figure a
fig_a.suptitle('Underlying distribution: X ~ U(0 , 100)', fontsize=16)
ax1 = fig_a.add_subplot(1, 2, 1) # Creates a subplot ax1 on first half of the figure fig_a
ax1.set_title('Histogram')
ax1.set_ylabel('Frequency')
ax1.set_xlabel('X')
ax2 = fig_a.add_subplot(1, 2, 2) # Creates a subplot ax2 on second half of the figure fig_a
ax2.set_title('Probability Density Function using Kernel Density Estimation')
ax2.set_ylabel('Probability Density')
ax2.set_xlabel('X')


fig_b = plt.figure(figsize=(15,15)) # Creates a figure b
fig_b.suptitle('Underlying distribution: X ~ Exp(λ),  λ = 0.05', fontsize=16)
bx1 = fig_b.add_subplot(1, 2, 1) # Creates a subplot bx1 on first half of the figure fig_b
bx1.set_title('Histogram')
bx1.set_title('Histogram')
bx1.set_ylabel('Frequency')
bx2 = fig_b.add_subplot(1, 2, 2) # Creates a subplot bx2 on second half of the figure fig_b
bx2.set_title('Probability Density Function using Kernel Density Estimation')
bx2.set_ylabel('Probability Density')
bx2.set_xlabel('X')

# Uniform distribution:
uniform_data_n_1 = generate_uniform_data(1, 100000)
uniform_data_n_5 = generate_uniform_data(5, 20000)
uniform_data_n_10 = generate_uniform_data(10, 10000)
sns.distplot(uniform_data_n_1, ax = ax1, norm_hist = False, kde = False, color = 'blue', label = 'n = 1')
sns.distplot(uniform_data_n_5, ax = ax1, norm_hist = False, kde = False, color = 'green', label = 'n = 5')
sns.distplot(uniform_data_n_10, ax = ax1, norm_hist = False, kde = False, color = 'red', label = 'n = 10')
sns.distplot(uniform_data_n_1, ax = ax2, hist = False, color = 'blue', label = 'n = 1')
sns.distplot(uniform_data_n_5, ax = ax2, hist = False, color = 'green', label = 'n = 5')
sns.distplot(uniform_data_n_10, ax = ax2, hist = False, color = 'red', label = 'n = 10')

# Exponential distribution:
exponential_data_n_1 = generate_exponential_data(1, 100000)
exponential_data_n_5 = generate_exponential_data(5, 20000)
exponential_data_n_10 = generate_exponential_data(10, 10000)
sns.distplot(exponential_data_n_1, ax = bx1, norm_hist = False, kde = False, color = 'blue', label = 'n = 1')
sns.distplot(exponential_data_n_5, ax = bx1, norm_hist = False, kde = False, color = 'green', label = 'n = 5')
sns.distplot(exponential_data_n_10, ax = bx1, norm_hist = False, kde = False, color = 'purple', label = 'n = 25')
sns.distplot(exponential_data_n_1, ax = bx2, hist = False, color = 'blue', label = 'n = 1')
sns.distplot(exponential_data_n_5, ax = bx2, hist = False, color = 'green', label = 'n = 5')
sns.distplot(exponential_data_n_10, ax = bx2, hist = False, color = 'red', label = 'n = 10')

# Show plots
plt.show()

# Test
print(f'uniform n = 10, μ = {np.mean(uniform_data_n_10)} and σ = {np.std(uniform_data_n_10)}')
print(f'exponential n = 10, μ = {np.mean(exponential_data_n_10)} and σ = {np.std(exponential_data_n_10)}')
