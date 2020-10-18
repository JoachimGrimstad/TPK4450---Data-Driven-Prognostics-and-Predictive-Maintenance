"""
title:          Problem2
version:        1.0.0
fileName:       Problem2.py 
author:         Joachim Nilsen Grimstad
description:    Problem 2, semester work II, TPK–4450, Autumn 2020 @NTNU                                
license:        GNU General Public License v3.0 https://www.gnu.org/licenses/gpl-3.0.en.html 
                
disclaimer:     Author takes no responsibility for any use other than authors own evaluation in courses at NTNU.
""" 

# Dependancies
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import Data
df = pd.read_csv('monitoring.txt', sep=",", names = ['t', 'Y(t)'])                  # Imports the txt file as a nice table and names the data columns (df = dataframe).

# Least Square Estimation
df['yt'] = df['t'] * df['Y(t)']                                                             # Creates a new column in df called yt = t * Y(t)
df['t^2'] = df['t']**2                                                                      # Creates a new column in df called t^2 = t * t
a_hat = df['yt'].sum() / df['t^2'].sum()                                                    # Calculates the â
print(f'The â is estimated to: {a_hat}')                                                    # Print result
df['X(t)'] = a_hat * df['t']                                                                # Adds the X(t) column to the df

# Least Square Estimation – with error mitigation and intercept
N = len(df.index)                                                                                                    # Gets the number of N datapoints
a_hat = ((N * df['yt'].sum()) - df['t'].sum() * df['Y(t)'].sum()) / ((N * df['t^2'].sum()) - (df['t'].sum()**2))     # Calculates the â.
b_hat = (df['Y(t)'].sum() - (a_hat * df['t'].sum())) / N                                                             # Calculates the b̂.
print(f'The â is estimated to: {a_hat} and b̂ is esttimated to: {b_hat}')                                             # Print result
df['X_improved(t)'] = a_hat * df['t'] + b_hat                                                                        # Adds the X_improved(t) column to the df                                          

# Plot
sns.set_style("whitegrid")                                                                              # Sets style with grids.                                        
sns.scatterplot(data = df, x = 't', y = 'Y(t)', label = 'Y(t)')                                         # Plots Y(t)
sns.lineplot(data = df, x = 't', y = 'X(t)', color = "green", label = '$X(t)$')                         # Plots X(t)
sns.lineplot(data = df, x = 't', y = 'X_improved(t)', color = "red", label = '$X_{improved}(t)$')       # Plots X_improved(t)
plt.title('Condition at time t')                                                                        # Sets title
plt.xlabel('Time [t]')                                                                                  # Sets X-axis label
plt.ylabel('Condition(t)')                                                                              # Sets Y-axis label
plt.xlim(0, 60)                                                                                         # Scales X-axis (min, max)
plt.axhline(y=0, lw=2, color='k')                                                                       # Creates a "bold" x-axis
plt.show()                                                                                              # Shows the plot
