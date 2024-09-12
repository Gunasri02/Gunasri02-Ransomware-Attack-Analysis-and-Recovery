import numpy as np
from skimage.io import imread
from skimage.color import rgb2gray
from skimage.transform import resize

def preprocess_image(image_path, target_size=(64, 64)):
    image = imread(image_path)
    gray_image = rgb2gray(image)
    resized_image = resize(gray_image, target_size, anti_aliasing=True)
    flat_image = resized_image.flatten()
    return flat_image

def encrypt_image(image_path, model):
    flat_image = preprocess_image(image_path)
    flat_image = np.reshape(flat_image, (1, -1))
    prediction = model.predict(flat_image)[0]
    probabilities = model.predict_proba(flat_image)[0]
    print(f"Encrypted data for {image_path}: prediction={prediction}, probabilities={probabilities}")
    return {"prediction": int(prediction), "probabilities": probabilities.tolist()}
