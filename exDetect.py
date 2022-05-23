
def exDetect( rgbImgOrig, removeON, onY, onX ):
    #  Parameters
    showRes = 0;  # show lesions in image
    imgProb = getLesions( rgbImgOrig, showRes, removeON, onY, onX )

    return imgProb,'Tesssst'

def getLesions( rgbImgOrig, showRes, removeON, onY, onX ):
    pass