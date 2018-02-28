from distutils.core import setup

setup(
    name = 'ohbot',
    packages = ['ohbot'],
    package_data={'': ['MotorDefinitionsv21.omd','Silence1.wav']},
    include_package_data=True,
    version = '2.4',  
    description = 'description',
    author = 'ohbot',
    author_email = 'info@ohbot.co.uk',
    url = 'https://github.com/ohbot/ohbot.git',
    download_url = 'https://github.com/ohbot/ohbot-python/archive/2.4.tar.gz',
    keywords = ['ohbot', 'robot'],
    classifiers = [],
    install_requires=[
          'pyserial','lxml',
      ],
)
