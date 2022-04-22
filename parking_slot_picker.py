import cv2 as cv
import pickle

pos_list = []
img = cv.imread('media/carParkImg.png')
width, height = 107, 48


def mouse_click(events, x, y, flags, params):
    if events == cv.EVENT_LBUTTONDOWN:
        pos_list.append((x,y))

    if events == cv.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(pos_list):
            x1, y1 = pos
            if x1<x<x1+width and y1<y<y1+height:
                pos_list.pop(i)

while True:

    for pos in pos_list:
        cv.rectangle(img, pos, (pos[0]+width,pos[1]+height), (255,0,255), 2)

    cv.imshow('Parking', img)
    cv.setMouseCallback('Parking', mouse_click)
    cv.waitKey(1)