# Uses python3
import sys;
import os;
import cv2;
from misc.Dmed import Dmed;
from exDetect import *;


def scaleIm (img):
    # width = int(img.shape[1] * scale_percent / 100)
    # height = int(img.shape[0] * scale_percent / 100)
    # return (width, height)

    origSize = img.shape
    newSize = np.array([750, round(750*(origSize[1]/origSize[0]))])

    maxWavDecom = 2

    pxToAddC = 2**maxWavDecom - (newSize[1] % (2**maxWavDecom))
    pxToAddR = 2**maxWavDecom - (newSize[0] % (2**maxWavDecom))
    sizeOut = newSize + [pxToAddR, pxToAddC]

    return cv2.resize(img, tuple(reversed(sizeOut))) 


if __name__ == '__main__':

    #  The location of the dataset
    DMEDloc = './DMED'
    data = Dmed( os.path.abspath(DMEDloc) )

    for i in range(0,data.getNumOfImgs()):
        # 1. get Image
        rgbImg = data.getImg(i)
        resizedImg = scaleIm(rgbImg)
        
        # 2. get optic nerve location
        [onY, onX] = data.getONloc(i)

        # 3. segment exudates
        imgProb = exDetect( rgbImg, 1, onY, onX )
        # print(imgProb)
        
        # 4. display results
        imgShow = cv2.cvtColor(resizedImg, cv2.COLOR_BGR2RGB)
        cv2.imshow('image',imgShow)

        # block execution up until an image is closed
        k = cv2.waitKey(0)
        # wait for ESC key to exit
        if k == 27:
            cv2.destroyAllWindows()