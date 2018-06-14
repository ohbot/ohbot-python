from ohbot import ohbot


ohbot.reset()

ohbot.setSynthesizer("pico2wave")

ohbot.say("now I can speak using pico2wave text to speech as well")

ohbot.wait(1)

ohbot.close()

