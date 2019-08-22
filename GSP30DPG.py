import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

reader = csv.reader(open('game_recall.csv'))
spin_date_gameID = []
plt.figure()
plt.rcParams.update({'figure.max_open_warning': 0})
for List in reader:
    spin_date_gameID.append([List[0], List[1][0:11], int(List[41])])
df = pd.DataFrame(spin_date_gameID,columns=['spin', 'date', 'id'])
df['date'] = pd.to_datetime(df['date'])
df = df.groupby('id')
#result = df['date'].value_counts()
for name, group in df:
    group = group.reset_index(drop=True)
    result = {'spin': group['spin'],'date':group['date']}
    df_counts = pd.DataFrame(result)
    df_counts = df_counts['date'].value_counts()
    # means = df_counts.rolling(2).mean()
    df_counts.plot()
    #df_counts.plot()

    #group = group.reset_index(drop=True)
    #result = {'spin':group.}
    #counts = group['date'].values_counts()
    #print counts
plt.title('Game Spin per 30 Day')
plt.show()