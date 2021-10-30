import cv2

faceCascade = cv2.CascadeClassifier("Lat 11 - Face Detection\Haarcascades\haarcascade_frontalface_default.xml")
img = cv2.imread('Lat 11 - Face Detection\Image\lena.png')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)

cv2.imshow("Result", img)
cv2.waitKey(0)



'''
    NB : 
        - cv2.CascadeClassifier()	~> Berfungsi untuk memanggil haar cascade.
        - cv2.CascadeClassifier("<lokasi haar cascade>")

        - .detectMultiScale()		~> Berfungsi untuk mendeteksi objek dengan ukuran berbeda pada gambar input. Objek yang terdeteksi akan direturn sebagai daftar rectangle.
        - cv2.CascadeClassifier().detectMultiScale(<input gambar / input array>, <scale factor [1.1]>, <min neighbors [3]> )
            - Scale factor	-> Parameter yang menentukan seberapa besar ukuran gambar diperkecil pada setiap skala gambar.
            - minNeighbors	-> Parameter yang menentukan berapa banyak neighbor yang harus dimiliki setiap kandidat rectangle untuk mempertahankannya.


'''


