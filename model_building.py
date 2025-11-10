import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense, Dropout
from tensorflow.keras.models import Model

def build_model(input_shape=(224, 224, 3), num_classes=3):
    """
    Builds a transfer learning model using the 3-step process.

    Args:
      input_shape (tuple): The shape of the input images.
      num_classes (int): The number of output classes for classification.

    Returns:
      A Keras Model object.
    """

    # ---
    # The Process:
    # ---

    # 1. Load the Pre-trained Model
    # We load the MobileNetV2 model pre-trained on the ImageNet dataset.
    # `include_top=False` ensures that the final classification layer of
    # MobileNetV2 is not included, allowing us to add our own.
    base_model = MobileNetV2(input_shape=input_shape,
                           include_top=False,
                           weights='imagenet')

    # 2. Freeze the Base Layers
    # This is a critical step. It locks the weights of the pre-trained layers,
    # so they are not updated during training. We are using MobileNetV2 as a
    # fixed feature extractor.
    base_model.trainable = False

    # 3. Add Your Custom Layers
    # This creates a new classification "head" on top of the base model.
    
    # Get the output from the last layer of the base model
    x = base_model.output
    
    # Add a GlobalAveragePooling2D layer to flatten the features into a vector
    x = GlobalAveragePooling2D()(x)
    
    # Add a fully-connected Dense layer with 1024 neurons to learn complex patterns
    x = Dense(1024, activation='relu')(x)
    
    # Add a Dropout layer to help prevent overfitting
    x = Dropout(0.5)(x)
    
    # Add the final output layer. It must have one neuron for each class.
    # The 'softmax' activation function converts the outputs into a probability
    # for each of the 3 classes.
    predictions = Dense(num_classes, activation='softmax')(x)

    # ---
    # Create the final model by specifying the input and output layers
    # ---
    final_model = Model(inputs=base_model.input, outputs=predictions)

    return final_model

# This part of the script will only run when you execute the file directly.
# It's useful for verifying that the model builds correctly.
if __name__ == '__main__':
    # Create the model by calling the function
    model = build_model()

    # Print a summary of the model's architecture.
    print("--- Model Built Successfully ---")
    print("This summary shows the MobileNetV2 base followed by your new custom layers.")
    model.summary()