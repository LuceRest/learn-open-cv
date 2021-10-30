import cv2
import numpy as np


img = cv2.imread('Resources/Test Image.jpg')

width, height = 250, 100
pts1 = np.float32([[341, 390], [579, 479], [352,470], [576, 406]])
pts2 = np.float32([[0,0], [width, 0], [0, height], [width, height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

# for x in range(0,4):
#     cv2.circle(img, (pts1[x][0], pts1[x][1]), 5, (0,0,255), cv2.FILLED)

cv2.imshow("Original Image", img)
cv2.imshow("Output Image", imgOutput)

cv2.waitKey(0)



'''
    NB :
        - cv2.getPerspectiveTrasnform()	~> Berfungsi untuk mengambil letak dari gambar dalam bentuk matriks pada suatu gambar dan mengubahnya menjadi gambar dengan letak matriks yg baru.
        - cv2.getPerspectiveTrasnform(<letak matriks lama>, <letak matriks baru>)

        - cv2.warpPerspective()	        ~> Berfungsi untuk membuat gambar baru dari matriks yg didapat dari function cv2.getPerspectiveTrasnform().
        - cv2.warpPerspective(<gambar lama>, <matriks baru>, (<lebar gambar baru>, <tinggi gambar baru>))


'''



