# Background

a robust and efficient platform for imaging and reconstructing complete neuronal morphologies, including axonal arbors that span substantial portions of the brain.

reconstruct more than 1,000 projection neurons in the motor cortex, thalamus, subiculum, and hypothalamus. 

## Method
### Viral labeling
### Tissue preparation and clearing
### Microscope
### Feature-based volume stitching
`A fully imaged brain consists of $20k imaged stacks that need to be stitched to create a coherent volume. Accurate stitching is necessary to eliminate discontinuous neurites at the borders, which is critical for reliable reconstruction and automation. 

To account for non-linear defor- mations (caused by physical sectioning, optical field curvature etc.), we extended the descriptor based stitching framework:

1. blob-like objects were detected in in- dividual tiles using a difference of Gaussian filter.  These descriptors were matched between adjacent tiles in both x, y, and z directions using a coherent point drift algorithm

2.  Matched descriptors were then used to estimate a non-rigid transformation which mapped voxel locations to a target coordinate space while preserving the spatial ordering. 

### 3D visualization and reconstruction B Semi-automated segmentation
For viewing and annotating terabyte-scale image stacks, each dataset (input tiles) was resampled into a common coordinate space according to the transforms determined during the stitching procedure. This produced a set of non-overlapping image stacks (output tiles) that spanned the imaged volume.

Resampling was achieved by back-projecting each voxel in each output tile to the nearest sampled voxel.

In regions where two or more input tiles overlapped, the maximum intensity was used for the corresponding location in the output tile. 

The resampling task was implemented on a cluster (64 nodes each with 32 cores and 512 GB RAM) of Intel CPUs with Advanced Vector Instructions 2 (AVX2) and parallel access to high-bandwidth network storage. The input tiles were partitioned into contiguous sets and traversed in Morton order to facilitate merging overlaps in memory. Execution was dominated by the time required to read and write data to disk. Data were resampled to 0.25 3 0.25 3 1 mm voxels, and stored on disk along with downsampled octree representations of the same volume for visualization at different spatial scales.
### Sample registration