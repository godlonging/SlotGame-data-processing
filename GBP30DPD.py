import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

reader = csv.reader(open('game_recall.csv'))
gameID_bet_date = []
for List in reader:
    gameID_bet_date.append([int(List[41]), int(List[5]), List[1][0:11]])
df = pd.DataFrame(gameID_bet_date, columns=['gameid', 'bet', 'date'])
df['date'] = pd.to_datetime(df['date'])
df = df.groupby(['gameid'])
for name, group in df:
    group = group.groupby(['date'])
    for sub_name,sub_group in group:
        print sub_group
        result = group['bet'].sum()
        #print result
        result.plot()
plt.title('Game Bet pre 30 Day')
plt.show()