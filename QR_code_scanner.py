import cv2
from pyzbar.pyzbar import decode


capture = cv2.VideoCapture(0)

barcode_received = None

while True:
    _, img = capture.read()

    decoded_barcode = decode(img)
    try:
        barcode = decoded_barcode[0][0]
        if barcode != barcode_received:
            print(barcode)
            barcode_received = barcode
    except:
        pass


    cv2.imshow('QR Code Scanner', img)

    key = cv2.waitKey(1)
    

    if key == ord('s'):
        break
