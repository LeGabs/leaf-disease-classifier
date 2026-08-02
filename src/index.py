import os

def get_data(folder_path, folder_name):
    names = os.listdir(folder_path)
    list_names = []
    for i in range(len(names)):
        path = f"{folder_path}/{names[i]}"
        list_names.append((path, folder_name))
    return list_names

#path_names = get_data("./data/PlantVillage/Pepper__bell___Bacterial_spot", "Pepper_Bacterial_Spot") + get_data("./data/PlantVillage/Pepper__bell___healthy", "Pepper_Healthy")



