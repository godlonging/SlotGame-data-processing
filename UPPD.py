import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
reader = csv.reader(open('game_recall.csv'))
UPPD = []
total_id = []
total_date = []
sorted_data = []
for list in reader:
    # print list[0]
    User_id = list[47]
    date = list[1][0:11]
    UPPD.append([User_id, date])
    total_id.append(list[47])
    total_date.append(list[1][0:11])
# print UPPD

# UPPD=tuple(UPPD)
# sorted(UPPD,key=tuple[1])
sort = sorted(UPPD,key=lambda t:t[1])
test = dict(zip(total_id, total_date))
test = sorted(test.items(),lambda x,y:cmp(x[1],y[1]))
df = pd.DataFrame(UPPD, columns=['id', 'date'])
df['date']=pd.to_datetime(df['date'])
df = df.drop_duplicates(keep='first', inplace=False)
lisc_c = df['date'].value_counts()
print lisc_c
lisc_c.plot()
plt.title('Unique Player per Day')
plt.show()
#df = df.set_index('date')
#s = pd.Series(df['id'],index=df.index)






