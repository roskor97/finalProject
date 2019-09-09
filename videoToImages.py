import cv2

def video_to_picture(directory):   #function to splite a video in images
    vid = cv2.VideoCapture(directory)  
    success, image = vid.read()
    count = 0

    while success:
        cv2.imwrite("B%d.jpg" % count, image)  # save images as jpg
        success, image = vid.read()
        print('Read a new frame: ', success)
        count += 1

video_to_picture("/Users/roskor/Desktop/Projecto_limpio/fg.mov")   #video directory

