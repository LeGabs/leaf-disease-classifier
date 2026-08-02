import cv2
import numpy as np
import matplotlib.pyplot as plt
import preprocess_image

def process(path):
    image_processed = preprocess_image.preprocess_image(path)
    
    hist_h = cv2.calcHist([image_processed], [0], None, [179], [0, 179])

    return hist_h.flatten()


#process("./data/PlantVillage/Pepper__bell___Bacterial_spot/0a0dbf1f-1131-496f-b337-169ec6693e6f___NREC_B.Spot 9241.JPG")
