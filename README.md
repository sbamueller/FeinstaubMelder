# FeinstaubMelder
Is an automated particle matter warning system. Once the PM Value of certain censors from the http://luftdaten.info systems raises above a threshold, it tweets a warning. The tweets are trigged by a cron job. 

The text o the tweet looks like this: 

- Achtung Freiburg!
Feinstaubwerte hoch - Sensor: 7446 ist bei PM10 20 ug/m3
 - aktuelle Sensorinfo: 
https://feinstaub.rexfue.de/7446 

This is currently developed by https://github.com/miskaknapek and me. 

There is one system currenlty used: https://twitter.com/FeinstaubFR

* More information in German *

Fragt bestimmte Sensoren ab und wenn diese über 50 y/m3 sind, dann twittert er eine Feinstaub Warnung

# Einige Hinweise:

Ändern sie unter:
* Freiburger Sensornummern, einfach neu dazugekommene hier an die Liste dranh
sd = [533,1224,1288,928,1210,1264,1685,1615,1667]
Diese Nummern, durch die Sensoren, von denen sie twittern wollen.

Die Nummern finden sie auf http://freiburg.maps.luftdaten.info/ wenn sie mit der Maus über den Sensor ziehen.

* hier kannst du den Maxwert anpassen
if maxwert > 50:
    tweet = 'Achtung Freiburg! Feinstaubwerte hoch - Sensor: ' + str(sensor) + ' ist bei PM10 ' + str(maxwert) + '  $
    
 Hier können sie zum einen den Wert anpassen ab dem eine Feinstaubwarnung getwittert werden sollt und auch den Text ändern.
 
Weitere Informationen zu diesem Projekt: https://sbamueller.wordpress.com/2017/04/23/twitterbot-2-feinstaubfr/
