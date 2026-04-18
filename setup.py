from distutils.core import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name = 'ohbot',
    packages = ['ohbot'],
      package_data={'': ['OhbotSettings.xml','Silence1.wav','ohbotspeech.wav','OhbotSpeech.csv','ohbot.obe','phonemes.txt','Images/movedown.gif','Images/moveright.gif','Images/off.gif','Images/offsmaller.gif','Images/on.gif','Images/onsmaller.gif','Images/picohlogo.gif','Images/picohlogoOn.gif','Images/picohlogoSmall.gif','Images/ohbotlogoSmall.gif','Images/logoPTOH.gif','Images/calibrate400.gif','Images/plus.gif','Images/resetIcon.gif','Images/savebutton.gif','Images/logoPT.gif','MotorDefinitionsv21.omd','Images/pixel.gif','Sounds/fanfare.wav','Sounds/loop.wav','Sounds/ohbot.wav','Sounds/smash.wav','Sounds/spring.wav']},
    include_package_data=True,
    version = '4.0.18',
    description = 'Python library for controlling an Ohbot Robot',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    author = 'ohbot',
    author_email = 'info@ohbot.co.uk',
    url = 'https://github.com/ohbot/ohbot-python',
    download_url = 'https://github.com/ohbot/ohbot-python/archive/refs/tags/v4.0.18.tar.gz',
    keywords = ['ohbot', 'robot','picoh'],
    classifiers = [],
    install_requires=[
        'pyserial',
        'requests',
        'numpy',
        'lxml; platform_system == "Windows" or platform_system == "Darwin"',
        'playsound3; platform_system == "Darwin" or platform_system == "Linux"',
        'comtypes; platform_system == "Windows" or platform_system == "Darwin"',
        'gTTS; platform_system == "Linux"',
        'pydub; platform_system == "Linux"',
    ],
)
