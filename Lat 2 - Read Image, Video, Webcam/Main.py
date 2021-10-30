import cv2


# ---------------------- | Read Images |----------------------

# img = cv2.imread('Resources/Test Image.jpg')

# cv2.imshow('Car', img)

# cv2.waitKey(0)


# ---------------------- | Read Video |----------------------

# frameWidth = 640
# frameHeight = 100

# cap = cv2.VideoCapture("Resources/Test Video.mkv")
# # cap.set(3, frameWidth)            # Resize lebar dari frame
# # cap.set(4, frameHeight)           # Resize tinggi dari frame

# while True:
#     sucess, img = cap.read()
#     # img = cv2.resize(img, (frameWidth, frameHeight))          # Resize frame
#     cv2.imshow("Video", img)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break


# ---------------------- | Read Webcam |----------------------

frameWidth = 1280
frameHeight = 720

cap = cv2.VideoCapture(0)
# cap.set(3, frameWidth)            # Resize lebar dari frame
# cap.set(4, frameHeight)           # Resize tinggi dari frame

while True:
    sucess, img = cap.read()
    cv2.imshow("Video", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break   

cap.release()
cv2.destroyAllWindows()



'''
    NB :
        - cv2.imread()		                        ~> Berfungsi untuk membaca suatu gambar input.
        - cv2.imread("<lokasi gambar>")

        - cv2.imshow()		                        ~> Berfungsi untuk menampilkan gambar yg telah dibaca dengan imread().
        - cv2.imshow("<nama window", <gambar yg ingin ditampilkan>)

        - cv2.waitKey()		                        ~> Berfungsi untuk memberi delay terhadap penampilan gambar.
        - cv2.waitKey(<lama delay [ms]>)
        - cv2.waitKey(0)		                    ~> Berfungsi untuk menampilkan gambar selama user tidak menutupnya.

        - cv2.VideoCapture()	                    ~> Berfungsi untuk membaca suatu video input atau urutan gambar input.
        - cv2.VideoCapture("<lokasi video>")
        - cv2.VideoCapture(0)	                    ~> Berfungsi untuk membaca webcam.

        - cv2.VideoCapture().read()	                ~> Berfungsi untuk membaca suatu video perframe (mereturn boolean & gambar perframe).
        - <nama variable boolean>, <nama variable perframe> = cv2.VideoCapture().read()

        - cv2.VideoCapture().set(3, <lebar frame>)	~> Berfunsi untuk mengatur lebar frame.

        - cv2.VideoCapture().set(4, <tinggi frame>)	~> Berfunsi untuk mengatur tinggi frame.

        - cv2.resize()		                        ~> Berfungsi untuk mengatur ukuran gambar yg telah dibaca.
        - cv2.resize(<gambar yg ingin diresize>, (<lebar frame>, <tinggi frame>))


'''



