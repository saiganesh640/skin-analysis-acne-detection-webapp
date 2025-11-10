import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

# --- PAGE CONFIGURATION ---
# Sets the title and icon of the browser tab
st.set_page_config(
    page_title="REAL TIME ACNE DETECTION",
    page_icon="",
    layout="centered",
    initial_sidebar_state="auto",
)

# --- MODEL LOADING ---
# Cache the model loading to prevent reloading on every interaction
@st.cache_resource
def load_acne_model():
    """Loads the pre-trained acne detection model."""
    model_path = 'acne_detection_model.h5'
    try:
        model = tf.keras.models.load_model(model_path)
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

model = load_acne_model()

# --- CLASS LABELS ---
# The names of the classes your model predicts
# Ensure this order matches the training order (usually alphabetical)
CLASS_NAMES = ['Clear Skin', 'Moderate Acne', 'Severe Acne']

# --- IMAGE PREPROCESSING ---
def preprocess_image(image):
    """Preprocesses the uploaded image to be model-ready."""
    # Resize the image to the model's expected input size
    image = image.resize((224, 224))
    # Convert the image to a numpy array
    image_array = np.array(image)
    # Normalize the pixel values to be between 0 and 1
    image_array = image_array / 255.0
    # Expand dimensions to create a batch of 1
    image_array = np.expand_dims(image_array, axis=0)
    return image_array

# --- UI DESIGN ---
st.title("Real time acne detection ")
st.markdown(
    "Upload an image or use your camera to get an AI-based analysis of skin condition. "
    "This tool helps classify skin as clear, moderately affected, or severely affected by acne."
)


# --- SIDEBAR FOR IMAGE UPLOAD ---
st.sidebar.header("Input Image")
source_option = st.sidebar.radio("Select Image Source", ["Upload an Image", "Use Camera"])

uploaded_file = None
camera_input = None

if source_option == "Upload an Image":
    uploaded_file = st.sidebar.file_uploader(
        "Choose an image...", type=["jpg", "jpeg", "png"]
    )
else:
    camera_input = st.sidebar.camera_input("Take a picture")

# --- MAIN PANEL FOR DISPLAY AND PREDICTION ---
if uploaded_file or camera_input:
    # Determine the image source
    image_source = uploaded_file if uploaded_file else camera_input
    
    # Display the image
    image = Image.open(image_source).convert("RGB")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.image(image, caption="Your Image", use_column_width=True)

    with col2:
        if st.button("Analyze Skin Condition", use_container_width=True):
            if model:
                with st.spinner("AI is analyzing the image..."):
                    # Preprocess the image and make a prediction
                    processed_image = preprocess_image(image)
                    prediction = model.predict(processed_image)
                    
                    # Get the predicted class and confidence
                    predicted_class_index = np.argmax(prediction)
                    predicted_class_name = CLASS_NAMES[predicted_class_index]
                    confidence = np.max(prediction) * 100

                    st.success("Analysis Complete!")
                    
                    # Display the result
                    st.metric(label="Predicted Condition", value=predicted_class_name)
                    st.metric(label="Confidence", value=f"{confidence:.2f}%")

                    # Provide a simple description based on the prediction
                    if predicted_class_name == 'Clear Skin':
                        st.info("The model indicates the skin is likely clear with no significant acne.")
                    elif predicted_class_name == 'Moderate Acne':
                        st.warning("The model suggests a moderate level of acne may be present.")
                    elif predicted_class_name == 'Severe Acne':
                        st.error("The model indicates that signs of severe acne may be present. Professional consultation is recommended.")
            else:
                st.error("Model not loaded. Cannot perform analysis.")
else:
    st.info("Please upload an image or use the camera to begin the analysis.")