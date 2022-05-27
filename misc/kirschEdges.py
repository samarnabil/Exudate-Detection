from scipy import signal
import numpy as np # For numeric computing, setting up matrices and performing computations at them

def kirschEdges(imgIn):
    """
    Calculate the edge map using Spatial Filtering by Kirsch's Templates
    _________
    Arguments:
        imgIn: green chanel of input image 
    Returns: 
        imgOut: edge map which contains maximum edges value
    """

    h1 = np.array([[5, -3, -3],[5, 0, -3],[5, -3, -3]])/15
    h2 = np.array([[-3, -3, 5],[-3, 0, 5],[-3, -3, 5]])/15
    h3 = np.array([[-3, -3, -3],[5, 0, -3],[5, 5, -3]])/15
    h4 = np.array([[-3, 5, 5],[-3, 0, 5],[-3, -3, -3]])/15
    h5 = np.array([[-3, -3, -3],[-3, 0, -3],[5, 5, 5]])/15
    h6 = np.array([[5, 5, 5],[-3, 0, -3],[-3, -3, -3]])/15
    h7 = np.array([[-3, -3, -3],[-3, 0, 5],[-3, 5, 5]])/15
    h8 = np.array([[5, 5, -3],[5, 0, -3],[-3, -3, -3]])/15

    #Spatial Filtering by Kirsch's Templates
    #signal.convolve2d Equivalent to Filter2 in matlab

    t1 = signal.convolve2d(imgIn, np.rot90(h1,2), mode='same')
    t2 = signal.convolve2d(imgIn, np.rot90(h2,2), mode='same')
    t3 = signal.convolve2d(imgIn, np.rot90(h3,2), mode='same')
    t4 = signal.convolve2d(imgIn, np.rot90(h4,2), mode='same')
    t5 = signal.convolve2d(imgIn, np.rot90(h5,2), mode='same')
    t6 = signal.convolve2d(imgIn, np.rot90(h6,2), mode='same')
    t7 = signal.convolve2d(imgIn, np.rot90(h7,2), mode='same')
    t8 = signal.convolve2d(imgIn, np.rot90(h8,2), mode='same')



    #Find the maximum edges value
    imgOut = np.maximum(t1,t2)
    imgOut = np.maximum(imgOut,t3)
    imgOut = np.maximum(imgOut,t4)
    imgOut = np.maximum(imgOut,t5)
    imgOut = np.maximum(imgOut,t6)
    imgOut = np.maximum(imgOut,t7)
    imgOut = np.maximum(imgOut,t8)

    return (imgOut)