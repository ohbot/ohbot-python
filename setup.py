from distutils.core import setup

setup(
    name = 'ohbot',
    packages = ['ohbot'],
    package_data={'': ['MotorDefinitionsv21.omd']},
    include_package_data=True,
    version = '1',  
    description = 'description',
    author = 'ohbot',
    author_email = 'info@ohbot.co.uk',
    url = 'https://github.com/ohbot/ohbotpython.git',
    download_url = 'https://github.com/ohbot/ohbot/archive/v1.tar.gz',
    keywords = ['ohbot', 'robot'],
    classifiers = [],
)

