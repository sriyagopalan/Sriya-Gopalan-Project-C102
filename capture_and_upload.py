import cv2
from time import time
from random import randint
import dropbox

start_time = time()

def take_snapshot():
    num = randint(1, 100)
    #video capture object from cv2
    videoCaptureOject = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    result = True
    white(result):
        ret, frame = videoCaptureObject.read()
        img_name = "img" + str(num) + ".png"
        cv2.imwrite(img_name, frame)
        #start_time = time()
        result = False
        return img_name
    print("Snapshot taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token = "YN6QGBztqNwAAAAAAAAAAcpVBInPhZgtreP6g8ehCjHv0pkOOIOf95pBHoX-lYge"
    file_from = img_name
    file_to = "/Python/" + img_name
    dbx = dropbox.Dropbox(access_token)
    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(),file_to,mode = dropbox.files.WriteMode.overwrite)
        print("File Uploaded")

def main():
    while(True):
        if ((time() - start_time) >= 5):
            name = take_snpashot()
            upload_file(name)

main()