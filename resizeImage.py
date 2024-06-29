from PIL import Image
import os

def resize_image(image_path, output_folder, new_width, new_height):
  """
  Resizes an image and saves it to a new location.

  Args:
      image_path: Path to the image file.
      output_folder: Path to the folder where the resized image will be saved.
      new_width: The desired width of the resized image.
      new_height: The desired height of the resized image.
  """
  # Open the image
  image = Image.open(image_path)

  # Maintain aspect ratio if only one dimension is provided
  width, height = image.size
  if new_width and not new_height:
    new_height = int(height * (new_width / width))
  elif new_height and not new_width:
    new_width = int(width * (new_height / height))

  # Resize the image
  resized_image = image.resize((new_width, new_height))

  # Get the filename
  filename = os.path.basename(image_path)

  # Create output path (optional: add prefix to avoid overwriting)
  output_path = os.path.join(output_folder, f"resized_{filename}")

  # Save the resized image
  resized_image.save(output_path)

def resize_images(folder_path, output_folder, new_width, new_height):
  """
  Resizes all images in a folder and saves them to a new folder.

  Args:
      folder_path: Path to the folder containing the images.
      output_folder: Path to the folder where the resized images will be saved.
      new_width: The desired width of the resized images.
      new_height: The desired height of the resized images.
  """
  # Create output folder if it doesn't exist
  os.makedirs(output_folder, exist_ok=True)  

  for filename in os.listdir(folder_path):
    # Check if it's an image file
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
      image_path = os.path.join(folder_path, filename)
      resize_image(image_path, output_folder, new_width, new_height)

# Edit these variables with your desired values
folder_path = "D:/hoctap/deeplearning/handTracking/handFinger"
output_folder = "D:/hoctap/deeplearning/handTracking/handTracking"
new_width = 120  # Optional, set width if you want to resize based on width
new_height = 120  # Optional, set height if you want to resize based on height

# Run the function to resize images
resize_images(folder_path, output_folder, new_width, new_height)

print("Images resized successfully!")
