import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# --- 1. DEFINE PATHS AND PARAMETERS ---

# These paths should point to the folders created by the splitting script
train_dir = 'split_dataset/train'
validation_dir = 'split_dataset/validation'

# Define image parameters
IMG_HEIGHT = 224
IMG_WIDTH = 224
BATCH_SIZE = 32

# --- 2. CREATE THE IMAGE DATA GENERATORS ---

# Create a data generator for the training data WITH augmentation.
# This creates new, altered images on-the-fly during training.
train_image_generator = ImageDataGenerator(
    rescale=1./255,                 # Normalize pixel values to be between 0 and 1
    rotation_range=40,              # Randomly rotate images up to 40 degrees
    width_shift_range=0.2,          # Randomly shift images horizontally by 20%
    height_shift_range=0.2,         # Randomly shift images vertically by 20%
    shear_range=0.2,                # Apply shearing transformations
    zoom_range=0.2,                 # Randomly zoom in on images by 20%
    horizontal_flip=True,           # Randomly flip images horizontally
    fill_mode='nearest'             # How to fill in new pixels that may appear
                                    # after a rotation or a width/height shift.
)

# Create a data generator for the validation data WITHOUT augmentation.
# We only need to rescale the validation images; we do not augment them.
validation_image_generator = ImageDataGenerator(
    rescale=1./255
)

# --- 3. LOAD DATA FROM DIRECTORIES USING THE GENERATORS ---

# This will find all images in the specified directories, apply the
# generator settings, and prepare them in batches.
train_data_gen = train_image_generator.flow_from_directory(
    directory=train_dir,
    target_size=(IMG_HEIGHT, IMG_WIDTH),
    batch_size=BATCH_SIZE,
    class_mode='categorical'  # For multi-class classification
)

val_data_gen = validation_image_generator.flow_from_directory(
    directory=validation_dir,
    target_size=(IMG_HEIGHT, IMG_WIDTH),
    batch_size=BATCH_SIZE,
    class_mode='categorical'
)

print("Data generators are ready.")
print("The model will receive training data from 'train_data_gen'.")
print("The model will be validated against data from 'val_data_gen'.")

