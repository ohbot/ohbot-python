# Ohbot Python setup for Pi

<a href="http://whoosh.co.uk/ohbothelp/images/eyes.gif" target="_blank"><img src="http://whoosh.co.uk/ohbothelp/images/eyes.gif" border="0" width = "30%"/></a>

This package is a starting point for people wanting to use Python 3 on a Raspberry Pi to control Ohbot. 

More information about Ohbot can be found on [ohbot.co.uk](http://www.ohbot.co.uk) Please contact [info@ohbot.co.uk.](info@ohbot.co.uk) if you have any problems installing or running Ohbot. 

Dependencies
----------

If you don't have Python or pip3 (the Python package manager) installed, open terminal and execute the following, one line at a time:

```
sudo apt-get install python3
sudo apt-get install python3-pip
```

Ohbot requires some libraries to be installed execute the following to install lxml, festival and finally the ohbot package. 

```
sudo apt-get install python3-lxml
sudo apt-get install festival
sudo pip3 install ohbot
```

Additonal voices can be used by installing ```espeak``` and ```pico2wave```

 ```
 sudo apt-get install espeak
 sudo apt-get install libttspico-utils
 ```
 
| Library    | Use         | Terminal command to install  |Link |
| ---------- |-------------| -----------------------------|-----|
| picoh   | Interface with Picoh          | ```sudo pip3 install ohbot``` |[ohbot](https://github.com/ohbot/ohbot-python/) |
| festival    | Generate text to speech  | ```sudo apt-get install festival```  |- |
| espeak (optional)    | Generate text to speech  | ```sudo apt-get install espeak```  |[espeak](http://espeak.sourceforge.net/) |
| pico2wave (optional)    | Generate text to speech  | ```sudo apt-get install libttspico-utils```  |-|
| lxml    | Import settings file          | ```sudo apt-get install python3-lxml``` |[lxml](https://github.com/lxml/lxml) |
| serial    | Communicate with serial port | Included with Ohbot |[pyserial](https://github.com/pyserial/pyserial/) |
| threading    | Run multiple threads     | Included in Python 3  |- |
| os    | Send commands to festival       | Included in Python 3  |- |
| time    | Run timers                    | Included in Python 3  |- |


Ohbot is tested with Python 3 running on a Raspberry Pi 3 Model B. 

To upgrade to the latest version of the library run the following in the console:
```sudo pip3 install ohbot --upgrade```


Ohbot library files (these will be installed with the `pip3 install ohbot` command above):

| File    | Use         |
| ---------- |------------|
| ohbot.py   | Ohbot package |
| MotorDefinionsv21.omd    | Motor settings file |
| OhbotSpeech.csv    | Speech database file |
| OhbotSettings.xml    | Settings file |
| Sounds/    | Folder containing Ohbot preset sound files |

_Note: The text to speech module Festival will generate an audio file, ‘ohbotspeech.wav’ and a text file ‘phonemes.txt’ inside your working folder._

---

Hardware
-----

Required:

* Raspberry Pi
* Ohbot
* USB Y Cable
* A 5 volt 1 amp USB power supply (for Ohbot)
* Speakers/headphones with 3.5mm headphone jack


Setup:

Plug the middle of USB Y cable into Raspberry Pi and the other large USB plug into the power adaptor. Then plug the mini USB into Ohbot. Finally plug your speakers into your Raspberry Pi. 

---

Starting Python Programs
--------

Open <b>IDLE</b> from <b>Applications</b>.

Select <b>New</b> from the <b>File menu.</b>

Go to the [hellworldohbot](https://github.com/ohbot/ohbot-python/blob/master/examples/helloworldohbot.py) example on Github, copy the code and paste it into the new Python window.

Select <b>Run Module</b> from the <b>Run</b> menu.

Ohbot should speak and move.

More example programs can be found [here.](https://github.com/ohbot/ohbot-python/tree/master/examples)
