# Ohbot Python Setup for Windows

<a href="http://whoosh.co.uk/ohbothelp/images/eyes.gif" target="_blank"><img src="http://whoosh.co.uk/ohbothelp/images/eyes.gif" border="0" width = "30%"/></a>

Background
-----

These instructions allow you to program your Ohbot using Python on a Windows PC.

More information about Ohbot can be found on [ohbot.co.uk.](http://www.ohbot.co.uk)

Please contact [info@ohbot.co.uk.](info@ohbot.co.uk) if you have any problems installing or running Ohbot.

Setup
--------
Download a Python installer from [here.](https://www.python.org/downloads/release/python-364/) On Windows the Ohbot library currently only works with Python versions up to 3.6.

We chose version 3.6 Windows x86-64 executable installer.

<a href="https://github.com/ohbot/ohbotWin-python/blob/master/images/screenshot4.jpg" target="_blank"><img src="https://github.com/ohbot/ohbotWin-python/blob/master/images/screenshot4.jpg" border="0" width = "65%"/></a>

Tick the option to Add Python 3.6 to PATH then click on Install Now.

Once install is complete type “Command” into the Windows search box.  Right click on <b>Command Prompt </b> and select <b>Run as administrator.</b>

<br>

<a href="https://github.com/ohbot/ohbotWin-python/blob/master/images/image2-24.tif" target="_blank"><img src="https://github.com/ohbot/ohbotWin-python/blob/master/images/image2-24.tif" border="0" width = "35%"/></a>

<br>

This will open a command prompt window. 

Type the folloing:

``pip install ohbot``

To upgrade to the latest version of the library run the following in the console:
```pip install ohbot --upgrade```

Installing more voices (optional)
--------

The Ohbot Python library will default to using SAPI voices which are the voices that are available through Windows Control Panel:Speech Propeties.

You can change this to espeak or espeak-ng by calling ohbot.setSynthesiser (“espeak”) or ohbot.setSynthesizer (“espeak-ng”).

Install the espeak library from [here.](http://espeak.sourceforge.net/download.html)


Install espeak and then copy the espeak.exe file in Windows File Explorer from 

C:\Program Files (x86)\eSpeak\command_line

To 

C:\Program Files\Python36

To use the espeak-ng library install it from [here.](https://github.com/espeak-ng/espeak-ng#binaries)

Install espeak-ng and then copy the espeak-ng.exe and espeak-ng.dll files in Windows File Explorer from 

C:\Program Files\eSpeak NG

To 

C:\Program Files\Python36

That should be it for the setup.

Dependencies
----------

The ``pip install ohbot`` command will install the following libraries:


| Library    | Use         | Terminal command to install  |Link |
| ---------- |-------------| -----------------------------|-----|
| ohbot   | Interface with Ohbot          | ```pip install ohbotWin```  |[ohbot](https://github.com/ohbot/ohbot-python/) 
| serial    | Communicate with serial port| ```pip install pyserial```  |[pyserial](https://github.com/pyserial/pyserial/) |
| lxml    | Import settings file          | ```pip install lxml```  |[lxml](https://github.com/lxml/lxml) |
| comtypes    | Required for serial communication      | ```pip install comtypes```  | [comtypes](https://github.com/enthought/comtypes) |


To upgrade to the latest version of the library run the following in the console:
```pip install ohbot -- upgrade```



Ohbot library files (these will be installed with the `pip install ohbot` command above):

| File    | Use         |
| ---------- |------------|
| ohbot.py   | Ohbot package |
| MotorDefinionsv21.omd    | Motor settings file |
| OhbotSpeech.csv    | Speech database file |
| OhbotSettings.xml    | Settings file |
| Sounds/    | Folder containing Picoh preset sound files |

_Note: The text to speech module will generate an audio file, ‘ohbotspeech.wav’ and a text file ‘phonemes.txt’ inside your working folder._

---

Hardware
-----

Required:


* PC Running Windows.
* Ohbot
* USB Y Cable
* A 5 volt 1 amp USB power supply (for Ohbot)
* Speakers/headphones.


Setup:


Plug the middle of USB Y cable into the PC and the other large USB plug into the power adaptor. Then plug the mini USB into Ohbot.

---

Starting Python Programs
--------

Go to the Windows Menu and run IDLE from the Python folder:


<a href="https://github.com/ohbot/ohbotWin-python/blob/master/images/image3-26.tif" target="_blank"><img src="https://github.com/ohbot/ohbotWin-python/blob/master/images/image3-26.tif" border="0" width = "35%"/></a>


Select <b>New</b> from the <b>File menu.</b>

Go to the [hellworldohbot](https://github.com/ohbot/ohbot-python/blob/master/examples/helloworldohbot.py) example on Github, copy the code and paste it into the new Python window.

Select <b>Run Module</b> from the <b>Run</b> menu.

Ohbot should speak and move.

More example programs can be found [here.](https://github.com/ohbot/ohbot-python/tree/master/examples)



