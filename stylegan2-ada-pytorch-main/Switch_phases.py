#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from PIL import Image
import os

def process_images(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get the list of files in the input folder
    file_list = os.listdir(input_folder)

    for filename in file_list:
        if filename.endswith('.png'):
            # Open the image
            image_path = os.path.join(input_folder, filename)
            image = Image.open(image_path)

            # Create a new image with modified pixel values
            modified_image = Image.new('L', image.size)  # 'L' mode for grayscale images

            # Iterate over each pixel and modify its value
            width, height = image.size
            for x in range(width):
                for y in range(height):
                    pixel_value = image.getpixel((x, y))

                    if pixel_value == 1:
                        modified_image.putpixel((x, y), 3)
                    elif pixel_value == 2:
                        modified_image.putpixel((x, y), 1)
                    elif pixel_value == 3:
                        modified_image.putpixel((x, y), 2)

            # Save the modified image in the output folder
            output_filename = os.path.splitext(filename)[0] + '.png'
            output_path = os.path.join(output_folder, output_filename)
            modified_image.save(output_path)

            # Close the images
            image.close()
            modified_image.close()

    print("Image processing completed.")

# Specify the input and output folders
input_folder = './outs/for_stack_filtered'
output_folder = './outs/for_stack_filtered_10000_switched'

# Process the images
process_images(input_folder, output_folder)

