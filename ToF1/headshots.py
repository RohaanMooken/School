import cv2
import time

name = 'Daniel'

cam = cv2.VideoCapture(0)

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("Failed to grab frame")
        break

    img_name = "dataset/" + name + "/image_{}.jpg".format(img_counter)
    cv2.imwrite(img_name, frame)
    print("{} written!".format(img_name))
    img_counter += 1

    time.sleep(1)
    if img_counter >= 20:
        break

cam.release()
