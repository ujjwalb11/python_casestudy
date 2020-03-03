"""
Ujjwal Bharadwaj
Emp_id : 142908
title : Google map plot of driver route
ver 1.0
"""

import gmplot
import pandas as pd


def googlemap():
    """to mapping the route and storing it in html file"""

    data = pd.read_csv('C:/Users/UJJWAL BHARADWAJ/Desktop/City Drive 2.csv')
    lat = data.loc[0:, ' Latitude']
    long = data.loc[0:, ' Longitude']
    gmap = gmplot.GoogleMapPlotter(lat.iloc[0], long.iloc[0], 15)
    gmap.plot(lat, long, 'purple', edge_width=4.5)
    gmap.draw('maproute.html')
    print('\n5. The journey route was successfully mapped to google maps')
