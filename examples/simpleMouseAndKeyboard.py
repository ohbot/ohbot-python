# Ohbot - simple mouse and keyboard control example.
# Pioch will follow mouse movements and speak when 'a','b' or 'c' keys are pressed. 

from tkinter import *
from ohbot import ohbot

# Create a 600x600 window. 
win=Tk()
win.geometry("600x600")

# Function that is called when the mouse is moved. 
def xy(event):
    # Get the coordinates of where the mouse movement happened. 
    xm, ym = event.x, event.y

    # Scale the coordniate so it is between 0-10. Divide by 60 as window is 600 x 600. 
    xm = xm/60
    ym = ym/60

    # Use the scaled position to set Ohbot's motor and pupil positions and base colour. 
    ohbot.move(ohbot.HEADTURN,xm)
    ohbot.move(ohbot.HEADNOD,ym)
    ohbot.move(ohbot.EYETURN,xm)
    ohbot.move(ohbot.EYETILT,ym)
    ohbot.setEyeColour(10-ym,ym,xm)

# Function for when the 'a' key is pressed
def aKey(event):
    ohbot.say("Hello I am Ohbot",untilDone = False)
    ohbot.setEyeColour(3,3,10)

# Function for when the 'b' key is pressed
def bKey(event):
    ohbot.playSound('spring',untilDone = False)
    ohbot.say("What's going on ?",untilDone = False)
    ohbot.setEyeColour(10,3,3)

# Function for when the 'c' key is pressed
def cKey(event):
    ohbot.say("Hello humans",untilDone = False)
    ohbot.setEyeColour(3,10,3)

# Function called when window is closed. 
def on_closing():
    ohbot.reset()
    ohbot.wait(1)
    ohbot.close()
    win.destroy()
    
# Bind the close button to the on_closing function.
win.protocol("WM_DELETE_WINDOW", on_closing)
    
# Bind windows Motion Action to xy function. Call the xy function whenever the mouse is moved.  
win.bind("<Motion>",xy)

# Bind keys to their functions. 
win.bind("a",aKey)
win.bind("b",bKey)
win.bind("c",cKey)

# Start the loop to make the window active.  
mainloop()
