import cv2
import threading

storage = []
cap = []


def initCamera(index):
    cap = cv2.VideoCapture(index)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    cap.set(cv2.CAP_PROP_FPS, 30)
    return cap

def capFrame():
    while True:
        ret, image = cap.read()
        if ret:
            storage.append(image)
            print(storage.__len__())



if __name__ == '__main__':
    cap = initCamera(1)

    newThread = threading.Thread(target=capFrame)
    newThread.setDaemon(False)
    newThread.start()
    while True:
        if storage.__len__() > 0:
            cv2.imshow('selfCamera', storage.pop())
            cv2.waitKey(1)


    cap.release()
    cv2.destroyAllWindows()
