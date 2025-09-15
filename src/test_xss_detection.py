import numpy as np
import cv2
from keras.models import load_model
import re
from bs4 import BeautifulSoup

# Function to convert HTML content to ASCII values
def convert_to_ascii(sentence):
    sentence_ascii = []

    for i in sentence:
        if ord(i) < 8222:  # Filter out characters above 8222
            if ord(i) == 8217:  # Special case for some characters
                sentence_ascii.append(134)
            if ord(i) == 8221:
                sentence_ascii.append(129)
            if ord(i) == 8220:
                sentence_ascii.append(130)
            if ord(i) == 8216:
                sentence_ascii.append(131)
            if ord(i) == 8217:
                sentence_ascii.append(132)
            if ord(i) == 8211:
                sentence_ascii.append(133)
            if ord(i) <= 128:  # Keep characters within the ASCII range
                sentence_ascii.append(ord(i))

    # Create a zero-padded array of size (100, 100)
    zer = np.zeros((10000))
    for i in range(len(sentence_ascii)):
        zer[i] = sentence_ascii[i]

    zer.shape = (100, 100)
    return zer

# Function to preprocess HTML content and prepare it for the model
def preprocess_html(html_content):
    # Clean HTML using BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")
    text = soup.get_text()  # Extract text from HTML

    # Convert text to ASCII representation
    ascii_image = convert_to_ascii(text)

    # Resize to (100, 100) and normalize
    image = np.asarray(ascii_image, dtype='float')
    image = cv2.resize(image, dsize=(100, 100), interpolation=cv2.INTER_CUBIC)
    image /= 128  # Normalize the values to be between 0 and 1

    return image.reshape(1, 100, 100, 1)  # Reshape for the model input

# Load the trained model
model = load_model('../model/xss_detection_model.keras')

# Load the HTML file to test
file_path = '../test/test.html'  # Replace with your HTML file path
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Preprocess the HTML file content
image_input = preprocess_html(html_content)

# Make a prediction using the trained model
prediction = model.predict(image_input)

# Interpret the prediction
if prediction[0] > 0.5:
    print("XSS Detected in the HTML file!")
else:
    print("No XSS detected in the HTML file.")
