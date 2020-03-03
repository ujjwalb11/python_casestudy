"""
Ujjwal Bharadwaj
Emp_id : 142908
title : Air-fuel mixture check
ver 1.0
"""

import matplotlib.pyplot as plt
import pandas as pd


def file_read():
    """reading the csv file"""

    data = pd.read_csv('City Drive 2.csv')
    return data


def timeframe(data):
    """storing time values"""

    time = data.iloc[:, 74]
    return time


def o2sensordata_read(data):
    """storing o2 sensor data"""

    o2sensordata = data.iloc[:, 60]
    return o2sensordata


def fuel_count(data):
    """to count the no of rich and lean air-fuel ratio during the journey"""

    threshold = 0.45
    i = 0
    rich_count = 0
    lean_count = 0
    o2sensordata = list(data.iloc[:, 60])
    while i <= 2575:
        if o2sensordata[i] > threshold:
            rich_count += 1
        else:
            lean_count += 1
        i += 1

    print('1. Air-Fuel ratio Check throughout the journey:\n The '
    'number of times air fuel ratio was rich is:', rich_count, '\n The '
    'number of times air fuel ratio was lean is:', lean_count)


def fuel_check_plot(x, y):
    """to plot the o2 sensor data"""

    plt.plot(x, y)
    plt.title('1a. O2 Sensor Data vs time')
    plt.xlabel('Time (in sec)')
    plt.ylabel('O2 Sensor Data (in Volts)')
    plt.show()


def richcounts_plot(data):
    """to locate the rich air-fuel ratio during the journey"""

    o2list = data.iloc[:, 60]
    time = data.iloc[:, 74]
    plt.figure()
    for i in range(0, len(o2list)):
        if o2list[i] > 0.45:
            plt.scatter(time[i], o2list[i], color=['black'])
    plt.title('1b. Rich air-fuel mixture counts vs time')
    plt.xlabel('Time (in sec)')
    plt.ylabel('Rich air-fuel counts')
    plt.show()


def leancounts_plot(data):
    """to locate the lean air-fuel ratio during the journey"""
    
    o2list = data.iloc[:, 60]
    time = data.iloc[:, 74]
    plt.figure()
    for i in range(0, len(o2list)):
        if o2list[i] < 0.45:
            plt.scatter(time[i], o2list[i], color=['green'])
    plt.title('1c. Lean air-fuel mixture counts vs time')
    plt.xlabel('Time (in sec)')
    plt.ylabel('Lean air-fuel counts')
    plt.show()
