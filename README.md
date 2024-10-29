# Pre-processing  

Before running the StyleGAN2ADA for generating 2D High-Resolution segmented training dataset, we need to pre-process the microscope images:  

1. Actually, segmenting the images. We did it manually with 4 phases: 0 = pore, 1 = quartz, 2 = fesdspar, and 3 = clay
2. Rescale images before "feeding" them to the StyleGAN2ADA because it was designed to work with 0-255 range. This way, for each segmentatied phase, we give a corresponding value in 0-255 range. You can use ```Step 1``` in the [Post_segmentation_procedure](Post_segmentation_procedure.ipynb) notebook
3. Take the segmented images and extract patches of size 1024x1024 with overlap. You can use ```Step 2``` in the [Post_segmentation_procedure](Post_segmentation_procedure.ipynb) notebook
4. Archive (zip) the obtained images and also put the .json file inside. As example, reference Seg_1024.zip
5. Put the .zip file into the code folder. Now, everything ready to start training StyleGAN2ADA

# Training  

1. 

