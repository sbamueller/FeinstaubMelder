#!/usr/bin/env python
# -*- coding: utf-8 -*-
# depends: python-requests

import json

import requests
import tweepy


# Auswerte Funktion
def pick_values(sensor):
    # Sensordaten f  r SDS011 abfragen und Maximum pr  fen
    # dazu die api von luftdaten.info nutzen
    # Peter F  rle @Alpensichtung Hotzenwald 04/2017
    r = requests.get(sensor)
    json_string = r.text
    parsed_json = json.loads(json_string)
    # pretty print um   berhaupt zu verstehen was da passiert
    # print json.dumps(parsed_json, sort_keys=True, indent=4, separators=(',',':'))
    l = len(parsed_json)
    if l:
        a = len(parsed_json[l - 1]['sensordatavalues'])
        if a:
            # in der Regel ist der erste Wert der PM10
            result = (parsed_json[l - 1]['sensordatavalues'][0]['value'])
            return (result)
    # Falls Json unvollst  ndig ist
    return (0)


# Freiburger Sensornummern, einfach neu dazugekommene hier an die Liste dranh  ngen
sd = [533, 1224, 1288, 928, 1210, 1264, 1685, 1615, 1667]
maxlist = []
for x in sd:
    print(x)
    url = 'http://api.luftdaten.info/static/v1/sensor/' + str(x) + '/'
    # Liste erzeugen mit den Werten, ok float() ist nicht ganz sauber...
    maxlist.append(float(pick_values(url)))

# welches ist der h  chste Wert ?
maxwert = max(maxlist)
# zu welchem Sensor aus der Liste sd geh  rt der H  chstwert ?
sensor = sd[maxlist.index(maxwert)]

tweet = ' Aktuell liegen keine Grenzwert- Überschreitungen in Freiburg vor '
alarm = False

# hier kannst du den Maxwert anpassen
if maxwert > 5:
    tweet = 'Achtung Freiburg! Feinstaubwerte hoch - Sensor: {} ist bei PM10 {} µg/m³'.format(sensor, maxwert)
    # hier den Tweet ausl  sen
    alarm = True

print tweet

# acess tokens
CONSUMER_KEY = 'x'
CONSUMER_SECRET = 'x'
ACCESS_KEY = 'x'
ACCESS_SECRET = 'x'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

# twittern nur Text
if alarm:
    api.update_status(status=tweet)
