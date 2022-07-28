# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns 

# import data from a Data-sheet
births = pd.read_csv("Dataset-Pro.csv") 
print(births.head())
births['day'].fillna(0, inplace=True) 
births['day'] = births['day'].astype(int)
# decade the data
births['decade'] = 10 * (births['year'] // 10)
births.head()
# Create a pivot table
births.pivot_table('birth',index='decade', columns='gender',aggfunc='sum')
print(births.head())
# Show the graph for Total births per year
sns.set() 
birth_decade = births.pivot_table('birth', index='decade', columns='gender', aggfunc='sum') 
birth_decade.plot() 
plt.ylabel("Total births per year") 
plt.show()
# Show the graph for mean births per year
quartiles = np.percentile(births['birth'], [25, 50, 75])
mu = quartiles[1]
sig = 0.74 * (quartiles[2] - quartiles[0])
births = births.query('(birth > @mu - 5 * @sig) & (birth < @mu + 5 * @sig)')
births['day'] = births['day'].astype(int)
births.index = pd.to_datetime(10000 * births.year +100 * births.month +births.day, format='%Y%m%d')
births['dayofweek'] = births.index.dayofweek
births.pivot_table('birth', index='dayofweek',columns='decade', aggfunc='mean').plot()
plt.gca().set_xticklabels(['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun'])
plt.ylabel('mean births by day');
plt.show()

births_month = births.pivot_table('birth', [births.index.month, births.index.day])
print(births_month.head())

births_month.index = [pd.datetime(2012, month, day)
                      for (month, day) in births_month.index]
print(births_month.head())
# Totlal Total births in the year between
fig, ax = plt.subplots(figsize=(12, 4))
births_month.plot(ax=ax)
plt.show()


