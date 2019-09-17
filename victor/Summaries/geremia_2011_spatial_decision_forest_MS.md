# Spatial decision forests for MS lesion segmentation in multi-channel magnetic resonance images
https://www.sciencedirect.com/science/article/abs/pii/S1053811911003740
## Introduction
* Multiple Sclerosis (MS) is a chronic disease that affects white matter (WM) of central nervous system
* automatic segmentation (locating) of lesions can help diagnosis and patient follow up

### past automatic segmentation methods
* intensity based k-nearest neighbors with spatial prior and a fuzzy inference system
* unsupervised learning based on hidden markov chains that estimates proportion of white matter (WM), gray matter (GM), and cerebro-spinal fluid (CSF) in each voxel
* Expectation maximization (EM) combined with Mahalanobis thresholding to highlight lesions

## MICCAI Grand Challenge 2008 dataset
* abbreviated to *MSGC*
* MSGC aims to evaluate and compare algorithms for task of MS lesion segmentation by providing two datasets
* both datasets have 3 Magnetic Resonance (MR) volumes:
  * T1-weighted image
  * T2-weighted image
  * FLAIR image
* MR volumes were co-registered and sampled to fit isotropic 0.5 x 0.5 x 0.5 mm^3 resolution

### Public dataset
* 20 cases, 10 from Children's Hospital in Boston (CHB) and 10 from University of North Carolina (UNC), are labeled by a CHB expert rater
* labels are publicly available; intended as training set

### Private dataset
* 25 cases, 15 from CHB and 10 from UNC
* labeled by a single expert rater at CHB and jointly by 2 expert raters at UNC
* labels are not available to public; intended as testing set

### Evaluation
* quantitative evaluation carried out on private dataset using a set of known metrics
  * TNR, TPR, FPR, PPV, volume overlap (VO), relative absolute volume difference (VD), and surface distance (SD)

### Four Top-Ranked methods
* Best method in 2008: Souplet et al.(2008)
  * global threshold on FLAIR MR sequence, inferred using EM brain tissue classification, suffices to  detect most MS lesions
  * final segmentation is constrained to appear in white matter via morphological operations
* Anbeek et al. (2008)
  * k-nearest neighbors provides voxel-wise probabilistic classification
* Bricq et a.(2008a)
  * unsupervised segmentation with hidden Markov chain model
  * uses neighborhood information, MR sequences, and probabilistic priors
* Shiee et al.(2008) and Shiee et al.(2010)
  * performs brain tissue classification and MS lesion segmentation by combining statistical and topological atlases

## Data preprocessing
* sub-sample and crop images so each has same size (159x207x79 voxels), and same resolution (1x1x2 mm^3) in order to reduce time spent learning the classifier
* correct for RF acquisition field inhomogeneities
  * *TO-DO* read (Prima et al., 2001) to find out more
* perform inter-subject intensity calibration
  * *TO-DO* read (Rey, 2002)
* Spatial normalization
  * *TO-DO* read (Prima et al., 2002)
* Spatial prior is added by registering MNI atlas to the MSGC images
  * each voxel of atlas provides probability of belonging to WM, GM, and CSF
  * Image Fusion module of MedINRIA is used to affine register MNI atlas


## Proposed method: Context-rich decision forest
* random forest with spatial, multi-channel features, and symmetry features
* assumption that healthy brain is approximately symmetric with respect to mid-sagittal plane and that MS lesions develop asymmetrically
* training data consists of set of labeled voxels
  * label = {0,1}; 1 for lesion and 0 for background

### Features

1. local
* intensity of voxel or probability from prior channel (registered MNI atlas)

2. neighborhood
* local voxel value in channel C_1 compared to mean value in channel C_2 over two 3D boxes R_1 and R_2
* C_1 and C_2 are both intensity or prior channels
* regions R_1 and R_2 are randomly sampled in large neighborhood of local voxel

3. symmetry Features
* compares local voxel of interest with its symmetric counterpart with respect to mid-sagittal plane

## Experiment and results
### Results on public MSGC dataset
* 3 fold cross-validation (RF trained on 2/3 of cases and tested on 1/3)
* Forest parameters
  * number of random regions 950
  * number of trees T = 30
  * tree depth D = 20
  * lower bound for information gain = 10^-5
  * posterior threshold = 0.5
* Context-rich RF TPR is 39.98 +/- 18.40 compared to Souplet et al. (2008)'s TPR of 19.21 +/- 13.68

### Results on private MSGC dataset
* MSCG website carried out a complementary and independent evaluation of context-rich random forest
* slightly larger TPR and comparable FPR but lower volume difference (VD) and surface distance (SD)
* significant improvement over Souplet et al.(2008) on SD (p = 4.2 x 10^-6) for the CHB rater and on SD (p=6.1x10^-3) for the UNC rater

## Discussion
* MSGC website gathers results of methods submitted
* score of 90 is equal to accuracy of a human rater
* context-rich random forest scores 82.0755
* some MS lesions are missed by experts, e.g. in the corpus callosum
  * this limits a supervised learning approach
* random forest is able to detect suspicious regions with high certainty
  * suspicious regions are visually similar to MS lesions and widely present in training data, but not labeled by the expert
* MICCAI does not show any MS lesion in gray matter, even though recent histopathological studies have shown that MS affects gray matter
