import cv2 as cv
import numpy as np
import pickle

# read video
cap = cv.VideoCapture('media/carPark.mp4')

with open('car_positions', 'rb') as file:
    pos_list = pickle.load(file)

width, height = 107, 48

def check_parking_space(frame_processed):
    space_counter = 0

    for pos in pos_list:
        x, y = pos
        frame_crop = frame_processed[y:y+height, x:x+width]
        count = cv.countNonZero(frame_crop)
        cv.putText(frame, str(count), (x, y+height-10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
    
        if count < 890:
            color = (0, 255, 0)
            space_counter += 1
        else:
            color = (0, 0, 255)
        
        cv.rectangle(frame, pos, (pos[0]+width,pos[1]+height), color, 2)

    cv.putText(frame, f'Free spaces: {space_counter}/{len(pos_list)}', (100, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

while True:
    if cap.get(cv.CAP_PROP_POS_FRAMES) == cap.get(cv.CAP_PROP_FRAME_COUNT):
        cap.set(cv.CAP_PROP_POS_FRAMES, 0)
    success, frame = cap.read()

    # whole frame processing 
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_blur = cv.GaussianBlur(frame_gray, (3,3), 1)
    frame_threshold = cv.adaptiveThreshold(frame_blur, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 25, 16)
    frame_median = cv.medianBlur(frame_threshold, 5)
    kernel = np.ones((3, 3), np.uint8)
    frame_dilate = cv.dilate(frame_median, kernel, iterations=1)

    check_parking_space(frame_dilate)

    cv.imshow('Parking video', frame)
    # cv.imshow('Video processed', frame_dilate)
    cv.waitKey(10)