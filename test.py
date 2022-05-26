# Uses python3
import os;
import keyboard;
from misc.Dmed import Dmed;
from exDetect import *;


if __name__ == '__main__':

    #  The location of the dataset
    DMEDloc = './DMED'
    data = Dmed( os.path.abspath(DMEDloc) )

    for i in range(0,data.getNumOfImgs()):
        # 1. get Image
        rgbImg = data.getImg(i)
        
        # 2. get optic nerve location
        [onY, onX] = data.getONloc(i)

        # 3. segment exudates
        imgProb = exDetect( rgbImg, 1, onY, onX )
        
        # 4. display results
        show_results(rgbImg, imgProb)

        if keyboard.is_pressed('q'):  # if key 'q' is pressed 
            print('Quit the Loop!')
            break  # finishing the loop