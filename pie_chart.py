import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

ipl=pd.read_csv('matches.csv')
print(ipl.head())
print(ipl.shape)
bating_first =ipl[ipl['result']=='runs']
print(bating_first['winner'].value_counts())
names = bating_first['winner'].value_counts().keys()[0:10]
values = bating_first['winner'].value_counts()[0:10]
plt.figure(figsize=(7,7))
plt.pie(values,labels=names,autopct='%0.1f%%')
plt.show()