import ohbot

# A list of voices can be found here: https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/language-support#text-to-speech
# You can register a free Azure account here: https://azure.microsoft.com/en-gb/free/

# Set up the Azure text to speech synth with your subscription key. 
ohbot.setSynthesizer('Azure',ID ="################################")

# This will be spoken in the default Azure voice.
ohbot.say("Woo now my voice comes from Azure")

# Change voice to MiaNeural
ohbot.setVoice("MiaNeural")

ohbot.say("My name is Mia")

# Change voice to HeatherRus and region to Canada.
ohbot.setVoice("HeatherRUS","en-CA")

picoh.say("And I am Heather")


