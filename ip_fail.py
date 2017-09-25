#!/bin/env python3
## Evan Widloski - 2017-08-31
## SSH Failed login stats
# journalctl -u sshd | grep -Po "[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}" > /tmp/fail_ip

# pip install python-geoip python-geoip-geolite2

from collections import Counter
from geoip import geolite2
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt

f = open('/tmp/fail_ip')
unique_ips, attempts = np.unique(f.read().splitlines(), return_counts=True)
max_attempts = np.max(attempts)

countries = []
longitudes = []
latitudes = []
for address in unique_ips:
    match = geolite2.lookup(address)
    if match is not None:
        countries.append(match.country)
        latitudes.append(match.location[0])
        longitudes.append(match.location[1])

countries = np.array(countries)
latitudes = np.array(latitudes)
longitudes = np.array(longitudes)

unique_countries, ips_by_country = np.unique(countries, return_counts=True)
attempts_by_country = []
for country in unique_countries:
    attempts_by_country.append(sum(attempts[country == countries]))


# map ips
m = Basemap(projection='mill', lon_0=0)
m.drawcoastlines()
m.drawcountries()
m.drawmapboundary(fill_color='powderblue')
m.fillcontinents(color='beige', lake_color='powderblue')
x, y = m(longitudes, latitudes)
# lons = [40.42, 10, -20, -20]
# lats = [86.90, -10, 40, -20]
# x,y = m(lons, lats)
x,y = m(longitudes, latitudes)
m.scatter(x, y, 400 * attempts.astype(np.float32) / max_attempts, marker='o', color='r', alpha=.5, zorder=10)
plt.show()

def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return val
    return my_autopct

fig1, (ax1, ax2) = plt.subplots(1, 2)
ax1.pie(ips_by_country, labels=unique_countries, autopct=make_autopct(ips_by_country))
ax1.set_title("Unique IPs by country")
ax2.pie(attempts_by_country, labels=unique_countries, autopct=make_autopct(attempts_by_country))
ax2.set_title("Unique attempts by country")
plt.show()


f.close()
