import cv2
import numpy as np
from numpy import linalg as la
import math

sobelKernelHor=np.matrix('-1, 0, 1; -2, 0, 2; -1, 0, 1')
sobelKernelVer=np.matrix('1, 2, 1; 0, 0, 0; -1, -2, -1')

print sobelKernelHor

prewittKernelHor=np.matrix('-1, 0, 1; -1, 0, 1; -1, 0, 1')
prewittKernelVer=np.matrix('1, 1, 1; 0, 0, 0; -1, -1, -1')















for i in range(1,4):
    pic_name="pictures/test"+str(i)+".jpg"
    img=cv2.imread(pic_name, 0)
    (row,col)=img.shape
    imgSHor=np.zeros((row, col))
    imgSVer=np.zeros((row, col))
    imgPHor=np.zeros((row, col))
    imgPVer=np.zeros((row,col))
    for j in range(0,row):
        for k in range(0,col):
            sobelMatrixHor=sobelKernelHor*img[j,k]
            sobelMatrixVer=sobelKernelVer*img[j,k]
            prewittMatrixHor=prewittKernelHor*img[j,k]
            prewittMatrixVer=prewittKernelVer*img[j,k]
            for filterRow in range(0,3):
                for filterCol in range(0,3):
                    if(j-1+filterRow>=0 and j-1+filterRow<row and k-1+filterCol>=0 and k-1+filterCol<col):
                        imgSHor[j-1+filterRow,k-1+filterCol]+=sobelMatrixHor[filterRow, filterCol]
                        imgSVer[j-1+filterRow,k-1+filterCol]+=sobelMatrixVer[filterRow, filterCol]
                        imgPHor[j-1+filterRow,k-1+filterCol]+=prewittMatrixHor[filterRow, filterCol]
                        imgPVer[j-1+filterRow,k-1+filterCol]+=prewittMatrixVer[filterRow, filterCol]
    imgS=imgSHor**2+imgSVer**2
    imgP=imgPHor**2+imgPVer**2
    for r in range(0,row):
        for c in range(0,col):
            imgS[r,c]=math.sqrt(imgS[r,c])
            imgP[r,c]=math.sqrt(imgP[r,c])
    #cv2.imwrite('pictures/result'+str(i)+'Sober.jpg',imgS)
    #cv2.imwrite('pictures/result'+str(i)+'Prewitt.jpg',imgP)
    print imgS
    print imgP
    #cv2.imwrite('pictures/result'+str(i)+'Thin.jpg',imgT)