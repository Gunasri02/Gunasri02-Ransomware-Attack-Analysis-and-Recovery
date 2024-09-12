import numpy as np
from sklearn.ensemble import RandomForestClassifier
import pickle
from skimage.io import imread
from skimage.color import rgb2gray
from skimage.transform import resize
import json

def preprocess_image(image_path, target_size=(64, 64)):
    image = imread(image_path)
    gray_image = rgb2gray(image)
    resized_image = resize(gray_image, target_size, anti_aliasing=True)
    flat_image = resized_image.flatten()
    return flat_image

def train_and_save_model(image_paths, labels, model_filename, mapping_filename):
    X_train = np.array([preprocess_image(path) for path in image_paths])
    y_train = np.array(labels)
    
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)
    
    with open(model_filename, 'wb') as model_file:
        pickle.dump(clf, model_file)
    
    mapping = {str(label): path for label, path in zip(labels, image_paths)}
    with open(mapping_filename, 'w') as map_file:
        json.dump(mapping, map_file)
    
    
    print(f"Model saved as '{model_filename}'")
    print(f"Mapping saved as '{mapping_filename}'")
