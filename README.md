# FeinstaubMelder
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
