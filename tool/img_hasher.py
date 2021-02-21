import cv2
import numpy


def calc_image_hash(img):
    hash_ = ""
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    resized: numpy.ndarray = cv2.resize(img, (8, 8), interpolation=cv2.INTER_AREA)
    avrg = resized.mean()
    _, threshold = cv2.threshold(resized, avrg, 255, cv2.THRESH_BINARY)

    for i in range(8):
        for j in range(8):
            value = threshold[i, j]
            hash_ += "1" if value == 255 else "0"

    return hash_


ss = cv2.imread("back_ss.png")
ss = cv2.GaussianBlur(ss, (5,5), 1)
print(calc_image_hash(ss))