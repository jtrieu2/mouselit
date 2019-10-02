# Manifold Forests: Closing the Gap on Neural Networks
## Ronan Perry et al. arXiv 2019.

## Summary

DFs, but choose distributions in a "manifold aware fashion": 
e.g. seelect continuous patches within images rather than random pixels
Outperforms other DFs in image, time-series, and torus data due to capturing space structure
Training and test faster than deep nets

## Introduction

* RFs and other methods view observations as unstructured feature vactors - this neglects indices which may encode addtl. information
* Past research extended RFs to computer vision and augmented RFs w/ structured pixel label info. These methods generate features a priori from individual pixels (do not take advantage of local topology) or lack the flexibility to *learn* "relevant patches."
* Existing manifold forest algorithms are unsupervised and aim to learn a low dimensional representation of data
* "At each node in the decision tree, sets of random spatially contiguous features are randomly selected using knowledge of the underlying manifold"
* Intensities of sampled featured are summed ot get a set of projections that can be evaluated to partition observations

* MORF is for classification tasks

## Methods

Consider a dictionary A of projection vectors. In naive RF, A is the standard basis vectors {e_j}; in SPORF, A contains sparse vectors.

In MORF, A = {a} is modified to take advantage of the underlying manifold of the data. Each atom a projects an observation to a real number and maps to a location on the manifold. Nonzero elements of a select and weight features. 

Patterns of contiguous points on the manifold define the atoms of A. At each node in a decision tree, MORF samples d atoms yielding d new features per obeservatoin and optimizes the best fit according to the Gini index.

In images (where observations are vectorized), MORF creates projections by summing the intensities of pixels in rectangular patches. The atoms are the vectors representing these patches. This allows MORF to learn features like edges or corners in images which may best distinguish between classes.

By counting the number of times a given feature is used in projections across the ensemble of DTs, we can determine important features to making a classification and interpret MORF.

## Simulation Results

Experiment A: observations are deiscretized circles
Experiment B: binary image classification (horizontal v. vertical bars)
Experiment C: signal classification

MORF outperforms all other ML algos tested except a CNN, especially at low numbers of training samples

## Real Data Results

Tested on MNIST.
MORF outperformed other methods except CNNs for all sample sizes.

On MNIST comparing 3 and 5 only, feature importance of MORF shows less noise than SPORF and is smoother than RF.

## Future Work

Other task-specific kernels may lead to improved CV performance - eg structured projection distributions could be incorporated into XGBoost.