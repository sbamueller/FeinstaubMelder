
### Feinstaub twitter-bot 

The Feinstaub bot tweets 

### requirements 
- python >= 3
- *tweepy* pyhton extension 


### Important settings 

- are_we_tweeting : this True/False switch sets whether the tweet text generated in the script is actually sent to twitter. 
This can be good for testing code, such that the generated tweet isn't sent to twitter all the time. 

- pm_safety_limit : when the sensor PM value exceeds this value, then the warning tweet is generated and sent to twitter ( unless the are_we_tweeting switch is set to False )

- twitter_access_tokens_filepath : filepath relative to the directory the script is started from, of the json file with twiter access tokens.

- url_of_sensor_list_ : url to the one line csv sensor list file, with comma separated sensor numbers


### Setting up on server

#### cronjob settings 
One of the easier ways of getitng the feinstaub bot to run on a regular basis is to run it as a crontjob. To do this, on a linux server… 

- start the cronjob settings by typing the following in a terminal 

```
crontab -e
```


- then add the following line at the end of the cronjobs 
( do change the file path to be the file path to the directory of your script )
   
```
0,5,10,12,15,20,25,30,35,40,45,50,55 * * * * cd /home/miska/documents/luftdaten/luftdaten_bot/code; /usr/bin/python3 luftDaten_bot_1pt5.py
```

** please note 1 : ** You do in fact need to add the file-path to the directory where you've stored the python script. 
** please note 2 : ** Please add the path to the python3 version you're using.

Cronjobs, if you've not used them before, are a bit tricky, to say the least. 
One doesn't necessaily see the terminal output of a script ( there are excpetions, see cronjob documentation ). So if things don't work, one needs to debug in various 'funny' ways. 
For this reason there are some commented-out code lines in the code, to write more log entries, for debugging reasons. 
Also, every time a cronjob starts, it leaves an entry in the system log. You can check the cronjobs in the log file by typing the following line in to the terminal :

```
grep CRON /var/log/syslog
```


#### access_keys.json settings

This is the file that contains the tokens needed to be able to use the twitter API to tweet. Make sure to get the right access tokens from twitter and insert them in this file.
Also do make sure to enter the right file-path, in the 

*NOTE:* this file needs to be on the same server as the python script and the path to this file needs to be entered in the script, by the *twitter_access_tokens_filepath* variable.

#### access_keys.json

This file contains a one line list of sensorIDs, to the sensors used by this twitter bot. please only enter their numbers, with each separated by a comma, in one line. 
No line-breaks or any other characters than numbers and commas. 
Otherwise Mr/s python script gets terribly confused.
Kindly put the file on a web-server and supply the url to the file in the *url_of_sensor_list_* variable. 

Something like this is what it should look like 

```
533,928,1210,1224,1264,1288,1615,1667,1685,1699,1939,2289,2384
```

You can also upload your list of sensor IDs onto github and link it, as here:
https://raw.githubusercontent.com/miskaknapek/test_repository__ipython_notebook_tests/master/luftDaten_sensor_list.csv