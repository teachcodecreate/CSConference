# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 16:00:11 2018

@author: lsorbara
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import gaussian_kde

def func(x):
    if 18 <= x < 25:
        return '18-25'
    elif 25 <= x < 30:
        return '25-30'
    elif 30 <= x < 35:
        return '30-35'
    elif 35 <= x < 40:
        return '35-40'
    elif 40 <= x < 45:
        return '40-45'
    elif 45 <= x < 50:
        return '45-50'
    elif 50 <= x < 55:
        return '50-55'
    elif 55 <= x < 60:
        return '55-60'
    elif 60 <= x < 65:
        return '60-65'
    elif 65 <= x < 70:
        return '65-70'
    elif 70 <= x < 75:
        return '70-75'
    elif 75 <= x < 80:
        return '75-80'
    elif 80 <= x < 85:
        return '80-85'
    elif 85 <= x < 90:
        return '85-90'    



plt.style.use('seaborn-white')

# real Boston Marathon Data - 2015
df15 = pd.read_csv('marathon_results_2015.csv')
df16 = pd.read_csv('marathon_results_2016.csv')
df17 = pd.read_csv('marathon_results_2017.csv')

dfa15 = df15['Age']
dfa16 = df16['Age']
dfa17 = df17['Age']

# look at the age distribution over the past 3 years
kwargs = dict(histtype='stepfilled',alpha=0.3,normed=True,bins=20)

plt.hist(dfa15, **kwargs, label='2015')
plt.hist(dfa16, **kwargs, label='2016')
plt.hist(dfa17, **kwargs, label='2017')
plt.title('Boston Marathon - Age Distribution')
plt.xlabel('Ages of Participants')
plt.ylabel('Normalized Frequency')
plt.legend(loc='upper right')


df15['Official Time'] = pd.to_timedelta(df15['Official Time']).astype('timedelta64[s]').astype(int)
df15['AgeGroup'] =  df['Age'].apply(func)

# fit an array of size [Ndim, Nsamples]
data = np.vstack([df15['Age'],df15['Official Time']])
kde = gaussian_kde(data)

# evaluate on a regular grid
xgrid = np.linspace(18,85, 40)
ygrid = np.linspace(7200,30000, 40)
Xgrid, Ygrid = np.meshgrid(xgrid, ygrid)
Z = kde.evaluate(np.vstack([Xgrid.ravel(), Ygrid.ravel()]))

# Plot the result as an image
plt.figure()
plt.imshow(Z.reshape(Xgrid.shape),
           origin='lower', aspect='auto',
           extent=[18,85,7200,30000],
           cmap='Blues')
cb = plt.colorbar()
cb.set_label("density")

plt.figure()
# Density Plot and Histogram of all arrival delays
sns.distplot(dfa15, hist=True, kde=True, 
             bins=65, color = 'darkblue', 
             hist_kws={'edgecolor':'black'},
             kde_kws={'linewidth': 4})
plt.title('Boston Marathon - Age Distribution')
plt.xlabel('Ages of Participants')
plt.ylabel('Normalized Frequency')


plt.figure()
df15.sort_values(by=['AgeGroup'])
sns.violinplot(x="AgeGroup", y="Official Time", hue="M/F",
               data=df15, palette="muted", split=True, order=['18-25','25-30', '30-35', '35-40', '40-45', '45-50', '50-55',
       '55-60', '60-65', '65-70', '70-75', '75-80', '80-85'])
plt.title('Boston Marathon - Finishing Time by Age Group')


