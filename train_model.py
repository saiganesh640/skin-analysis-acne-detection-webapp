import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense, Dropout
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam

# --- 1. DATA PREPROCESSING (FROM STEP 2) ---

# Define paths and parameters
train_dir = 'split_dataset/train'
validation_dir = 'split_dataset/validation'
IMG_HEIGHT = 224
IMG_WIDTH = 224
BATCH_SIZE = 32

# Set up data generators with augmentation for training and rescaling for validation
train_image_generator = ImageDataGenerator(
    rescale=1./255,
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

validation_image_generator = ImageDataGenerator(rescale=1./255)

# Load data from directories
train_data_gen = train_image_generator.flow_from_directory(
    directory=train_dir,
    target_size=(IMG_HEIGHT, IMG_WIDTH),
    batch_size=BATCH_SIZE,
    class_mode='categorical'
)

val_data_gen = validation_image_generator.flow_from_directory(
    directory=validation_dir,
    target_size=(IMG_HEIGHT, IMG_WIDTH),
    batch_size=BATCH_SIZE,
    class_mode='categorical'
)

# --- 2. MODEL BUILDING (FROM STEP 3) ---

# Load the base MobileNetV2 model and freeze it
base_model = MobileNetV2(input_shape=(IMG_HEIGHT, IMG_WIDTH, 3),
                       include_top=False,
                       weights='imagenet')
base_model.trainable = False

# Add the custom classification head
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(1024, activation='relu')(x)
x = Dropout(0.5)(x)
predictions = Dense(train_data_gen.num_classes, activation='softmax')(x)

# Create the final model
model = Model(inputs=base_model.input, outputs=predictions)


# --- 3. TRAINING THE MODEL (STEP 4) ---

# --- Compile the Model ---
# This configures the model for training.
print("\nCompiling the model...")
model.compile(
    # Optimizer: Adam is an efficient choice that adapts the learning rate.
    optimizer=Adam(learning_rate=0.0001),
    
    # Loss Function: 'categorical_crossentropy' is used for multi-class classification.
    # It measures how well the predicted probabilities match the actual labels.
    loss='categorical_crossentropy',
    
    # Metrics: We monitor 'accuracy' to see the percentage of correctly classified images.
    metrics=['accuracy']
)
print("Model compiled.")

# --- Train the Model ---
# The model.fit() function starts the actual training process.
NUM_EPOCHS = 20  # You can start with 20 and increase if needed

print(f"\nStarting model training for {NUM_EPOCHS} epochs...")

history = model.fit(
    train_data_gen,
    epochs=NUM_EPOCHS,
    validation_data=val_data_gen,
    steps_per_epoch=train_data_gen.samples // BATCH_SIZE,
    validation_steps=val_data_gen.samples // BATCH_SIZE
)

print("\nTraining has completed!")

# --- 4. SAVE THE TRAINED MODEL ---
# This saves the entire model (architecture, weights, etc.) to a single file.
model.save('acne_detection_model.h5')
print("Model has been saved to 'acne_detection_model.h5'")