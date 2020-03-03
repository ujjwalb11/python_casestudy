"""
Ujjwal Bharadwaj
Emp_id : 142908
title : Rash driving
ver 1.0
"""

import matplotlib.pyplot as plt


def rashdriving_check(data):
    """to check the no of rash driving alerts raised during journey"""

    i = 0
    rashcount = 0
    speed = data.loc[0:, 'Speed (GPS)(km/h)']
    pedal = data.loc[0:, 'Accelerator PedalPosition D(%)']
    while i <= 2575:
        if speed[i] > 50:
            if pedal[i] > 50:
                rashcount += 1
        i += 1
    print('\n4. The number of times rash driving alert raised is: ',rashcount)


def rashdriving_location(data):
    """to locate the rash driving incidents during the journey"""

    speed = data.loc[0:, 'Speed (GPS)(km/h)']
    pedal = data.loc[0:, 'Accelerator PedalPosition D(%)']
    lat = data.loc[0:, ' Latitude']
    long = data.loc[0:, ' Longitude']
    plt.figure()
    plt.plot(lat, long)
    for i in range(len(speed)):
        if speed[i] > 50:
            if pedal[i] > 50:
                plt.scatter(lat[i], long[i], color=['red'])
    plt.title('4. Rash driving locations')
    plt.xlabel('Latitude')
    plt.ylabel('Longitude')
    plt.legend(['journey route', 'Rash driving alert'])
    plt.show()
