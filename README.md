#  Skin Analysis & Acne Detection WebApp

A full-stack web app that analyzes facial images to detect acne severity (Clear, Moderate, Severe) and delivers personalized skincare recommendations, combining deep learning (TensorFlow) with an intuitive PHP/XAMPP frontend for accessible, real-time skin health insights.


---

## 🧩 Project Overview

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

## 🧠 Tech Stack

| Layer         | Technology                       |
|---------------|----------------------------------|
| Machine Learn | TensorFlow, Keras, NumPy, Pillow |
| Backend API   | Flask, Flask-CORS                |
| Frontend      | PHP, HTML5, CSS3, JavaScript     |
| Database      | MySQL (via XAMPP)                |
| Environment   | Python 3.11, XAMPP, VS Code      |


---

## 📂 Folder Structure

<img width="389" height="684" alt="image" src="https://github.com/user-attachments/assets/59f8eba4-249c-40bb-a24b-f6c65ab9c4aa" />

---

## 🚀 Setup Instructions

### 1. Clone the Repository

### 2. Run Flask Model API

cd acne_detection_project
pip install -r requirements.txt
text
Flask API will run at: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

### 3. Setup PHP Frontend

- Move the `skin_analyzer` folder to your XAMPP `htdocs` directory:

C:\xampp\htdocs\skin_analyzer

text

- Start Apache and MySQL in XAMPP.


---

## 🤖 Model Explanation

**AI Pipeline:**

1. **Data Collection**: Images categorized as Clear, Moderate, Severe.
2. **Preprocessing**: Image resizing, normalization, augmentation.
3. **Model Building**: Convolutional Neural Network (CNN) with Keras/TensorFlow.
4. **Training**: Optimizer = Adam, Loss = categorical_crossentropy.
5. **Evaluation**: Accuracy and confusion matrix calculation.
6. **Deployment**: Flask API for serving real-time predictions.

---

## 🌐 Frontend Workflow

1. User authentication (login/registration)
2. Skin health quiz for personal data
3. Image capture/upload (webcam or file)
4. PHP backend sends image & quiz data to Flask API
5. Displays result and recommendations
6. Personalized skincare advice based on results

---

## 💡 Future Enhancements

- Convert frontend to React.js for better responsiveness
- Deploy Flask API to AWS Lambda or Render
- Enhance CNN accuracy using a larger dataset
- Store analysis history in MySQL
- Add a voice-based AI skincare assistant

---

## contact details

**Pitta Saiganesh**

**Python | Machine Learning**


[LinkedIn](https://www.linkedin.com/in/sai-ganesh-s15092005) | [GitHub](https://github.com/saiganesh640) | [Email](mailto:saiganesh1901@gmail.com)



## 📜 License

You are free to use, modify, and distribute this project for educational or research purposes with appropriate credit.
