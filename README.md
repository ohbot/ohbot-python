# Ohbot for Python

More information about Ohbot can be found on [ohbot.co.uk](http://www.ohbot.co.uk)

<a href="http://whoosh.co.uk/ohbothelp/images/eyes.gif" target="_blank"><img src="http://whoosh.co.uk/ohbothelp/images/eyes.gif" border="0" width = "30%"/></a>

This package is a starting point for people wanting to use Python 3 to control Ohbot. Choose your platform and click the links to get started!

|||||
|-------|-------|---------|-------|
|macOS|[Getting Started](https://github.com/ohbot/ohbot-python/blob/master/Docs/Setup_Mac.md)|[Examples](https://github.com/ohbot/ohbot-python/tree/master/examples/)|[Text to speech documentation](https://github.com/ohbot/ohbot-python/blob/master/Docs/VoiceDoc_Mac.md)|
|Windows|[Getting Started](https://github.com/ohbot/ohbot-python/blob/master/Docs/Setup_Windows.md)|[Examples](https://github.com/ohbot/ohbot-python/tree/master/examples/)|[Text to speech documentation](https://github.com/ohbot/ohbot-python/blob/master/Docs/VoiceDoc_Windows.md)|
|Pi|[Getting Started](https://github.com/ohbot/ohbot-python/blob/master/Docs/Setup_Pi.md)|[Examples](https://github.com/ohbot/ohbot-python/tree/master/examples/)|[Text to speech documentation](https://github.com/ohbot/ohbot-python/blob/master/Docs/VoiceDoc_Pi.md)|

If you are new to Python here is a short guide explaining some of the key concepts: [Programming Ohbot in Python](https://docs.google.com/document/d/e/2PACX-1vRoe6kxmSYFnR3upGNZuBgTO31c5xkpoxtLbrVmalGlT7IYsCmaV4DJ4QhnCDMo-kMslbZNtnSbDWfj/pub)

To be expanded soon!

ohbotData Folder
-------
The first time you run an Ohbot program a new folder called ohbotData is created in your working directory. This folder is used to store various files that you can read from within your Ohbot programs, these include a SpeechDatabase file, motor definitions and a Sounds folder.

There are a various tools you can use to help edit these data files. When using a tool please download it and save it in the same folder as the your Ohbot program file, this will ensure it is reading and writing to the correct folder. 


The data files include: 

* ohbotspeech.csv - Holds phrases for Ohbot to say. Edit using the  [Speech Database Tool.](https://github.com/ohbot/ohbot-python/tree/master/tools/SpeechDatabase) Phrases are accessed using ohbot.getPhrase(), see below for more information. 

* MotorDefinitionsv21.omd - Holds motor minimums, maximums and ranges.

* Sounds/... - A folder that can be accessed using the ohbot.playSound() function. See the [lightAndSounds example](https://raw.githubusercontent.com/ohbot/ohbot-python/master/examples/lightsAndSounds.py) for more information. The ohbot library copies 5 sounds to get you started, add your own by putting move sound files in the sounds folder. .wav's only for now. Preloaded sounds are: 'spring', 'smash', 'loop', 'ohbot' and 'fanfare' 

If you delete a file in ohbotData (or the whole folder) the default files will be copied back over from the ohbot library folder.  

You can share the ohbotData folder between multiple programs by saving them in the same folder. 

For example:
```
ohbotProgramsFolder
│   ohbotTest1.py
|   ohbotTest2.py
|   SpeechDatabse.py 
|
└───ohbotData (Created Automatically)
    |   MotorDefinitionsv21.omd
    |   ohbotspeech.csv
    └───Sounds/...
```
Alternatively you can have seperate ohbotData folders by saving your programs in different folders, you will need a copy of the tools you want to use in the folder as well:
```
ohbotProgramsFolder
└───folderOne
│   │   ohbotTest1.py
|   |   SpeechDatabase.py
|   |   
│   └───ohbotData (Created Automatically)
│       |   MotorDefinitionsv21.omd
│       |   ohbotspeech.csv
|       └───Sounds/...
|
└───folderTwo
    │   ohbotTest2.py
    |   SpeechDatabase.py
    |   
    └───ohbotData (Created Automatically)
        |   MotorDefinitionsv21.omd
        |   ohbotspeech.csv
        └───Sounds/...
 ```       
Functions
-------

ohbot.init(portName)
----------

Called internally looking for a port with name containing "USB Serial Device" but if your port is different you can call it and override this port name. It returns True if the port is found and opened successfully, otherwise it returns false. This is likely with Operating Systems in languages other than English.

ohbot.move(m, pos, speed=5)
----------


| Name| Range| Description | Default |
| --- |------|-------------|---------|
| m   | 0-6 (int)  | Motor Number| - |
| pos | 0-10 (int)  | Desired Position| - |
| speed | 0-10 (int) | Motor Speed| 5 |


For Example:

```python
ohbot.move(1,7)
```
or
```python
ohbot.move(2,3,speed=1) 
```
or you can use a constant from the library to specify the motor:
```python
ohbot.move(ohbot.EYETURN,speed=3) 
```

Motor index reference:

| m | 0 | 1 | 2 | 3 | 5 | 6 |
| ----| --- | --- |  --- |  --- |  --- |  --- |
| constant | HEADNOD | HEADTURN | EYETURN | LIDBLINK | BOTTOMLIP | EYETILT | 
  
---

ohbot.say(text, untilDone=True, lipSync=True, hdmiAudio=False, soundDelay=0)
---------

| Name| Range| Description | Default |
| --- |------|-------------|---------|
| text   | 'A string with no punctuation'  | Words to say| - |
| untilDone | bool  | Return when finished speaking| True |
| lipSync | bool | Move lips in time with speech| True |
| hdmiAudio | bool | Fixes missing start of phrase when HDMI audio output is being used| False |
| soundDelay | float | Set to positive if lip movement is lagging behind sound and negative if sound is lagging behind lip movement| 0 |

For Example:
```python
ohbot.say('Hello I am Ohbot')

ohbot.say('Goodbye',False,False)

ohbot.say('Goodbye',False,False,True)

ohbot.say('Goodbye',soundDelay = 0.3)
```
---

More info on speech
---

Platform specific documentation for setting voices and languages:


* [macOS](https://github.com/ohbot/ohbot-python/blob/master/Docs/VoiceDoc_Mac.md)

* [Windows](https://github.com/ohbot/ohbot-python/blob/master/Docs/VoiceDoc_Windows.md)

* [Pi](https://github.com/ohbot/ohbot-python/blob/master/Docs/VoiceDoc_Pi.md)


ohbot.wait(seconds)
----------

Seconds - float or int required wait time. ohbot.wait(1.5)

| Name| Range| Description  |
| --- |------|-------------|
| seconds   | float or int  | Length of wait in seconds|


For Example:
```python
ohbot.wait(2)

ohbot.wait(0.5)
```

*Note: It is important to use ohbot.wait() commands between motor sequential commands for the same motor.*

For Example:
```python
ohbot.move(1,7,2)

ohbot.wait(2)

ohbot.move(1,4,2)
```

ohbot.getPhrase(set,variable)
------

set: Int - The desired set for phrase. 
variable: Int - The desired variable for phrase. 

Use ohbot.getPhrase() to retrieve a phrase from Ohbot's speech database. 

You can view and edit the speech database using the Speech Databse tool. Each entry in the speech database has a set and a variable associated with it. When you use getPhrase() you can choose to get phrases with specific values for set and/or variable.  

If more than one phrase matches the set and variable provided a random match is returned. 

To see available phrases and write your own see the [Speech Database Tool](https://github.com/ohbot/ohbot-python/tree/master/tools/SpeechDatabase). 

For Example:
```python

ohbot.say(ohbot.getPhrase(1,2))

```
or get a random phrase from a specific set:
```python

ohbot.say(ohbot.getPhrase(set=1)))
# Ohbot will say a random phrase from set 1.

ohbot.say(ohbot.getPhrase(variable=2))
# Ohbot will say a random phrase with variable = 2.
```

or get a random phrase from the whole database:
```python

ohbot.say(ohbot.getPhrase())

```

ohbot.eyeColour(r, g, b)
----------

Set the colour of Ohbot’s eyes. (This feature requires the [Illuminating Eyes Ohbot accessory.](https://www.ohbot.co.uk/store/p11/Illuminating_Eyes_for_Ohbot.html))

| Name| Range| Description  | Default |
| ---      |------|-------------| ------- |
| r        | 0-10 (int)  | Red| - |
| g        | 0-10 (int)  | Green| - |
| b        | 0-10 (int)  | Blue| - |


For Example:
```python
ohbot.eyeColour(2,3,8)
```

---

ohbot.reset()
----------

Resets Ohbot's motors back to rest positions and turns off Ohbot's eye LEDs. Useful to start programs with this. You may need an ohbot.wait() after this to give time for the motors to move. 

For Example:
```python
ohbot.reset()
ohbot.move(1,7,2)
ohbot.wait(1)
ohbot.move(1,1)
...
```
---

ohbot.close()
----------

Call to detach all Ohbot's motors which stops them using power, you can call ohbot.attach(m) or ohbot.detach(m) for individual motors.

For Example:
```python
ohbot.move(1,7,2)
ohbot.wait(1)
ohbot.move(1,1)

ohbot.close()
```
---

ohbot.readSensor(sensorNumber)
----------

| Name| Range| Description  |
| --- |------|-------------|
| sensorNumber   | 0-6 (int) | the pin the sensor is connected to |

returns the value as a float 0 - 10.

For Example:
```python
reading = ohbot.readSensor(3)
ohbot.move(ohbot.HEADTURN, reading)
```

ohbot.playSound(sound,untilDone = True)
----------

sound - string name of sound.

untilDone - wait till sound has finished before moving to next line in  your program. Defaults to True. Set this to False to play the sound on a seperate thread, allowing your program to continue while it is playing. 

Sounds are read from ohbotData/Sounds/ add new sound files to this folder to access them. .wav files only for the moment. When writing the file name in your program please do not include the .wav file extension. 

Some demo sounds will be pre installed:

* fanfare
* loop
* ohbot
* smash
* spring

For Example:
```python
ohbot.playSound('fanfare')

```
or

```python
ohbot.playSound('spring',False)

```
