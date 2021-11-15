import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

ipl=pd.read_csv('matches.csv')
print(ipl.head())
print(ipl.shape)
win_by_wkt = ipl[ipl['result']=='wickets']
print(win_by_wkt['winner'].value_counts())
#plot  pie chart

plt.figure(figsize=(7.5,7.5))
names = win_by_wkt['winner'].value_counts().keys()
values = win_by_wkt['winner'].value_counts()
plt.pie(values,labels=names,autopct='%0.2f%%')
plt.show()