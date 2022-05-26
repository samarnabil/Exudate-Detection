import numpy as np
from skimage.morphology import binary_erosion, disk


def getFovMask(gImg, erodeFlag, seSize):
    """
    Get a binary image of the Field of View mask to remove background
    _________
    Arguments:
        gImg: Image representing intensity channel from HSV color space
        erodeFlag: an integer, acts as flag for applying erosion on image or not - (0,1)
        seSize: structural element radius
    Returns: 
        Field of view mask
    """

    lowThresh = 0

    histRes , bins = np.histogram(gImg, bins=256, range=(0,255))
    d = np.diff(histRes)
    
    lvlFound  = [index for (index, val) in enumerate(d) if val  >= lowThresh][0]
    fovMask = ~(gImg <= lvlFound)
    
    if erodeFlag > 0 :
        fovMask = binary_erosion(fovMask, disk(seSize))
 
        #  erode also borders
        [row,col] = fovMask.shape
        fovMask[0:seSize*2,:] = 0
        fovMask[:,0:seSize*2] = 0
        fovMask[row-seSize*2:row,:] = 0
        fovMask[:,col-seSize*2:] = 0

    return fovMask.astype(int)
        
