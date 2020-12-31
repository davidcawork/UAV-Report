#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt

reposbyYear = pd.read_csv('data/githubTrendYear.csv')

reposbyYear.set_index('Year', inplace=True)

print(reposbyYear.head())
print(reposbyYear.info())

reposbyYear.plot.bar(figsize=(10, 8), color='#ffb630', legend=False, zorder=3, linewidth=1, edgecolor=['black']*13)
plt.title('Repositories created on Github ')
plt.rc('axes', axisbelow=True)
plt.grid(zorder=0, color='gray', linestyle='dashed')
plt.xlabel('Year', labelpad=15, fontsize=12)
plt.savefig("fig/githubTrend.pdf", bbox_inches='tight')
plt.show()
