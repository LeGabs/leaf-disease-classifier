import index
import image_analysis
import preprocess_image

liste = index.list_names("./data/PlantVillage/Pepper__bell___Bacterial_spot", "Bacterial_Spot")

for path in liste:
    image_analysis.process(path[0])


