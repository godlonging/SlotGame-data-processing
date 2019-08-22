import csv
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
gameID_bet_payout_date = []
reader = csv.reader(open('game_recall.csv'))
for List in reader:
    gameID_bet_payout_date.append([int(List[41]), int(List[5]), int(List[46]), List[1][0:11]])
df = pd.DataFrame(gameID_bet_payout_date, columns=['gameid', 'bet', 'payout', 'date'])
df['date'] = pd.to_datetime(df['date'])
df['RTP'] = df['payout']/df['bet']
#print df
df = df.groupby('gameid')
for name, group in df:
    group = group.groupby('date')
    tmp = []
    tmp_1 = []
    for sub_name, sub_group in group:
        sub_group = sub_group.reset_index(drop=True)
        result = sub_group['RTP'].mean()
        tmp.append([result])
        tmp_1.append([sub_name])
    plt.plot(tmp_1, tmp)

        #print avg_RTP
plt.title('Game RTP pre Day')
plt.show()
    #group = group.reset_index(drop=True)

