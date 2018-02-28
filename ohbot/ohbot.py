#This is a script to help control an Ohbot Robot. www.ohbot.co.uk

import serial
import serial.tools.list_ports
import time
import threading
import os
import sys
import wave
import subprocess
from lxml import etree

#define constants for motors
HEADNOD = 0
HEADTURN = 1
EYETURN = 2
LIDBLINK = 3
TOPLIP = 4
BOTTOMLIP = 5
EYETILT = 6

# array to hold 
sensors = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]

#define a module level variable for the serial port
port=""
#define library version
version ="2.4"

ser = None

def init(portName):
    # pickup global instances of port and ser variables    
    global port,ser
    
    #Search for the Ohbot serial port 
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        # If port has Ohbot connected save the location
        if portName in p[1]:
            port = p[0]
            print ("Ohbot found on port:" + port)
        elif portName in p[0]:
            port = p[0]
            print ("Ohbot found on port:" + port)

    if port == "":
        print ("Ohbot port " + portName + " not found")
        return False

    #Open the serial port
    ser = serial.Serial(port, 19200)

    ser.timeout = 1

    ##    ser.timeout = None

    # Make an initial call to Festival without playing the sound to check it's all okay
    text = "Hi"
        
    # Create a bash command with the desired text. The command writes two files, a .wav with the speech audio and a .txt file containing the phonemes and the times. 
    bashcommand = "festival -b '(set! mytext (Utterance Text " + '"' + text + '"))' + "' '(utt.synth mytext)' '(utt.save.wave mytext " + '"ohbotspeech.wav")' + "' '(utt.save.segs mytext " + '"phonemes"' + ")'"

    # Execute bash command.
    subprocess.call(bashcommand,shell=True)

    return True

# xml file for motor definitions
dir = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(dir, 'MotorDefinitionsv21.omd')
tree = etree.parse(file)
root = tree.getroot()

# Put motor ranges into lists
motorPos = [11,11,11,11,11,11,11,11]
motorMins = [0,0,0,0,0,0,0,0]
motorMaxs = [0,0,0,0,0,0,0,0]
motorRev = [False,False,False,False,False,False,False,False]
restPos = [0,0,0,0,0,0,0,0]
isAttached = [False,False,False,False,False,False,False,False]

# For each line in motor defs file
for child in root:
    indexStr = child.get("Motor")
    index = int(indexStr)
    motorMins[index] = int(int(child.get("Min"))/1000*180)
    motorMaxs[index] = int(int(child.get("Max"))/1000*180)
    motorPos[index] = int(child.get("RestPosition"))
    restPos[index] = int(child.get("RestPosition"))

    if child.get("Reverse") == "True":
        rev = True
        motorRev[index] = rev
    else:
        rev = False
        motorRev[index] = rev
        
# initialise with default port name
init("ttyACM")

# Function to move Ohbot's motors. Arguments | m (motor) → int (0-6) | pos (position) → int (0-10) | spd (speed) → int (0-10) **eg move(4,3,9) or move(0,9,3)**
def move(m, pos, spd=3):


 
    
    # Limit values to keep then within range
    pos = limit(pos)
    spd = limit(spd)

    # Reverse the motor if necessary   
    if motorRev[m]:
        pos = 10 - pos

    # Attach motor       
    attach(m)
    
    # Ensure the lips do not crash into each other. 
    if m == TOPLIP and pos + motorPos[BOTTOMLIP] > 10:
        pos = 10 - motorPos[BOTTOMLIP]

    if m == BOTTOMLIP and pos + motorPos[TOPLIP] > 10:
        pos = 10 - motorPos[TOPLIP]
        
    # Convert position (0-10) to a motor position in degrees
    absPos = int(getPos(m,pos))

    # Scale range of speed
    spd = (250/10)*spd

    # Construct message from values
    msg = "m0"+str(m)+","+str(absPos)+","+str(spd)+"\n"

    # Write message to serial port
    ser.write(msg.encode('latin-1'))

    # Update motor positions list
    motorPos[m] = pos  
 


# Function to attach Ohbot's motors. Argument | m (motor) int (0-6)
def attach(m):
    if isAttached[m] == False:
        # Construct message
        msg = "a0"+str(m)+"\n"

        # Write message to serial port
        ser.write(msg.encode('latin-1'))

        # Update flag
        isAttached[m] = True
    

# Function to detach Ohbot's motors.  Argument | m (motor) int (0-6)
def detach(m):
    msg = "d0"+str(m)+"\n"    
    ser.write(msg.encode('latin-1'))
    isAttached[m] = False
    
# Function to find the scaled position of a given motor. Arguments | m (motor) → int (0-6) | pos (position) → int (0-10) | Returns a position
def getPos(m, pos):
    mRange = motorMaxs[m]-motorMins[m]
    scaledPos = (mRange/10)*pos
    return scaledPos + motorMins[m]

# Function to make Ohbot Speak. Arguments | text String "Hello World" **eg say("Hello my name is Ohbot") or
# untilDone - wait in function until speech is complete, lipSync - move lips in time with speech, hdmiAudio - adds a delay to give hdmi channel time to activate.
# soundDelay - positive if lip movement is lagging behind sound, negative if sound is lagging behind lip movement.
def say(text, untilDone = True, lipSync=True, hdmiAudio = False, soundDelay = 0):

    if hdmiAudio:
        soundDelay = soundDelay - 1
    
    safetext = re.sub(r'[^ .a-zA-Z0-9?\']+', '', text)
    
    # Create a bash command with the desired text. The command writes two files, a .wav with the speech audio and a .txt file containing the phonemes and the times. 
    bashcommand = "festival -b '(set! mytext (Utterance Text " + '"' + safetext + '"))' + "' '(utt.synth mytext)' '(utt.save.wave mytext " + '"ohbotspeech.wav")' + "' '(utt.save.segs mytext " + '"phonemes"' + ")'"

    # Execute bash command.
    subprocess.call(bashcommand,shell=True)
    
    # Open the text file containing the phonemes
    f = open("phonemes",'r')

    # Empty the lists that contain phoneme data and reset count
    phonemes = []
    times = []
    vals = []

    # Read a line to move past the first line
    line = f.readline()
    
    # While there are more lines to read.
    while line:

        # Read the line
        line = f.readline()

        # Split the line into values 
        vals = line.split()

        # If values exist add the phoneme to the phonemes list and the timecode to the times list. 
        if vals:
            phonemes.append(vals[2])
            times.append(float(vals[0]))
    
    if lipSync:
        if soundDelay > 0:
            # Set up a thread for the speech sound synthesis, delay start by soundDelay
            t = threading.Timer(soundDelay, saySpeech, args=(hdmiAudio,), kwargs=None)
            # Set up a thread for the speech movement
            t2 = threading.Thread(target=moveSpeech, args=(phonemes,times))
        else:
            # Set up a thread for the speech sound synthesis
            t = threading.Thread(target=saySpeech, args=(hdmiAudio,))
            # Set up a thread for the speech movement, delay start by - soundDelay
            t2 = threading.Timer(-soundDelay, moveSpeech, args=(phonemes,times), kwargs=None)
        t2.start() 
    else:
        # Set up a thread for the speech sound synthesis
        t = threading.Thread(target=saySpeech, args=(hdmiAudio,))      
    t.start()

    # if untilDone, keep running until speech has finished    
    if untilDone:
        totalTime = times[len(times)-1]
        startTime = time.time()
        while time.time()-startTime < totalTime:
            continue
        
# Function to limit values so they are between 0 - 10
def limit(val):
     if val > 10:
       return 10
     elif val < 0: 
        return 0
     else:
        return val

# Function to play back the speech wav file, if hmdi audio is being used play silence before speech sound
def saySpeech(addSilence):
    
    if addSilence:
        
        dir = os.path.dirname(os.path.abspath(__file__))
        silenceFile = os.path.join(dir, 'Silence1.wav')
        commandString = 'aplay ' + silenceFile + '\naplay ohbotspeech.wav'
        os.system(commandString)
    else:
        os.system('aplay ohbotspeech.wav')
   
# Function to move Ohbot's lips in time with speech. Arguments | phonemes → list of phonemes[] | waits → list of waits[]
def moveSpeech(phonemes, times):
    startTime = time.time()
    timeNow = 0
    totalTime = times[len(times)-1]
    currentX = -1
    while timeNow < totalTime:     
        timeNow = time.time() - startTime
        for x in range (0,len(times)):
            if timeNow > times[x] and x > currentX:                
                posTop = phonememapTop(phonemes[x])
                posBottom = phonememapBottom(phonemes[x])
                move(TOPLIP,posTop,10)
                move(BOTTOMLIP,posBottom,10)
                currentX = x
    move(TOPLIP,5)
    move(BOTTOMLIP,5)
            
# Function mapping phonemes to top lip positions. Argument | val → phoneme | returns a position as int
def phonememapTop(val):
    return {
        'p': 5,
        'b': 5,
        'm': 5,
        'ae': 7,
        'ax': 7,
        'ah': 7,
        'aw': 10,
        'aa': 10,
        'ao': 10,
        'ow': 10,
        'ey': 7,
        'eh': 7,
        'uh': 7,
        'ay': 7,
        'h': 7,
        'er': 8,
        'r': 8,
        'l': 8,
        'y': 6,
        'iy': 6,
        'ih': 6,
        'ix':6,
        'w': 6,
        'uw': 6,
        'oy': 6,
        's': 5,
        'z': 5,
        'sh': 5,
        'ch': 5,
        'jh': 5,
        'zh': 5,
        'th': 5,
        'dh': 5,
        'd': 5,
        't': 5,
        'n': 5,
        'k': 5,
        'g': 5,
        'ng': 5,
        'f': 6,
        'v': 6
}.get(val, 5)

# Function mapping phonemes to lip positions. Argument | val → phoneme | returns a position as int
def phonememapBottom(val):
    return {
        'p': 5,
        'b': 5,
        'm': 5,
        'ae': 8,
        'ax': 8,
        'ah': 8,
        'aw': 5,
        'aa': 10,
        'ao': 10,
        'ow': 10,
        'ey': 7,
        'eh': 7,
        'uh': 7,
        'ay': 7,
        'h': 7,
        'er': 8,
        'r': 8,
        'l': 8,
        'y': 6,
        'iy': 6,
        'ih': 6,
        'ix':6,
        'w': 6,
        'uw': 6,
        'oy': 6,
        's': 6,
        'z': 6,
        'sh': 6,
        'ch': 6,
        'jh': 6,
        'zh': 6,
        'th': 6,
        'dh': 6,
        'd': 6,
        't': 6,
        'n': 6,
        'k': 6,
        'g': 6,
        'ng': 6,
        'f': 5,
        'v': 5
}.get(val,5)  

# Function to set the color of the LEDs in Ohbot's eyes.Arguments | r (red) → int (0-10) | g (green) → int (0-10) | b (blue) → int (0-10) 
# swapRandG is used to swap the red and green values on older Ohbots
def eyeColour(r, g, b, swapRandG = False):

    # Limit the values to keep them within range.
    r = limit(r)
    g = limit(g)
    b = limit(b)

    # Scale the values so they are between 0 - 255.
    r = int((255/10)*r)

    g = int((255/10)*g)

    b = int((255/10)*b)

    # Construct a message with the values.
    if swapRandG:
        msg1 = "l00,"+str(g)+","+str(r)+","+str(b)+"\n"
        msg2 = "l01,"+str(g)+","+str(r)+","+str(b)+"\n"
    else:       
        msg1 = "l00,"+str(r)+","+str(g)+","+str(b)+"\n"
        msg2 = "l01,"+str(r)+","+str(g)+","+str(b)+"\n"

    # Write message to serial port.
    ser.write(msg1.encode('latin-1'))    
    ser.write(msg2.encode('latin-1'))    

def wait(seconds):
    time.sleep(float(seconds))
    return

def close():       
    for x in range(0, len(motorMins)-1):
        detach(x)   

# Reset Ohbot back to start position
def reset():
    eyeColour(0,0,0)
    for x in range(0,len(restPos)-1):
        move(x,restPos[x])

# Return the sensor value between 0-10 for a given sensor number. Values stored in sensors[] array.
def readSensor(index):
    ser.flushInput()
    
    msg = "i0"+str(index)+"\n"
    ser.write(msg.encode('latin-1'))

    line = ser.readline()
    lineStr = line.decode("utf-8")
    lines = lineStr.split(",")

    if len(lines) > 1:

        indexIn = lines[0]
        indexIn = indexIn[1]

        intdex = int(indexIn)
        
        newVal = int(lines[1])/1024
        newVal = newVal *10
        sensors[intdex] = limit(newVal)

    return sensors[index]
 
 

