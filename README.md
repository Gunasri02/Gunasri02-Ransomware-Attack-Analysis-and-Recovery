# Ransomware-Attack-Analysis-and-Recovery
# Image Encryption and Decryption with Machine Learning

This project demonstrates how to use machine learning for encrypting and decrypting images. It involves training a Random Forest Classifier on image data to perform encryption and decryption based on the model's predictions.

## Project Structure

1. **Image Preprocessing**: Converts images to grayscale, resizes them, and flattens them into a 1D array.
2. **Encryption**: Uses the trained model to predict and encrypt an image.
3. **Decryption**: Retrieves the encrypted image based on model predictions and mapping.
4. **Web Interface**: Provides a user interface for training the model, encrypting images, and decrypting them.

## Setup

### Prerequisites

Make sure you have the following installed:
- Python 3.x
- `numpy`
- `scikit-learn`
- `scikit-image`
- `Flask`
- `Pillow`
- `pickle` (for model serialization)

### Installation

1. **Clone the Repository**

   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Install Required Packages**

   You can install the necessary packages using pip:

   ```bash
   pip install numpy scikit-learn scikit-image Flask Pillow
   ```

3. **Directory Structure**

   Ensure your project directory includes:
   - `uploads/`: Directory for uploaded images.
   - `static/`: Directory for saved images and static files.
   - `templates/`: Directory for HTML templates.

4. **Create the Mapping File**

   The `mapping.json` file should be created during model training. No manual setup is needed for this.

## Usage

### Training the Model

1. Navigate to the main directory and run the Flask app:

   ```bash
   python app.py
   ```

2. Open your web browser and go to `http://127.0.0.1:5000/`.

3. **Train the Model**:
   - Go to the "Train the Model" section.
   - Upload two images and provide corresponding labels.
   - Click "Train" to train the model and save it.

### Encrypting an Image

1. **Upload an Image**:
   - Go to the "Encrypt an Image" section.
   - Upload the image you want to encrypt.
   - Click "Encrypt" to get the encrypted data.

### Decrypting an Image

1. **Decrypt the Encrypted Data**:
   - Go to the "Decrypt an Image" section.
   - Enter the encrypted data (as obtained from the encryption step).
   - Click "Decrypt" to recover the original image.

## Files and Functions

- **`encrypt_image.py`**: Contains functions for preprocessing and encrypting images.
- **`decrypt_image.py`**: Contains functions for decrypting images and saving them.
- **`train_model.py`**: Contains functions for training and saving the machine learning model.
- **`app.py`**: The main Flask application script.
- **`templates/`**: Contains HTML templates for the web interface.

## Troubleshooting

- **Model Training Issues**: Ensure you upload at least two images with labels.
- **File Handling**: Ensure `uploads/` and `static/` directories are correctly set up.
- **Image Format**: Ensure uploaded images are in a supported format (e.g., PNG, JPEG).

## Contributing

Feel free to open issues or submit pull requests to enhance the functionality of this project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
