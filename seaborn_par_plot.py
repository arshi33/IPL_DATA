import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

ipl=pd.read_csv('matches.csv')
print(ipl.head())
print(ipl.shape)
sns.pairplot(ipl,hue='result')
plt.show()