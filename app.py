from flask import Flask, request, render_template, redirect, url_for, flash
import os
import numpy as np
import pickle
from train_model import train_and_save_model
from encrypt_image import encrypt_image
from decrypt_image import decrypt_image

app = Flask(_name_)
app.secret_key = 'your_secret_key'  # For flash messages

# Configuration
UPLOAD_FOLDER = 'uploads'
STATIC_FOLDER = 'static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Define MODEL_PATH and MAPPING_PATH
MODEL_PATH = 'random_forest_image_model.pkl'
MAPPING_PATH = 'mapping.json'

# Ensure the directories exist
for folder in [UPLOAD_FOLDER, STATIC_FOLDER]:
    if not os.path.exists(folder):
        os.makedirs(folder)
@app.route('/')
def index():
    return render_template('index.html', title="Machine Learning Implementation in Encryption And Decryption..")

@app.route('/train', methods=['POST'])
def train():
    image_paths = []
    labels = []

    for i in range(1, 3):  # Adjust based on the number of images
        image_file = request.files.get(f'image{i}')
        label = request.form.get(f'label{i}')
        if image_file and label: 
            filename = f"train_image_{i}.png"
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image_file.save(filepath)
            image_paths.append(filepath)
            labels.append(int(label))

    if len(image_paths) < 2:
        flash('Please upload at least two images with labels for training.', 'error')
        return redirect(url_for('index'))

    train_and_save_model(image_paths, labels, MODEL_PATH, MAPPING_PATH)
    flash('Model trained successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/encrypt', methods=['POST'])
def encrypt():
    if 'image' not in request.files:
        flash('No file part', 'error')
        return redirect(url_for('index'))

    image_file = request.files['image']
    if image_file.filename == '':
        flash('No selected file', 'error')
        return redirect(url_for('index'))

    if image_file:
        filename = "to_encrypt.png"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        image_file.save(filepath)

        with open(MODEL_PATH, 'rb') as f:
            model = pickle.load(f)

        encrypted_data = encrypt_image(filepath, model)
        return render_template('encrypt.html', encrypted_data=encrypted_data)

@app.route('/decrypt', methods=['POST'])
def decrypt():
    encrypted_data = request.form['encrypted_data']
    try:
        encrypted_data = [int(encrypted_data)]
    except ValueError:
        flash('Invalid encrypted data. Please enter a valid number.', 'error')
        return redirect(url_for('index'))
    
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)

    decrypted_image_filename = decrypt_image(encrypted_data, model, MAPPING_PATH)

    if decrypted_image_filename == 'default_image.png':
        flash('Decryption failed. Please try again.', 'error')

    return render_template('result.html', image_file=decrypted_image_filename, encrypted_value=encrypted_data)

if _name_ == '_main_':
    app.run(debug=True)
