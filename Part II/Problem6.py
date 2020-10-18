"""
title:          Problem6
version:        1.0.0
fileName:       Problem6.py 
author:         Joachim Nilsen Grimstad
description:    Problem 6, semester work II, TPK–4450, Autumn 2020 @NTNU                                
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

# Wiener process
I = []
for i in range(len(df['Y(t)']) - 1):
    I.append(df['Y(t)'][i + 1] - df['Y(t)'][i])

df_I = {}
df_I['I'] = I
df_I = pd.DataFrame.from_dict(df_I)  


# Plot
sns.set_style("whitegrid")                                                                                                            # Sets style with grids. 
sns.distplot(df_I['I'], kde = True, color = 'blue')                                                                                   # Plot Histogram with kde.                                        
plt.title('Histogram')                                                                                                                # Sets title
plt.ylabel('Frequency')                                                                                                               # Sets X-axis label
plt.xlabel('I')                                                                                                                       # Sets Y-axis label
plt.show()  

# MLE
𝜇_W = df_I['I'].mean()
𝜎_W = df_I['I'].std(ddof=0)
print(f'The arithmetic mean is: {𝜇_W} and the  statistical standard deviation is: {𝜎_W}')

# Simulated trajectories
simulation_time = 60                                                                            # Simualte from t = 0 to simulation time. 
number_trajectories = 10000                                                                     # Number of trajectories to simulate.
number_trajectories_plotted = 100                                                               # Number of trajectories to plot.
trajectories = {}                                                                               # Dictionary of trajectories.
time = [i for i in range(0, simulation_time + 1, 1)]                                            # Generates the values for time.
trajectories['t'] = time                                                                        # Add time to the dictionary.
for i in range(0, number_trajectories):                                                         # Generates trajectories, for each i:
    trajectory = []                                                                             # Empty trajectory
    for t in time:                                                                              # For each t in time.
        if t == 0:                                                                              # If t = 0   
            trajectory.append(df['Y(t)'][0])                                                    # Adds the first data point of Y(t)
        else:
            increment = np.random.normal(𝜇_W, 𝜎_W, size=1)                                      # Generates a random I ~ N(𝜇_W, 𝜎_W)
            trajectory.append(trajectory[t - 1] + increment[0])                                 # Appends I(t-1) + I(t) 
    trajectories[f'T_{i}(t)'] = trajectory                                                      # Add the trajectory T_i(t) to the dictionary
trajectories = pd.DataFrame.from_dict(trajectories)                                             # Convert trajectories from a dictionary to a df
trajectories['T_mean(t)'] = trajectories.drop('t', axis=1).apply(lambda x: x.mean(), axis=1)    # Adds a mean trajectory

# Plot
sns.set_style("whitegrid")                                                                                                                          # Sets style with grids.                                                                                                           # Plots X(t)
for i in range(number_trajectories_plotted -  1):
    sns.lineplot(data = trajectories, x = 't', y = f'T_{i}(t)', color = "Gray", lw = 0.5)                                                           # Plots the number of requested trajectories
sns.lineplot(data = trajectories, x = 't', y = f'T_{number_trajectories_plotted - 1}(t)', color = "Gray", lw = 0.5, label = '$T_{i}(t)$')           # Plots last requested trajectory with label.
sns.lineplot(data = trajectories, x = 't', y = 'T_mean(t)', color = "Blue", label = '$T_{mean}(t)$')                                                # Plots T_mean(t)
sns.lineplot(data = df, x = 't', y = 'Y(t)', label = 'Y(t)', color = 'Red')                                                                         # Plots Y(t)
plt.title('Condition at time t')                                                                                                                    # Sets title
plt.xlabel('Time [t]')                                                                                                                              # Sets X-axis label
plt.ylabel('Condition(t)')                                                                                                                          # Sets Y-axis label
plt.xlim(0, simulation_time)                                                                                                                        # Scales X-axis (min, max)
plt.axhline(y=0, lw=2, color='k')                                                                                                                   # Creates a "bold" x-axis
plt.show()                                                                                                                                          # Shows the plot
