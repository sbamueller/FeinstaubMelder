
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
0,5,10,12,15,20,25,30,35,40,45,50,55 * * * * cd /FILEPATH/TO/YOUR/SCRIPTS/DIRECTORY; /usr/bin/python3 tweetbeialarm.py
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
