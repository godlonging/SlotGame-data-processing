import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
reader = csv.reader(open('game_recall.csv'))
spin_date = []
for List in reader:
    spin_date.append([List[0], List[1][0:11]])
df = pd.DataFrame(spin_date, columns=['id', 'date'])
df['date'] = pd.to_datetime(df['date'])
SPPPD = df['date'].value_counts()
plt.title('Spin per Player per Day')
SPPPD.plot()
plt.show()