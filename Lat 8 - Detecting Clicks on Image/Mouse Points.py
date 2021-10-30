import cv2
import numpy as np


def mousePoints(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,y)


img = cv2.imread('Resources/Test Image.jpg')

cv2.imshow("Original Image", img)
cv2.setMouseCallback("Original Image", mousePoints)

cv2.waitKey(0)



'''
    NB :
        - cv2.EVENT_LBUTTONDOWN	-> Menunjukkan left klik pada mouse ditekan

        - setMouseCallBack()	~> Berfungsi untuk menjalankan suatu function apabila mouse diklik / untuk mengatur pengendali mouse untuk window tertentu.
        - setMouseCallBack(<nama window>, <function yg akan dijalankan>)


'''

