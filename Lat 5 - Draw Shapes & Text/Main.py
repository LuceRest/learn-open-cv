import cv2
import numpy as np


img = np.zeros((512, 512, 3), np.uint8)
# 0 255
print(img)


# -----------| Memberi Warna |-----------

img[:] = 255, 0, 0    


# -----------| Membuat Garis |-----------

cv2.line(img, (0,0), (img.shape[1], img.shape[0]), (0, 255, 0), 2)


# -----------| Membuat Rectangle |-----------

cv2.rectangle(img, (350,100), (450,200), (0,0,255), cv2.FILLED)


# -----------| Membuat Lingkaran |-----------

cv2.circle(img, (150,400), 50, (150,0,255), 3)


# -----------| Memmbuat Text |-----------

cv2.putText(img, "Draw Shapes", (75,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,150,0), 1)


cv2.imshow("Image", img)
cv2.waitKey(0)



'''
    NB :
        - <variable gambar>[:] = <warna [rgb]>
            ~> Berfungsi untuk memberi warna dalam rgb pada suatu gambar.

        - cv2.line()		~> Berfungsi untuk membuat garis pada suatu gambar.
        - cv2.line(<gambar>, (<lokasi x garis awal>, <lokasi y garis awal>), (<lokasi x garis akhir>, <lokasi y garis akhir>), (<warna [rgb]>), <ketebalan>)

        - cv2.rectangle()	~> Berfungsi untuk membuat suatu rectangle.
        - cv2.rectangle(<gambar>, (<lokasi x garis awal>, <lokasi y garis awal>), (<lokasi x garis akhir>, <lokasi y garis akhir>), (<warna [rgb]>), <ketebalan>)

        - cv2.FILLED	    ~> Berfungsi untuk memberi warna penuh pada suatu rectangle di suatu gambar.

        - cv2.circle()	    ~> Berfungsi untuk membuat suatu lingkaran pada suatu gambar.
        - cv2.circle(<gambar>, (<lokasi x titik pusat>, <lokasi y titik pusat>), <jari-jari [radius]>,  (<warna [rgb]>), <ketebalan>)

        - cv2.putText()	    ~> Berfungsi untuk memberi text pada suatu gambar.
        - cv2.putText(<gambar>, "<text>", (<lokasi x awal text>, <lokasi y awal text>), <jenis font [cv2.FONT_]>, <ukuran text>, (<warna [rgb]>), <ketebalan>)


'''

