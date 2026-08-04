# Leaf Disease Classifier

Classifying plant leaf diseases from images using **classical computer vision** — hand-crafted color and texture features fed to classic machine-learning classifiers (no deep learning).

This is a learning project exploring how far traditional feature engineering can go on the [PlantVillage](https://www.kaggle.com/datasets/abdallahalidev/plantvillage-dataset) dataset, and *where* it starts to break down.

## Approach

Each image is turned into a single fixed-length feature vector, then classified:

1. **Preprocess** — resize to 256×256 and convert to HSV color space.
2. **Extract features:**
   - **Color** — a 179-bin histogram of the Hue channel (color distribution of the leaf).
   - **Texture** — GLCM (Gray-Level Co-occurrence Matrix) statistics: contrast, dissimilarity, homogeneity, energy, correlation.
3. **Classify** — Random Forest or SVM (RBF kernel), evaluated across multiple train/test splits.

## Results

| Task | Classes | Accuracy |
|------|---------|----------|
| Pepper (healthy vs. bacterial spot) | 2 | ~97% |
| Potato (healthy, early blight, late blight) | 3 | ~96% |
| Tomato (9 disease/healthy classes) | 9 | ~90% |

**Key finding:** the value of texture features depends on the problem. On the easy, color-separable potato task, GLCM texture accounted for only ~1.4% of the model's feature importance — color alone did the work. On the harder 9-class tomato task, where several diseases share a color but differ in pattern, texture importance rose to ~10%. Features aren't intrinsically useful; they matter when the problem needs the information they carry.

## Project structure

```
leaf-disease-classifier/
├── data/            # PlantVillage images (not tracked in git)
├── notebooks/       # exploration, feature extraction, training & evaluation
└── src/
    ├── index.py             # builds (image_path, label) lists from folders
    ├── preprocess_image.py  # resize + HSV conversion
    └── image_analysis.py    # Hue histogram + GLCM feature extraction
```

## Requirements

- Python 3.x
- `opencv-python`, `scikit-image`, `scikit-learn`, `numpy`, `matplotlib`

## Dataset

Download the [PlantVillage dataset](https://www.kaggle.com/datasets/abdallahalidev/plantvillage-dataset) and place the class folders under `data/PlantVillage/`. The `data/` folder is gitignored.
