# evaluate_model.py

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import classification_report, confusion_matrix

# --- 1. LOAD THE TRAINED MODEL AND DATA ---

# Define paths and parameters
MODEL_PATH = 'acne_detection_model.h5'
VALIDATION_DIR = 'split_dataset/validation'
IMG_HEIGHT = 224
IMG_WIDTH = 224
BATCH_SIZE = 32

# Load the model you saved after training
print(f"Loading model from: {MODEL_PATH}")
model = tf.keras.models.load_model(MODEL_PATH)

# Create a data generator for the validation set (IMPORTANT: NO AUGMENTATION)
# We only need to rescale the pixels, just like we did for validation during training.
validation_datagen = ImageDataGenerator(rescale=1./255)

# Create the generator to load images from the directory
# Set shuffle=False so the predictions and true labels are in the same order.
validation_generator = validation_datagen.flow_from_directory(
    directory=VALIDATION_DIR,
    target_size=(IMG_WIDTH, IMG_HEIGHT),
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    shuffle=False  # Crucial for confusion matrix
)

# --- 2. EVALUATE ACCURACY AND LOSS ---

# Use the .evaluate() method to get the final loss and accuracy
print("\nEvaluating model on the validation set...")
loss, accuracy = model.evaluate(validation_generator)
print(f"Validation Loss: {loss:.4f}")
print(f"Validation Accuracy: {accuracy*100:.2f}%")


# --- 3. GENERATE THE CONFUSION MATRIX ---

print("\nGenerating confusion matrix and classification report...")
# Get the true labels from the generator
y_true = validation_generator.classes

# Get the predicted probabilities for each class
y_pred_probs = model.predict(validation_generator)

# Convert the probabilities to class predictions (the index of the highest probability)
y_pred = np.argmax(y_pred_probs, axis=1)

# Get the class names (labels) from the generator
class_labels = list(validation_generator.class_indices.keys())

# --- Print Classification Report ---
# This shows precision, recall, and f1-score for each class
print("\nClassification Report:")
print(classification_report(y_true, y_pred, target_names=class_labels))


# --- Create and Display the Confusion Matrix ---
conf_matrix = confusion_matrix(y_true, y_pred)

plt.figure(figsize=(10, 8))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues',
            xticklabels=class_labels, yticklabels=class_labels)

plt.title('Confusion Matrix')
plt.ylabel('Actual Class')
plt.xlabel('Predicted Class')
plt.show()