"""
Ujjwal Bharadwaj
Emp_id : 142908
title : main file
ver 1.0
"""

import airfuelmix_check as afc  # importing first feature function file
import pothole_detection as pt  # importing second feature function file
import CO2emission as CO2e  # importing third feature function file
import Rashdriving as Rd  # importing fourth feature function file
import googlemap_plot as gm  # importing fifth feature function file

# read the input file

DF = afc.file_read()  # reading the excel sheet data

# 1. for fuel check using O2 sensor data 
# (check corresponding function file for details)

TIME = afc.timeframe(DF)
O2SENSORDATA = afc.o2sensordata_read(DF)
afc.fuel_count(DF)
afc.fuel_check_plot(TIME, O2SENSORDATA)
afc.richcounts_plot(DF)
afc.leancounts_plot(DF)

# 2. for detection of potholes in the path 
# (check corresponding function file for details)

pt.pothole_plot(DF)

# 3. for detection of fuel economy using CO2 emissions 
# (check corresponding function file for details)

CO2e.economy_check(DF)
CO2e.fueleconomylocations_plot(DF)

# 4. for Rash driving alert 
# (check corresponding function file for details)

Rd.rashdriving_check(DF)
Rd.rashdriving_location(DF)

# 5. for plotting the route on google map 
# (check corresponding function file for details)

gm.googlemap()  # calling the function for mapping the route and storing it in html file
