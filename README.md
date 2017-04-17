# ohbot for python

<a href="http://s1380.photobucket.com/user/ohbot/media/eyesgif_zpslphplowu.gif.html" target="_blank"><img src="http://i1380.photobucket.com/albums/ah188/ohbot/eyesgif_zpslphplowu.gif" border="0" alt=" photo eyesgif_zpslphplowu.gif" width = "30%"/></a>


This package is a starting point for people wanting to use Python 3 to control Ohbot. 

More information about Ohbot can be found on [ohbot.co.uk](http://www.ohbot.co.uk)

Dependencies
----------

Ohbot requires the following libraries be installed:


| Library    | Use         | Terminal command to install  |Link |
| ---------- |-------------| -----------------------------|-----|
| ohbot   | Interface with Ohbot          | ```sudo pip3 install ohbot```  |[ohbot](https://github.com/ohbot/ohbot/) |
| serial    | Communicate with serial port| ```sudo pip3 install pyserial```  |[pyserial](https://github.com/pyserial/pyserial/) |
| fesitival    | Generate text to speech  | ```sudo apt-get install festival```  |- |
| lxml    | Import settings file          | ```sudo apt-get install python3-lxml```  |[lxml](https://github.com/lxml/lxml) |
| threading    | Run multiple threads     | Included in Python 3  |- |
| os    | Send commands to festival       | Included in Python 3  |- |
| time    | Run timers                    | Included in Python 3  |- |


Ohbot is tested with Python 3 running on a Raspberry Pi 3 Model B. 


Ohbot library files (these will be installed with the pip3 command above):

| File    | Use         |
| ---------- |------------|
| ohbot.py   | Ohbot package |
| MotorDefinionsv21.omd    | Motor settings file |

_Note: The text to speech module Festival will generate an audio file, ‘ohbotspeech.wav’ and a text file ‘phonemes.txt’ inside your working folder._

---

Hardware
-----

Required:


* Raspberry Pi
* Ohbot
* USB Y Cable
* USB Power Socket Adaptor
* Speakers/headphones with 3.5mm headphone jack


Setup:



Plug the middle of USB Y cable into Raspberry Pi and the other large USB plug into the power adaptor. Then plug the mini USB into Ohbot. Finally plug your speakers into your Raspberry Pi. 

---

Writing Programs
--------

1. Open Python 3 (IDLE)
2. Click File → New File
3. Save your file as a python script (.py) in a new folder called Ohbot somewhere on your Pi.

Import
-------

Make sure you import ohbot at the start of your program. 
```python
From ohbot import ohbot
```

---

Functions
-------

ohbot.move(m,pos,speed = 3)
----------


| Name| Range| Description | Defualt |
| --- |------|-------------|---------|
| m   | 0-6 (int)  | Motor Number| - |
| pos | 0-10 (int)  | Desired Postition| - |
| speed | 0-10 (int) | Motor Speed| 3 |


For Example:
```python
ohbot.move(1,7)

ohbot.move(2,3,1) 
```
Motor index reference:

| m | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| ----| --- | --- |  --- |  --- |  --- |  --- |  --- |
| motor | HeadNod | HeadTurn | EyeTurn | LidBlink | TopLip | Bottom Lip| EyeTurn | 
  

ohbot.say(text,untilDone = True,lipSync = True)
----------

| Name| Range| Description | Defualt |
| --- |------|-------------|---------|
| text   | 'A string with no punctuation'  | Words to say| - |
| untilDone | bool  | Return when finished speaking| True |
| lipSync | bool | Move lips in time with speech| True |


For Example:
```python
ohbot.say('Hello I am Ohbot')

ohbot.say('Goodbye',False,False)
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

ohbot.eyeColour(r,g,b)
----------

Set the colour of Ohbot’s eyes. 

| Name| Range| Description  |
| --- |------|-------------|
| r   | 0-10 (int)  | Red|
| g   | 0-10 (int)  | Green|
| b   | 0-10 (int)  | Blue|


For Example:
```python
ohbot.eyeColour(2,3,8)
```
---

ohbot.reset()
----------

Resets Ohbot’s motors back to rest positions and turns off Ohbot’s eyes. Useful to start programs with this. 

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

Call at the end of your program to detach Ohbot’s motors.

For Example:
```python
ohbot.move(1,7,2)
ohbot.wait(1)
ohbot.move(1,1)

ohbot.close()
```

**_Press fn + f5 to run your program_**



