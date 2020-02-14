# Ohbot Python setup for Mac

<a href="http://whoosh.co.uk/ohbothelp/images/eyes.gif" target="_blank"><img src="http://whoosh.co.uk/ohbothelp/images/eyes.gif" border="0" width = "30%"/></a>


Background
-----

These instructions allow you to program your Ohbot using Python on a Mac.

More information about Ohbot can be found on [ohbot.co.uk.](http://www.ohbot.co.uk)

Please contact [info@ohbot.co.uk.](info@ohbot.co.uk) if you have any problems installing or running Ohbot.


Setup
--------

Install the latest version of Python from [here.](https://www.python.org/downloads/release/python-364/)

Open the Terminal app and type the folloing:

``sudo pip3 install ohbot``

You can find the Terminal app by searching for it in spotlight.

<a href="https://github.com/ohbot/ohbot-python/blob/master/images/ss.png" target="_blank"><img src="https://github.com/ohbot/ohbot-python/blob/master/images/ss.png" border="0" width = "60%"/></a>

Dependencies
----------

The ``pip3 install ohbot`` command will install the following libraries:


| Library    | Use         | Terminal command to install  |Link |
| ---------- |-------------| -----------------------------|-----|
| ohbot   | Interface with Ohbot          | ```pip3 install ohbot```  |[ohbot](https://github.com/ohbot/ohbotWin-python/) 
| serial    | Communicate with serial port| ```pip3 install pyserial```  |[pyserial](https://github.com/pyserial/pyserial/) |
| lxml    | Import settings file          | ```pip3 install lxml```  |[lxml](https://github.com/lxml/lxml) |
| playsound    | Play sound files       | ```pip3 install playsound```  |[playsound](https://github.com/TaylorSMarks/playsound) |
| pyobjc    | Python Objective C library       | ```pip3 install objc```  |[pyobjc](https://pypi.org/project/pyobjc/) |



To upgrade to the latest version of the library run the following in the console:
<br>
```sudo pip3 install ohbot --upgrade```


Ohbot library files (these will be installed with the `sudo pip3 install ohbot` command above):

| File    | Use         |
| ---------- |------------|
| ohbot.py   | Ohbot package |
| MotorDefinionsv21.omd    | Motor settings file |
| OhbotSpeech.csv    | Speech database file |
| OhbotSettings.xml    | Settings file |
| Sounds/    | Folder containing Ohbot preset sound files |

_Note: The text to speech module will generate an audio file, ‘ohbotspeech.wav’_

---

Hardware
-----

Required:


* Mac running OSX
* Ohbot
* USB Y Cable
* A 5 volt 1 amp USB power supply (for Ohbot)
* Speakers/headphones.


Setup:


Plug the middle of USB Y cable into the PC and the other large USB plug into the power adaptor. Then plug the mini USB into Ohbot. (Note with newer devices the power adaptor may not be required.)

---

Starting Python Programs
--------

Open <b>IDLE</b> from <b>Applications</b>.

Select <b>New</b> from the <b>File menu.</b>

Go to the [hellworldohbot](https://github.com/ohbot/ohbot-python/blob/master/examples/helloworldohbot.py) example on Github, copy the code and paste it into the new Python window.

Select <b>Run Module</b> from the <b>Run</b> menu.

Ohbot should speak and move.

More example programs can be found [here.](https://github.com/ohbot/ohbot-python/tree/master/examples)
