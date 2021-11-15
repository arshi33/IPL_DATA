import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

ipl=pd.read_csv('matches.csv')
print(ipl.head())
print(ipl.shape)
print(ipl['player_of_match'].value_counts()[0:10])#top 10 player most played
#create bar plot
plt.figure(figsize=(8,5))
names = list(ipl['player_of_match'].value_counts().keys()[0:5])
values = list(ipl['player_of_match'].value_counts()[0:5])
plt.bar(names,values,color='g')
plt.xlabel('player_of_match')
plt.ylabel('values')
plt.title('player_of_match bar plot')
plt.show()
