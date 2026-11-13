🚗 Vehicle Damage Detection Using ResNet50

A Deep Learning-based Vehicle Damage Detection application that analyzes uploaded vehicle images and classifies them into six different damage categories using a trained ResNet50 Convolutional Neural Network (CNN).

The project uses PyTorch for model development, FastAPI for backend API services, and Streamlit for the user interface.

📸 Application Preview

"Vehicle Damage Detection Application" (streamlit-app/img.png)

🎯 Project Overview

Vehicle damage assessment is an important part of insurance claims and vehicle inspection processes. Manually identifying vehicle damage can be time-consuming.

This project automates the initial damage classification process using deep learning.

Users can upload a vehicle image, and the trained ResNet50 model predicts its damage category along with a confidence score.

✨ Key Features

- Upload vehicle images in JPG and PNG formats.
- Deep learning-based image classification using ResNet50.
- Classifies vehicle images into six damage categories.
- FastAPI backend for model inference.
- Streamlit frontend for user interaction.
- Returns predicted damage category and confidence score.
- REST API documentation through Swagger UI.

🏷️ Damage Categories

The model predicts one of the following six categories:

Category| Description
Front Breakage| Vehicle with front-side breakage
Front Crushed| Vehicle with front-side crushing damage
Fronted Normal| Vehicle with normal front condition
Rear Breakage| Vehicle with rear-side breakage
Rear Crushed| Vehicle with rear-side crushing damage
Rear Normal| Vehicle with normal rear condition

Note: The category names and their order must match the class indices used during model training.

🛠️ Technologies Used

Technology| Purpose
Python| Programming language
PyTorch| Deep learning framework
ResNet50| Image classification model
FastAPI| Backend API development
Streamlit| Frontend user interface
Torchvision| Image transformations and pretrained models
Pillow (PIL)| Image processing
Uvicorn| ASGI server

🧠 Model Architecture

This project uses ResNet50 (Residual Network with 50 layers) for vehicle damage classification.

ResNet50 is a deep convolutional neural network that uses residual connections to improve training of deeper networks.

Why ResNet50?

- Extracts meaningful visual features from vehicle images.
- Uses residual connections to improve information flow.
- Supports transfer learning with pretrained weights.
- Suitable for image classification tasks.

Classification Process

1. Load the uploaded vehicle image.
2. Resize and preprocess the image.
3. Convert the image into a PyTorch tensor.
4. Pass the image through the trained ResNet50 model.
5. Generate predictions for six classes.
6. Apply Softmax to obtain class probabilities, if configured in the inference code.
7. Return the predicted category and confidence score.

🔄 Project Workflow

        Vehicle Image
              |
              v
       Streamlit Frontend
              |
              v
         FastAPI Backend
              |
              v
       Image Preprocessing
              |
              v
        ResNet50 Model
              |
              v
       Classification Layer
              |
              v
       Predicted Category
              |
              v
        Confidence Score
              |
              v
       Display Prediction

📂 Project Structure

vehicle-damage-detection/
│
├── main.py
├── model_helper.py
├── requirements.txt
├── README.md
│
├── models/
│   └── saved_model.pth
│
├── assets/
│   └── vehicle_damage_example.png
│
└── streamlit-app/
    ├── app.py
    └── img.png

Note: Adjust the folder structure according to your actual repository. Keep the trained model checkpoint in the "models" directory.

⚙️ Installation and Setup

1. Clone the Repository

git clone https://github.com/Teja0229/vehicle-damage-detection.git

Navigate to the project directory:

cd vehicle-damage-detection

2. Create a Virtual Environment

python -m venv .venv

Activate the environment on Windows:

.venv\Scripts\activate

3. Install Dependencies

python -m pip install --upgrade pip
pip install -r requirements.txt

Important: Ensure that your PyTorch and Torchvision versions are compatible. For CPU-only systems, install the appropriate CPU versions.

4. Verify Model File

Ensure that the trained model checkpoint exists:

models/saved_model.pth

The model architecture and checkpoint must match the implementation in "model_helper.py".

🚀 Running the Application

Step 1: Start FastAPI Backend

Open the terminal and execute:

python -m uvicorn main:app --reload

The API will run at:

http://127.0.0.1:8000

Step 2: Open Swagger Documentation

Visit:

http://127.0.0.1:8000/docs

Use the Swagger interface to test the prediction endpoint.

Step 3: Start Streamlit Frontend

Open a second terminal and run:

streamlit run streamlit-app/app.py

The Streamlit application will open in your browser.

Important: Keep both FastAPI and Streamlit running simultaneously.

🔗 API Endpoints

1. Health Check

Endpoint:

GET /health

Checks whether the API is running.

2. Vehicle Damage Prediction

Endpoint:

POST /predict

Accepts a vehicle image and returns the predicted damage category and confidence score.

Example Response

{
  "predicted_class": "Front Crushed",
  "confidence": 0.94
}

Example response only; actual output depends on the uploaded image and model prediction.

🧪 Testing

You can test the application using:

- Vehicle images in JPG format.
- Vehicle images in PNG format.
- Images showing front-side damage.
- Images showing rear-side damage.
- Images showing normal vehicle conditions.

Check whether the predicted category corresponds to the expected image label.

⚠️ Limitations

- The model performs image-level classification.
- It does not identify the exact damaged region.
- It does not generate bounding boxes around damaged areas.
- It does not estimate vehicle repair costs.
- Prediction confidence does not guarantee prediction correctness.
- Performance depends on the training dataset, image quality, and class distribution.

🔮 Future Enhancements

- Implement object detection to localize damaged regions.
- Add vehicle damage severity estimation.
- Integrate repair cost estimation.
- Expand the dataset with more vehicle images.
- Improve classification performance through hyperparameter tuning.
- Deploy the application to a cloud platform.

👨‍💻 Author

Thulasi Teja Kuruva

B.Tech – Computer Science and Engineering (Cyber Security)

GitHub: "Teja0229" (https://github.com/Teja0229)

📜 License

This project is developed for educational and learning purposes. Add an appropriate open-source license if you intend to distribute or reuse the project.
