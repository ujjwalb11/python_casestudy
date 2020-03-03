"""
Ujjwal Bharadwaj
Emp_id : 142908
title : Pothole detection
ver 1.0
"""

import matplotlib.pyplot as plt


def pothole_plot(data):
    """to detect no of potholes and locate them on google map"""

    acc = data.loc[0:, 'Acceleration Sensor(Z axis)(g)']
    lat = data.loc[0:, ' Latitude']
    long = data.loc[0:, ' Longitude']
    count = 0
    plt.figure()
    plt.plot(lat, long)
    for i in range(len(acc)):
        if acc[i] > 1.10:
            plt.scatter(lat[i], long[i], color=['green'])
            count += 1
        elif acc[i] < 0.70:
            plt.scatter(lat[i], long[i], color=['green'])
            count += 1
    print('\n2. The number of potholes encountered in the path: ', count)
    plt.title('2. pothole locations')
    plt.xlabel('Latitude')
    plt.ylabel('Longitude')
    plt.legend(['path', 'pothole'])
    plt.show()
