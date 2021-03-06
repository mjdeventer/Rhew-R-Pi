from time import sleep
import csv
import os.path

#import datetime
from datetime import datetime

#import sensors
import Adafruit_DHT

#VARIABLES
#data directory path
DATA_PATH = '/home/pi/Documents/env_datalogs'
#data file name
DATA_NAME = 'dht_logs'
#todays date
now = datetime.now()
date_string = now.date().strftime("%Y_%m_%d")

DELAY_INTERVAL = 5
#sensors
dht_sensor = Adafruit_DHT.DHT22
dht_pin = 4

#create total file path (with date)
file_name = DATA_PATH + '/' + date_string + '_' + DATA_NAME

#if the file does not already exist, create a new file with headers
if not os.path.isfile(file_name):
    csv_headers = ['Date', 'Time','Temperature', 'Humidity']
    with open(file_name, 'w') as new_data_file:
        datawriter = csv.writer(new_data_file)
        datawriter.writerow(csv_headers)


#main logging sequence
while True:
    new_log = []

    now = datetime.now()
    date_string = now.date().strftime("%Y_%m_%d")
    time_string = now.time().strftime("%H:%M:%S")
    
    new_log.append(date_string)
    new_log.append(time_string)

    #sensor1 
    humidity, temperature = Adafruit_DHT.read_retry(dht_sensor, dht_pin)
    new_log.append(temperature)
    new_log.append(humidity)
    
    #write results to log
    with open(file_name, 'a') as data_log:
        logwriter = csv.writer(data_log)
        logwriter.writerow(new_log)
    print "Wrote Log: ", new_log
    sleep (DELAY_INTERVAL)
