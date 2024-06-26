from distutils.core import setup

import platform

if platform.system() == "Darwin":
    includes =['pyserial','lxml','playsound','numpy','comtypes','requests']

if platform.system() == "Windows":
    includes =['pyserial','lxml','playsound','numpy','comtypes','requests']

if platform.system() == "Linux":
    includes =['pyserial','playsound','gTTS','pydub','requests']

setup(
    name = 'ohbot',
    packages = ['ohbot'],
      package_data={'': ['OhbotSettings.xml','Silence1.wav','ohbotspeech.wav','OhbotSpeech.csv','ohbot.obe','phonemes.txt','Images/movedown.gif','Images/moveright.gif','Images/off.gif','Images/offsmaller.gif','Images/on.gif','Images/onsmaller.gif','Images/picohlogo.gif','Images/picohlogoOn.gif','Images/picohlogoSmall.gif','Images/ohbotlogoSmall.gif','Images/logoPTOH.gif','Images/calibrate400.gif','Images/plus.gif','Images/resetIcon.gif','Images/savebutton.gif','Images/logoPT.gif','MotorDefinitionsv21.omd','Images/pixel.gif','Sounds/fanfare.wav','Sounds/loop.wav','Sounds/ohbot.wav','Sounds/smash.wav','Sounds/spring.wav']},
    include_package_data=True,
    version = '4.0.14',
    description = 'Python library for controlling an Ohbot Robot',
    author = 'ohbot',
    author_email = 'info@ohbot.co.uk',
    url = 'https://github.com/ohbot/ohbot-python',
    download_url = 'https://github.com/ohbot/ohbot-python/archive/4.0.14.tar.gz',
    keywords = ['ohbot', 'robot','picoh'],
    classifiers = [],
    install_requires= includes,
)
