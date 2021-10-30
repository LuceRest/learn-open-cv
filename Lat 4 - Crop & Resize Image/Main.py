import cv2


path = "Resources/Test Image.jpg"
img = cv2.imread(path)
print(img.shape)
print()

width, height = 1000, 1000
imgResize = cv2.resize(img, (width, height))
print(imgResize.shape)
print()

imgCroppped = img[300:540, 430:480]
imgCropResize = cv2.resize(imgCroppped, (img.shape[1], img.shape[0]))

cv2.imshow("Car", img)
cv2.imshow("Car Resized", imgResize)
cv2.imshow("Car Cropped", imgCroppped)
cv2.imshow("Car Cropped Resized", imgCropResize)

cv2.waitKey(0)



'''
    NB :
        - cv2.imread().shape	~> Berfungsi untuk mengetahui dimensi dari sebuah gambar (tinggi, lebar, channels).

        - cv2.imread()[<tinggi pixel awal>:<tinggi pixel akhir>, <lebar pixel awal>:<lebar pixel akhir>]
            ~> Berfungsi untuk mengcrop suatu gambar berdasarkan ukuran pixel yg ingin ditampilkan.

        - cv2.resize()	        ~> Berfungsi untuk meresize suatu gambar yg telah dibaca.
        - cv2.resize("<gambar>", (<lebar/width>, <tinggi/height>))


'''


