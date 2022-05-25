import cv2
import numpy as np
import scipy # For numeric computing, setting up matrices and performing computations at them
from skimage.color import rgb2hsv
from misc.getFovMask import getFovMask
from misc.kirschEdges import kirschEdges

def exDetect( rgbImgOrig, removeON, onY, onX ):
    #  Parameters
    showRes = 0;  # show lesions in image
    imgProb = getLesions( rgbImgOrig, showRes, removeON, onY, onX )

    return []

def getLesions( rgbImgOrig, showRes, removeON, onY, onX ):

    # Resize :part of exdetect function befire call kirsch fun
    origSize = rgbImgOrig.shape
    newSize = np.array([750, round(750*(origSize[1]/origSize[0]))])
 
    #newSize = newSize-mod(newSize,2); # force the size to be even
    newSize = findGoodResolutionForWavelet(newSize)
   
    # resize image to become as newsize 
    # reverse newsize bc it takes new width and height, not the new height and the width and tuple to convert numpy array to tuple
    imgRGB = cv2.resize(rgbImgOrig, tuple(reversed(newSize)),interpolation=cv2.INTER_CUBIC) 
    
    # Green channel
    imgG = imgRGB[:,:,1]

    #change colour plane
    imgHSV = rgb2hsv(imgRGB)
    imgV = imgHSV[:,:,2]
    imgV8 = np.uint8(imgV*255)

    #  Remove OD region
    #  Parameters
    winOnRatio = [1/8,1/8]
    if removeON :
        # get ON window
        onY = onY * newSize[0]/origSize[0]
        onX = onX * newSize[1]/origSize[1]
        onX = round(onX)
        onY = round(onY)
        winOnSize = np.round(winOnRatio * newSize).astype(int)
        print(winOnSize)
        #  remove ON window from imgTh
        winOnCoordY = [onY-winOnSize[0],onY+winOnSize[0]]
        winOnCoordX = [onX-winOnSize[1],onX+winOnSize[1]]
        if(winOnCoordY[0] < 1): winOnCoordY[0] = 1
        if(winOnCoordX[0] < 1): winOnCoordX[0] = 1
        if(winOnCoordY[1] > newSize[0]): winOnCoordY[1] = newSize[0]
        if(winOnCoordX[1] > newSize[1]): winOnCoordX[1] = newSize[1]

    #Create FOV mask
    imgFovMask = getFovMask(imgV8, 1, 30 )
    imgFovMask[int(winOnCoordY[0]):int(winOnCoordY[1]), int(winOnCoordX[0]):int(winOnCoordX[1])] = 0
    # cv2.imshow('image',np.uint8(imgFovMask)*255)
    # k = cv2.waitKey(0)

    # --- start line 120

    #Calculate edge strength of lesions
    #fixed threshold using median Background (with reconstruction)

    kernelSize = int(round(newSize[0]/30))
    medBg = np.array(scipy.signal.medfilt2d (np.array(imgV8,np.float),[kernelSize,kernelSize]),np.float)
    #cv2.imshow('median filter',medBg)
    #reconstruct bg
    maskImg = np.array(imgV8,np.float)
    pxLbl = maskImg < medBg
    pxLbl= pxLbl.astype(int)
    maskImg[pxLbl] = medBg[pxLbl]
    


    #subtract, remove fovMask and threshold

    #subImg = np.array(imgV8,np.float) - np.array(medRestored,np.float)
    #subImg = subImg * np.array(imgFovMask,np.float)


    #Calculate edge strength of lesions

    imgKirsch = kirschEdges( imgG )
    #cv2.imshow('KirschEdges Output',imgKirsch)
    #img0 = imgG * uint8(imgThNoOD == 0)
    #img0recon = imreconstruct(img0, imgG)
    #img0Kirsch = kirschEdges(img0recon)
    #imgEdgeNoMask = imgKirsch - img0Kirsch; #edge strength map
    
    #remove mask and ON (leave vessels)
    #imgEdge = np.array(imgFovMask,np.float) * imgEdgeNoMask
    

    
def findGoodResolutionForWavelet(sizeIn):
    maxWavDecom = 2

    pxToAddC = 2**maxWavDecom - (sizeIn[1] % (2**maxWavDecom))
    pxToAddR = 2**maxWavDecom - (sizeIn[0] % (2**maxWavDecom))
    sizeOut = sizeIn + [pxToAddR, pxToAddC]

    return (sizeOut)
