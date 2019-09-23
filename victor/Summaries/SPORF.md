# Sparse Projection Oblique Randomer Forests

## Abstract
Decision forests, including Random Forests and Gradient Boosting Trees, have recently demon- strated superior performance in a variety of machine learning settings. Decision forests are typ- ically ensembles of axis-aligned decision trees; that is, trees that split only along feature dimen- sions. In contrast, many recent extensions to decision forests are based on axis-oblique splits. Unfortunately, these extensions forfeit one or more of the favorable properties of axis-aligned splits, such as interpretability or computational efficiency. We introduce yet another decision forest, called “Sparse Projection Oblique Randomer Forests” (SPORF). SPORF uses very sparse random projections, i.e., linear combinations of a small subset of features. SPORF significantly improves accuracy over existing state-of-the-art on a standard benchmark suite for classifica- tion with > 100 problems of varying dimension, sample size, and number of classes. To illus- trate how, why, and when SPORF outperforms other methods, we conduct extensive simulated experiments. SPORF typically yields improved performance over existing decision forests, while mitigating computational efficiency and scalability and maintaining interpretability. SPORF can easily be incorporated into other ensemble methods such as boosting to obtain potentially similar gains.

## Oblique Extensions to Random Forests
* oblique splits are along directions olbique to the coordinate axes
* advantage over traditional RF, which only split along coordinate axes
* weights of each projection are independently sampled uniformly

## Random projections
* given a data matrix, one can construct a random projection matrix whose entries are i.i.d. with zero mean and constant variance
* very sparse random projections can maintain high accuracy and significantly speed up matrix multiplication

## Desirable properties for Ensembles of trees
* Random search for splits: better tree diversity
* flexible sparsity
* ease of tuning: relative insensitivity to hyperparameter settings
* data insight: use Gini importance to assess relative importance of each feature (existing oblique forests do not allow for easy computation of Gini)
* expediency and scalability: existing oblique forest algo are computationally expensive

## Simulated Data Empirical performance

### SPORF and other oblique forests are "more consistent" than RF
* SPORF approach perfect classification whereas RF cannot achieve error lower than 1/6
### Simulated datasets
* sparse parity: multivariate generalization of noisy XOR problem
* orthant: multi-class problem where each class label is determined by the orthant in which a data point resides; designed to be easy for RF

### SPORF combines best of existing axis-aligned and axis-oblique methods
* sparse parity: SPORF performs as well as or better than other algorithms (RF, F-RC, CCF)
* orthant: SPORF performs just as well as RF
### SPORF is Robust to hyperparameter selection
* SPORF requires sparsity to be specified on entire random matrix
### SPORF learns important features
* compute Gini importance for each unique univariate projection
* SPORF learns features thant are more important than any of the observed faetures and they are interpretable because of sparse linear combinations of observed features
Â
