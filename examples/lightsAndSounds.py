# Example of how to use the play sound function and change the eye colour of Ohbot.

from ohbot import ohbot
import random

ohbot.reset()
ohbot.wait(1)
ohbot.close()
ohbot.move(ohbot.LIDBLINK,0)

ohbot.playSound('fanfare',untilDone = False)
ohbot.wait(1.5)

ohbot.move(ohbot.LIDBLINK,5)

ohbot.wait(1)

ohbot.move(ohbot.LIDBLINK,10)
ohbot.wait(4)

ohbot.playSound('ohbot',untilDone = False)

for x in range(0,40):
    ohbot.setEyeColour(random.randrange(0,10),random.randrange(0,10),random.randrange(0,10))
    ohbot.wait(0.05)
    
ohbot.setEyeColour(0,0,0)
ohbot.wait(0.5)

ohbot.playSound('smash',untilDone = False)
ohbot.setEyeColour(10,0,0)

for x in range(0,14):
    ohbot.move(ohbot.EYETILT,3)
    ohbot.wait(x/100)
    ohbot.move(ohbot.EYETILT,6)
    ohbot.wait(x/100)
    
# Spring, play on a sepereate thread using untilDone = False.  
ohbot.playSound('spring',untilDone = False)

for x in range(0,14):
    ohbot.move(ohbot.EYETURN,3)
    ohbot.wait(x/100)
    ohbot.move(ohbot.EYETURN,7)
    ohbot.wait(x/100)
    ohbot.setEyeColour(x,10-x,0)

ohbot.move(ohbot.EYETURN,5)

ohbot.playSound('loop', untilDone = False)

# The length of a beat in seconds
lengthOfBeat = 0.565

for x in range(0,8):

    ohbot.move(ohbot.HEADNOD,6)
    ohbot.setEyeColour(x,10-x,0)

    ohbot.wait(lengthOfBeat/2)
    
    ohbot.move(ohbot.HEADTURN,7)
    ohbot.move(ohbot.HEADNOD,4)
    ohbot.setEyeColour(0,x,10-x)

    ohbot.wait(lengthOfBeat/2)
    ohbot.setEyeColour(10-x,x,0)

    ohbot.move(ohbot.HEADNOD,6)

    ohbot.wait(lengthOfBeat/2)

    ohbot.move(ohbot.HEADTURN,3)
    ohbot.move(ohbot.HEADNOD,4)
    ohbot.setEyeColour(0,10-x,x)

    ohbot.wait(lengthOfBeat/2)
    
ohbot.reset()
ohbot.wait(1)
ohbot.close()
