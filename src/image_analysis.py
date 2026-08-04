import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.feature import graycomatrix, graycoprops

def get_histogram(image):

    hist_h = cv2.calcHist([image], [0], None, [179], [0, 179])

    return hist_h.flatten()


def GLCM(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    gray_image = (gray_image // 8).astype(np.uint8) 

    glcm = graycomatrix(gray_image, distances=[1], angles=[0, np.pi/4, np.pi/2, 3*np.pi/4], levels=32, symmetric=True, normed=True)

    contrast      = graycoprops(glcm, 'contrast').mean()
    dissimilarity = graycoprops(glcm, 'dissimilarity').mean()
    homogeneity   = graycoprops(glcm, 'homogeneity').mean()
    energy        = graycoprops(glcm, 'energy').mean()
    correlation   = graycoprops(glcm, 'correlation').mean()

    return np.array([contrast, dissimilarity, homogeneity, energy, correlation])



#process("./data/PlantVillage/Pepper__bell___Bacterial_spot/0a0dbf1f-1131-496f-b337-169ec6693e6f___NREC_B.Spot 9241.JPG")
