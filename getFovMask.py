import cv2
import numpy as np

def getFovMask(gImg, erodeFlag, seSize):

    #GETFOVMASK get a binary image of the Field of View mask
    #gImg: green challe uint8 image
    #erodeFlag: if set it will erode the mask

    lowThresh = 0
    if nargin < 3 :
        seSize = 10
        
    