# Speech Databse Tool.

Use the Speech Database Editor to edit the phrases in your speech database.  Each phrase can be assigned a Set and and Variable to help use them inside your Ohbot programs. 

<a href="https://github.com/ohbot/picoh-python/blob/master/.images/speechdbscreenshot.png?raw=true" target="_blank"><img src="https://github.com/ohbot/picoh-python/blob/master/.images/speechdbscreenshot.png?raw=true" border="0" width = "100%"/></a>

* Tested on Python 3.7.  on macOS and Python 3.6 on Windows 10 and Python 3.4 on Raspberry Pi.
Right click and save file as:

How to run
----------
1) Right click and save in your working directory: [SpeechDatabase.py](https://raw.githubusercontent.com/ohbot/ohbot-python/master/tools/SpeechDatabase/SpeechDatabase.py)  

2) Run in IDLE or a Python editor/launcher of your choice. 


Using phrases from your database. 
----------
The speech database tool will read and write from OhbotSpeech.csv found within the ohbotData/ in your working directory. 


To use a phrase in a Ohbot program select it using its set and/or variable for example:


```python

ohbot.getPhrase(1,2)

```
This command would make Ohbot say "how can I help?" if you are using the default speech database as this is the only phrase where set = 1 and variable = 2.   

or

```python

ohbot.say(ohbot.getPhrase(set=1)))
# Ohbot will say a random phrase from set 1.

ohbot.say(ohbot.getPhrase(variable=2))
# Ohbot will say a random phrase with variable = 2.

ohbot.say(ohbot.getPhrase())
# Ohbot will say a random phrase from the whole database. 

```
Please ensure you save your program inside the same folder as the speech database tool so they can both access the same copy of the ohbotData folder. See the ohbotData Folder section in the main [README](https://github.com/ohbot/ohbot-python/blob/master/README.md) for more information.
