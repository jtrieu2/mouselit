# Reconstruction of 1,000 Projection Neurons Reveals New Cell Types and Organization of Long-Range Connectivity in the Mouse Brain

https://www.sciencedirect.com/science/article/pii/S0092867419308426?via%3Dihub#mmc3

## Abstract
Neuronal cell types are the nodes of neural circuits that determine the flow of information within the brain. Neuronal morphology, especially the shape of the axonal arbor, provides an essential descriptor of cell type and reveals how individual neurons route their output across the brain. Despite the importance of morphology, few projection neurons in the mouse brain have been reconstructed in their entirety. Here we present a robust and efficient platform for imaging and reconstructing complete neuronal morphologies, including axonal arbors that span substantial portions of the brain. We used this platform to reconstruct more than 1,000 projection neurons in the motor cortex, thalamus, subiculum, and hypothalamus. Together, the reconstructed neurons comprise more than 75 meters of axonal length and are available in a searchable online database. Axonal shapes revealed previously unknown subtypes of projection neurons and suggest organizational principles of long-range connectivity.

## Glossary
* **projection neurons** - neurons whose axons extend from neuronal cell body within central nervous system (CNS) to one or more distant regions of CNS
* **morphology** - the study of the forms of things, especially the relationships between structure in living things
* **morphological skeleton** - In digital image processing, morphological skeleton is a skeleton (or medial axis) representation of a shape or binary image, computed by means of morphological operators

## Introduction
* mammalian neurons possess extensive axonal arbors that project over long distances
* projections dictate how information flows across brain areas
* current methods label populations of neurons, obscuring fine-scale spatial organization
* morphological reconstruction of individual neurons are important for delineating cell types and understanding routing of information flow
* tracing of axons in entirety is laborious and time consuming
* microscopy-based neuronal reconstructions remain "gold standard" for analysis of connectivity
* authors developed semi-automated, high throughput reconstruction pipeline
* **reconstructed more than 1,000 neurons in neocortex, hippocampus, thalamus, and hypothalamus**
* uncovered new cell types and found novel organizational principles governing the connections between brain regions

## Method Details

### Animals
* wild-type C57BL/6 animals, Rorb-IRES2-Cre transgeneic, and Sim1-Cre transgenic animals
* adult females (>8 weeks) used for all experiments
* healthy, had access to *ad libitum* food and water, and housed in enriched environment
* imaged 25 brains and reconstructed neurons in each
* reconstructed a total of 1,093 neurons

### Viral labeling
* C57/BL6 injected with adeno associated virus expressing Cre-recombinase (AAV syn-iCre) and high-titer reporter virus coding for fluorescent reporter
* Rorb-IRES2-Cre: diluted Cre-dependent FLP-recombinase and FLP-dependent reporter virus
* Sim1-Cre: systemic injection via retro-orbital sinus with Cre-dependent FLP-recombinase and FLP-dependent reporter virus
* injected up to 5 separate areas of brain to label larger number of cells while retaining sparse labeling in any one brain region

### Tissue preparation and cleaning
* transfected mice were anesthetized and transcardially perfused
* brains extracted and post-fixed in 4% paraformaldehyde
* for imaging of endogenous fluorescence, brains were delipidated (removal of lipids and lipid groups)
* selected samples were incubated in primary and secondary antibodies
* brains were embedded in 12% gelatin and fixed in 4% paraformaldehyde
* final imaging medium had refractive index of 1.468, allowing for imaging up to depths of 250 um in the tissue without significant loss of fluorescence

### Microscope
* samples imaged using a resonant scanner two-photon microscope
* microscope integrated with motorized stage and vibratome
* imaging performed with 40x/1.3 NA oil-immersion objective attached to piezo collar
* **image stacks (385 x 450 x 250 um^3)** were collected with **voxel size of 0.3 x 0.3 x 1 um^3** in two channels (red and green)
* surface of sample automatically detected using difference in autofluorescence between tissue and embedding gelatin
* each exposed brain block-face was scanned by dividing it into smaller image stacks
* overlap between adjacent stacks (25 um) allowed feature-based registration and stitching
* overlap of 75 um across imaged sections: each block-face was imaged to a depth of 250 um and the vibratome removed 175 um of tissue
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
* data was resampled to 0.25 x 0.25  x 1 um voxels
* annotation done in Janelia Workstation https://github.com/MouseLightProject/workstation

### Semi-automated segmentation
* done with Janelia Workstation https://ars.els-cdn.com/content/image/1-s2.0-S0092867419308426-mmc3.mp4
#### Classifier to identify axonal processes and neurite segments
* trained binary random forest classifier to identify axonal processes using five appearance and shape features
  * Gaussian, Laplacian, gradient magnitude, difference of Gaussian, structure tensor Eigenvalues, Hessian of Gaussian Eigenvalues at multiple spatial scales (\sigma = 0.3, 1, 1.6, 3.5, and 5 um)
* training sets created by pixel-based classification in regions containing different morphological features
  * axons close to soma, termination zones, etc.)
* output of classifier consisted of a probability stack where the value of each pixel reflects the likelihood of it belonging to an axon
* morphological skeleton was created by extracting the centerline of the classifier output after thresholding (>0.5)
* for visualization efficiency, resulting line segments downsampled to approximately 20 um spacing between nodes
* all segmented neurites were split into linear segments by separating them at their axonal branch points
  * length before split: 263.4 +/- 625.6 um
  * length after split: 96.5 +/- 155.4 um
* filtering steps applied on resulting segmentation to remove incorrectly identified axonal processes
  * path-length based pruning strategy that removed branches <15 um

#### Human annotation
* human annotators started from soma and reconstructed neurons by linking neurite segments
* annotators also filled in parts of neuron missed by segmentation
* location of branch points and axonal endpoints were annotated to ensure that entire axonal tree were reconstructed
* axons of neurons with insufficient expression that were too dim were abandoned because they were indistinguishable from background fluorescence
  * median 19% of cells in samples with more than 50 cells
  * experienced annotators could identify these neurons after ~30 min. of tracing
* two annotators independently reconstructed each neuron and compared work to generate a consensus reconstruction
* **axons distinguished from dendrites by their thickness, branching patterns, lack of dendritic spines, and overall length**

### Sample registration
* imaged brains were aligned to the Allen Mouse Common Coordinate Framework (CCF)
* parts of brain not present in Allen atlas (e.g. anterior olfactory bulb) and imaged gelatin were cropped out of sample volume
* 3D slicer software platform used to take a downsampled version of entire sample volume (~5x 5 x 15 um voxel) and registering it to averaged Allen anatomical template (10 x 10 x 10 um)
* initial automated intensity-based affine registration performed to align the sample to Allen atlas
* iterative landmark-registration process then used to achieve more precise registration
* all registration steps combined to generate a single displacement vector field used to align reconstructed neurons to the CCF
* observed registration error was typically below 100 um


## Results

### Dorsal Subiculum Contains at Least Four Projection Types
* dorsal subiculum is a major output structure of hippocampus studied for role in memory, navigation, and motivated behavior
* neurons in dosral subiculum fall under 4 projection groups
* because neurons in dosral subiculum project to ~6 areas in various combinations, previous studies using retrograde tracers in pairwise combinations failed to elucidate complex projection patterns

### Motor Cortex: A Diverse Collection of Projection Types

### Parallel Projections from Motor Cortex to the Thalamus

### VAL Thalamus Contains Fine-Scale Projection Maps

## Discussion
* > 1,000 reconstructed neurons available on online database (mouselight.janelia.org)
* reconstruction of axonal arbors is valuable toward generating cellular circuit diagrams and classifying neurons on the basis of morphology
* while pipeline does not detect synapses, axonal arborizations contain an approximately constant density of synapses, and axonal length is therefore a convenient surrogate for interareal connectivity
* authors' histological treatments and imaging result in series of preserved brain slices, allowing for post hoc gene expression analysis by *in situ* hybridization techniques and other types of molecular characterization
* complete  characterization of cell types of mouse brain will require reconstructions of 100,000 neurons or more over hundreds of brains using diverse labeling techniques
* speed of reconstructions is still limiting
  * all decision points (i.e. linking of automatically segmented neurites to a tree) are done manually which is the limiting step
  * mouselight dataset of "gold-standard reconstructions will serve as training data for machine-learning algorithms" to increase reconstruction speed by 10 - 100 fold


## Questions
1. Table S2 in Supplemental Information shows that they imaged 25 brains and reconstructed 7 - 176 neurons in each. Total reconstructed neurons is 1,093. Did they combine the neurons into one 3D volume? If so how did they do this and make sure that each neuron is unique or did not overlap?
2. What does the following under Semi-automated segmentation of STAR Methods mean? "The coverage of axonal processes by these generated segments was determined using fine-scale reconstructions (internode interval < 5 um) of all axonal projections in the caudoputamen of one sample and manually assigning fragments to each neuron (without merging)"
3. What's the difference between "axonal process" and "axonal projection"?
