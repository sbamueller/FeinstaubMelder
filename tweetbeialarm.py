
#!/usr/bin/python3
# -*- coding: utf-8 -*-
# depends: python-requests


##### import main components 
 
import json

import requests
import tweepy

# for debugging : 
import os
import time



############ key variables  ######################
############ key variables  ######################
############ key variables  ######################



# Switch to actually send tweets or not.
# Good for testing, so one can test the code without tweeting.
# Set to False if you ond't want the code to send a tweet.
are_we_tweeting = True 


# Current safety limit 
# - the warning tweets happen when this is exceeded
pm_safety_limit = 25


# -- for debugging - writes a comment to a log file, when the script starts
#   -- can be good when running this script by cron jobs, where there might not be crash output
## os.system("echo '-- tweeting started at "+str( time.ctime() )+"' >> /home/miska/python_tweeting_debugging.txt" )

# file path to access tokens for twitter access
twitter_access_tokens_filepath = "access_keys.json"

# http path to the sensor list 
# url_of_sensor_list_ = "http://sourisr.kapsi.fi/luftDaten/sensor_list.csv"
url_of_sensor_list_ = "https://raw.githubusercontent.com/miskaknapek/test_repository__ipython_notebook_tests/master/luftDaten_sensor_list.csv"





############ functions ######################
############ functions ######################
############ functions ######################



# for feching and storing access codes 
def fetch_access_keys( twitter_access_tokens_filepath_ ):
    print( ">>>> fetch_access_keys() ")
    # fetches the access key file 
    local_file = open( twitter_access_tokens_filepath_ ).read()
    return json.loads( local_file );    

def fetch_sensor_list( url_of_sensor_list_ ):
    print(">>>> fetch_sensor_list - with url |"+url_of_sensor_list_+"|" )
    # fetch data
    raw_data = requests.get( url_of_sensor_list_ ).text
    # split text
    split_data = raw_data.split(",")
    # get the integers
    sensor_id_list = []
    for item in split_data:
        sensor_id_list.append( int( item) )
    # retun something nice 
    return sensor_id_list

# Advanced version : Auswerte Funktion
# - also retuns the sensor location. 
def pick_values_value_and_location(sensor):
    # Sensordaten f  r SDS011 abfragen und Maximum pr  fen
    # dazu die api von luftdaten.info nutzen
    # Peter F  rle @Alpensichtung Hotzenwald 04/2017
    r = requests.get(sensor)
    json_string = r.text
    parsed_json = json.loads(json_string)
    # pretty print um   berhaupt zu verstehen was da passiert 
    # print( json.dumps(parsed_json, sort_keys=True, indent=4, separators=(',',':')) )
    l = len(parsed_json)
    if l:
        a = len(parsed_json[l - 1]['sensordatavalues'])
        if a:
            # in der Regel ist der erste Wert der PM10
            result__sensor_value = (parsed_json[l - 1]['sensordatavalues'][0]['value'])
            result__location = [ float( parsed_json[l - 1]['location']['latitude'] ), float( parsed_json[l - 1]['location']['latitude'] ) ]
            print( " - has PM value : "+str(result__sensor_value) )
            print( " - and location : "+str(result__location) )
            return [result__sensor_value, result__location]
    # Falls Json unvollst  ndig ist
    return (0)

# Auswerte Funktion
def pick_values(sensor):
    # Sensordaten f  r SDS011 abfragen und Maximum pr  fen
    # dazu die api von luftdaten.info nutzen
    # Peter F  rle @Alpensichtung Hotzenwald 04/2017
    r = requests.get(sensor)
    json_string = r.text
    parsed_json = json.loads(json_string)
    # pretty print um   berhaupt zu verstehen was da passiert 
    # print( json.dumps(parsed_json, sort_keys=True, indent=4, separators=(',',':')) )
    l = len(parsed_json)
    if l:
        a = len(parsed_json[l - 1]['sensordatavalues'])
        if a:
            # in der Regel ist der erste Wert der PM10
            result = (parsed_json[l - 1]['sensordatavalues'][0]['value'])
            print( " - has PM value : "+str(result) )
            return (result)
    # Falls Json unvollst  ndig ist
    return (0)





############  script executing things  ######################
############  script executing things  ######################
############  script executing things  ######################


#### in case you want to store Sensor ID locations in this script - use the variable below and disable the fetch_sensor_list() function further below … which fetches the sensorIDs from elsewhere
# Freiburger Sensornummern, einfach neu dazugekommene hier an die Liste dranh  ngen
#sd = [533, 1224, 1288, 928, 1210, 1264, 1685, 1615, 1667]
# sd = [533,928,1210,1218,1224,1264,1288,1615,1667,1685,1699,1939,1975,2001,2289,2384,2388,2392,2408,2410,2438,2452,2456,2546,2564,2602,2662,2712,2728,2734,3525,3527,4206,4299,5335,5559,6590,6642,6924,7124,7243,7324,7381,7408,7446,7665,7725,7793,7799,7967,8070,8189,8213,9280,9958,11406,11425,12257,12302,13870,13891]
## sd = [533,928,1210,1224,1264,1288,1615,1667,1685,1699,1939,2289,2384,2388,2392,2408,2410,2438,2452,2456,2546,2564,2602,2662,2712,2728,2734,3525,3527,4206,4299,5335,5559,6590,6642,6924,7124,7243,7324,7381,7408,7446,7665,7725,7793,7799,7967,8070,8189,8213,9280,9958,11406,11425,12257,12302,13870,13891]
maxlist_sensor_values = []
location_list = []

# TEST - try fetch external list of sensors 
sd = fetch_sensor_list( url_of_sensor_list_ )
print("\n ------------------ printing fetched sensor id list : ")
print( sd )
print("\n ------------------  ")

print("\n\n ------------------ now fetching sensor data values : ")


# fetch sensor data, accordign to the sd list sensor ids 
for x in sd:
    print( "\n -Fetching data from sensor #"+str(x) )
    url = 'http://api.luftdaten.info/static/v1/sensor/' + str(x) + '/'
    # Liste erzeugen mit den Werten, ok float() ist nicht ganz sauber...
    maxlist_sensor_values.append(float(pick_values(url)))
    ## below : advanced pick_values - with location tracking too
    # location_list.append( pick_values_value_and_location(url) )
    # print("-- printing location again!")
    # temp_loc = location_list[ len(location_list)-1 ]
    # print( temp_loc )

# welches ist der h  chste Wert ?
maxwert = max(maxlist_sensor_values)
# zu welchem Sensor aus der Liste sd geh  rt der H  chstwert ?
sensor = sd[maxlist_sensor_values.index(maxwert)]

# tweet text if the 'macwer' is not exceeded
tweet = "- Aktuell liegen keine Grenzwert- Uberschreitungen in Freiburg vor - die maxwert ist "+str( maxwert )+" ug/m3 - "
alarm = False # the script only tweets if this value is set to True 
                # - if you want the non-warning message (above) to be tweeted 
                # set this value to True. 
                # when False, it won't be tweeted.

# Tweet text if the 'maxwert' is exeeded
# hier kannst du den Maxwert anpassen
if maxwert > pm_safety_limit:
    tweet = "- Achtung Freiburg! \n Feinstaubwerte hoch - Sensor: {} ist bei PM10 {} ug/m3".format(sensor, int( maxwert) )
    # add the second line and url to the tweet 
    tweet = tweet + "\n - aktuelle Sensorinfo : https://feinstaub.rexfue.de/{}".format( sensor )
    # hier den Tweet ausl  sen
    alarm = True

# DEBUGGING - so we can see the tweet text, even if we're not tweeting
print( "\n ----- printing tweet : ----------------- \n "+tweet+"\n --------------------------- \n" )


# --- ACESS TOKENS --- 
# Consumer keys and access tokens, used for OAuth  
# - Fetching access token from local file 
access_keys = fetch_access_keys( twitter_access_tokens_filepath )
## for debugging purposes : 
print(" ------------------ printing access keys : ")
print( access_keys )
print(" ------------------  ")

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(access_keys['CONSUMER_KEY'], access_keys['CONSUMER_SECRET'])
auth.set_access_token(access_keys['ACCESS_KEY'], access_keys['ACCESS_SECRET'])

# Creation of the actual interface, using authentication
api = tweepy.API( auth )

if are_we_tweeting == True : 
    # twittern nur Text
    # if alarm:                                 // disabled while testing
    #    api.update_status(status=tweet)        // disabled while testing
    if alarm:
        try: 
            api.update_status(status=tweet )
            ## debugging ( the line below )
            # os.system("echo '---- tweet on its way "+str( time.ctime() )+"' >> /home/miska/python_tweeting_debugging.txt" ) 
        except tweepy.error.TweepError as e:    
            print( "\n ---- err got error - : "+str( e ) );
            ## debugging ( the line below )
            # os.system("echo '---- tweepy error at time "+str( time.ctime() )+" : "+str( e )+" ' >> /home/miska/python_tweeting_debugging.txt" ) 
else:
    print("\n --- ERRRRRR - TWEETING HAS BEEN SWITCHED OFF! ")


# -- (last script line below) for debugging - writes a comment to a log file, when the script ends. 
#   -- can be good when running this script by cron jobs, where there might not be crash output
## os.system("echo '-- python script (part2) at "+str( time.ctime() )+" "+str( tweepy.error.TweepError )+" ' >> /home/miska/pythondebugging.txt" ) 