from pyzbar.pyzbar import decode
import cv2

cam = cv2.VideoCapture(0)

while True:
    check, frame = cam.read()

    if not check:
        continue