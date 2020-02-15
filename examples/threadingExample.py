# Example of threading using the ohbot library.
# Threading allows Ohbot to do multiple things at once.
# The program is split into functions, each of which runs on its own thread. 
# This example will make Ohbot look around randomly and blink at random intervals.

# Import the relevant libraries. 
from ohbot import ohbot
from random import *
import threading

# Create global variables to enable movement and blinking to be turned on and off. 
global moving, blinking

# Set these global variables to False for the time being. 
moving = False
blinking = False


def blinkLids():
    global blinking
    
    # While True - Loop forever.
    while True:
        # if blinking is True.
        if blinking:
            # for the numbers 10 to 0 set the lidblink position. 
            for x in range(10, 0, -1):
                ohbot.move(ohbot.LIDBLINK,x)
                ohbot.wait(0.01)
                
            # for the numbers 0 to 10 set the lidblink position.
            for x in range(0, 10):
                ohbot.move(ohbot.LIDBLINK,x)
                ohbot.wait(0.01)

            # wait for a random amount of time for realistic blinking
            ohbot.wait(random() * 6)

def randomLook():
    global moving 
    while True:
        # if moving is True. 
        if moving:
            # Look in a random direction.
            ohbot.move(ohbot.EYETILT, randint(2, 8))
            ohbot.move(ohbot.EYETURN, randint(2, 8))

            # Wait for between 0 and 5 seconds. 
            ohbot.wait(random() * 5)

def randomTurn():
    global moving
    while True:
        if moving:
            # Move Ohbot's HEADTURN motor to a random position between 3 and 7.
            ohbot.move(ohbot.HEADTURN, randint(3, 7))

            # wait for a random amount of time before moving again. 
            ohbot.wait(random() * 4)

def randomNod():
    global moving
    while True:
        if moving:

            # Move Ohbot's HEADNOD motor to a random position between 4 and 7.
            ohbot.move(ohbot.HEADNOD, randint(4, 7))

            # wait for a random amount of time before moving again. 
            ohbot.wait(random() * 4)

def eyeCol():
    while True:
        # Set the base to a random rgb values between 0 and 10. 
        ohbot.setEyeColour(random() * 10, random() * 10, random() * 10)
        # Wait between 10 and 20 seconds before changing again. 
        ohbot.wait(randint(10, 20))

# Reset Ohbot and wait for a second for motors to move to reset positions. 
ohbot.reset()
ohbot.wait(1)

# Set the moving and blinking global variables to True. 
moving = True
blinking = True

# Create a thread for blinking.
t1 = threading.Thread(target=blinkLids, args=())

# Create a thread to make eyes look around randomly.
t2 = threading.Thread(target=randomLook, args=())

# Create a thread for random head nod positions.
t3 = threading.Thread(target=randomNod, args=())

# Create a thread for random head turn positions. 
t4 = threading.Thread(target=randomTurn, args=())

# Create a thread for random base colour. 
t5 = threading.Thread(target=eyeCol, args=())

# Start the threads. 
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

ohbot.say("Hello my name is Ohbot")
