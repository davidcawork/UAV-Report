#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt

paperbyYear = pd.read_csv('data/paperTrend.csv')

paperbyYear.set_index('Year', inplace=True)

print(paperbyYear.head())
print(paperbyYear.info())

paperbyYear.plot.bar(figsize=(9, 9), color='#c1f288', legend=False, zorder=3, linewidth=1, edgecolor=['black']*13)
plt.title('Publication of papers per year')
plt.rc('axes', axisbelow=True)
plt.grid(zorder=0, color='gray', linestyle='dashed')
plt.xlabel('Year', labelpad=15, fontsize=12)
plt.savefig("fig/papersTrend.pdf", bbox_inches='tight')
plt.show()
