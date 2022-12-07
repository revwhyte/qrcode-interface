import cv2

# Initialize the cv2 QRCode detector.
detector = cv2.QRCodeDetector()
# Initialize the cam.
cam = cv2.VideoCapture(0)

read_successfully = False
key = 0
while not read_successfully and key != 27:
    is_frame_captured, frame = cam.read()

    if not is_frame_captured:
        continue
    # Detect and decode.
    data, bbox, straight_qrcode = detector.detectAndDecode(frame)
    # Sometimes the bbox exists but the data is empty due to a false positive.
    if bbox is not None and len(data) != 0:
        # read_successfully = True
        print(f"QRCode string: {data}")
        # Display the image with lines (optional).
        for i in range(4):
            point1 = tuple(bbox[0][i])
            point2 = tuple(bbox[0][(i+1) % 4])
            # cv2.line requires int for point and the bbox provide as float.
            # So, we need to convert the tuple of float into tuple of ints.
            point1 = tuple(map(int, point1))
            point2 = tuple(map(int, point2))
            cv2.line(frame, point1, point2, color=(0, 255, 0), thickness=2)

    # Display the result.
    cv2.imshow("Image from CAM", frame)
    # How many milliseconds to wait.
    key = cv2.waitKey(10)

