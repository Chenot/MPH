from PIL import Image, ImageOps
import os

# Define the directory containing the source images
source_directory = r'D:\Google Drive\Professionnel\3_Post-doc_ISAE-MPH\Experience_MPH\project\code\PsychopyTasks\Speed_Symbols\ressources\save'

# Define the directory to save the processed images
destination_directory = r'D:\Google Drive\Professionnel\3_Post-doc_ISAE-MPH\Experience_MPH\project\code\PsychopyTasks\Speed_Symbols\ressources'

# Function to resize an image and invert colors
def process_image(file_path, destination_path, scale_factor=0.2):
    # Open an image file
    with Image.open(file_path) as img:
        # Ensure the image is in RGBA mode
        img = img.convert("RGBA")
        # Calculate new dimensions
        new_width = int(img.width * scale_factor)
        new_height = int(img.height * scale_factor)
        # Resize the image
        resized_img = img.resize((new_width, new_height), Image.LANCZOS)
        # Split the image into RGBA bands
        r, g, b, a = resized_img.split()
        # Invert the RGB bands
        rgb_inverted = ImageOps.invert(Image.merge("RGB", (r, g, b)))
        # Merge the inverted RGB bands with the original alpha channel
        inverted_img = Image.merge("RGBA", (rgb_inverted.getchannel("R"),
                                            rgb_inverted.getchannel("G"),
                                            rgb_inverted.getchannel("B"),
                                            a))
        # Save it to the destination path
        inverted_img.save(destination_path, "PNG", optimize=True)

# Iterate over all files in the source directory
for filename in os.listdir(source_directory):
    if filename.endswith(".png"):
        source_file_path = os.path.join(source_directory, filename)
        destination_file_path = os.path.join(destination_directory, filename)
        print(f"Processing {source_file_path}...")
        process_image(source_file_path, destination_file_path)
        print(f"Processed {destination_file_path}")

print("All images have been processed.")
