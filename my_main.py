import cv2
import numpy as np
from keras.models import load_model
model = load_model('/Users/roskor/Downloads/final.h5')

class_names = {0:"O",1:"S",2:"T",3:"Y",4:"por aqui",5:"AMIGO"}
cap = cv2.VideoCapture(0)
ret, frame = cap.read()

roi_start = 90
roi_size = 300

def process_img(img):
    ancho = 500
    alto = 350
    img = cv2.resize(img, (ancho, alto))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    X = []
    X.append(img)

    X = np.array(X, dtype="uint8")
    X = X.reshape(1, ancho, alto, 1)
    X = X/255.

    prediction = model.predict(X)


    return prediction


cont = 0

while True:


    ret, frame = cap.read()



    w = frame.shape[1]
    h = frame.shape[0]
    hcenter = w // 2
    vcenter = h // 2

    roi = frame[roi_start:roi_start + roi_size,
    roi_start:roi_start + roi_size]


    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

    gray_cropped = gray[:, (hcenter - h // 2):(hcenter + h // 2)]

    cuadro = process_img(roi)

    cv2.rectangle(frame, (roi_start, roi_start), (roi_start + roi_size, roi_start + roi_size), (0, 255, 0), 0)

    confidence = np.amax(cuadro)



    prediction = class_names[np.argmax(cuadro)]






    cv2.putText(frame,
                prediction + ' ' + str(confidence) if confidence > 0.7 else 'sign not detected',
                (int(roi_start),
                int(roi_start + .09 * roi_size)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 0, 255))

    cv2.imshow('my_webcam_frame', frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):

        break
cap.release()
cv2.destroyAllWindows()
