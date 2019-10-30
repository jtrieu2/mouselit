# Deep Regression Forests for age Estimation
Wei Shen, Yilu Guo, Yan Wang, Kai Zhao, Bo Wang, Alan Yuille | CVPR | 2018
https://cs.jhu.edu/~alanlab/Pubs18/shen2018deep.pdf

## Abstract

Age estimation is usually a nonlinear regression problemm.
Challenge: Homogeneous facial feature space due to different age patterns
DRFs 1) connect *split nodes* to a *CNN* 
2) Deal with inhomogeneous data jointly learning data partitions at split nodes; abstractions at leaves

Method
1. Fix leaf nodes - split nodes and CNN optimized by backprop
2. Fix split nodes - leaf nodes optimized

## Intro

Goal: Nonlinear map from face to age
Challenges: 
* large variation in facial appearance among people of same age
* human face matures in different ways at different ages (bone growth in childhood; wrinkles when old)

Existing methods
a) find a kernal-based mapping or
b) partition data and learn local regressors

Regular regression forests make hard data partitions - the proposed method performs a *soft* data partition, so an input-dependent partition function can be learned to handle inhomogeneous data

Method
1. Fix leaf nodes - optimize partitions at split nodes and  optimize CNN by backprop
2. Fix split nodes - leaf nodes (local regressors) optimized by Variational Bounding
3. Repeat these two steps alternatively to jointly optimize feature learning and regression modeling

Note: Inspired by Deep Neural Decision Forests and Label Distribution Learning Forests
but used for regression, not classification/label dist. learning

## Related Work

"Tree growing is usually based on greedy algorithms which make locally-optimal
hard data partition decisions at each split node. Thus, this
makes it intractable to integrate decision trees and deep
networks in an end-to-end learning manner."
*The proposed method addressed this by using a soft partition function at split nodes, so the trees are differentiable

## Deep Regression Forests
objective: map g: x-> y
soft split function sigmoid(f_psi (x; th)) 
psi(.) - index function to bring up psi(n)th output of f(x; th)
th - parameter for split function determine to send sample to left or right subtree
f: x -> R^M
Here, f is a CNN and th is the network parameter.
Psi specifies correspondence between split nodes and output units of f.

Gradient of loss:
![img](https://i.ibb.co/HxBS9x4/image.png)
Left term depends on tree; right term depends on f

Fixing split nodes is an optimization problem solved by Variational Bounding (which is quite a bit of math)

Each tree in the forest has its own leaf node distribution - they are updated in mini-batches
At test stage, average over predictions of F trees

## Experiments

VGG-16 is used for the CNN portion of the network
5 trees, depth 6

Data is augmented; faces detected and aligned
91% cumulative score on MORPH (setting 2) data; beats all other methods (second best 85% cumulative score), cumulative score is for l = 5 years (percent of images predicted within 5 years of truee age)


