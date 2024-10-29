#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import numpy as np
from PIL import Image
import tifffile as tiff

# Path to the folder containing the PNG images
folder_path = "./outs/for_stack_filtered_10000_switched"

# Get a list of all PNG files in the folder
png_files = [f for f in os.listdir(folder_path) if f.endswith(".png")]

# Sort the files alphabetically
png_files.sort()

# Load the first image to get the dimensions
first_image_path = os.path.join(folder_path, png_files[0])
first_image = Image.open(first_image_path)
width, height = first_image.size

# Create an empty 3D volume
volume = np.zeros((len(png_files), height, width), dtype=np.uint8)

# Iterate over the PNG files and stack them in the volume
for i, png_file in enumerate(png_files):
    image_path = os.path.join(folder_path, png_file)
    image = Image.open(image_path)
    volume[i, :, :] = np.array(image)

# Save the volume as a TIFF file
output_directory = "./outs/Stack"
output_path = os.path.join(output_directory, "Berea_CSLM_new_10000_switched.tiff")
tiff.imsave(output_path, volume)

