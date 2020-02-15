from ohbot import ohbot
import random

ohbot.reset()

ohbot.wait(0.2)

ohbot.say("Commencing hardware tests")

ohbot.say("Eyes to red")
ohbot.setEyeColour(10,0,0,True)

ohbot.say("Eyes to green")
ohbot.setEyeColour(0,10,0,True)

ohbot.say("Eyes to blue")
ohbot.setEyeColour(0,0,10,True)

ohbot.say("HeadTurn motor 0 to 10")

for x in range(0,10):

    ohbot.move(ohbot.HEADTURN,x)
    ohbot.wait(0.2)
    
ohbot.move(ohbot.HEADTURN,5)

ohbot.say("HeadNod motor 0 to 10")

for x in range(0,10):

    ohbot.move(ohbot.HEADNOD,x)
    ohbot.wait(0.2)

ohbot.move(ohbot.HEADNOD,5)

ohbot.say("Commencing random movement")

count = 0

while count < 10:
    ohbot.move(ohbot.HEADTURN,random.randint(2, 8))
    ohbot.move(ohbot.HEADNOD,random.randint(2, 8))
    ohbot.move(ohbot.EYETILT,random.randint(2, 8))
    ohbot.move(ohbot.EYETURN,random.randint(2, 8))
    count = count + 1
    ohbot.wait(random.random()*2)

ohbot.reset()

ohbot.say("playing sound")

ohbot.playSound('spring')

ohbot.say("Random phrase from speech database")

ohbot.say(ohbot.getPhrase())

ohbot.reset()
ohbot.say("Goodbye")
ohbot.wait(1)
ohbot.close()

