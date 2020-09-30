import cv2
from pyzbar.pyzbar import decode


capture = cv2.VideoCapture(0)
#VideoCapture(0) is capturing the data with default camera.

barcode_received = None
#initially barcode data received is none.


while True:
    _, img = capture.read()
    #here capture.read() is reading the data which captured.

    decoded_barcode = decode(img)
    #Here the read data gets decoded

    try:
        barcode = decoded_barcode[0][0]


        if barcode != barcode_received:
            print(barcode)
            barcode_received = barcode
    
    except:
        pass


    cv2.imshow('QR Code Scanner', img)
    #Here cv2.imshow shows the data

    key = cv2.waitKey(1)
    

    if key == ord('s'):
    #Here if 's' is pressed the scanner window gets closed.

        break
