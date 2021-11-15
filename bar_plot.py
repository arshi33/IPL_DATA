import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

ipl=pd.read_csv('matches.csv')
print(ipl.head())
print(ipl.shape)
print(ipl['winner'].value_counts()[0:10])#top 10 player most played
#create bar plot
names = ipl['winner'].value_counts().keys()[0:3]
values = ipl['winner'].value_counts()[0:3]
plt.figure(figsize=(7,5))
plt.bar(names,values,color=['g','r','b','y','y'])
plt.show()