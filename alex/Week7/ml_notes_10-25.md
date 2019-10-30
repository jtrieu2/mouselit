# Mouselight notes 10/25

## Voxel Retreival
### Spatial to Voxel
	* Voxel location error consistently off by 1,-1 with no real consistency, otherwise works well.

## Convolutional Experiments
	* Fastest time for loading whole subvolume into np array with convolution windows is size of tif dimension:
	518x408x208
## Image Preprocessing
	* Simple techniques (filters, gradients) work on 2d images
	* Later will get to more complex algorithms(neural nets, etc.)
## 3 Mo. Milestones
* Workstation software, where to host data/how to compute
* Image Processing:
	* Data Retrieval: Coordinate orientation and origin - Done
	* Retrieve 3d rectangle around coordinate - Done

	* Estimate scale of dataset
	* Quantitative quality control

* (Misc) Intel Python - possible performance increase for running through an entire subvolume
