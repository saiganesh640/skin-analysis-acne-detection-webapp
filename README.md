#  Skin Analysis & Acne Detection WebApp

A full-stack web app that analyzes facial images to detect acne severity (Clear, Moderate, Severe) and delivers personalized skincare recommendations, combining deep learning (TensorFlow) with an intuitive PHP/XAMPP frontend for accessible, real-time skin health insights.


---

##  Project Overview
![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange?logo=tensorflow)
![Keras](https://img.shields.io/badge/Keras-Deep_Learning-red?logo=keras)
![Flask](https://img.shields.io/badge/Flask-Web_Framework-black?logo=flask)
![PHP](https://img.shields.io/badge/PHP-7.4%2B-blue?logo=php)
![MySQL](https://img.shields.io/badge/MySQL-Database-blue?logo=mysql)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow?logo=javascript)
![HTML5](https://img.shields.io/badge/HTML5-Web-orange?logo=html5)
![CSS3](https://img.shields.io/badge/CSS3-Stylesheet-blue?logo=css3)


This project is a friendly AI-powered Skin Health Analyzer that helps you understand your acne severity from a simple facial photo. It combines smart deep learning technology with a smooth web experience built using Flask and PHP. After signing up and answering a quick skin quiz, you can upload or snap a picture of your face, and the AI will tell you whether your skin is Clear, Moderate, or Severely affected by acne  with a confidence score. Based on both your quiz answers and the AI’s prediction, it also gives you personalized tips to take better care of your skin.

In short, it’s like having a skin expert and a helpful assistant right in your browser, making skincare easier and more personalized for everyone.

**Key Features:**
- User registration and login
- Skin health quiz
- Image capture or upload (webcam/file)
- AI-powered acne severity detection (Clear / Moderate / Severe)
- Confidence score for predictions
- Personalized skincare recommendations

---

##  Tech Stack

| Layer         | Technology                       |
|---------------|----------------------------------|
| Machine Learn | TensorFlow, Keras, NumPy, Pillow |
| Backend API   | Flask, Flask-CORS                |
| Frontend      | PHP, HTML5, CSS3, JavaScript     |
| Database      | MySQL (via XAMPP)                |
| Environment   | Python 3.11, XAMPP, VS Code      |


---

##  Folder Structure

<img width="368" height="686" alt="image" src="https://github.com/user-attachments/assets/ebbba444-8bfc-4d88-ad84-ac2c7c0002b8" />


---
## 🧱 Step-by-Step Model Creation Process

### Step 1️ — Data Collection
- Collected a dataset of acne images representing 3 categories:
  - `Clear`
  - `Moderate`
  - `Severe`
- Images are resized and normalized for consistent input to the CNN model.

---

### Step 2️ — Data Preprocessing  
**File:** `data_preprocessing.py`
Tasks handled:
- Image normalization (pixel values scaled 0–1)
- Resizing to (224x224)
- Train/Test split (80:20)
- Augmentation (rotation, flip, zoom)
text

---

### Step 3️ — Model Building  
**File:** `model_building.py`
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

Model Architecture (CNN)
model = Sequential([
Conv2D(32, (3,3), activation='relu', input_shape=(224,224,3)),
MaxPooling2D(2,2),
Conv2D(64, (3,3), activation='relu'),
MaxPooling2D(2,2),
Flatten(),
Dense(128, activation='relu'),
Dense(3, activation='softmax') # 3 classes: Clear, Moderate, Severe
])

---

### Step 4️ — Model Training  
**File:** `train_model.py`

✅ Output: `acne_detection_model.h5` — your trained Deep Learning model.

---

### Step 5️ — Model Evaluation  
**File:** `evaluate_model.py`
loss, acc = model.evaluate(test_data)
print(f"Accuracy: {acc*100:.2f}%")

---

### Step 6️ — Model Deployment via Flask  
**File:** `flask_model_api.py`

✅ Flask runs at: [http://127.0.0.1:5000/predict](http://127.0.0.1:5000/predict)

---

## 🌐 Web Frontend – Skin Analyzer WebApp

Handles user interaction, quiz input, image capture/upload, and displaying results.

### Folder Structure (WebApp)

<img width="657" height="336" alt="image" src="https://github.com/user-attachments/assets/8c0f7d01-617a-4f5d-8fff-8ad0baeba3b9" />

---

### Frontend Workflow

#### Step 1️ — User Login / Registration  
- PHP connects to MySQL (`users4` table) for user authentication via `db.php`.

#### Step 2️ — Skin Health Quiz  
- `quiz.html` contains 5 questions about skin type, sleep, hydration, etc.  
- On submit, quiz answers are saved to browser storage:
localStorage.setItem("quiz_answers", JSON.stringify(answers));

text

#### Step 3️ — Capture or Upload Image  
- `camera.html` lets users:
  - Capture image via webcam (`getUserMedia()` API)  
  - Or upload image manually  
- Sends image + quiz JSON to `upload_and_predict.php`.

#### Step 4️ — Backend Integration (PHP → Flask)  
**File:** `upload_and_predict.php`
$cfile = new CURLFile($_FILES['image']['tmp_name']);
$post = ['image' => $cfile, 'quiz' => $_POST['quiz']];
curl_setopt($curl, CURLOPT_URL, 'http://127.0.0.1:5000/predict');
// Forward request to Flask API and return JSON response

text

#### Step 5️ — AI Result Display  
**File:** `result.html`
- Displays prediction and skincare improvement recommendations.

#### Step 6️ — Recommendation System  
**File:** `recommendation.html`  
- Custom advice based on the model result:  
  - Clear → Maintain routine  
  - Moderate → Mild acne treatment  
  - Severe → Dermatologist consultation

##  Model Explanation

1. **Data Collection**: Images categorized as Clear, Moderate, Severe.
2. **Preprocessing**: Image resizing, normalization, augmentation.
3. **Model Building**: Convolutional Neural Network (CNN) with Keras/TensorFlow.
4. **Training**: Optimizer = Adam, Loss = categorical_crossentropy.
5. **Evaluation**: Accuracy and confusion matrix calculation.
6. **Deployment**: Flask API for serving real-time predictions.

---

##  Frontend Workflow

1. User authentication (login/registration)
2. Skin health quiz for personal data
3. Image capture/upload (webcam or file)
4. PHP backend sends image & quiz data to Flask API
5. Displays result and recommendations
6. Personalized skincare advice based on results

---

##  Future Enhancements

- Build a more responsive and modern frontend using React.js for smoother user experience  
- Deploy the Flask API on cloud platforms like AWS Lambda or Render for easy scalability and uptime  
- Improve the acne detection accuracy by training the CNN model on a larger and more diverse dataset  
- Add a feature to store users’ past skin analysis results in MySQL for tracking progress over time  
- Explore adding a voice-based AI assistant to make skincare advice even more accessible and interactive  


---

##  Contact details

**Pitta Saiganesh**

**Python | Machine Learning**


[LinkedIn](https://www.linkedin.com/in/sai-ganesh-s15092005) | [GitHub](https://github.com/saiganesh640) | [Email](mailto:saiganesh1901@gmail.com)

---

remaining 4 files/folders and datasets present in (acne detection project) folder is in my google drive , so i am sharing the drive link with you all  

1. https://drive.google.com/drive/folders/10rG4bgMrSpjHQySrB2gb5MhUIdl_qRaa?usp=drive_link
2. https://drive.google.com/drive/folders/1RWY_5Qpz9OyGiuXDSrRnJqyo34JmMgy7?usp=drive_link
3. https://drive.google.com/drive/folders/1LXmoKj6qLhVXpPLRJEaja6BlQo2z8Cbc?usp=drive_link
4. https://drive.google.com/drive/folders/1vitNc8fqloRD94o0HT3nTd8k6znK3aG0?usp=drive_link



