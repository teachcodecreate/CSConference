# CS Education Conference
# Data Visualizations Functions

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from scipy.interpolate import spline

def scatterplot(x_data, y_data, x_label="", y_label="", title="", color = "r", yscale_log=False):

    # Create the plot object
    _, ax = plt.subplots()

    # Plot the data, set the size (s), color and transparency (alpha)
    # of the points
    ax.scatter(x_data, y_data, s = 10, c = color, alpha = 0.75)

    if yscale_log == True:
        ax.set_yscale('log')

    # Label the axes and provide a title
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    
def lineplot(fig,x_data, y_data, color="r", x_label="", y_label="", title=""):
    # Create the plot object
    ax = fig.add_subplot(111)

    # Plot the best fit line, set the linewidth (lw), color and
    # transparency (alpha) of the line
    ax.plot(x_data, y_data, lw = 2, color = color, alpha = 1)

    # Label the axes and provide a title
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    return ax

def histogram(data, n_bins, cumulative=False, x_label = "", y_label = "", title = ""):
    _, ax = plt.subplots()
    ax.hist(data, n_bins = n_bins, cumulative = cumulative, color = '#539caf')
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.set_title(title)
    
def barplot(x_data, y_data, x_label="", y_label="", title=""):
    _, ax = plt.subplots()
    # Draw bars, position them in the center of the tick mark on the x-axis
    ax.bar(x_data, y_data, color = '#539caf', align = 'center')
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.set_title(title)
    
def smooth(fig,data,color="r",xlab='',ylab='',title=''):
    # smooth the line
    x = []
    y = []
    for index,row in data.iterrows():
        x.append(row['Age'])
        y.append(row['AvgMakesPerGame'])
    
    x_sm = np.array(x)
    x_smooth = np.linspace(x_sm.min(), x_sm.max(),200)
    y_smooth = spline(x,y,x_smooth)
    lineplot(fig,x_smooth,y_smooth,color,xlab,ylab,title)
    
def bubble(fig,subnum,x,y,size,miny,maxy, xlab='',ylab='',title='',color='R',axis=True):
    ax = fig.add_subplot(subnum)
    ax.scatter(x,y,s=size,edgecolor='w',c=color)
    if not axis:
        ax.set_axis_off()
    ax.set_xlabel(xlab)
    ax.set_ylabel(ylab)
    ax.set_title(title)
    ax.set_ylim(miny,maxy)
    return ax
    
# Look at the number of shots taken at different points within the shot clock
currentPath = os.path.abspath(os.path.dirname(__file__))
#path = currentPath + "\\Vollyball OLOL.txt"
#path = currentPath + "\\St Marys Oct 2.txt"
path = currentPath + "\\volleyball_data_full_raw.csv"
data = pd.read_csv(path)


fig = plt.figure()
ax1 = fig.add_subplot(111)
First = data[data.Set==1]
Second = data[data.Set==2]
Third = data[data.Set==3]
Fourth = data[data.Set==4]

ax1.scatter(First.X, First.Y, s=10, c='b', marker="s", label='first')
ax1.scatter(Second.X, Second.Y, s=10, c='r', marker="o", label='second')
ax1.scatter(Third.X, Third.Y,s=10,c='g', marker="p", label='third')
ax1.scatter(Fourth.X,Fourth.Y,s=10,c='y',marker="*",label='fourth')
plt.plot([0,227], [156, 156], 'k-', lw=2)
plt.plot([0,227], [-156, -156], 'k-', lw=2)
plt.plot([0,0], [156, -156], 'k-', lw=2)
plt.plot([227,227], [156, -156], 'k-', lw=2)
plt.plot([76,76],[156,-156],'k-',lw=2)
plt.legend(loc='lower right');
plt.show()
#scatterplot(data.X, data.Y,'Court Length', 'Court Net',data.Play)


plt.hist2d(data.X, data.Y, bins=(10, 14), cmap=plt.cm.jet)
plt.xlim(-10,250)
plt.plot([4,227], [156, 156], 'w-', lw=2)
plt.plot([4,227], [-156, -156], 'w-', lw=2)
plt.plot([4,4], [156, -156], 'w-', lw=2)
plt.plot([227,227], [156, -156], 'w-', lw=2)
plt.plot([76,76],[156,-156],'w-',lw=2)
plt.legend(loc='lower right');
cbar = plt.colorbar()
cbar.ax.set_ylabel('Counts')




