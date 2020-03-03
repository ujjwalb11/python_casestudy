"""
Ujjwal Bharadwaj
Emp_id : 142908
title : CO2 emission
ver 1.0
"""

import matplotlib.pyplot as plt


def economy_check(data):
    """to check the no of good and bad fuel economy during the journey"""
    
    i = 0
    t1 = 195.00
    t2 = 205.00
    goodeco_count = 0
    badeco_count = 0
    co2data = data.loc[0:, 'CO₂ in g/km (Average)(g/km)']
    while i <= 2575:
        if co2data[i] < t1:
            goodeco_count += 1
        elif co2data[i] > t2:
            badeco_count += 1
        i += 1

    print('\n3.Fuel economy check throughout the journey:\n\nThe number of times fuel economy '
          'was good is:', goodeco_count)
    print('The number of times fuel economy was bad is:', badeco_count)


def fueleconomylocations_plot(data):
    """to locate the two phases of fuel economy during the journey"""
    
    co2data = data.loc[0:, 'CO₂ in g/km (Average)(g/km)']
    plt.figure()
    lat = data.loc[0:, ' Latitude']
    long = data.loc[0:, ' Longitude']
    plt.plot(lat, long)
    for i in range(len(co2data)):
        if co2data[i] < 195:
            plt.scatter(lat[i], long[i], color=['green'])
        elif co2data[i] > 205:
            plt.scatter(lat[i], long[i], color=['black'])
    plt.title('3. Good or bad fuel economy type location')
    plt.xlabel('Latitude')
    plt.ylabel('Longitude')
    plt.legend(['journey route', 'good fuel economy', 'bad fuel economy'])
    plt.show()
