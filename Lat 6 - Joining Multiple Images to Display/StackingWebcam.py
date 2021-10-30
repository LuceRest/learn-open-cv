import cv2
import numpy as np
import Util


frameWidth = 1280
frameHeight = 720

cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)            # Resize lebar dari frame
cap.set(4, frameHeight)           # Resize tinggi dari frame

while True:
    sucess, img = cap.read()
    # cv2.imshow("Video", img)

    kernel = np.ones((5,5), np.uint8)

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(img, (7,7), 0)
    imgCanny = cv2.Canny(img, 100, 200)
    imgDilation = cv2.dilate(img, kernel, iterations = 1)
    imgEroded = cv2.erode(img, kernel, iterations = 1)

    imgBlank = np.zeros((200, 200), np.uint8)

    stackedImages = Util.stackImages(0.3, (
                                    [img, imgGray, imgBlur],
                                    [imgCanny, imgDilation, imgEroded]
                                    ))

    # cv2.imshow('Car', img)
    # cv2.imshow('Car Grayscale', imgGray)
    # cv2.imshow('Car Blur', imgBlur)
    # cv2.imshow('Car Canny', imgCanny)
    # cv2.imshow('Car Dilation', imgDilation)
    # cv2.imshow('Car Erosion', imgEroded)

    cv2.imshow('Stacked Images', stackedImages)
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break   

# cap.release()
# cv2.destroyAllWindows()

