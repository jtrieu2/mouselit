# Deep Learning for Brain MRI Segmentation: State of the Art and Future Directions
Akkus et al. 2017
J Digit Imaging https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5537095/pdf/10278_2017_Article_9983.pdf


* Segmentation is necessary for quantitative analysis of brain MRI to detect diseases and conditions
* This article is an overview of deep learning-based approaches for segmenting quantitative brain MRI

## Background
- MRI is the most popular type of brain scan
- Quantitative analysis of brain MRI is used for characterizing disorders like Alzherimer's, epilepsy, schizophrenia, MS, cancer, and other diseases
Examples where segmentation is used:
- A common biomarker for these diseases is tissue atrophy - to quantify this, segmentation and corresponding measurements are needed
- We can segment to quantify change in brain structures at different time points
- Detection and localization of abnormal tissue is important for diagnosis and surgical and radiotherapy planning
- Quantitative characterization in space and time are often part of clinical trials

Segmentation - "labeling of pixels / voxels"
Gold standard is manual segmentation for in vivo images
- expensive, tedious, prone to human error

Traditional ML algos for segmentation require careful engineering and do not generalize welll
Challenges: normal anatomical variations, bariations in aquisition settings and MRI scanners, image aquisition imperfections, and variations in the appearance of pathology

Deep learning referes to neural nets with many layers
CNNs are the type of DL most commonly applied to image segmentation and classification

Papers in two groups: Works on normal structures and on brain lesions

Ground truth: Manual delineations of brain lesions or structures
intra-expert variabilities 20%, inter-expert variabilities 28%
Alleviate this by combining multiple expert segmentations using a fusion algorithm like STAPLE
Brain lesion ground truth can be obtained with biopsy and pathological tests

Common data sets are vailable like BRATS and ISLES


## Image Preprocessing
Challenges: Images have intensity inhomogeneity and variability in noise, contrast, and intensity ranges
Make the images appear more similar by preprocessing
1. Registration spatial alignment of images to a common anatomical space - interpatient and intrapatient
2. Skull stripping (removing skull from images)
3. Bias Field Correction - correct images contrast variations
Intensity Normalizations - Map intensities of images to a standard or reference scale
4. Noise Reduction - Reduce "locally-variant Rician noise"

## CNN Architecture Styles
Patch-Wise - extract an NxN patch around each pixel and train the model on these patches, giving class labels to identify classes as for example tumor or normal brain
Multiscale CNNs use multiple pathways, each using a patch of different size around the same pixel

### Semantic-Wise CNN Architecture
Make predictions for each pixel like semantic segmentation. An encoder extracts features and a decoder upsamples or deconvolves features from the encoder and combines lower level features from the encoder. The input image is mapped to segmentation labels.

### Cascaded CNN Architecture
Combine two CNNs - the furst CNN trains the model with initial predictions, and is input to the second CNN which further tunes the results of the first CNN.

## Segmentation of Normal Brain Strucutre
Classify WM, GM, CSF

Atlas-based approaches - match intensity between an atlas and target images
pattern recognition approaches - classify tissues based on local intensity features

CNNs avoid explicit definition of spatial and intensity ffeatures nad outperform these classical appraoches
SOTA CNNs achieve ~85% accuracy

## Segmentation of Lesions
Measurements of biomarkers: largest diameter, volume, count, progression of lesions to quantify treatment response of diseases
CNN approach has DSC values of .88, .83, .77 for different regions on Brats 2013 data
3D convolutional kernels for 3D data

In general, random forest and CNN perform best among ML methods for MRI takss

Potential of DL is limited because medical image data sets are small
Data augmentation (eg flipping or rotating training data) is helpful

There is an unavoidable number of FPs / FNs due to overlapping regions (partial volume effect) - these require additional processing to quantify accurately

Semantic architectures produce results faster than patch architectures
can do patchwise following semantic architecture to resolve issues of each approach

May help to try transfer learning (although MRIs aren't RGB like ImageNet, so probably use transfer learning from different MRI data sets)
