# Background

SPORF uses very sparse random projections, i.e., linear combinations of a small subset of features. At each node of each tree, SPORF searches for splits over a sample of very sparse random projections.

"Oblique" ensembles: splits on linear combinations of coordinates rather than individual coordinates, and therefore ahve an increased expressive capacity. However, these methods forfeit many of the desirable properties that axis-aligned trees possesses, such as computational efficiency, ease of tuning, insensitivity to a large proportion of irrelevant inputs or noise and interpretability.

Breiman's Forest-RC (F-RC) algorithm, which constructs d univariate projections, each projection a linear combination of L randomly chosen dimensions.

Very sparse random projections, in which a large fraction of entries in A are zero, can maintain high accuracy and significantly speed up the matrix multiplication by a factor of sqrt(p) or more. 

A study by Wyner et al. argues tha tRF and GBT are both successful for the same reason - namely both are weighted ensembles of interpoloating classifiers that learn local decision rules. 

Canonical Correlation Forest (CCF), Random Rotation Random Forest (RR-RF)

## Desirable Properties

Random search for splits: supervised linear search procedures can result in failure to learn good split direction. 
Flexible sparsity: sometimes a very large space can render the probability of sampling discriminative random projections very small; therefore needs to control the amount of sparsity.

## SPORF and other oblique forests are 'more consistent' than RF

Sparse Parity and Orthant Problem Testings

SPORF learns important features

One such measure in RF is the mean decrease of Gini importance. 

# Real Data Empirical Performance
## SPORF exhibits best overall classification performance
Cohen's kappa: fractional decrease in error rate over the chance error rate
It is possible that RF and SPORF are more robust to heavier processing (of missing data) of the categorical dataset. 
