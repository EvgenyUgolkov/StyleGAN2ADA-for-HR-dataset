#!/usr/bin/env python
# coding: utf-8

# In[9]:


import os
from PIL import Image, ImageFilter

def apply_median_filter(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Get the list of PNG files in the input folder
    file_list = [f for f in os.listdir(input_folder) if f.endswith('.png')]

    # Process each image in the input folder
    for file_name in file_list:
        # Read the image using PIL
        image_path = os.path.join(input_folder, file_name)
        image = Image.open(image_path)

        # Apply median filter to the image
        filtered_image = image.filter(ImageFilter.MedianFilter(size=3))  # Adjust the size as needed

        # Save the filtered image to the output folder
        output_path = os.path.join(output_folder, file_name)
        filtered_image.save(output_path)

        print(f"Processed: {file_name}")

    print("Filtering completed!")

# Specify the input and output folders
input_folder = './outs/for_stack'
output_folder = './outs/for_stack_filtered'

# Call the function to apply median filter to the images
apply_median_filter(input_folder, output_folder)

