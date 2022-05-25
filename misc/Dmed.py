from glob import glob 
import cv2
from os.path import join, basename, splitext
import re
import struct

from cv2 import IMREAD_UNCHANGED

class Dmed():
    def __init__(self, dirIn):
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
        # print(dirList)

        # for i in range(0,len(dirList)+1):
        for i in range(0,5):
            fileName = splitext(basename(dirList[i]))[0]
            # check bad - ignored for now
            self.data[i] = fileName
        # print(self.data)

        # set constants
        self.origImgNum = len(self.data)         # real img num
        self.imgNum = self.origImgNum            # current imgNum
        # self.idMap = range(0,self.imgNum)      # maps abstract id to real id
        # print(self.data[4])
        

    def getNumOfImgs (self):
        return self.imgNum


    def getImg (self,id): 
        try:
            imgAddress = self.baseDir +'/' + self.data[id]+ self.imgExt
            img = cv2.imread( imgAddress , cv2.IMREAD_UNCHANGED)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        except:
            img = []
            print('Index exceeds dataset size of ' + str(self.imgNum) )
        
        return img

    def getONloc(self, id):
        '''
        Get optical nerve location
        '''
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
        
    
