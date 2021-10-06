import get_carlicense as m 
import cv2

capture = cv2.VideoCapture(0)

if capture.isOpened():
    while True:
        sucess, img = capture.read()
        if sucess:
            cv2.imshow("Frame", img)
        k = cv2.waitKey(100)
        if k == ord('s') or k ==ord("S"):
            cv2.imwrite('screenshot.jpg',img)
            text = m.get_license(img)
            print("車牌:",text)
        if k == ord("q")or k ==ord("Q"):
            print("exit")
            cv2.destroyAllWindows()
            capture.release()
            break
    else:
        print("開啟攝影機失效")
