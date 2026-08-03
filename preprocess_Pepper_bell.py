from src import index, preprocess_image
import os
import cv2


liste = index.get_data("./data/PlantVillage/Pepper__bell___Bacterial_spot", "Bacterial_Spot")

for path in liste:
    image = preprocess_image.preprocess(path[0])
    os.makedirs(f"./data/processed_images_Pepper/{path[1]}", exist_ok=True)
    cv2.imwrite(f"./data/processed_images_Pepper/{path[1]}/{os.path.basename(path[0])}", image)
    print(f"Saved preprocessed image to ./data/processed_images_Pepper/{path[1]}/{os.path.basename(path[0])}")

liste_healty = index.get_data("./data/PlantVillage/Pepper__bell___healthy", "Healthy")

for path in liste_healty:
    image = preprocess_image.preprocess(path[0])
    os.makedirs(f"./data/processed_images_Pepper/{path[1]}", exist_ok=True)
    cv2.imwrite(f"./data/processed_images_Pepper/{path[1]}/{os.path.basename(path[0])}", image)
    print(f"Saved preprocessed image to ./data/processed_images_Pepper/{path[1]}/{os.path.basename(path[0])}")


