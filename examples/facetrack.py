import cv2
import sys
from ohbot import ohbot

# uses opencv-python from here https://pypi.org/project/opencv-python/

# get the face detect definition which is installed with opencv
cascPath = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"

print ("Haar definitions loaded from:" + cascPath)

faceCascade = cv2.CascadeClassifier(cascPath)

# Set video input to first camera device in list.
# Takes a while to initialize
print ("Initializing camera")
video_capture = cv2.VideoCapture(0)

if (video_capture):
    print ("Camera Initialized")
    # Set up variables to hold face position and size.
    faceX = 5
    faceY = 5
    faceSize = 0

    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        if (frame.any()):
            height, width, channels = frame.shape

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Experiment with changing scaleFactor (larger numbers will mean it can run faster)
            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=2,
                minNeighbors=5,
                minSize=(50, 50),
                flags =cv2.CASCADE_SCALE_IMAGE
            )
            

            
            # For each face detected.
            for (x, y, w, h) in faces:

                # Draw a rectangle around the face. 
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

                # Work out the size of the face. 
                faceSize = int((w+h)/2)

                # Scale the x and y position of the face so that it is between 0 - 10. 
                faceX = (x+(w/2))/width*10
                faceY = (y+(h/2))/height*10
            
            # Display the resulting frame
            cv2.imshow('Video', frame)

            # Move ohbot to the position of the face detected. 
            ohbot.move(ohbot.HEADTURN,10-faceX,10)
            ohbot.move(ohbot.HEADNOD,10-faceY,10)
            
            # Uncomment this to move the eyes too
            #ohbot.move(ohbot.EYETURN,10-faceX,10)
            #ohbot.move(ohbot.EYETILT,10-faceY,10)

            # Quit on q key
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            print ("no frame")

    # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()
else:
    print ("no camera found")

