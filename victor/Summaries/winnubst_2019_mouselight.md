# Reconstruction of 1,000 Projection Neurons Reveals New Cell Types and Organization of Long-Range Connectivity in the Mouse Brain

https://www.sciencedirect.com/science/article/pii/S0092867419308426?via%3Dihub#mmc3

## Abstract
Neuronal cell types are the nodes of neural circuits that determine the flow of information within the brain. Neuronal morphology, especially the shape of the axonal arbor, provides an essential descriptor of cell type and reveals how individual neurons route their output across the brain. Despite the importance of morphology, few projection neurons in the mouse brain have been reconstructed in their entirety. Here we present a robust and efficient platform for imaging and reconstructing complete neuronal morphologies, including axonal arbors that span substantial portions of the brain. We used this platform to reconstruct more than 1,000 projection neurons in the motor cortex, thalamus, subiculum, and hypothalamus. Together, the reconstructed neurons comprise more than 75 meters of axonal length and are available in a searchable online database. Axonal shapes revealed previously unknown subtypes of projection neurons and suggest organizational principles of long-range connectivity.

## Introduction

## Method Details

### Animals
* wild-type C57BL/6 animals, Rorb-IRES2-Cre transgeneic, and Sim1-Cre transgenic animals
* adult females (>8 weeks) used for all experiments
* healthy, had access to *ad libitum* food and water, and housed in enriched environment

### Viral labeling
* sparse labelling
* C57/BL6 injected with adeno associated virus expressing Cre-recombinase (AAV syn-iCre) and high-titer reporter virus coding for fluorescent reporter
* Rorb-IRES2-Cre: diluted Cre-dependent FLP-recombinase and FLP-dependent reporter virus
* Sim1-Cre: systemic injection via retro-orbital sinus with Cre-dependent FLP-recombinase and FLP-dependent reporter virus

### Tissue preparation and cleaning
* transfected mice were anesthetized and transcardially perfused
* brains extracted and post-fixed in 4% paraformaldehyde
* for imaging of endogenous fluorescence, brains were delipidated (removal of lipids and lipid groups)
* selected samples were incubated in primary and secondary antibodies
* brains were embedded in 12% gelatin and fixed in 4% paraformaldehyde
* final imaging medium had refractive index of 1.468, allowing for imaging up to depths of 250 $\mu m$ in the tissue without significant loss of fluorescence

### Microscope
* samples imaged using a resonant scanner two-photon microscope
* microscope integrated with motorized stage and vibratome
* imaging performed with 40x/1.3 NA oil-immersion objective attached to piezo collar
* **image stacks (385 x 450 x 250 $\mu m^3$)** were collected with **voxel size of 0.3 x 0.3 x 1 $\mu m^3$** in two channels (red and green)
* surface of sample automatically detected using difference in autofluorescence between tissue and embedding gelatin
* each exposed brain block-face was scanned by dividing it into smaller image stacks
* overlap between adjacent stacks (25 $\mu$) allowed feature-based registration and stitching
* overlap of 75 $\mu m$ across imaged sections: each block-face was imaged to a depth of 250 $\mu m$ and the vibratome removed 175 $\mu m$ of tissue
* software to track processing of each tile https://github.com/MouseLightProject/MouseLight-Acquisition-Pipeline
  * each image stack was analyzed for possible faults in imaging (e.g. air bubble in front of lens) or sectioning (e.g. larger than expected slice thickness)

### Feature-based volume stitching
* fully imaged brain consists of ~20k imaged stacks that need to be stitched to create a coherent volume
* accurate stitching necessary to eliminate discontinuous neurites at the borders
* non-linear deformations (caused by physical sectioning, optical field curvature, etc.) were accounted for by using a stitching framework https://elifesciences.org/articles/10566.pdf

### 3D visualization and reconstruction
* for viewing and annotating terabyte-scale image stacks, input tiles were resampled into a common coordinate space according to transforms determined during stitching procedure
* produced set of non-overlapping image stacks (output tiles) that spanned the imaged volume
* resampled by back-projecting each voxel in each output tile to the nearest sampled voxel
  * in regions where two or more input tiles overlapped, maximum intensity was used for the corresponding location in the output tile
* data was resampled to 0.25 x 0.25  x 1 $\mu m$ voxels
* annotation done in Janelia Workstation https://github.com/MouseLightProject/workstation

### Semi-automated segmentation
#### Classifier to identify axonal processes
* trained binary random forest classifier to identify axonal processes using five appearance and shape features
  * Gaussian, Laplacian, gradient magnitude, difference of Gaussian, structure tensor Eigenvalues, Hessian of Gaussian Eigenvalues at multiple spatial scales ($\sigma$ = 0.3, 1, 1.6, 3.5, and 5 $\mu m$)
* training sets created by pixel-based classification in regions containing different morphological features
  * axons close to soma, termination zones, etc.)
* output of classifier consisted of a probability stack where the value of each pixel reflects the likelihood of it belonging to an axon
* morphological skeleton was created by extracting the centerline of the classifier output after thresholding (>0.5)
* for visualization efficiency, resulting line segments downsampled to approximately 20 $\mu m$ spacing between nodes


https://ars.els-cdn.com/content/image/1-s2.0-S0092867419308426-mmc3.mp4
####

### Sample registration

## Results

## Discussion
