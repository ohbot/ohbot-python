# ohbot for python

ohbot
========================

This package is a starting point for people wanting to use Python 3 to control Ohbot. 

Dependencies
----------

Ohbot requires the following libraries be installed:


<table border="1">
<tr>
<b>
<td>Library</td>
<td>Use</td>
<td>Terminal command to install</td>
</b>
</tr>
<tr>
<td>ohbot</td>
<td>Interface with Ohbot</td>
<td>sudo pip3 install ohbot</td>
</tr>
<tr>
<td>serial</td>
<td>Communicate with serial port</td>
<td>sudo pip3 install pyserial</td>
</tr>
<tr>
<td>fesitival</td>
<td>Generate text to speech</td>
<td>sudo apt-get install festival</td>
</tr>
<tr>
<td>lxml</td>
<td>Import settings file</td>
<td>sudo apt-get install python3-lxml</td>
</tr>
<tr>
<td>threading</td>
<td>Run multiple threads</td>
<td>core</td>
</tr>
<tr>
<td>os</td>
<td>Send commands to festival</td>
<td>core</td>
</tr>
<tr>
<td>time</td>
<td>Run timers</td>
<td>core</td>
</tr>
</table>

Ohbot is tested with Python 3 running on a Raspberry Pi 3 Model B. 


Ohbot library files: (these will be installed with the pip3 command above)

<table border="1">
<tr>
<b>
<td>ohbot.py</td>
<td>Ohbot package</td>
</b>
</tr>
<tr>
<td>MotorDefinionsv21.omd</td>
<td>Motor settings file.</td>
</tr>
</table>

<i> Note: The text to speech module Festival will generate an audio file, ‘ohbotspeech.wav’ and a text file ‘phonemes.txt’ inside your working folder. </i>

Hardware
-----

Raspberry Pi
Ohbot
USB Y Cable
USB Power Socket Adaptor
Speakers/headphones with 3.5mm headphone jack

Plug middle of USB Y cable into Raspberry Pi and the other large plug into the power adaptor. Then plug the mini usb into Ohbot.

Plug in speakers. 


Writing Programs
--------

1.Open Python 3 (IDLE)
2.Click File → New File
3.Save your file as a python script (.py) in the Ohbot folder you created earlier

Import
-------

Make sure you import ohbot at the start of your program. 

From ohbot import ohbot


Functions
-------

<b>ohbot.move(m,pos,speed = 3)</b>

<table border="1">
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

ohbot.move(1,7)
ohbot.move(2,3,1) 



ohbot.say(text,untilDone = True,lipSync = True)



For Example:

ohbot.say(“Hello my name is Ohbot”)
ohbot.say(“Goodbye”,False,False)



ohbot.wait(seconds)

Seconds - float or int required wait time. ohbot.wait(1.5)


For Example:

ohbot.wait(2)
ohbot.wait(0.5)

Note: It is important to use ohbot.wait() commands between motor sequential commands for the same motor. 

For Example:

ohbot.move(1,7,2)
ohbot.wait(2)
ohbot.move(1,4,2)

ohbot.eyeColour(r,g,b)


ohbot.reset()

Resets Ohbot’s motors back to rest positions and turns off Ohbot’s eyes. 

ohbot.close()

Call at the end of your program to detach Ohbot’s motors.

Press fn + f5 to run your program. 


<iframe src="https://docs.google.com/document/d/1fdeQwX18cFidcXlgQg04Bvm2ZvxkuvLu7mM3-8rfrYo/pub?embedded=true"></iframe>





