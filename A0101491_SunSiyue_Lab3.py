import cv2
import numpy as np
from numpy import linalg as la
import math

sobel_Kernel_Horizontal = np.matrix('-1, 0, 1; -2, 0, 2; -1, 0, 1')
sobel_Kernel_Vertical = np.matrix('1, 2, 1; 0, 0, 0; -1, -2, -1')

prewitt_Kernel_Horizontal = np.matrix('-1, 0, 1; -1, 0, 1; -1, 0, 1')
prewitt_Kernel_Vertical = np.matrix('1, 1, 1; 0, 0, 0; -1, -1, -1')


#loop runs three times to process three pictures
for i in range(1, 4):
    pic_name = "pictures/test" + str(i) + ".jpg"
    img = cv2.imread(pic_name, 0)
    rows, columns = img.shape

    img_Sobel_Horizontal = np.zeros((rows, columns))
    img_Sobel_Vertical = np.zeros((rows, columns))
    img_Prewit_Horizontal = np.zeros((rows, columns))
    img_Prewit_Vertical = np.zeros((rows, columns))
    
    for j in range(0,rows):
        for k in range(0,columns):
            #sobel method
            sobel_Horizontal_Matrix = sobel_Kernel_Horizontal*img[j,k]
            sobel_Vertical_Matrix = sobel_Kernel_Vertical*img[j,k]
            #prewit method
            prewitt_Horizontal_Matrix = prewitt_Kernel_Horizontal*img[j,k]
            prewitt_Vertical_Matrix = prewitt_Kernel_Vertical*img[j,k]
            for rowIndex in range(0,3):
                for colIndex in range(0,3):
                    if(j + rowIndex - 1 >= 0 and j + rowIndex - 1 < rows and k + colIndex - 1 >= 0 and k + colIndex - 1<columns):
                        img_Sobel_Horizontal[j-1+rowIndex,k-1+colIndex]+=sobel_Horizontal_Matrix[rowIndex, colIndex]
                        img_Sobel_Vertical[j-1+rowIndex,k-1+colIndex]+=sobel_Vertical_Matrix[rowIndex, colIndex]
                        img_Prewit_Horizontal[j-1+rowIndex,k-1+colIndex]+=prewitt_Horizontal_Matrix[rowIndex, colIndex]
                        img_Prewit_Vertical[j-1+rowIndex,k-1+colIndex]+=prewitt_Vertical_Matrix[rowIndex, colIndex]
    img_Sobel_Result = img_Sobel_Horizontal**2+img_Sobel_Vertical**2
    img_Prewit_Result = img_Prewit_Horizontal**2+img_Prewit_Vertical**2
    for r in range(0,rows):
        for c in range(0,columns):
            img_Sobel_Result[r,c]=math.sqrt(img_Sobel_Result[r,c])
            img_Prewit_Result[r,c]=math.sqrt(img_Prewit_Result[r,c])
    

    cv2.imwrite('pictures/test'+str(i)+'_Sobel_result.jpg',img_Sobel_Result)
    cv2.imwrite('pictures/test'+str(i)+'_Prewitt_result.jpg',img_Prewit_Result)




    #thinning of sobel image
    thinningC, thinningR = img_Sobel_Result.shape

    print "thinning: " + str(thinningC) + "  " + str(thinningR)

    img_thinned = np.zeros((thinningC, thinningR))
    


    prevIntensity = 0
    curIntensity = 0
    for thinningIndexR in range(0, thinningR):
        for thinningIndexC in range(0, thinningC):

            if(thinningIndexC < thinningC-2 and thinningIndexR < thinningR-2):
                prevIntensity = img_Sobel_Result[thinningIndexC, thinningIndexR]
                curIntensity = img_Sobel_Result[thinningIndexC+1, thinningIndexR]
                if(curIntensity + 15 < prevIntensity):
                    img_thinned[thinningIndexC, thinningIndexR] = prevIntensity

            
            



    cv2.imwrite('pictures/test'+str(i)+'_thinned.jpg',img_thinned)


























    