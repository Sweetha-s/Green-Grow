from flask import Flask, request, render_template, redirect, url_for
import os
import numpy as np
import cv2
import tensorflow as tf

app = Flask(__name__, template_folder="D:/3rdSem/DesignThinking/GreenGrow")
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limit to 16MB

# Load the trained model
model_path = r"D:\3rdSem\DesignThinking\GreenGrow"
model = tf.keras.models.load_model(model_path)

# Unique labels (classes) used for predictions
unique_labels = ["Black Soil", "Cinder Soil", "Laterite Soil", "Peat Soil", "Yellow Soil"]

def predict_soil_type(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (128, 128))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    prediction = model.predict(img)
    predicted_class = unique_labels[np.argmax(prediction)]
    return predicted_class

@app.route('/')
def upload_form():
    return render_template('/templates/summa.html')



@app.route('/predict', methods=['POST'])
def predict():
    if 'soil_image' not in request.files:
        return "No file part in the request"

    file = request.files['soil_image']
    if file.filename == '':
        return "No selected file"

    if file:
        # Ensure the uploads directory exists
        uploads_dir = 'uploads'
        if not os.path.exists(uploads_dir):
            os.makedirs(uploads_dir)

        # Save the file temporarily
        file_path = os.path.join(uploads_dir, file.filename)
        file.save(file_path)

        # Run prediction
        predicted_soil_type = predict_soil_type(file_path)

        # Clean up the temporary file
        os.remove(file_path)

        # Redirect to the specific soil type page
        if predicted_soil_type == "Black Soil":
            return render_template('/templates/black.html')  # Directly render black.html
        elif predicted_soil_type == "Cinder Soil":
            return render_template('/templates/cinder.html')  # Directly render cinder.html
        elif predicted_soil_type == "Laterite Soil":
            return render_template('/templates/lateritesoil.html')  # Directly render laterite.html
        elif predicted_soil_type == "Peat Soil":
            return render_template('/templates/peat_soil.html')  # Directly render peat.html
        elif predicted_soil_type == "Yellow Soil":
            return render_template('/templates/yellow_soil.html')  # Directly render yellow.html
        else:
            return "Unknown Soil Type"

if __name__ == "__main__":
    app.run(debug=True) 
