from PIL import Image
import os

# Define the directory containing the images
directory = r'D:\Google Drive\Professionnel\3_Post-doc_ISAE-MPH\Experience_MPH\project\code\PsychopyTasks\Speed_Coding\ressources'

# Function to resize an image
def resize_image(file_path, scale_factor=0.2):
    # Open an image file
    with Image.open(file_path) as img:
        # Calculate new dimensions
        new_width = int(img.width * scale_factor)
        new_height = int(img.height * scale_factor)
        # Resize the image
        resized_img = img.resize((new_width, new_height), Image.LANCZOS)
        # Save it back to the same file path
        resized_img.save(file_path, "PNG", optimize=True)

# Iterate over all files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".png"):
        file_path = os.path.join(directory, filename)
        print(f"Resizing {file_path}...")
        resize_image(file_path)
        print(f"Resized {file_path}")

print("All images have been resized.")
