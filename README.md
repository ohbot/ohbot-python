# ohbot for python

ohbot
========================

This package is a starting point for people wanting to use Python 3 to control Ohbot. 

Dependencies
----------

Ohbot requires the following libraries be installed:


<img src="http://i1380.photobucket.com/albums/ah188/ohbot/table1_zpsdh5r28rl.png" width="70%">


Ohbot is tested with Python 3 running on a Raspberry Pi 3 Model B. 


Ohbot library files: (these will be installed with the pip3 command above)

<img src="http://i1380.photobucket.com/albums/ah188/ohbot/table2_zpskejkvuhc.png" width="70%">

<table border="1">
<tr>
<td>Row 1, Column 1</td>
<td>Row 1, Column 2</td>
</tr>
<tr>
<td>Row 2, Column 1</td>
<td>Row 2, Column 2</td>
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

ohbot.move(m,pos,speed = 3)


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






