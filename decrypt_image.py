import json
import os
import numpy as np
from skimage.io import imread, imsave
from skimage.color import rgb2gray
from skimage.transform import resize

def load_mapping(mapping_filename):
    with open(mapping_filename, 'r') as map_file:
        return json.load(map_file)

def get_decrypted_content(prediction, mapping):
    return mapping.get(str(prediction), 'Unknown')
def decrypt_image(encrypted_data, model, mapping_filename):
    try:
        encrypted_data_array = np.array(encrypted_data).reshape(1, -1)
        print(f"Encrypted data: {encrypted_data}")
        print(f"Encrypted data shape:{encrypted_data_array.shape}")
        if encrypted_data_array.shape[1]<4096:
            padded_data=np.pad(encrypted_data_array,((0,0),(0,4096-encrypted_data_array.shape[1])))
        else:
            padded_data=encrypted_data_array[:,:4096]
        print(f"Padded data shape:{padded_data.shape}")
        
        prediction = model.predict(padded_data)
        print(f"Model prediction:{prediction}")
        
        mapping = load_mapping(mapping_filename)
        print(f"Mapping:{mapping}")
        
        decrypted_image_path = get_decrypted_content(prediction[0], mapping)
        print(f"Decrypted image path: {decrypted_image_path}")
        
        if decrypted_image_path == 'Unknown' or not os.path.isfile(decrypted_image_path):
            decrypted_image_path = 'static/default_image.png'
        
        image_data = imread(decrypted_image_path)
        
        if image_data.dtype != np.uint8:
            image_data = (image_data * 255).astype(np.uint8)
        
        decrypted_image_filename = 'decrypted_image.png'
        output_path = os.path.join('static', decrypted_image_filename)
        imsave(output_path, image_data)
        
        print(f"Decrypted image saved to: {output_path}")
        
        return decrypted_image_filename
    except Exception as e:
        print(f"Error in decrypt_image: {str(e)}")
        return 'default_image.png'
