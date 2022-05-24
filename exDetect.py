import cv2
import numpy as np # For numeric computing, setting up matrices and performing computations at them
from getFovMask import getFovMask
from kirschEdges import kirschEdges

def exDetect( rgbImgOrig, removeON, onY, onX ):
    #  Parameters
    showRes = 0;  # show lesions in image
    imgProb = getLesions( rgbImgOrig, showRes, removeON, onY, onX )

    rgbImgOrig = cv2.imread("1.jpg")
    #print (type(rgbImgOrig))
    print(rgbImgOrig.shape)

    # Resize :part of exdetect function befire call kirsch fun

    origSize = rgbImgOrig.shape
    newSize = np.array([750, round(750*(origSize[1]/origSize[0]))])
    print(newSize)
    #newSize = newSize-mod(newSize,2); # force the size to be even
    newSize = findGoodResolutionForWavelet(newSize)
    print(newSize)
    # resize image to become as newsize 
    # reverse newsize bc it takes new width and height, not the new height and the width and tuple to convert numpy array to tuple
    imgRGB = cv2.resize(rgbImgOrig, tuple(reversed(newSize))) 
    print (imgRGB.shape)
    imgG = imgRGB[:,:,2]
    print (imgG.shape)
    #cv2.imshow('image window',imgG)

    #change colour plane
    imgHSV = cv2.cvtColor(imgRGB, cv2.COLOR_RGB2HSV)
    imgV = imgHSV[:,:,3]
    imgV8 = np.int8(imgV*255)

    #Create FOV mask
    imgFovMask = getFovMask(imgV8, 1, 30 )

    #Calculate edge strength of lesions
    imgKirsch = kirschEdges(imgG)


    return imgProb

def getLesions( rgbImgOrig, showRes, removeON, onY, onX ):
    # All algorithm functions
    pass

def findGoodResolutionForWavelet(sizeIn):
    maxWavDecom = 2

    pxToAddC = 2**maxWavDecom - (sizeIn[1] % (2**maxWavDecom))
    pxToAddR = 2**maxWavDecom - (sizeIn[0] % (2**maxWavDecom))
    sizeOut = sizeIn + [pxToAddR, pxToAddC]

    return (sizeOut)
