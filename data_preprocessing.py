# data_preprocessing.py

import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# --- Define Paths and Parameters ---
train_dir = 'split_dataset/train'
validation_dir = 'split_dataset/validation'

# This is where you set the desired size for all images.
IMG_HEIGHT = 224
IMG_WIDTH = 224
BATCH_SIZE = 32

# --- Create the Image Data Generators ---

# This generator will apply transformations to the training images.
train_image_generator = ImageDataGenerator(
    # This line handles the NORMALIZATION for the training images.
    # It divides every pixel's value by 255, scaling them to the 0-1 range.
    rescale=1./255,

    # These are the data augmentation steps
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

# This generator is for the validation images.
validation_image_generator = ImageDataGenerator(
    # This line handles the NORMALIZATION for the validation images.
    rescale=1./255
)


# --- Load Data and Apply Preprocessing ---

# When loading the data, Keras automatically performs the preprocessing.
train_data_gen = train_image_generator.flow_from_directory(
    directory=train_dir,

    # This line handles the RESIZING for the training images.
    # It ensures every image is converted to 224x224 pixels.
    target_size=(IMG_HEIGHT, IMG_WIDTH),

    batch_size=BATCH_SIZE,
    class_mode='categorical'
)

val_data_gen = validation_image_generator.flow_from_directory(
    directory=validation_dir,

    # This line handles the RESIZING for the validation images.
    target_size=(IMG_HEIGHT, IMG_WIDTH),

    batch_size=BATCH_SIZE,
    class_mode='categorical'
)

print("Data preprocessing (resizing and normalization) is set up and will be applied automatically.")