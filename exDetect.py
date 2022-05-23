
def exDetect( rgbImgOrig, removeON, onY, onX ):
    #  Parameters
    showRes = 0;  # show lesions in image
    imgProb = getLesions( rgbImgOrig, showRes, removeON, onY, onX )

    return imgProb

def getLesions( rgbImgOrig, showRes, removeON, onY, onX ):
    # All algorithm functions
    pass