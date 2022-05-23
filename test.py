# Uses python3
import sys;
import os;
import cv2;
from misc.Dmed import Dmed;
from exDetect import *;


def scaleIm (img,scale_percent):
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    return (width, height)


if __name__ == '__main__':

    #  The location of the dataset
    DMEDloc = './DMED'
    data = Dmed( os.path.abspath(DMEDloc) )

    for i in range(0,data.getNumOfImgs()):
        # 1. get Image
        rgbImg = data.getImg(i)
        resizedImg = cv2.resize(rgbImg, scaleIm(rgbImg,20), interpolation = cv2.INTER_AREA)
        
        # 2. get optic nerve location
        [onY, onX] = data.getONloc(i)

        # 3. segment exudates
        imgProb = exDetect( rgbImg, 1, onY, onX )
        # print(imgProb)
        
        # 4. display results
        cv2.imshow('image',resizedImg)

        # block execution up until an image is closed
        k = cv2.waitKey(0)
        # wait for ESC key to exit
        if k == 27:
            cv2.destroyAllWindows()