from src import index, preprocess_image
import os
import cv2


liste = index.get_data("./data/PlantVillage/Potato___Early_blight", "Early_Blight")

for path in liste:
    image = preprocess_image.preprocess(path[0])
    os.makedirs(f"./data/processed_images_Potato/{path[1]}", exist_ok=True)
    cv2.imwrite(f"./data/processed_images_Potato/{path[1]}/{os.path.basename(path[0])}", image)
    print(f"Saved preprocessed image to ./data/processed_images_Potato/{path[1]}/{os.path.basename(path[0])}")

liste_healty = index.get_data("./data/PlantVillage/Potato___healthy", "Healthy")

for path in liste_healty:
    image = preprocess_image.preprocess(path[0])
    os.makedirs(f"./data/processed_images_Potato/{path[1]}", exist_ok=True)
    cv2.imwrite(f"./data/processed_images_Potato/{path[1]}/{os.path.basename(path[0])}", image)
    print(f"Saved preprocessed image to ./data/processed_images_Potato/{path[1]}/{os.path.basename(path[0])}")

liste_late_blight = index.get_data("./data/PlantVillage/Potato___Late_blight", "Late_Blight")

for path in liste_late_blight:
    image = preprocess_image.preprocess(path[0])
    os.makedirs(f"./data/processed_images_Potato/{path[1]}", exist_ok=True)
    cv2.imwrite(f"./data/processed_images_Potato/{path[1]}/{os.path.basename(path[0])}", image)
    print(f"Saved preprocessed image to ./data/processed_images_Potato/{path[1]}/{os.path.basename(path[0])}")