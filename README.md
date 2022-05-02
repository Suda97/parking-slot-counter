# Hello there!
In this simple CV2 project I have created the parking space counter.

## How to run it?
Well first of all You have to run the parking_slot_picker.py to mark every parking space on the photo (Nah, it's not using AI to derminate which group of pixels is a parking space. Maybe next time!)

Later you can just run the main.py and watch some magic stuff :D

## How is it done?
It just simply counts all pixels (In frame_cropped) which are not zeros and if number of this kind of pixels is below certain value then program recognizes parking space as free. Also frame has to be processed in certain way!
```
frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_blur = cv.GaussianBlur(frame_gray, (3,3), 1)
    frame_threshold = cv.adaptiveThreshold(frame_blur, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 25, 16)
    frame_median = cv.medianBlur(frame_threshold, 5)
    kernel = np.ones((3, 3), np.uint8)
    frame_dilate = cv.dilate(frame_median, kernel, iterations=1)
```

## Disclaimer!
There are few values which You will have to play around for it to work on your video/image. There are comments which points out these values!

