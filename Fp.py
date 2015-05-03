# import modules
import serial
import time
import struct
import cv2


arduino = serial.Serial('COM5', 9600)                                    # connect to communication port
FCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')  # Detect objects in a video stream
video_capture = cv2.VideoCapture(-1)                                     # Set video source to USB webcam

while True:                                                              # Continue to loop until told otherwise
    ret, frame = video_capture.read()                                    # Capture video frame-by-frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)                       # Convert frame to grayscale
    Fsearch = FCascade.detectMultiScale(                                 # Search for face in frame
        gray,                                                            # use grayscale image
        scaleFactor=1.1,                                      # rescale image to detect face in algorithm for xml file
        minNeighbors=3,                         # determine how many neighbors each rectangle should have to keep image
        minSize=(40, 40),                                               # minimum object size to be detected
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE                #make the algorithm scale the image instead of the detector
    )

    for (x, y, w, h) in Fsearch:                                       # Draw a rectangle around the faces
        rect =cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
        x1 = (int(x)*.3)                                               # multiply x value by scale number ".3"
        print x1                           # print value to terminal to see what is being sent to arduino to move servo

        arduino.write(struct.pack('>B',x1))                            # Send x1 value to arduino as a number value

    cv2.imshow('Video', frame)                                              # Display on screen the resulting frame

    if cv2.waitKey(1) & 0xFF == ord('q'):                                   # Break out of loop when q is entered
        break

video_capture.release()                                                     # Turn off webcam
arduino.close()                                                             # Turn off Arduino
cv2.destroyAllWindows()                                                     # Close window