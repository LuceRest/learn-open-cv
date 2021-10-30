import cv2
import numpy as np


kernel = np.ones((5,5), np.uint8)
print(kernel)
print()

path = "Resources/Test Image.jpg"
img = cv2.imread(path)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(img, (7,7), 0)
imgCanny = cv2.Canny(img, 100, 200)
imgDilation = cv2.dilate(img, kernel, iterations = 1)
imgEroded = cv2.erode(img, kernel, iterations = 1)

cv2.imshow('Car', img)
cv2.imshow('Car Grayscale', imgGray)
cv2.imshow('Car Blur', imgBlur)
cv2.imshow('Car Canny', imgCanny)
cv2.imshow('Car Dilation', imgDilation)
cv2.imshow('Car Erosion', imgEroded)

cv2.waitKey(0)



'''
    NB :
        - cv2.imread("<lokasi gambar>", 0)  ~> Berfungsi untuk membaca suatu gambar input dan memberinya efek grayscale (abu-abu).

        - cv2.cvtColor()		             ~> Berfungsi untuk mengubah warna dari suatu gambar.
        - cv2.cvtColor(<gambar yg dibaca>, <warna baru>)

        - cv2.COLOR_BGR2GRAY	             ~> Berfungsi untuk memberi warna abu-abu.

        - cv2.GaussianBlur()		        ~> Berfungsi untuk memberi efek blur pada gambar yg telah dibaca.
        - cv2.GaussianBlur(<gambar yg ingin diberi efek blur>, (<besar blur [angka ganjil], <besar blur [angka ganjil]), 0)

        - cv2.Canny()			             ~> Berfungsi untuk memberi efek canny pada gambar yg telah dibaca.
        - cv2.Canny(<gambar yg ingin diberi efek canny>, 100, 100)
        - cv2.Canny(<gambar yg ingin diberi efek canny>, <lower threshold>, <upper threshold>)

        - cv2.dilate()			             ~> Berfungsi untuk memberi filter morfologi pelebaran pada gambar yg telah dibaca.
        - cv2.dilate(<sumber gambar>, <kernel>, <iterations>) 
            - kernel = numpy.ones((5, 5), numpy.uint8)

        - cv2.erode()			             ~> Berfungsi untuk memberi filter morfologi penipisan pada gambar yg telah dibaca.
        - cv2.erode(<sumber gambar>, <kernel>, <iterations>) 
            - kernel = numpy.ones((5, 5), numpy.uint8)



'''





