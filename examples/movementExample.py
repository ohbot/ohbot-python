from ohbot import ohbot

# Reset Ohbot
ohbot.reset()

'''
The ohbot.move() function needs at least 2 arguments: movement name and desired position.

ohbot.HEADTURN
ohbot.HEADNOD
ohbot.EYETURN
ohbot.EYETILT
ohbot.BOTTOMLIP
ohbot.LIDBLINK

position can be any number 0-10.

'''
# Move the HEADTURN motor to 2. 
ohbot.move(ohbot.HEADTURN,2)
ohbot.say("head turn to 2")
# Move the HEADTURN motor to 5.
ohbot.move(ohbot.HEADTURN,5)
ohbot.say("head turn to 5")

# Move the HEADNOD motor to 9. 
ohbot.move(ohbot.HEADNOD,9)
ohbot.say("head nod to 9")
# Move the HEADNOD motor to 5. 
ohbot.move(ohbot.HEADNOD,5)
ohbot.say("head nod to 5")

'''
The ohbot.move() function can also take an optional third arguement 'spd'
to change the speed of the movement. If unspecified speed defaults to 5. 
'''

# Move HEADTURN motor to position 0 at speed 1.
ohbot.move(ohbot.HEADTURN,0,spd=1)
ohbot.say("Head turn to 0, speed 1")

# Wait for motor to move
ohbot.wait(2)

# Move HEADTURN motor to position 10 at speed 1.
ohbot.move(ohbot.HEADTURN,10,spd=1)
ohbot.say("Head turn to 10, speed 1")

# Wait for motor to move
ohbot.wait(1)

# Move HEADTURN motor to position 0 at speed 10.
ohbot.move(ohbot.HEADTURN,0,spd=10)
ohbot.say("Head turn to 0, speed 10")

# Wait for motor to move
ohbot.wait(0.5)

ohbot.move(ohbot.HEADTURN,10,spd=10)
ohbot.say("Head turn to 10, speed 10")

# Wait for motor to move
ohbot.reset()
ohbot.wait(1)

'''
Finally the move function supports another optional argument 'eye'.
This will only have an effect when moving, EYETURN, EYETILT or LIDBLINK.
The eye arguments allows the eyes to be move individually, 0 - Both, 1 - Right, 2 - Left
If unspecified, default value 0 (Both) is used. 
'''


# Blink

for x in range(10,0,-1):
    ohbot.move(ohbot.LIDBLINK,x,eye = 0)
    ohbot.wait(0.04)

for x in range(0,10):
    ohbot.move(ohbot.LIDBLINK,x,eye = 0)
    ohbot.wait(0.04)

# Set both eyes back to 5. 
ohbot.move(ohbot.EYETILT,8)
    
ohbot.wait(1)

# Set both eyes back to 5. 
ohbot.move(ohbot.EYETILT,5)

ohbot.wait(1)

# Set eye turn to 10
ohbot.move(ohbot.EYETURN,10)

ohbot.wait(1)

# set eye turn to 0. 
ohbot.move(ohbot.EYETURN,0)

ohbot.wait(1)



ohbot.reset()







