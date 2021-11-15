import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

ipl=pd.read_csv('matches.csv')
print(ipl.head())
print(ipl.shape)
win = np.sum(ipl['toss_winner']==ipl['winner'])
print(win)

