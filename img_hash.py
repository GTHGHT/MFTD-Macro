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


def comp_hash(hash1, hash2):
    diff_count = 0
    for i in range(len(hash1)):
        diff_count += 1 if hash1[i] != hash2[i] else 0

    return diff_count
