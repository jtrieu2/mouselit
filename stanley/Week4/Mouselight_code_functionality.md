# From src/image_getters.py

## Feature-based volume stitching
-Extended the descriptor based stitching framework:

1. blob-like objects were detected in individual tiles using a difference of Gaussian filter.  These descriptors were matched between adjacent tiles in both x, y, and z directions using a coherent point drift algorithm

2.  Matched descriptors were then used to estimate a non-rigid transformation which mapped voxel locations to a target coordinate space while preserving the spatial ordering. 


## 3D visualization and reconstruction B Semi-automated segmentation
For viewing and annotating terabyte-scale image stacks, each dataset (input tiles) was resampled into a common coordinate space according to the transforms determined during the stitching procedure. This produced a set of non-overlapping image stacks (output tiles) that spanned the imaged volume.

Resampling was achieved by back-projecting each voxel in each output tile to the nearest sampled voxel.

In regions where two or more input tiles overlapped, the maximum intensity was used for the corresponding location in the output tile. 

Data were resampled to 0.25x0.25x3x1 um voxels, and stored on disk along with downsampled octree representations of the same volume for visualization at different spatial scales.