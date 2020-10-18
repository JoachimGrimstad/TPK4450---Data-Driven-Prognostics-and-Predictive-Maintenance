"""
title:          Problem10b
version:        1.0.0
fileName:       Problem10b.py 
author:         Joachim Nilsen Grimstad
description:    Problem 10b, semester work II, TPK–4450, Autumn 2020 @NTNU                                
license:        GNU General Public License v3.0 https://www.gnu.org/licenses/gpl-3.0.en.html 
                
disclaimer:     Author takes no responsibility for any use other than authors own evaluation in courses at NTNU.
""" 

# Dependancies
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from math import exp, pi, sqrt

# Seed
np.random.seed(4450)                                                                        # Seeds the pseudo random generator.

# Import Data
df = pd.read_csv('monitoring.txt', sep=",", names = ['t', 'Y(t)'])                          # Imports the txt file as a nice table and names the data columns (df = dataframe).

# Wiener process
I = []
for i in range(len(df['Y(t)']) - 1):
    I.append(df['Y(t)'][i + 1] - df['Y(t)'][i])

df_I = {}
df_I['I'] = I
df_I = pd.DataFrame.from_dict(df_I)  

# MLE
𝜇_W = df_I['I'].mean()
𝜎_W = df_I['I'].std(ddof=0)

# Simulated trajectories
simulation_time = 250                                                                            # Simualte from t = 0 to simulation time. 
number_trajectories = 10000                                                                     # Number of trajectories to simulate.
number_trajectories_plotted = 10                                                               # Number of trajectories to plot.
trajectories = {}                                                                               # Dictionary of trajectories.
time = [i for i in range(60, simulation_time + 1, 1)]                                            # Generates the values for time.
trajectories['t'] = time                                                                        # Add time to the dictionary.
for i in range(0, number_trajectories):                                                         # Generates trajectories, for each i:
    trajectory = []                                                                             # Empty trajectory
    for t in time:                                                                              # For each t in time.
        if t == 60:                                                                              # If t = 0   
            trajectory.append(df['Y(t)'][len(df['Y(t)']) - 1])                                                    # Adds the first data point of Y(t)
        else:
            increment = np.random.normal(𝜇_W, 𝜎_W, size=1)                                      # Generates a random I ~ N(𝜇_W, 𝜎_W)
            trajectory.append(trajectory[t - 61] + increment[0])                                 # Appends I(t-1) + I(t) 
    trajectories[f'T_{i}(t)'] = trajectory                                                      # Add the trajectory T_i(t) to the dictionary
trajectories = pd.DataFrame.from_dict(trajectories)                                             # Convert trajectories from a dictionary to a df
trajectories['T_mean(t)'] = trajectories.drop('t', axis=1).apply(lambda x: x.mean(), axis=1)    # Adds a mean trajectory

# Threshold
threshold_times = []                                                                            # Empty list of times
for i in range(number_trajectories):                                                            # For all trajectories
    for point in trajectories[f'T_{i}(t)']:                                                     # For all points in a trajectory
        if point >= 10:                                                                         # If that point is larger or equal to 10
            index = trajectories.loc[trajectories[f'T_{i}(t)'] == point].index[0]               # Row index of point
            time_0 = trajectories['t'][index - 1]                                               # Time of previous point
            time_1 = trajectories['t'][index]                                                   # Time of point
            point_0 = trajectories[f'T_{i}(t)'][index - 1]                                      # Previous point        
            point_1 = point                                                                     # Point
            point_L = 10                                                                        # Threshold
            time_L = time_0 + ((time_1 - time_0) * ((point_L - point_0) / (point_1 - point_0))) # Linear Interpolation 
            threshold_times.append(time_L)                                                      # Append to threshold_times
            break                                                                               # Dont look for more points for this trajectory.
List_of_RULs = [time - 60 for time in threshold_times]                                          # deduct the current time to find RUL(t_j)
y_t_j = df['Y(t)'][len(df['Y(t)']) - 1]
𝜇_I = (10 - y_t_j) / 𝜇_W 
𝜆_I = ((10 - y_t_j / 𝜎_W))**2

def integrate_composite_trapezoidal_rule(func, lower_limit, upper_limit, n):                    # Numerical integration routine using composite_trapezoidal_rule 
    # Composite trapezodial rule                                                                # Copy paste from work in previous course TDT4127
    dx = (upper_limit - lower_limit) / n
    I = 0
    for k in range(0,n):
        step_lower_limit = lower_limit + (dx * k)
        step_upper_limit = lower_limit + (dx * (k + 1))
        I += (step_upper_limit - step_lower_limit) * ((func(step_lower_limit) + func(step_upper_limit)) / 2)
    return I

def func(t):
    return sqrt(𝜆_I/(2*pi*(t**3)))* exp(- 𝜆_I/(2*(𝜇_I**2))*(((t-𝜇_I)**2)/t))

Probability = integrate_composite_trapezoidal_rule(func, 0.00001, 34, 20) 
print(f'b) The probability is: {Probability}')
