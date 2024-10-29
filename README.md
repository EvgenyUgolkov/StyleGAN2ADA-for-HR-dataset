# Pre-processing  

Before running the StyleGAN2ADA for generating 2D High-Resolution segmented training dataset, we need to pre-process the microscope images:  

1. Actually, segmenting the images. We did it manually with 4 phases: 0 = pore, 1 = quartz, 2 = fesdspar, and 3 = clay
2. Rescale images before "feeding" them to the StyleGAN2ADA because it was designed to work with 0-255 range. This way, for each segmentatied phase, we give a corresponding value in 0-255 range. You can use ```Step 1``` size in the (Post_segmentation_procedure)[Post_segmentation_procedure] notebook
