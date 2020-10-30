from cv2 import cv2
from reconnaissance.fonction_yolo import reconnaissance
from reconnaissance.fonction_sans_yolo import reconnaissance_sans_yolo

def open_webcam(filename = "temp.jpg"):
        cv2.namedWindow("Webcam",cv2.WINDOW_AUTOSIZE)
        cam = cv2.VideoCapture(0) 
        take_picture = False
        while(True): 

            # Capture frame-by-frame 

            ret, frame = cam.read() 
            #print(frame)
            frame2 = reconnaissance_sans_yolo(frame)

            # Display the resulting frame 
            cv2.imshow('Webcam',frame2) 
            
            if cv2.waitKey(1) & 0xFF == ord(' '):
                take_picture = True
                break 
            if cv2.waitKey(1) & 0xFF == ord('x'):
                take_picture = False
                break

        # When everything done, release the capture 
        if ret and take_picture:
            cv2.imwrite(filename,frame2)
        cam.release() 
        cv2.destroyAllWindows() 
        return()

def open_webcam_yolo(filename = "temp.jpg"):
        cv2.namedWindow("Webcam",cv2.WINDOW_AUTOSIZE)
        cam = cv2.VideoCapture(0) 
        take_picture = False
        while(True): 

            # Capture frame-by-frame 

            ret, frame = cam.read() 
            frame2 = reconnaissance(frame)
            
            
            # Display the resulting frame 
            cv2.imshow('Webcam',frame2) 
            
            if cv2.waitKey(1) & 0xFF == ord(' '):
                take_picture = True
                break 
            if cv2.waitKey(1) & 0xFF == ord('x'):
                take_picture = False
                break

        # When everything done, release the capture 
        if ret and take_picture:
            cv2.imwrite(filename,frame2)
        cam.release() 
        cv2.destroyAllWindows() 
        return()