import cv2
import numpy as np
from skimage.morphology import binary_erosion, disk


def getFovMask(gImg, erodeFlag, seSize):

    # GETFOVMASK get a binary image of the Field of View mask
    # gImg: green challe uint8 image
    # erodeFlag: if set it will erode the mask
    lowThresh = 0

    histRes , bins = np.histogram(gImg, bins=256, range=(0,255))
    d = np.diff(histRes)
    # print('hist', histRes)
    # print('diff',d)
    
    lvlFound  = [index for (index, val) in enumerate(d) if val  >= lowThresh][0]
    # print(lvlFound)
    fovMask = ~(gImg <= lvlFound)
    
    if erodeFlag > 0 :
        fovMask = binary_erosion(fovMask, disk(seSize))
 
        #  erode also borders
        [row,col] = fovMask.shape
        fovMask[0:seSize*2,:] = 0
        fovMask[:,0:seSize*2] = 0
        fovMask[row-seSize*2:row,:] = 0
        fovMask[:,col-seSize*2:] = 0
        # cv2.imshow('image',np.uint8(fovMask.astype(int)*255))
        # k = cv2.waitKey(0)

    return fovMask
        
