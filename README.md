<div align="justify">

# DIVA & GENUAGE : VR for image and point cloud trajectories
Localizing molecules in large images can generate a huge amount of data to process. The exploration of these point clouds and trajectories to detect localization errors can therefore be very time consuming. This is why we decided to combine two platforms, **DIVA** and **Genuage** to visualize in virtual reality raw image overlayed with the trajectory data and thus allow a quick and easy exploration to check the validity of multidimensional point cloud data.

 <img align="left" src="https://user-images.githubusercontent.com/49953723/211052369-473243ed-088c-45d6-a74d-57218fe67cb1.png" width="180px"/>

 **DIVA** (Data Integration and Visualisation in Augmented and virtual environments) software is a user-friendly platform that generates volumetric reconstructions from raw 3D image stacks and enables efficient visualization and quantification in virtual reality (VR) without pre-treatment. For more details see the article [El Beheiry M., Godard C., Caporal C. et al. DIVA: natural navigation inside 3D images using virtual reality. *Journal of Molecular Biology*. (2020)](https://www.biorxiv.org/content/biorxiv/early/2020/04/10/2020.04.09.019935.full.pdf). <br/>
 
**Genuage** is a plateform for visualizing and analyzing multidimensional point cloud data such those generated from Single Molecule Localization Microscopy (SMLM). SMLM refers to methods for generating super-resolution microscopy images (PALM, STORM, DNA-PAINT …) and Single Particle Tracking (SPT) data. Genuage is compatible with multidimensional localization data. For more details see the article [Blanc T., El Beheiry M., Caporal C. et al. Genuage: visualize and analyze multidimensional single-molecule point cloud data in virtual reality. *Nature Methods* 17, 1100–1102. (2020)](https://www.nature.com/articles/s41592-020-0946-1).
 

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
  * [Explore the data](#explore-the-data)
  * [Select trajectories](#select-trajectories)
  * [Export selected trajectories](#export-selected-trajectories)


# Requirements and Installation
DIVA is designed to run on the Windows 10 and 11 operating systems with at least OpenCL 2.0. We recommend using DIVA with an Intel i5 processor equivalent or better, at least 4GB RAM of memory, 300 MB of storage and a NVIDIA GeForce 900 Series or better Graphical Processing Unit (GPU). DIVA can be used with and without VR headset and is compatible with HTC Vive, HTC Vive Pro, Oculus Rift, Oculus Rift S, Oculus Quest (with Link Cable) and Windows Mixed Reality headsets. For each type of VR headsets you have to download the corresponding installation software (such as [ViveSetup](https://www.vive.com/fr/setup/pc-vr/) or [Oculus](https://www.oculus.com/setup/?locale=fr_FR)). In addition, [SteamVR](https://www.steamvr.com/fr/) is required to use VR functions. You can find DIVA user manual and all the information about the legacy software [here](https://diva.pasteur.fr/). 

To install this new version of DIVA, load the [diva folder](/diva) and execute DIVA by double-clicking on the provided *diva.exe* file. DIVA will take a moment to load as it allocates memory (roughly 20–30 seconds).
 
 
# Import image
## Data requirements
To load a 4D image, DIVA requires Tagged Image File Format (TIFF) image files in 8 or 16-bits. We recommend limiting the size of loaded files to less than 1 GB. Larger files may be scaled or cropped via [ImageJ/Fiji](https://imagej.net/software/fiji/downloads) for example. Multichannel files organized using the ImageJ/Fiji convention are supported. To improve DIVA performances, use images that are located on your disk.

?TODO? Manip pour mettre les datas entre 0 et 255 

## Load your image
Importation can be done in DIVA using the <img src="https://user-images.githubusercontent.com/49953723/211051703-d4e8065b-2d44-40a0-b7cf-70ec3de687f4.png" width="20px"/> button with the *TIFF* option (in the top-left corner) which opens a file browser or by drag-and-dropping your TIFF file direclty. 

If the image is a 4D image (i.e. with temporal information), this <img src="https://user-images.githubusercontent.com/49953723/211319952-7a64f9ac-4693-40b3-b8d3-bafe9faf6eb3.png" width="20px"/> icon  will appear in the ```Information``` panel to allow you to explore the different frames forwards <img src="https://user-images.githubusercontent.com/49953723/211320199-80d2be99-07aa-4fc4-8fda-a7df3d3ce677.png" width="20px"/> or backwards <img src="https://user-images.githubusercontent.com/49953723/211320192-f79a4f59-2ce4-48d3-9601-05a123a978ea.png" width="20px"/>.
 
<img align="left" src="https://user-images.githubusercontent.com/49953723/211052080-a576c3a7-7718-4ded-b719-7586d79068d3.png" width="80px"/> 
 
> *Remark*: if you see this type of behavior after loading your image in DIVA, press R in your keyboard to reload the image and correct the rendering artefact.

## Improve the visualisation
Voxel color and opacity can be modified in real-time through a user-friendly transfer function interface located in the ```Volume``` panel under <img src="https://user-images.githubusercontent.com/49953723/211052882-578af9f6-4ba9-47ee-90fb-ecb68dd2d0c3.png" width="20px"/> or <img src="https://user-images.githubusercontent.com/49953723/211052912-4d1e5c92-6694-4207-ba1b-d1f15a6c249e.png" width="20px"/> icon if the image has two channels. 

https://user-images.githubusercontent.com/49953723/211350518-a62a306f-fd42-4822-80bf-6ddefef23881.mp4

As shown on the video above with a CT-scan of lung tumor from the [Medical Segmentation Decathlon Challenge database](https://drive.google.com/drive/folders/1HqEgzS8BV2c7xYNrZdEAnrHk7osJJ--2), this interface is composed of the image histogram in gray, one white curve for the opacity and one color bar. Each of them are defined with control points which can be adjusted by dragging with the left mouse button (more details on the [DIVA user manual](https://diva.pasteur.fr/wp-content/uploads/2019/09/diva-viewer-manual.pdf)). The basic principle of the transfer function is that each pixel of the histogram under the curve will be displayed with the corresponding color in the color bar, and each pixel above the curve will be disabled in the 3D and VR view. 
 
For multichannel files, each channel possesses its own transfer function which can be activated by left clicking on the corresponding channel icon in the ```Volume``` panel. For 4D images, the transfer function will be applied to all frames. We recommend you to customize this transfer function to highlight your object of interest and save it as .json file using the <img alt="save_button" src="https://user-images.githubusercontent.com/49953723/211335017-aa3917ef-725d-43aa-ad49-9db8490adf69.png" width="60px"/> button in order to be able to re-open if necessary with the <img alt="open_button" src="https://user-images.githubusercontent.com/49953723/211335290-b61fce90-217e-4c95-941c-785f93ea8040.png" width="60px"/> button.


# Import trajectories
## Data requirements
DIVA requires a trajectory file in a .csv format with five colums: ```trajectory id```, ```frame index```, ```x```, ```y```, ```z``` where each variable is separated by a comma. Point coordinates have to be in the image coordinates system (no need to normalize between 0 and 1). 

## Load your trajectories
To activate the point cloud trajectories interface go to the ```Advanced``` panel and click on the <img alt="volume_sphere_icon" src="https://user-images.githubusercontent.com/49953723/211362394-697d6ef6-25eb-4b37-aa53-b43e4917a887.png" width="20px"/> icon. Trajectories data can be loaded with the <img alt="load_trajectories_button" src="https://user-images.githubusercontent.com/49953723/211362160-a96a8dd2-03df-45f2-8494-817545dfa14b.png" width="170px"/> button.
    
 ## Trajectories options
 <img align="right" src="/materials/videos/demo_trajectories_desktop_interface.gif" width="520" height="240"/> 
After loading, each point in the file will be added to the volume and rendered as Gaussian spheres as well as the trajectories which will be rendered as lines connecting the points. 

The desktop interface for point cloud trajectories is composed of:
 - ```timestep```: two sliders to control the interval of frames (of point clouds and trajectories) to display.
 - ```point size```: one slider to control the size of gaussian spheres that represent each point.
 - ```selected trajectories```: the list of the trajectories selected in VR.
 
> *Rendering information:*
> 
> Points are rendered with the following plasma texture <img src="https://user-images.githubusercontent.com/49953723/211572478-fa85b902-e5d0-46c5-b5e8-1113b85df7a0.png" width="80px"/> according to their positions in the frame. For example a point in the frame 1/50 will be dark purple while a point in the frame 50/50 will be yellow.
> 
> Trajectories are rendered with the following texture <img src="https://user-images.githubusercontent.com/49953723/211572514-ece8b422-1427-4b76-ab33-3bb58e3766bf.png" width="80px"/> according to their ids. For example a trajectory with a low id will be displayed in dark puple while a trajectory with a high id will be displayed in pink. This texture was chosen to facilitate the differentiation of trajectories when the number of trajectories is important. 
> 
> /!\ Only one frame of the raw image is displayed at a time while the points of the trajectories of several frames are displayed at the same time. Points of the actual frame of the raw image are displayed in green.

 
# Virtual Reality
Switching to and from the VR mode is performed by clicking on <img src="https://user-images.githubusercontent.com/49953723/211378148-6eca762b-8e7f-4b31-8dcf-b114bb0ea25c.png" width="20px"/> in the top-left corner and then <img src="https://user-images.githubusercontent.com/49953723/211378358-7eb9f04b-9489-464b-9ce3-7dd08a826290.png" width="20px"/> or <img src="https://user-images.githubusercontent.com/49953723/211378719-2374eafb-7881-4047-906e-85631c2d1bd4.png" width="20px"/>. This will automatically launch SteamVR to activate the plugged VR headset. 

> /!\ The button will not respond if SteamVR is not installed. To avoid possible crash, launch SteamVR before launching DIVA.

https://user-images.githubusercontent.com/49953723/211558891-5d6f1e67-8a8f-4af7-bb9a-69b46f88bb18.mp4

Interaction with the volume and trajectories can be done with the VR controller.

## Explore the data
Open the VR menu by clicking on the <img src="https://user-images.githubusercontent.com/49953723/211567755-e1a703d4-bded-41e8-8991-8be9ca9b4018.png" width="20px"/> button of the VR controller, then click on the <img src="https://user-images.githubusercontent.com/49953723/211560765-d95b2def-f034-4b2a-ab24-f7aa9bf10d7e.png" width="20px"/> icon and <img src="https://user-images.githubusercontent.com/49953723/211561191-8dd5315f-ab5d-41f0-bea5-b1e3651c8d70.png" width="20px"/> icon. This will add icons on the controller, as in the desktop interface you can explore the different frames forwards <img src="https://user-images.githubusercontent.com/49953723/211320199-80d2be99-07aa-4fc4-8fda-a7df3d3ce677.png" width="20px"/> or backwards <img src="https://user-images.githubusercontent.com/49953723/211320192-f79a4f59-2ce4-48d3-9601-05a123a978ea.png" width="20px"/>. 

> /!\ Changing the frame index too often in VR can cause the software to crash due to a memory allocation problem.

## Select trajectories
Open the VR menu by clicking on the <img src="https://user-images.githubusercontent.com/49953723/211567755-e1a703d4-bded-41e8-8991-8be9ca9b4018.png" width="20px"/> button of the VR controller, then click on the <img src="https://user-images.githubusercontent.com/49953723/211562450-4aad4e08-7f16-4296-9bf3-a3f1dbda44bd.png" width="20px"/> icon and <img src="https://user-images.githubusercontent.com/49953723/211562470-2ee6dde3-0cbf-4bab-aa82-96b226812c91.png" width="20px"/> icon. 

- To select a trajectory, go with the VR controller to the position of a point of the trajectory and click on the <img src="https://user-images.githubusercontent.com/49953723/211562957-e70b53c8-d312-4a9d-b4e5-0bf6cc12a2bd.png" width="20px"/> icon on the controller. 
- To remove a trajectory from the list of selected trajectories, go with the VR controller to the position of a point of the trajectory an click on the <img src="https://user-images.githubusercontent.com/49953723/211562979-fc2154d8-221b-4f11-bb45-ce31c771bf39.png" width="20px"/> icon on the controller. 

Ids of selected trajectories are displayed under the panel ```Selected Trajectories``` on the desktop interface.

 > *Remark*: A point in the cloud is highlited in green when the controller passes over it. 

## Export selected trajectories
Exportation of the selected trajectories can be done on the desktop interface by clicking the <img src="https://user-images.githubusercontent.com/49953723/211569177-e09271e8-0930-4489-99e1-ea765edc5633.png" width="170px"/> button. Data is exported as a .csv file with the same format than the input file and contains the list of points of the selected trajectories.
