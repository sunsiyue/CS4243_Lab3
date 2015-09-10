import cv2
import numpy as np
from numpy import linalg as la
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
                    if(j + rowIndex - 1 >= 0 and j + rowIndex - 1 < rows and k + colIndex - 1 >= 0 and k + 
colIndex - 1<columns):
                        img_Sobel_Horizontal[j-1+rowIndex,k-
1+colIndex]+=sobel_Horizontal_Matrix[rowIndex, colIndex]
                        img_Sobel_Vertical[j-1+rowIndex,k-1+colIndex]+=sobel_Vertical_Matrix[rowIndex, colIndex]
                        img_Prewit_Horizontal[j-1+rowIndex,k-1+colIndex]+=prewitt_Horizontal_Matrix[rowIndex, colIndex]
                        img_Prewit_Vertical[j-1+rowIndex,k-1+colIndex]+=prewitt_Vertical_Matrix[rowIndex, colIndex]

    img_Sobel_Result = img_Sobel_Horizontal**2+img_Sobel_Vertical**2
    img_Prewit_Result = img_Prewit_Horizontal**2+img_Prewit_Vertical**2
    img_Sobel_Result=np.sqrt(img_Sobel_Result)
    img_Prewit_Result=np.sqrt(img_Prewit_Result)
    img_Sobel_Result=255*(img_Sobel_Result -  img_Sobel_Result .min())/(img_Sobel_Result.max()-  
    img_Sobel_Result.min())
    img_Prewit_Result=255*(img_Sobel_Result -  img_Prewit_Result.min())/(img_Prewit_Result.max()-  img_Prewit_Result.min())

    cv2.imwrite('pictures/test'+str(i)+'_Sobel_result.jpg',255-img_Sobel_Result)
    cv2.imwrite('pictures/test'+str(i)+'_Prewitt_result.jpg',255-img_Prewit_Result)
    #thinning of sobel image
    thinningR, thinningC = img_Sobel_Result.shape
    
    print "thinning: thinningR" + str(thinningR) + "  thinningC: " + str(thinningC)
    img_thinned = np.zeros((thinningR, thinningC))

    for thinningIndexR in range(1, thinningR-1):
        for thinningIndexC in range(1, thinningC-1): 
            if ((img_Sobel_Result[thinningIndexR][thinningIndexC] > img_Sobel_Result[thinningIndexR-1][thinningIndexC] and img_Sobel_Result[thinningIndexR][thinningIndexC]>img_Sobel_Result[thinningIndexR+1][ thinningIndexC]) or (img_Sobel_Result[thinningIndexR][thinningIndexC]> img_Sobel_Result[thinningIndexR][thinningIndexC-1] and img_Sobel_Result[thinningIndexR][thinningIndexC]>img_Sobel_Result[thinningIndexR][thinningIndexC+1])):
                img_thinned[thinningIndexR, thinningIndexC] = img_Sobel_Result[thinningIndexR, thinningIndexC]

            else :img_thinned[thinningIndexR, thinningIndexC]=0

    cv2.imwrite('pictures/test'+str(i)+'_thinned.jpg',255-img_thinned)




