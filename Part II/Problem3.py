"""
title:          Problem3
version:        1.0.0
fileName:       Problem3.py 
author:         Joachim Nilsen Grimstad
description:    Problem 3, semester work II, TPK–4450, Autumn 2020 @NTNU                                
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
df['X(t)'] = a_hat * df['t']                                                                # Adds the X(t) column to the df
df['E(t)'] = df['Y(t)'] - df['X(t)']                                                        # Adds the E(t) column to the df

𝜇_L = df['E(t)'].mean()
𝜎_L = df['E(t)'].std(ddof=0)                                                                # Non-normalized standard deviation.
print(f'The arithmetic mean is: {𝜇_L} and the  statistical standard deviation is: {𝜎_L}')
