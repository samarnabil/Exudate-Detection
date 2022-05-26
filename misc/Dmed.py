from glob import glob 
import cv2
from os.path import join, basename, splitext
import re

class Dmed():
    def __init__(self, dirIn):
        """
        Constructor - Load dataset 
        _________
        Arguments:
            dirIn: Dataset absolute path
        """
        # set constants
        self.data = {}
        self.roiExt = '.jpg.ROI' 
        self.imgExt = '.jpg' 
        self.metaExt = '.meta' 
        self.gndExt = '.GND' 
        self.mapGzExt = '.map.gz' 
        self.mapExt = '.map' 
        self.baseDir = dirIn 
           
        dirList = glob(join(self.baseDir,'*'+self.imgExt))

        for i in range(0,len(dirList)):
            fileName = splitext(basename(dirList[i]))[0]
            self.data[i] = fileName

        # set constants
        self.origImgNum = len(self.data)         # real img num
        self.imgNum = self.origImgNum            # current imgNum
        

    def getNumOfImgs (self):
        """
        Get number of images in the dataset
        _________
        Returns: 
            number of images
        """
        return self.imgNum


    def getImg (self,imgID): 
        """
        Get image with the given imgID.
        _________
        Arguments:
            id: dictionary key for accessing its photo
        Returns: 
            Fundus image
        """
        try:
            imgAddress = self.baseDir +'/' + self.data[imgID]+ self.imgExt
            img = cv2.imread( imgAddress , cv2.IMREAD_UNCHANGED)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        except:
            img = []
            print('Index exceeds dataset size of ' + str(self.imgNum) )
        
        return img

    def getONloc(self, id):
        """
        Get the hand identified location of the optic nerve
        _________
        Arguments:
            id: dictionary key for accessing its photo
        Returns: 
            onRow: X coordinate of optical nerve
            onCol: Y coordinate of optical nerve
        """
        onRow = []
        onCol = []
        try:
            metaFile = self.baseDir +'/' + self.data[id]+ self.metaExt
            fMeta = open(metaFile, "r")
            res = fMeta.read()
            fMeta.close()
            tokRow = re.search('ONrow\W+([0-9\.]+)', res)
            tokCol = re.search('ONcol\W+([0-9\.]+)', res)
            
            if  tokRow and tokCol:
                onRow = int(tokRow.group().split('~')[1])
                onCol = int(tokCol.group().split('~')[1])

        except:
            print('Location not Found, exceeds image size')

        return onRow, onCol
        
    
