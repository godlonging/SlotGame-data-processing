import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

reader = csv.reader(open('game_recall.csv'))
PlayerID_date_gameID = []
for List in reader:
    PlayerID_date_gameID.append([List[47], List[1][0:11], int(List[41])])

df = pd.DataFrame(PlayerID_date_gameID, columns=['playerid', 'date', 'gameid'])
df['date'] = pd.to_datetime(df['date'])
df = df.groupby('gameid')
for name, group in df:
    group = group.reset_index(drop=True)
    result = {'playerid': group['playerid'],'date':group['date']}
    df_counts = pd.DataFrame(result)
    df_counts = df_counts.drop_duplicates(keep='first', inplace=False)
    df_counts = df_counts['date'].value_counts()
    df_counts.plot()
plt.title('Game Player per 30 Day')
plt.show()
