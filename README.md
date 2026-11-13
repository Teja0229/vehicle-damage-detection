Vehicle Damage Detection Using ResNet50

A deep learning project that predicts vehicle damage categories from uploaded images using a trained ResNet50 model.

Features

- Upload vehicle images (JPG/PNG).
- Predicts vehicle damage using ResNet50.
- Returns the predicted category and confidence score.
- FastAPI for backend API.
- Streamlit for user interface.

Damage Categories

1. Front Breakage
2. Front Crushed
3. Fronted Normal
4. Rear Breakage
5. Rear Crushed
6. Rear Normal

Technologies Used

- Python
- PyTorch
- ResNet50
- FastAPI
- Streamlit
- Torchvision

Project Workflow

Vehicle Image → FastAPI → Image Preprocessing → ResNet50 Model → Predicted Damage Category

Installation

Clone the repository:

git clone https://github.com/Teja0229/vehicle-damage-detection.git
cd vehicle-damage-detection

Install dependencies:

pip install -r requirements.txt

Run the Application

Start FastAPI:

python -m uvicorn main:app --reload

Open API documentation:

http://127.0.0.1:8000/docs

Start Streamlit in another terminal:

streamlit run streamlit-app/app.py

Project Output

The application displays the predicted vehicle damage category along with its confidence score.

Limitations

- Classifies the entire vehicle image.
- Does not identify exact damaged regions.
- Does not estimate repair costs.

Author

Thulasi Teja Kuruva

GitHub: https://github.com/Teja0229
