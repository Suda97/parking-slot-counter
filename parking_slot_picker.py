import cv2 as cv
import pickle

try:
    # read pickle
    with open('car_positions', 'rb') as file:
            pos_list = pickle.load(file)
except:
    pos_list = []

# value to play around
width, height = 107, 48


def mouse_click(events, x, y, flags, params):
    if events == cv.EVENT_LBUTTONDOWN:
        pos_list.append((x, y))

    if events == cv.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(pos_list):
            x1, y1 = pos
            if x1 < x < x1 + width and y1 < y < y1 + height:
                pos_list.pop(i)

    with open('car_positions', 'wb') as file:
        pickle.dump(pos_list, file)


while True:
    img = cv.imread('media/carParkImg.png')
    for pos in pos_list:
        cv.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 2)

    cv.imshow('Parking', img)
    cv.setMouseCallback('Parking', mouse_click)
    cv.waitKey(1)