# SPORF Paper Summary
### Introduction

Decision trees and random forests have been proven to be optimal learners, and improvements have been made using axis oblique trees, as opposed to axis aligned. We want to build a better ensemble method that addresses the issues of these oblique trees, which include reduced computational efficiency or reduced interpretability. SPORF aims to address these issues while improving on the classification potency of random forests.

### Background
* Gradient boosted Decision trees currently are the top-of-the-line learners for a variety of classification problems, with Random Forests (RF) performing similarly in most cases.
*  Oblique forests, a method of improving RFs, makes splits that are not parallel to coordinate axes, allowing for more accurate splits but inducing more computational complexity.
 * Example is Brieman's Forest RC algorithm, which tends to empirically outperform RFs and Random Rotation Random Forests, which rotates data prior to splitting.

* Sparse random projections significantly speed up calculations with matrices while maintaining high accuracy.
* Best properties for an Ensemble of Trees include:
 * Random splitting of trees (prevents overfitting and reduces complexity of calculations)
 * Flexible sparsity (can sample important projections at higher dimensions with increased sparsity and can make meaningful splits with no single informative feature where high sparsity would fail)
 * Tuning for oblique projections (as they are sensitive to hyperparameter settings)
 * Scalability and efficiency for axis-oblique forests (as they are computationally more intensive)
 * Data insight using Gini importance as metrics for feature importance (difficult to compute for current oblique forests)

### Methods - How it works
* SPORF splits on sparse, random projections at the node level, maximizing reduction in Gini impurity

### Empirical Results and Performance
* Supposed "consistency" boost over RF.
* SPORF solves 4 classification problems
* SPORF outperforms RF, Boosted Trees, RR-RF and CCF on many benchmark datasets
  * Specifically, SPORF outperforms RF on numeric datasets, as to others, but also outperforms on categorical problems, where the others perform worse than RF

## Conclusion

* SPORF is an powerful tool that preserves the computational efficiency and interpretability of RFs while improving on its robustness and scalability using sparse-projection, axis-oblique splits.
* Further work includes full implementation of regression   
