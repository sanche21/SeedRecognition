import os
import numpy as np
from scipy.misc import imread, imsave, imresize

def visualizeImages(imageMat, numRows=5, numCols=10, fileName="images.png", maxImgSize=64):
    imageSize = [imageMat.shape[1], imageMat.shape[2], imageMat.shape[3]]
    CombinedImage = np.ones([imageSize[0]*numRows, imageSize[1]*numCols, imageSize[2]])
    rowStart = 0
    i=0
    for r in range(numRows):
        rowEnd = rowStart + imageSize[0]
        RowImage = np.zeros([imageSize[0], imageSize[1]*numCols, imageSize[2]])
        lastStart = 0
        for c in range(numCols):
            thisImage = imageMat[i,:,:,:]
            end = lastStart + imageSize[1]
            RowImage[:, lastStart:end, :] = thisImage
            lastStart = end
            i=i+1
        CombinedImage[rowStart:rowEnd,:,:] = RowImage
        rowStart = rowEnd
    if maxImgSize is not None:
        CombinedImage = imresize(CombinedImage, [maxImgSize*numRows, maxImgSize*numCols])
    imsave(fileName, CombinedImage)


def getImagesFromDir(imageDir, imageSize=[640, 700, 3]):
    pathList = []
    for root,dir, files in os.walk(imageDir):
        for file in files:
            if ".png" in file:
                pathList += [os.path.join(root,file)]
    matSize = [len((pathList))] + imageSize
    imageMat = np.zeros(matSize)
    i=0
    for path in pathList:
        img = imread(path)
        imageMat[i,:,:,:] = img
        i=i+1
    return imageMat


if __name__ == "__main__":
    imageDir = "/Users/Sanche/Datasets/Seeds_Xin"
    imageMat = getImagesFromDir(imageDir)
    visualizeImages(imageMat, fileName="orig.png")


