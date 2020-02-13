# Ohbot for Python

More information about Ohbot can be found on [ohbot.co.uk](http://www.ohbot.co.uk)

<a href="http://whoosh.co.uk/ohbothelp/images/eyes.gif" target="_blank"><img src="http://whoosh.co.uk/ohbothelp/images/eyes.gif" border="0" width = "30%"/></a>

This package is a starting point for people wanting to use Python 3 to control Ohbot. Choose your platform and click the links to get started!

|||||
|-------|-------|---------|-------|
|macOS|[Getting Started](https://github.com/ohbot/ohbot-python/blob/master/Docs/Setup_Mac.md)|[Examples](https://github.com/ohbot/ohbot-python/tree/master/examples/)|[Text to speech documentation](https://github.com/ohbot/ohbot-python/blob/master/Docs/VoiceDoc_Mac.md)|
|Windows|[Getting Started](https://github.com/ohbot/ohbot-python/blob/master/Docs/Setup_Windows.md)|[Examples](https://github.com/ohbot/ohbot-python/tree/master/examples/)|[Text to speech documentation](https://github.com/ohbot/ohbot-python/blob/master/Docs/VoiceDoc_Windows.md)|
|Pi|[Getting Started](https://github.com/ohbot/ohbot-python/blob/master/Docs/Setup_Pi.md)|[Examples](https://github.com/ohbot/ohbot-python/tree/master/examples/)|[Text to speech documentation](https://github.com/ohbot/ohbot-python/blob/master/Docs/VoiceDoc_Pi.md)|


If you are new to Python here is a short guide explaining some of the key concepts: [Programming Ohbot in Python](https://docs.google.com/document/d/e/2PACX-1vTM9FmTBpGGJ4Ddvutpv3kxXkS0oyT4U9JPBV95UXdSJU10TD5JC1XWTf2cRGjHWApHOrTC6JLizD64/pub)

To be expanded soon!

ohbotData Folder
-------
The first time you run a Ohbot program a new folder called ohbotData is created in your working directory. This folder is used to store various files that you can read from within your Ohbot programs, these include a SpeechDatabase file, a Motor Definitions file and an EyeShapes file. 


There are a various tools you can use to help edit these data files. When using a tool please download it and save it in the same folder as the your Ohbot program file, this will ensure it is reading and writing to the correct folder. 


The data files include: 

* ohbotspeech.csv - Holds phrases for Picoh to say. Edit using the  [Speech Database Tool.](https://github.com/ohbot/ohbot-python/tree/master/tools/SpeechDatabase) Phrases are accessed using ohbot.getPhrase(), see below for more information. 

* MotorDefinitionsv21.omd - Holds motor minimums, maximums and ranges.

* Sounds/... - A folder that can be accessed using the ohbot.playSound() function. See the [lightAndSounds example](https://raw.githubusercontent.com/ohbot/ohbot-python/master/examples/lightsAndSounds.py) for more information. The ohbot library copies 5 sounds to get you started, add your own by putting move sound files in the sounds folder. .wav's only for now. Preloaded sounds are: 'spring', 'smash', 'loop', 'ohbot' and 'fanfare' 

If you delete a file in ohbotData (or the whole folder) the default files will be copied back over from the ohbot library folder.  

You can share the ohbotData between multiple programs by saving them in the same folder. 

For example:
```
ohbotProgramsFolder
│   ohbotTest1.py
|   ohbotTest2.py
│   EyeShapeDesigner.py 
|   SpeechDatabse.py 
│   Calibrate.py   
|
└───ohbotData (Created Automatically)
    |   Ohbot.obe
    |   MotorDefinitionsv21.omd
    |   ohbotspeech.csv
    └───Sounds/...
```
Alternatively you can have seperate ohbotData folders by saving your programs in different folders, you will need a copy of the tools you want to use in the folder as well:
```
ohbotProgramsFolder
└───folderOne
│   │   ohbotTest1.py
│   │   Calibrate.py 
│   │   EyeShapeDesigner.py
|   |   SpeechDatabase.py
|   |   
│   └───ohbotData (Created Automatically)
│       |   Ohbot.obe
│       |   MotorDefinitionsv21.omd
│       |   ohbotspeech.csv
|       └───Sounds/...
|
└───folderTwo
    │   ohbotTest2.py
    │   Calibrate.py 
    │   EyeShapeDesigner.py
    |   SpeechDatabase.py
    |   
    └───ohbotData (Created Automatically)
        |   Ohbot.obe
        |   MotorDefinitionsPicoh.omd
        |   ohbotspeech.csv
        └───Sounds/...
        
```

Functions
-------

ohbot.init(portName)
----------

Called internally using portName = "ttyACM" but if your port is different you can call it and override this port name. It returns True if the port is found and opened successfully, otherwise it returns false. 

ohbot.move(m, pos, speed=3)
----------


| Name| Range| Description | Default |
| --- |------|-------------|---------|
| m   | 0-6 (int)  | Motor Number| - |
| pos | 0-10 (int)  | Desired Position| - |
| speed | 0-10 (int) | Motor Speed| 3 |


For Example:
```python
ohbot.move(1,7)
```
or
```python
ohbot.move(2,3,1) 
```
or you can use a constant from the library to specify the motor:
```python
ohbot.move(ohbot.EYETURN,3,1) 
```
Motor index reference:

| m | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| ----| --- | --- |  --- |  --- |  --- |  --- |  --- |
| constant | HEADNOD | HEADTURN | EYETURN | LIDBLINK | TOPLIP | BOTTOMLIP | EYETILT | 
  

ohbot.say(text, untilDone=True, lipSync=True, hdmiAudio=False, soundDelay=0)
----------

| Name| Range| Description | Defualt |
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
---

ohbot.eyeColour(r, g, b, swapRandG=False)
----------

Set the colour of Ohbot’s eyes. 

| Name| Range| Description  | Default |
| ---      |------|-------------| ------- |
| r        | 0-10 (int)  | Red| - |
| g        | 0-10 (int)  | Green| - |
| b        | 0-10 (int)  | Blue| - |
| swapRandG| bool | swap r and g value for some older Ohbots | False |


For Example:
```python
ohbot.eyeColour(2,3,8)
```
or 
```python
ohbot.eyeColour(2,3,8,True)
```

---

ohbot.reset()
----------

Resets Ohbot’s motors back to rest positions and turns off Ohbot’s eyes. Useful to start programs with this. You may need an ohbot.wait() after this to give time for the motors to move. 

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

Call to detach all Ohbot’s motors which stops them using power, you can call ohbot.attach(m) or ohbot.detach(m) for individual motors.

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
ohbot.setSynthesizer(synth)
----------

| synth | Full Name |
|----|-------- |
| “festival” | festival speech |
| “espeak” | espeak speech |
| “pico2wave” | pico2wave speech |


For Example:
```python
ohbot.setSynthesizer("espeak")
```

ohbot.setVoice(voice)
------

Use ohbot.setVoice() to set the voice synthesizer:

<b>Using ESPEAK</b>

http://espeak.sourceforge.net/commands.html<br>

| Name| Description|
| --- |------|
| -v followed by a letter code| enter 'espeak --voices' in terminal to see what's available|
|   +m1 to m7   | male voices |
|   +f1 to f4   | remale voices |
|   +croak or whisper   | tone |
|   -a0 to a200   | amplitude |
|   -s80 to s500   | speed |
|   -p0 to p99   | pitch |


Examples:<br>

| Command | Result |
| ------ | ------- |
| ``ohbot.setVoice("-ven+croak")`` | English croaky voice |
| ``ohbot.setVoice("-vzh+m2 -s26")`` | Chinese male voice, Fast |
| ``ohbot.setVoice("-vfr+f1 -p99 -s180")`` | French female whisper voice, medium speed and high pitched |

More examples can be found in our [espeakVoices example program.](https://github.com/ohbot/ohbot-python/blob/master/examples/espeakVoices.py)


**_Press fn + f5 to run your program_**



