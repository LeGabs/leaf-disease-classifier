from src import index, preprocess_image
import os
import cv2


liste = index.get_data("./data/PlantVillage/Tomato__Target_Spot", "Target_Spot")

for path in liste:
    image = preprocess_image.preprocess(path[0])
    os.makedirs(f"./data/processed_images_Tomato/{path[1]}", exist_ok=True)
    cv2.imwrite(f"./data/processed_images_Tomato/{path[1]}/{os.path.basename(path[0])}", image)
    print(f"Saved preprocessed image to ./data/processed_images_Tomato/{path[1]}/{os.path.basename(path[0])}")

liste_healty = index.get_data("./data/PlantVillage/Tomato_healthy", "Healthy")

for path in liste_healty:
    image = preprocess_image.preprocess(path[0])
    os.makedirs(f"./data/processed_images_Tomato/{path[1]}", exist_ok=True)
    cv2.imwrite(f"./data/processed_images_Tomato/{path[1]}/{os.path.basename(path[0])}", image)
    print(f"Saved preprocessed image to ./data/processed_images_Tomato/{path[1]}/{os.path.basename(path[0])}")

liste_late_blight = index.get_data("./data/PlantVillage/Tomato_Late_blight", "Late_Blight")

for path in liste_late_blight:
    image = preprocess_image.preprocess(path[0])
    os.makedirs(f"./data/processed_images_Tomato/{path[1]}", exist_ok=True)
    cv2.imwrite(f"./data/processed_images_Tomato/{path[1]}/{os.path.basename(path[0])}", image)
    print(f"Saved preprocessed image to ./data/processed_images_Tomato/{path[1]}/{os.path.basename(path[0])}")

liste_early_blight = index.get_data("./data/PlantVillage/Tomato_Early_blight", "Early_Blight")

for path in liste_early_blight:
    image = preprocess_image.preprocess(path[0])
    os.makedirs(f"./data/processed_images_Tomato/{path[1]}", exist_ok=True)
    cv2.imwrite(f"./data/processed_images_Tomato/{path[1]}/{os.path.basename(path[0])}", image)
    print(f"Saved preprocessed image to ./data/processed_images_Tomato/{path[1]}/{os.path.basename(path[0])}")

liste_bacterial_spot = index.get_data("./data/PlantVillage/Tomato_Bacterial_spot", "Bacterial_Spot")

for path in liste_bacterial_spot:
    image = preprocess_image.preprocess(path[0])
    os.makedirs(f"./data/processed_images_Tomato/{path[1]}", exist_ok=True)
    cv2.imwrite(f"./data/processed_images_Tomato/{path[1]}/{os.path.basename(path[0])}", image)
    print(f"Saved preprocessed image to ./data/processed_images_Tomato/{path[1]}/{os.path.basename(path[0])}")

liste_mosaic_virus = index.get_data("./data/PlantVillage/Tomato__Tomato_Mosaic_virus", "Mosaic_Virus")

for path in liste_mosaic_virus:
    image = preprocess_image.preprocess(path[0])
    os.makedirs(f"./data/processed_images_Tomato/{path[1]}", exist_ok=True)
    cv2.imwrite(f"./data/processed_images_Tomato/{path[1]}/{os.path.basename(path[0])}", image)
    print(f"Saved preprocessed image to ./data/processed_images_Tomato/{path[1]}/{os.path.basename(path[0])}")

liste_spider_mites = index.get_data("./data/PlantVillage/Tomato_Spider_mites_Two_spotted_spider_mite", "Spider_Mites")

for path in liste_spider_mites:
    image = preprocess_image.preprocess(path[0])
    os.makedirs(f"./data/processed_images_Tomato/{path[1]}", exist_ok=True)
    cv2.imwrite(f"./data/processed_images_Tomato/{path[1]}/{os.path.basename(path[0])}", image)
    print(f"Saved preprocessed image to ./data/processed_images_Tomato/{path[1]}/{os.path.basename(path[0])}")

"""liste_yellow_leaf_curl = index.get_data("./data/PlantVillage/Tomato__Tomato_YellowLeaf__Curl_Virus", "Yellow_Leaf_Curl_Virus")

for path in liste_yellow_leaf_curl:
    image = preprocess_image.preprocess(path[0])
    os.makedirs(f"./data/processed_images_Tomato/{path[1]}", exist_ok=True)
    cv2.imwrite(f"./data/processed_images_Tomato/{path[1]}/{os.path.basename(path[0])}", image)
    print(f"Saved preprocessed image to ./data/processed_images_Tomato/{path[1]}/{os.path.basename(path[0])}")"""

liste_septoria_leaf_spot = index.get_data("./data/PlantVillage/Tomato_Septoria_leaf_spot", "Septoria_Leaf_Spot")

for path in liste_septoria_leaf_spot:
    image = preprocess_image.preprocess(path[0])
    os.makedirs(f"./data/processed_images_Tomato/{path[1]}", exist_ok=True)
    cv2.imwrite(f"./data/processed_images_Tomato/{path[1]}/{os.path.basename(path[0])}", image)
    print(f"Saved preprocessed image to ./data/processed_images_Tomato/{path[1]}/{os.path.basename(path[0])}")

liste_leaf_mold = index.get_data("./data/PlantVillage/Tomato_Leaf_Mold", "Leaf_Mold")

for path in liste_leaf_mold:
    image = preprocess_image.preprocess(path[0])
    os.makedirs(f"./data/processed_images_Tomato/{path[1]}", exist_ok=True)
    cv2.imwrite(f"./data/processed_images_Tomato/{path[1]}/{os.path.basename(path[0])}", image)
    print(f"Saved preprocessed image to ./data/processed_images_Tomato/{path[1]}/{os.path.basename(path[0])}")