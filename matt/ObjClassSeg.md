# Read Object Class Segmentation using Random Forests 
## (Schroff et al., Proceedings of the British Machine Vision Conference, 2008)

## Abstract
Random Forest for class-based, pixel-wise image segmentation.
Contributions of paper:
1. Nearest neighbors and texton class histograms can be mapped onto a RF architecture.
2. Performence of classifiers can be improved by incoroporating spatial context and discriminative learning from RF framework.
3. RFs combine multiple features, leading to a further increase in performance when textons, color, filterbanks, and HOG are used together.

## Introduction
Benefits of RF:
1. Computational efficiency in training and classification
2. Probabilistic output
3. Seamless handling of a variety of visual features.
4. Inherent feature sharing of a multi-class classifier

### Datasets
9-class and 21-class MSRC dataset (natural images andcorresponding ground truth object class maps)
Also VOC2007

## Random Forests
For a pixel in position p, node function $t_p = sum_{ r \in P} w_r \dot f_r$
* r indices 1 or 2 rectangles described in p
* w_r describes filter selecting pixels in the rectangle and a weighting for each dimension of the feature vector f_r

2 node functions used:
abtest - consists of the accumulated response in one feature channel in a single rectangle P = {1}
difftest - two rectangles P = {1,2}

During training each node has a random subset of P available
Choose node function yielding maximum information gain

## Fusing global and local cues into RFs

### Global class modeling via SHCM

texton representation - use single-histogram class models
each class SHCM is the average of texton distirbutions across all training example images
in their paper - textons are computed on dense 5×5 color patches using k-means
clustering, resulting in a 8000 texton dictionary

The SHCMs segment an image into classes by a sliding window classifier

###  Casting SHCM classification as a node function

NN class histogram is found by hierarchical tests comparing test window histogram toa pair of SHCMs - select the more likely one
Combine two SHCMs into a weight, now define a node function comparing KL-divergence of a single test histogram to two class models

w is weighted by globally induced weights for each feature channel

## From SHCM to local features

Experiments with progressively more freedom in featyre selection:
Fixed-tree - learn posterior from data
Learn tree - select basic test
Flexible rectangles - explore various aspects of rectangele position

### Evaluation
RF size 10, max depth 15 (except fixed-tree)
Evaluated on 9-class MSRC

fixed-tree 75.2%
learn tree 76.2% (fixed rectangles)
flexible rectangles 82.0%
- rectangles tend to be small towards bottom of tree

## More visual cues
Combine all features in decision trees

RGB features - node functions are simple differences of rectangles computed over 1 of 3 color channels
HOG features - compute HOG for whole image using various cell sizes, block sizes, and number of gradient bins
F17 filterbank is also used, in same manner as RGB

### Combining features
Each feature is treated as a separate pool and feature maximizing information gain selected for each node
Combining RGB and HOG hugely boosts performance

## CRF - Conditional Random Field
After learning class posteriors, a CRF stage is applied to the pixel grid, where the state space of each pixel is the number of classes (9 in 9-class MSRC)

## Future work
Incorporating image level class priors
Move from direct pixel classification to intermediate object detection before pixel classification