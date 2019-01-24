import urllib
import csv

def get_text_lines_from_url(url):
    url_data = urllib.request.urlopen(url)
    lines = url_data.readlines()
    decoded_lines = []
    for line in lines:
        decoded_line = line.decode("utf-8")[0:-1]
        decoded_lines.append(decoded_line)
    return (decoded_lines)

def test_get_lines_from_url():
    urls = ["http://www.comp.leeds.ac.uk/brandon/vle/geek-music.csv",
            "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.csv"]
    for url in urls:
        print ("First 10 lines from "+url+" are:")
        print (get_text_lines_from_url(url)[0:10])
        print ("\n")

def find_largest_magnitude(data):
    quakes = csv.reader(data)
    next(quakes)
    highest_mag = 0.0
    for line in quakes:
        if float(line[4]) > highest_mag:
            highest_mag = float(line[4])
        else:
            None
    return highest_mag
    
def display_quake_data(data,magnitude):
    quakes = csv.reader(data)
    next(quakes)
    for line in quakes:
        if float(line[4]) == magnitude:
            print("Largest magnitude quake is:")
            print("Time:       "+line[0])
            print("Latitude:   "+line[1])
            print("Longitude:  "+line[2])
            print("Location:   "+line[13])
            print("Magnitude:  "+line[4])
            print("Depth:      "+line[3])
        else:
            None

def offline_display_largest_quake(date):
    print("Loading earthquake data from local earthquake data file:")
    print("earthquakes_2016-11-08.csv")
    with open("earthquakes_"+date+".csv","r") as data:
        highest_magnitude = find_largest_magnitude(data)
    with open("earthquakes_"+date+".csv","r") as data:
        display_quake_data(data,highest_magnitude)
    
def online_display_largest_quake():
    print("Downloading earthquake data from USGS ...")
    data = get_text_lines_from_url("http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.csv")
    highest_magnitude = find_largest_magnitude(data)
    data = get_text_lines_from_url("http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.csv")
    display_quake_data(data,highest_magnitude)

def display_largest_quake():
    try:
        online_display_largest_quake()
    except:
        print("ERROR: Unable to get data from USGS website!!!")
        offline_display_largest_quake("2016-11-08")
display_largest_quake()