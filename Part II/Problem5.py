"""
title:          Problem5
version:        1.0.0
fileName:       Problem5.py 
author:         Joachim Nilsen Grimstad
description:    Problem 5, semester work II, TPK–4450, Autumn 2020 @NTNU                                
license:        GNU General Public License v3.0 https://www.gnu.org/licenses/gpl-3.0.en.html 
                
disclaimer:     Author takes no responsibility for any use other than authors own evaluation in courses at NTNU.
""" 

# Dependancies
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Seed
np.random.seed(4450)                                                                        # Seeds the pseudo random generator.

# Import Data
df = pd.read_csv('monitoring.txt', sep=",", names = ['t', 'Y(t)'])                          # Imports the txt file as a nice table and names the data columns (df = dataframe).

# Least Square Estimation
df['yt'] = df['t'] * df['Y(t)']                                                             # Creates a new column in df called yt = t * Y(t)
df['t^2'] = df['t']**2                                                                      # Creates a new column in df called t^2 = t * t
a_hat = df['yt'].sum() / df['t^2'].sum()                                                    # Calculates the â
df['X(t)'] = a_hat * df['t']                                                                # Adds the X(t) column to the df
df['E(t)'] = df['Y(t)'] - df['X(t)']                                                        # Adds the E(t) column to the df
𝜇_L = df['E(t)'].mean()                                                                     # Arithmetic mean.
𝜎_L = df['E(t)'].std(ddof=0)                                                                # Non-normalized standard deviation.

# Simulated trajectories
simulation_time = 250                                                                           # Simualte from t = 60 to simulation time. 
number_trajectories = 10000                                                                     # Number of trajectories to simulate.
number_trajectories_plotted = 10                                                                # Number of trajectories to plot.
trajectories = {}                                                                               # Dictionary of trajectories.
time = [i for i in range(60, simulation_time + 1, 1)]                                           # Generates the values for time.
trajectories['t'] = time                                                                        # Add time to the dictionary.
for i in range(number_trajectories):                                                            # Generates trajectories, for each i:
    trajectory = []                                                                             # Empty trajectory
    for t in time:                                                                              # For each t in time.
        if i == 60:                                                                             # If t = 60   
            trajectory.append(df['Y(t)'][len(df['Y(t)']) - 1])                                  # Adds the last data point of Y(t)
        else:
            E = np.random.normal(𝜇_L, 𝜎_L, size = 1)                                            # Generates a random E ~ N(𝜇_L, 𝜎_L)
            trajectory.append(a_hat * t + E[0])                                                 # Appends a_hat * t + E[0] 
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
RUL = [time - 60 for time in threshold_times]                                                   # deduct the current time to find RUL(t_j)

# Plot

sns.set_style("whitegrid")    
sns.distplot(RUL, norm_hist = False, kde = False, color = 'blue')                                                                                   # Sets style with grids.                                        
plt.title('Histogram')                                                                                                                              # Sets title
plt.ylabel('Frequency')                                                                                                                             # Sets X-axis label
plt.xlabel('$RUL(t)$')                                                                                                                              # Sets Y-axis label
plt.show()  

