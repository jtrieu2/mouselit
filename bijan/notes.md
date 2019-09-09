## Random Projection Forests
!(link)[https://arxiv.org/pdf/1506.03410.pdf]

### Intro

Ensemble methods win a lot in ML settings.
Generalizing decision tree methods results in Random Projection Forests (RPF)
which uses linear projections. There is a special case of RPF called lumberjack, which is RPF on a small subset of features (L1 regularized?).

Gradient-boosted decision trees have become very popular and often are the "winning" alg. The variations of RFs which utilize linear combinations of features lose speed and insensitivity to noise, and have not been thoroughly tested.

All previously proposed ensemble tree based methods apply a linear projection at each node, differences between algorithms being the distribution which the proections are sampled.

### Background

Let $(X,Y) \sim f_{XY}$, where $X \in \mathcal{X} = \mathbb{R}^p$ is a random real p-vector. There is also $Y \in \mathcal{Y} = \{c_1, \dots, c_k\}$ representing the $K$ categories. We want to minimize the probability of misclassification.

In the regression setting, let $Y \in \mathcal{Y} = \mathbb{R}$ be a real-valued response variable. Then, the goal is to learn a function mapping from $\mathbb{R}^p \to \mathcal{Y}$ to predict $Y$ associated with observed $X$, minimizing mean-squared error (for example).

Random forests build $T$ decision trees via recursively binary-splitting the data. Measuring information gain can be done with the Gini impurity $I(S) = \sum_{k=1}^K f_k(1-f_k)$, where $f_k = \frac{1}{|S|}\sum_{i\in S}\mathbb{I}[y_i=k]$. Regression uses a different criteria $I(S) = \sum_{y\in S}(y-\bar{y})^2$, where $\bar{y} = \frac{1}{|S|}\sum_{y \in S} y$. We let $\theta = (j, t)$, where $j$ selects an index and $t$ selects a threshold. Everything less than the threshold in the $j$-selected dimension goes in the left group, and the $x^{(j)}$ greater go in the right group. The split is made on the best $\theta^*$ via

$$\theta^* = \underset{\theta}{\argmax} |S|I(S) - |S^L(\theta)|I(S^L(\theta)) - |S^R(\theta)|I(S^R(\theta))$$

This is just the information of the whole tree minus the information of each resulting left and right trees.
A subset of the $p$ features is sampled, observations are sorted from least to greatest, and each midway point between obbservations is tested in order to choose the optimal split.

This splitting is done recursively until a maximum depth is reached, minimum leaf size is reached, or a node contains only one class label. At the end, the leaf nodes are disjoint partitions of the feature space. Letting $l_m$ be a leaf node of a tree, $S(l_m) = \{i  : x_i \in l_m \forall i \in [n]\} is the training data in $l_m$. The leaf prediction for classification is
$$h(l_m) = \underset{c_k \in \mathcal{Y}}{\argmax} \sum_{i \in S(l_m)} \mathbb{I}[y_i = c_k]$$.
The leaf prediction for regression is
$$h(l_m) = \frac{1}{|S(l_m)|}\sum_{i \in S(l_m)} y_i$$.

If we let $\hat{y}^[(t)] be the prediction made by the $t$th tree, the prediction of the RF is the plurality vote $$\hat{y} = \underset{c_k \in \mathcal{Y}}{\argmax} \sum_{t=1}^T \mathbb{I}[\hat{y}^{(t)} = c_k]$$ in classification and the average $$\hat{y} = \frac{1}{|T|}\sum_{t=1}^T \hat{y}^{(t)}$$ in regression.

The coolest things about RF is that individual classifiers only have to perform better than chance as long as their predictions have low correlation. RF decorrelated the trees via building each tree on a random bootstrap of the training data, and restricting the splitting dimension $j$ over a random subset of the total $p$ dims.

RFs that don't restrict splitting along coordinate axes of the feature space are referred to as oblique. Breiman proposed Forest-RC which constructs linear combinations of $L$ randomly chosen dimensions and samples weights uniformly over $[-1,1]$. Yet this alg never became popular, even though it regularly outperforms RF on many datasets. Other algs such as random rotation random forest (RR-RF) and canonical correlation forests (CCF) are also oblique algs, but are specific versions of a more general procedure.

#### Random projections

A matrix $X \in \mathbb{R}^{n x p}$ can be multiplied by a random projection matrix $A \in \mathbb{R}^{p x d}$ (with iid entries of zero mean and constant variance) to get
$$\tilde{X} = XA \in \mathbb{R}^{n x d}, d << min(n,p)$$
The much smaller matrix $\tilde{X}$ preserves pairwise distances of $X$ in expectation!!!!

Different probability distribution over the entries of $A$ lead to different error tail bounds. It have been shown that very sparse random projections, where most entries in $A$ are zero, can maintain high accuracy and speed up maxtrix mult. by a factor of $\sqrt{p}$ or more! This is done by $a_{ij} = +1$ with prob $\frac{1}{2s}$, $= 0$ with prob $1 - \frac{1}{s}$, and $=-1$ with prob $\frac{1}{2s}$, where $S$ is typically $>> 3$.

#### Forest packing

By storing nodes likely to be accessed near each other in memory, and removing duplicated leaf nodes, reduces retrieval time by improving memory coherence. The number of unique leaf nodes is the number of classes in the training data set, and leaf nodes account for half of all nodes in a tree. Other methods like storing multiple trees together in bins with the first couple leves intertwined improves multi-core evaluation.


### Methods

At each split of a tree, there is a set of predictor data points $\bar{X} = \{x_s\}_{s\in S_i^l} \in \mathbb{R^{p x S_i^l}$, where $S_i^l$ is the cardinality of the set of predictor data points at the $i$th node of the $l$th tree. A matrix $A \in \mathbb{R}^{p x d}$ is sampled from the projection distribution $f_A$ to create a reduced dimension projected space $\tilde{X} = A^T\bar{X}$. The choice of projection distribution significantly impacts the strength and diversity of trees! The original axis-aligned RF picks a coordinate and puts a $1$ in that $d_i$ column and $0$s elsewhere. F-RCs samples a fixed number of coordinates without replacement for each of the $d$ columns and puts a value uniformly between $[-1,1]$ there, with $0$ elsewhere. Rotation forests contruct $A$ from the top $d$ PCs of the data $\bar{X}$. CCF uses CCA to construct $A$. While the "best" $f_A$ is data-set dependent, its too hard to try them all. Thus, we choose a good default.

Using dense linear combinations (like in RR-RF) isn't so good with noisy or irrelevant dimensions.

#### lumberjack

rather than sampline $d$ non-zero elements of $A$ and enforcing that each column gets a single non-zero number like RF, we sample $\lceil \lambda p d \rceil$ non-zero numbers from $\{-1,+1\}$ with equal probability. $\lambda \in (0, 1]$ is the density of $A$. The nonzero values are distributed uniformly at random across $A$.

In an example of parallel data in 20-dimensional hyperplanes, regular RF fails and RR-RF fails because not any one axis is informative, and in high $d$ rotations tested will almost always be orthogonal to the optimal projection. In the sparse case, lumberjack is clearly better. In the dense case lumberjack struggles more but everyone else still has a hard time for the same reasons.

#### hyperparam tuning

The number of trees in each algorithm is 500, chosen to be sufficient for convergence of out-of-bag error. In regression, trees above 100 dont vary results, so they choose 500 as well. Nodes are split until pure. The objective is to maximize reduction in gini impurity in classification and split-wise mse in regression.

values of $d$ are $p^{1/4}, p^{1/2}, p^{3/4}, p$. L-jack and F-RC are trained for $d = p^2$ also.

### testing

Lumberjack is tested against F-RC, RF, CCF, RR-RF. Lumberjack has lower error rate in sparse parity and orthant data sets, even in decreasing sparsity parameter. Lumberjack is also able to trade off tree correlation for tree strength as $n$ increases, allowing it to win against other algs in both low $n$ and high $n$ settings. For smaller training sets, lumberjack wins through lower bias, while for larger sets it wins through lower variance.

### theoretical analysis of random projection forests
