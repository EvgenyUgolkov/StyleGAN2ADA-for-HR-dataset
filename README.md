# Important  

We apply the famous StyleGAN2ADA for generating High-Resolution images of rocks. The authentic repository can be found here  
https://github.com/NVlabs/stylegan2-ada-pytorch

# Overview  

This repository contains information about how to use StyleGAN2ADA to create a training dataset with High-Resolution images of rocks as follow  

![Super-Resolution results for Berea sandstone](GitHub_images/image.png)

# Pre-processing  

Before running the StyleGAN2ADA for generating 2D High-Resolution segmented training dataset, we need to pre-process the microscope images:  

1. Actually, segment the images. We did it manually, in Avizo software, with 4 phases: 0 = pore, 1 = quartz, 2 = fesdspar, and 3 = clay
2. Rescale images before "feeding" them to the StyleGAN2ADA because it was designed to work with 0-255 range. This way, for each segmentatied phase, we give a corresponding value in 0-255 range. You can use ```Step 1``` in the [Post_segmentation_procedure](Post_segmentation_procedure.ipynb) notebook
3. Take the segmented images and extract patches of size 1024x1024 with overlap. You can use ```Step 2``` in the [Post_segmentation_procedure](Post_segmentation_procedure.ipynb) notebook
4. Archive (zip) the obtained images and also put the .json file inside. As example, reference Seg_1024.zip
5. Put the .zip file into the [code](stylegan2-ada-pytorch-main) folder. Now, everything ready to start training StyleGAN2ADA

# Training  

To start the training, from the [code](stylegan2-ada-pytorch-main) folder, run
```
train.py --outdir=training-runs --data=Seg_1024.zip --gpus=4
```
where  

```--outdir``` folder to save network snapshots  

```--data``` zip-archive with training dataset  

```--gpus``` number of available GPUs  

# Post-processing  

1. After the StyleGAN2ADA is trained and converged, you can generate arbitrary large number of random 2D images using the [gen_imgs.py](gen_imgs.py) and pre-trained model stored in the folder you set as ```--outdir``` in the Training. Just set the path for the pre-trained model ```model_path```, output folder ```outdir```, and number of images you would like to generate ```n_imgs``` in [gen_imgs.py](gen_imgs.py) and run it
2. The algorithm will generate images with values in some range. To use Super-Resolution algorithm, we must put them back into a single-value values for each pixel. For the Super-Resolution code, we should choose 0, 1, 2, 3, etc. For this, You can use ```Step 3``` in the [Post_segmentation_procedure](Post_segmentation_procedure.ipynb) notebook
3. Next, for the Super-Resolution algorithm, we need to stack High-Resolution images. To do it, you can store your images, provide the storage path ```folder_path``` in [Stack.py](Stack.py), and run it. After it, you have a High-Resolution training dataset




