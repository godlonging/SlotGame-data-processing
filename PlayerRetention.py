import csv
import pandas as pd
import matplotlib.pyplot as plt

reader = csv.reader(open('game_recall.csv'))
playerID_date = []
tmp = []
tmp_name = []
tmp_times = []
for List in reader:
    playerID_date.append([List[47], List[1][0:11]])

df = pd.DataFrame(playerID_date,columns=['playerid','date'])
df['date'] = pd.to_datetime(df['date'])
df = df.drop_duplicates(keep='first', inplace=False)
df = df.sort_values('date')
counts = df['date'].value_counts()
counts = pd.DataFrame(counts)
# print counts
df = df.groupby(df['date'])
for name, group in df:
    group = group.reset_index(drop=True)
    tmp.append(group['playerid'])
    tmp_name.append(name)

for i in range(len(tmp)-1):
    first = pd.DataFrame(tmp[i],columns=['playerid'])
    second = pd.DataFrame(tmp[i+1],columns=['playerid'])
    result = pd.concat([first,second])
    result_1 = result.drop_duplicates(keep='first')
    result_2 = result.drop_duplicates(keep=False)
    result = result_1.append(result_2).drop_duplicates(keep=False)
    tmp_times.append(result.shape[0])
tmp_times = tmp_times + [0]
counts['Y'] = tmp_times
PR = counts['Y'] / counts['date']
PR.plot()
plt.title('Player Retention')
plt.show()

#levels = df.index[0]
#print df.loc[levels]
#print levels
#for name, group in df:
    #print group
 #   pass
    #group = group['date'].values_counts()
    #print group