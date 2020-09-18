"""
title:          Task_a_2
version:        1.0.0
fileName:       Task_a_2.py 
author:         Joachim Nilsen Grimstad
description:    Just a small script to plot task a 2), semesterwork I, in
                TPK4450 - Data Driven Prognostics and Predictive Maintenance                               
license:        GNU General Public License v3.0 https://www.gnu.org/licenses/gpl-3.0.en.html 
                
disclaimer:     Author takes no responsibility for any use other than authors own evaluation in courses at NTNU.
""" 

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from math import sqrt
from scipy.stats import norm

μ = 0
σ = 2
n = 10

domain = np.linspace(-3, 3, 10000) # Make a domain (x-values) 
data = norm.pdf(domain, μ, σ / sqrt(n)) # y-points for the normal distribution in the domain. 
line_x = [1.04038935, 1.04038935] # x-coordinates for max limit
line_y = [0, 0.8] # y-coordinates for max limit
plt.plot(domain, data, label = 'PDF($\overline{X}$)') # Plot PDF
plt.plot(line_x, line_y, label = '$\overline{X}_{max}$') # plot limit
plt.ylim(0, 0.7) # scale plot y-direction
plt.xlim(-3, 3)  # scale plot x-direction
plt.xlabel('$\overline{X}$') # x-axis label
plt.ylabel('Probability Density')   # y-axis label
plt.legend() # show legend
plt.show() # display plot
