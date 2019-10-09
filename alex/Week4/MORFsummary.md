# MORF -

## What is MORF?
* An extension of the decision forest classifier to function in structured data environments, e.g images.
* Must take into account the closeness of data points

## Background
* SPORF/Random forest explanations, same deal

## Manifold Methods
* Optimization and node splitting done in the same manner as SPORF
* To obtain relevance of neighboring units of structured data, MF creates projections by summing intensities of the unit data in rectangular patches. 
* Use prior knowledge of the data manifold to map from projection vectors of the forest to form patterns of projection vectors. At nodes of the trees, split according to minimize gini impurity. For example, in images, projections made by summing intensities of neighboring pixels in patches and vectorized.

## Results
* MORF shows smoother pixel feature importance than Random Forest and SPORF, getting rid of feature noise at low sample sizes. Also, run time on single core CPU are on par with random forest implementations with similar performance to deep learning methods.
* Manifold Forests show considerable improvement over other decision forests and can compete with CNNs in accuracy with a much faster training time. More work can be with real time object detection and other computer vision tasks.
