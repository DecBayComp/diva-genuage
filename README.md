<div align="justify">

# DIVA & GENUAGE : VR POINT TRAJECTORY

Quick presentation  ?TODO?

<img align="left" src="https://user-images.githubusercontent.com/49953723/211052369-473243ed-088c-45d6-a74d-57218fe67cb1.png" width="120px"/>

 **DIVA** (Data Integration and Visualisation in Augmented and virtual environments) software is a user-friendly platform that generates volumetric reconstructions from raw 3D image stacks and enables efficient visualization and quantification in virtual reality (VR) without pre-treatment. <br/>

**Genuage** is a plateform for visualizing and analyzing multidimensional point cloud data such those generated from Single Molecule Localization Microscopy (SMLM). SMLM refers to methods for generating super-resolution microscopy images (PALM, STORM, DNA-PAINT …) and Single particle tracking (SPT) data. Genuage is compatible with multidimensional localization data.

EXPLAIN AVANTAGE COMBINAISON DES 2


# Table of Contents
- [Requirements](#requirements-and-installation)
- [Import image](#import-image)
  * [Data requirements](#data-requirements)
  * [Load your image](#load-your-image)
  * [Improve the visualisation](#improve-the-visualisation)
- [Import trajectories](#import-trajectories)
  * [Data requirements](#data-requirements)
  * [Load your trajectories](#load-your-trajectories)
  * [Trajectories options](#trajectories-options)
- [Virtual Reality](#virtual-reality)
  * [Select trajectories](#select-trajectories)
- [Example](#example)


# Requirements and Installation
DIVA is designed to run on the Windows 10 and 11 operating systems with at least OpenCL 2.0. We recommend using DIVA with an Intel i5 processor equivalent or better, at least 4GB RAM of memory, 300 MB of storage and a NVIDIA GeForce 900 Series or better Graphical Processing Unit (GPU). DIVA can be used with and without VR headset and is compatible with HTC Vive, HTC Vive Pro, Oculus Rift, Oculus Rift S, Oculus Quest (with Link Cable) and Windows Mixed Reality headsets. For each type of VR headsets you have to download the corresponding installation software (such as [ViveSetup](https://www.vive.com/fr/setup/pc-vr/) or [Oculus](https://www.oculus.com/setup/?locale=fr_FR)). In addition, [SteamVR](https://www.steamvr.com/fr/) is required to use VR functions. You can find DIVA user manual and all the information about the legacy software [here](https://diva.pasteur.fr/). 

To install this new version of DIVA, load the ?TODO? folder and execute DIVA by double-clicking on the provided *diva.exe* file. DIVA will take a moment to load as it allocates memory (roughly 20–30 seconds).
 
# Import image

?TODO? ADD VIDEO COMPLETE PIPELINE 

## Data requirements
To load a 4D image, DIVA requires Tagged Image File Format (TIFF) image files in 8 or 16-bits. We recommend limiting the size of loaded files to less than 1 GB. Larger files may be scaled or cropped via [ImageJ/Fiji](https://imagej.net/software/fiji/downloads) for example. Multichannel files organized using the ImageJ/Fiji convention are supported. To improve DIVA performances, use images that are located on your disk.

?TODO? Manip pour mettre les datas entre 0 et 255 

## Load your image
Importation can be done in DIVA using the <img src="https://user-images.githubusercontent.com/49953723/211051703-d4e8065b-2d44-40a0-b7cf-70ec3de687f4.png" width="20px"/> button with the *TIFF* option (in the top-left corner) which opens a file browser or by drag-and-dropping your TIFF file direclty. 

If the image is a 4D image (i.e. with temporal information), this <img src="https://user-images.githubusercontent.com/49953723/211319952-7a64f9ac-4693-40b3-b8d3-bafe9faf6eb3.png" width="20px"/> icon  will appear in the **Volume** panel to allow you to explore the different frames forwards <img src="https://user-images.githubusercontent.com/49953723/211320199-80d2be99-07aa-4fc4-8fda-a7df3d3ce677.png" width="20px"/> or backwards <img src="https://user-images.githubusercontent.com/49953723/211320192-f79a4f59-2ce4-48d3-9601-05a123a978ea.png" width="20px"/>.

 <img align="left" src="https://user-images.githubusercontent.com/49953723/211052080-a576c3a7-7718-4ded-b719-7586d79068d3.png" width="80px"/> 
Remark : if you see this type of behavior after loading your image in DIVA, press R in your keyboard to reload the image and correct the rendering artefact.


## Improve the visualization
Voxel color and opacity can be modified in real-time through a user-friendly transfer function interface located in the **Volume** panel under <img src="https://user-images.githubusercontent.com/49953723/211052882-578af9f6-4ba9-47ee-90fb-ecb68dd2d0c3.png" width="20px"/> or <img src="https://user-images.githubusercontent.com/49953723/211052912-4d1e5c92-6694-4207-ba1b-d1f15a6c249e.png" width="20px"/> icon if the image has to channels. 

 <img align="left" src="/materials/videos/TF1D_lung_01_MSD.gif" width="480" height="270"/>
 
https://user-images.githubusercontent.com/49953723/211350518-a62a306f-fd42-4822-80bf-6ddefef23881.mp4

As shown on the video above with a CT-scan of lung tumor from the [Medical Segmentation Decathlon Challenge database](https://drive.google.com/drive/folders/1HqEgzS8BV2c7xYNrZdEAnrHk7osJJ--2), this interface is composed of the image histogram in gray, one white curve for the opacity and one color bar. Each of them are defined with control points which can be adjusted by dragging with the left mouse button (more details on the [DIVA user manual](https://diva.pasteur.fr/wp-content/uploads/2019/09/diva-viewer-manual.pdf)). The basic principle of the transfer function is that each pixel of the histogram under the curve will be displayed with the corresponding color in the color bar, and each pixel above the curve will be disabled in the 3D and VR view. 
 
For multichannel files, each channel possesses its own transfer function which can be activated by left clicking on the corresponding channel icon in the **Volume** panel. For 4D images, the transfer function will be applied to all frames. We recommend you to customize this transfer function to highlight your object of interest and save it as .json file using the <img alt="save_button" src="https://user-images.githubusercontent.com/49953723/211335017-aa3917ef-725d-43aa-ad49-9db8490adf69.png" width="60px"/> button in order to be able to re-open if necessary with the <img alt="open_button" src="https://user-images.githubusercontent.com/49953723/211335290-b61fce90-217e-4c95-941c-785f93ea8040.png" width="60px"/> button .


# Import trajectories

## Data requirements
DIVA requires a trajectory file in a .csv format with five colums: ```trajectory id```, ```frame index```, ```x```, ```y```, ```z``` where each variable is separated by a virgule. Point coordinates have to be in the image coordinates system (no need to between 0-1).


## Load your trajectories

?TODO? 

- requirements des fichiers 
- how to load 

## Trajectories options

- define each buttons (with screenshots)


# Virtual Reality

TODO : 

point highligh vert quand passe dessus
option crop 
option changer de frame ? 



## Select trajectories
comment activer l'option 
ou sont affichés les data
comment export


# Example


