# ohbot for python

<a href="http://s1380.photobucket.com/user/ohbot/media/eyesgif_zpslphplowu.gif.html" target="_blank"><img src="http://i1380.photobucket.com/albums/ah188/ohbot/eyesgif_zpslphplowu.gif" border="0" alt=" photo eyesgif_zpslphplowu.gif" width = "30%"/></a>


This package is a starting point for people wanting to use Python 3 to control Ohbot. 

More information about Ohbot can be found on [ohbot.co.uk](www.ohbot.co.uk.)

Dependencies
----------

Ohbot requires the following libraries be installed:


| Library    | Use         | Terminal command to install  |Link |
| ---------- |-------------| -----------------------------|-----|
| ohbot   | Interface with Ohbot          | ```sudo pip3 install ohbot```  |[ohbot](https://github.com/ohbot/ohbot/) |
| serial    | Communicate with serial port| ```sudo pip3 install pyserial```  |[pyserial](https://github.com/pyserial/pyserial/) |
| fesitival    | Generate text to speech  | ```sudo apt-get install festival```  |- |
| lxml    | Import settings file          | ```sudo apt-get install python3-lxml```  |[lxml](https://github.com/lxml/lxml) |
| threading    | Run multiple threads     | core  |- |
| os    | Send commands to festival       | core  |- |
| time    | Run timers                    | core  |- |


Ohbot is tested with Python 3 running on a Raspberry Pi 3 Model B. 


Ohbot library files (these will be installed with the pip3 command above):

| File    | Use         |
| ---------- |------------|
| ohbot.py   | Ohbot package |
| MotorDefinionsv21.omd    | Motor settings file |

_Note: The text to speech module Festival will generate an audio file, ‘ohbotspeech.wav’ and a text file ‘phonemes.txt’ inside your working folder._

Hardware
-----

Required:


*Raspberry Pi
*Ohbot
*USB Y Cable
*USB Power Socket Adaptor
*Speakers/headphones with 3.5mm headphone jack


Setup:



Plug the middle of USB Y cable into Raspberry Pi and the other large USB plug into the power adaptor. Then plug the mini USB into Ohbot. Finally plug your speakers into your Raspberry Pi. 


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

<br>

Functions
-------

ohbot.move(m,pos,speed = 3)
----------

<table>
<tr>
<td>Name</td>
<td>Range</td>
<td>Description</td>
<td>-</td>
</tr>
<tr>
<td>m</td>
<td>0-6(int)</td>
<td>Motor Number</td>
<td>-</td>
</tr>
<tr>
<td>pos</td>
<td>0-10(int)</td>
<td>Desired Position</td>
<td>-</td>
</tr>
<tr>
<td>speed</td>
<td>0-10(int)</td>
<td>Motor Speed</td>
<td>3</td>
</tr>
</table>


For Example:
```python
ohbot.move(1,7)

ohbot.move(2,3,1) 
```
Motor index reference:
<table>
<tr>
<td>m</td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>3</td>
<td>4</td>
<td>5</td>
<td>6</td>
</tr>
<tr>
<td>motor</td>
<td>HeadNod</td>
<td>HeadTurn</td>
<td>EyeTurn</td>
<td>LidBlink</td>
<td>TopLip</td>
<td>BottomLip</td>
<td>EyeTurn</td>
</tr>

</table>

<br>


ohbot.say(text,untilDone = True,lipSync = True)
----------

<table>
<tr>
<td>Name</td>
<td>Range</td>
<td>Description</td>
<td>Default</td>
</tr>
<tr>
<td>text</td>
<td>“A string with no punctuation”</td>
<td>Words to say</td>
<td>-</td>
</tr>
<tr>
<td>untilDone</td>
<td>bool</td>
<td>Return when finished speaking</td>
<td>True</td>
</tr>
<tr>
<td>lipSync</td>
<td>bool</td>
<td>Move lips in time with speech</td>
<td>True</td>
</tr>
</table>

For Example:
```python
ohbot.say('Hello I am Ohbot')

ohbot.say('Goodbye',False,False)
```

<br>

ohbot.wait(seconds)
----------

Seconds - float or int required wait time. ohbot.wait(1.5)

<table>
<tr>
<td>Name</td>
<td>Range</td>
<td>Description</td>
</tr>
<tr>
<td>seconds</td>
<td>float or int</td>
<td>Length of wait in seconds</td>
</tr>
</table>

For Example:
```python
ohbot.wait(2)

ohbot.wait(0.5)
```

<i>Note: It is important to use ohbot.wait() commands between motor sequential commands for the same motor. </i>

For Example:
```python
ohbot.move(1,7,2)

ohbot.wait(2)

ohbot.move(1,4,2)
```

<br>


ohbot.eyeColour(r,g,b)
----------

Set the colour of Ohbot’s eyes. 

<table>
<tr>
<td>Name</td>
<td>Range</td>
<td>Description</td>
</tr>
<tr>
<td>r</td>
<td>0-10(int)</td>
<td>Red</td>
</tr>
<tr>
<td>g</td>
<td>0-10(int)</td>
<td>Green</td>
</tr>
<tr>
<td>b</td>
<td>0-10(int)</td>
<td>Blue</td>
</tr>
</table>

For Example:
```python
ohbot.eyeColour(2,3,8)
```

<br>

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

<br>

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



