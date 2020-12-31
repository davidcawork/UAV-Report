#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt


# Read csv trend
trend = pd.read_csv('data/timeTrend.csv',  header=1)
trend = trend.replace({'<1': 1})


# Convert month to datetime
trend['Mes'] = pd.to_datetime(trend['Mes'])

# At this point, there are some columns that are not numeric types, let's  convert it
for column in trend.columns:
    if trend[column].dtype == 'O':
        trend[column] = pd.to_numeric(trend[column])

# It's not necessary, but, it's easier to put datetime as index in order to plot
trend.set_index('Mes', inplace=True)

# Debug info
print(trend.head())
print(trend.info())


# Time to plot :D
trend.plot(figsize=(16, 6))
plt.title('Interest over time (around the world)')
plt.xlabel('Year', labelpad=15, fontsize=12)
plt.legend(["UAV (Unmanned Aerial Vehicle)", "UAS (Unmanned Aerial System)", "Dji", "Drone"])
plt.savefig("fig/timelineTrend.pdf", bbox_inches='tight')
plt.show()
