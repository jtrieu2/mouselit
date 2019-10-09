# Manifold Forests: Closing the Gap on Neural Networks

## Abstract
* decision forests (DF) dominate other methods in tabular data (feature space is unstructured and invariant to permuting feature indicies)
* neural nets (NN) tend to outperform DF on structured data lying on a manifold e.g. images, text, and speech
* Manifold Forest (MORF) empirically outperforms other approaches that ignore feature space structure on images, time-series, and a torus
* MORF training and test time is faster than deep nets

## Methods

### Random Projections Forests on Manifolds
* dictionary of projection vectors A = {a} is modified to take advantage of underlying manifold on which the data lies
* MORF creates projections by summing the intensities of pixels in rectangular patches
  * {a} are vectorized representations of these rectangular patches
* rectangular patch parameterized by
  * upper-left corner (u,v)
  * height (h)
  * width (w)
* to generate a patch
  * index of upper-left corner is sampled (u,v)
  * height and width are independently sampled from separate uniform distributions
  * hyperparameters determine minimum/maximum heights and widths to sample from
    * prevents patch from exceeding data-matrix boundaries
* {a} yields a projection of data (a^T)(x_i), selecting and summing pixel intensities in sampled rectangular patch

### Feature Importance
* projection forest specific metric used to estimate relative importance of each feature
  * count number of times a given feature was used in projections across the ensemble of decision trees

## Simulation Results

### Simulation Settings
* tested MORF against logistic regression, linear SVM, SVM with radial basis function kernel, k-nearest neighbors (kNN), RF, multi-layer perceptron (MLP), SPORF, and CNN with two convolution layers, ReLU activators, maxpooling, followed by dropout and two densely connected layers
* Experiment A: discretization of circle into 100 features with two non-adjacent segments of 1's in two differing patterns
  * class 1 has two segments of length five; class 2 has 1 segment of length 4 and 1 segment of length 6
* Experiment B: 28x28 binary image classification
  * class 0 had randomly sized and spaced horizontal and class 1 had vertical bars
* Experiment C: signal classification
  * class 1 has 100 values of Gaussian noise while class 2 has added exponentially decaying unit step beginning at time 20

### Classification Accuracy
* in all three experiments, MORF outperforms all other classifiers, especially at low sample sizes, except for CNN which has similar performance

### Run time
* all experiments run on single core CPU
* MORF had train and test times comparable to SPORF and RF
* CNN took longer to run

## Real Data Results

### Classification Accuracy
* MORF evaluated on MNIST
* restricted to use patches up to only 3 pixels in height and width
* MORF has lower classification error than all other algorithms besides CNNs for all sample sizes

### Feature importance
* evaluated capability of MORF to identify importance features compared to SPORF and RF
* methods ran on subset of MNIST dataset: only 3's and 5's with 100 images from each class
* MORF visibly results in smoother pixel importance, possibly from continuity of neighboring pixels in selected projections
