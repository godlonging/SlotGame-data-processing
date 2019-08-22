import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

reader = csv.reader(open('game_recall.csv'))
bet_payout_id = []
labels = []
for List in reader:
    bet_payout_id.append([int(List[5]), int(List[46]), int(List[41])])

df = pd.DataFrame(bet_payout_id, columns=['bet', 'payout', 'ID'])
df = df.groupby('ID')
for name, group in df:
    group = group.reset_index(drop=True)
    print group
    result = group['payout'] / group['bet']
    result = result.cumsum()
    cum_result = {'times': result.index, 'rtp': result.values}
    df_counts = pd.DataFrame(cum_result)
    avg_RTP = df_counts['rtp'] / df_counts['times']
    avg_RTP.plot()
    labels.append('game_' + str(name))
#result = df['payout']/df['bet']
# result[result['value']<1] = -result['value']
#result = result.cumsum()
#cum_result = {'times': result.index, 'rtp': result.values}
#df_counts = pd.DataFrame(cum_result)
#avg_RTP = df_counts['rtp'] / df_counts['times']
#avg_RTP.plot()
plt.hlines(1,1000000000,0,colors='r')
plt.title('Game RTP')
plt.show()
# plt.figure(figsize=(60,1))
# result.plot()
# plt.show()
