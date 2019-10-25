import datetime
import pandas as pd
#%matplotlib  #(in iPython)
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

now = datetime.datetime.now()
DATA_URL = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_day.csv'
df = pd.read_csv(DATA_URL)
print("Data fetched at " + now.strftime("%Y-%m-%d %H:%M"))

fig, ax = plt.subplots(figsize=(14, 8))

earth = Basemap(ax=ax)
#earth.drawcoastlines(color='#000000', linewidth=1)
earth.bluemarble(alpha=0.8) # for blue color of water

ax.scatter(df['longitude'], df['latitude'], df['mag'] ** 2, c='red', alpha=0.5, zorder=10)
ax.set_title("Earthquakes of magnitude 4.5+ in the last 24 hours") 

fig.savefig('output_usgs_4.5quakes_'+now.strftime("%Y-%m-%d_%H-%M")+'.png', dpi=350)
plt.show()