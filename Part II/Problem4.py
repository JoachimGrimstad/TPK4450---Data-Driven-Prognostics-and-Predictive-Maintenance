"""
title:          Problem4
version:        1.0.0
fileName:       Problem4.py 
author:         Joachim Nilsen Grimstad
description:    Problem 4, semester work II, TPK–4450, Autumn 2020 @NTNU                                
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
df = pd.read_csv('monitoring.txt', sep=",", names = ['t', 'Y(t)'])                  # Imports the txt file as a nice table and names the data columns (df = dataframe).

# Least Square Estimation
df['yt'] = df['t'] * df['Y(t)']                                                             # Creates a new column in df called yt = t * Y(t)
df['t^2'] = df['t']**2                                                                      # Creates a new column in df called t^2 = t * t
a_hat = df['yt'].sum() / df['t^2'].sum()                                                    # Calculates the â
df['X(t)'] = a_hat * df['t']                                                                # Adds the X(t) column to the df
df['E(t)'] = df['Y(t)'] - df['X(t)']                                                        # Adds the E(t) column to the df

𝜇_L = df['E(t)'].mean()
𝜎_L = df['E(t)'].std(ddof=0)                                                                # Non-normalized standard deviation.

# Simulated trajectories
simulation_time = 120                                                                           # Simualte from t = 60 to simulation time. 
number_trajectories = 10000                                                                     # Number of trajectories to simulate.
number_trajectories_plotted = 10                                                                # Number of trajectories to plot.
trajectories = {}                                                                               # Dictionary of trajectories.
time = [i for i in range(60, simulation_time + 1, 1)]                                           # Generates the values for time.
trajectories['t'] = time                                                                        # Add time to the dictionary.

for i in range(number_trajectories):                                                            # Generates trajectories, for each i:
    trajectory = []                                                                             # Empty trajectory
    for t in time:                                                                              # For each t in time.
        if t == 60:                                                                             # If t = 60   
            trajectory.append(df['Y(t)'][len(df['Y(t)']) - 1])                                  # Adds the last data point of Y(t)
        else:
            E = np.random.normal(𝜇_L, 𝜎_L, size=1)                                              # Generates a random E ~ N(𝜇_L, 𝜎_L)
            trajectory.append(a_hat * t + E[0])                                                 # Appends a_hat * t + E[0] 
    trajectories[f'T_{i}(t)'] = trajectory                                                      # Add the trajectory T_i(t) to the dictionary
trajectories = pd.DataFrame.from_dict(trajectories)                                             # Convert trajectories from a dictionary to a df
trajectories['T_mean(t)'] = trajectories.drop('t', axis=1).apply(lambda x: x.mean(), axis=1)    # Adds a mean trajectory

# Plot
sns.set_style("whitegrid")                                                                                                                          # Sets style with grids.                                        
sns.scatterplot(data = df, x = 't', y = 'Y(t)', label = 'Y(t)')                                                                                     # Plots Y(t)
sns.lineplot(data = df, x = 't', y = 'X(t)', color = "green", label = '$X(t)$')                                                                     # Plots X(t)
for i in range(number_trajectories_plotted-1):
    sns.lineplot(data = trajectories, x = 't', y = f'T_{i}(t)', color = "Gray", lw = 0.5)                                                           # Plots the number of requested trajectories
sns.lineplot(data = trajectories, x = 't', y = f'T_{number_trajectories_plotted-1}(t)', color = "Gray", lw = 0.5, label = '$T_{i}(t)$')             # Plots last requested trajectory with label.
sns.lineplot(data = trajectories, x = 't', y = 'T_mean(t)', color = "Blue", label = '$T_{mean}(t)$')                                                # Plots T_mean(t)
plt.title('Condition at time t')                                                                                                                    # Sets title
plt.xlabel('Time [t]')                                                                                                                              # Sets X-axis label
plt.ylabel('Condition(t)')                                                                                                                          # Sets Y-axis label
plt.xlim(0, simulation_time)                                                                                                                        # Scales X-axis (min, max)
sns.lineplot(x = [i for i in range(simulation_time + 1)], y = [10 for i in range(simulation_time + 1 )], color = "Red", lw = 2, label = 'L')        # Makes L line
plt.axhline(y=0, lw=2, color='k')                                                                                                                   # Creates a "bold" x-axis
plt.show()                                                                                                                                          # Shows the plot