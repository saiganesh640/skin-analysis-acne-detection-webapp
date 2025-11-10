import os
import shutil
import random

def split_image_dataset(source_dir, dest_dir, train_split_ratio=0.8):
    """
    Splits an image dataset organized by class folders into training and validation sets.

    Args:
      source_dir (str): Path to the folder containing the class subfolders
                        (e.g., 'clear skin data', 'moderate acne data').
      dest_dir (str): Path to the folder where 'train' and 'validation' folders
                      will be created.
      train_split_ratio (float): The percentage of data to be used for training (e.g., 0.8 for 80%).
    """
    # Create the destination, train, and validation directories
    train_dir = os.path.join(dest_dir, 'train')
    validation_dir = os.path.join(dest_dir, 'validation')

    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(validation_dir, exist_ok=True)

    print(f"Splitting data from '{source_dir}' into '{dest_dir}'...")

    # Iterate through each class folder in the source directory
    for class_name in os.listdir(source_dir):
        class_path = os.path.join(source_dir, class_name)
        if not os.path.isdir(class_path):
            continue

        # Create the class subfolders in both train and validation directories
        os.makedirs(os.path.join(train_dir, class_name), exist_ok=True)
        os.makedirs(os.path.join(validation_dir, class_name), exist_ok=True)

        # Get a list of all files in the class folder and shuffle them
        all_files = [f for f in os.listdir(class_path) if os.path.isfile(os.path.join(class_path, f))]
        random.shuffle(all_files)

        # Calculate the split point
        split_index = int(len(all_files) * train_split_ratio)
        train_files = all_files[:split_index]
        validation_files = all_files[split_index:]

        # Copy files to the training directory
        for file_name in train_files:
            shutil.copy(os.path.join(class_path, file_name), os.path.join(train_dir, class_name, file_name))

        # Copy files to the validation directory
        for file_name in validation_files:
            shutil.copy(os.path.join(class_path, file_name), os.path.join(validation_dir, class_name, file_name))
        
        print(f"- Class '{class_name}': {len(train_files)} training images, {len(validation_files)} validation images.")

    print("\nSplitting complete!")

# --- HOW TO USE ---

# 1. Set the name of your main folder that contains the class subfolders.
#    (e.g., 'MyAcneDataset', or whatever your folder is called)
SOURCE_FOLDER = 'dataset'

# 2. Set the name for the new folder where the split data will be saved.
DESTINATION_FOLDER = 'split_dataset'

# --- RUN THE SCRIPT ---
split_image_dataset(SOURCE_FOLDER, DESTINATION_FOLDER)