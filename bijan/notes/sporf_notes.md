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

### numberical analysis of lumberjack

The few simulated classification problems considered are Sparse parity, Orthant, and Trunk. Sparse parity is a multivariate XOR such that the class label is 0 if the number of dimensions having positive values amongst the first p' < p dimensions is even, and 1 otherwise. Thus, no individual dimension contains any information, while only p' of the total p dimensions do jointly. 

Orthant is a multi-class problem where the orthant of a datapoint determines its class. Individual dimensions are strongly and equally informative. Note an orthant in Rp is a generalization of a quadrant in R2. Since there are 2^p orthants in p dimensions, there will be 2^p classes.

Trunk is a two-class problem were each class is a multivariate gaussian with identity covariance matrix. Each dimension is informative, with information gain decreasing as number of dimensions used increases. The means of class 1 is mu1=(1, 1/root(2), 1/root(3), dots, 1/root(p)), and mu0=-mu1, where the bayes optimal decision boundary is the hyperplane (mu1-mu0)X=0

### testing

Lumberjack is tested against F-RC, RF, CCF, RR-RF. Lumberjack has lower error rate in sparse parity and orthant data sets, even in decreasing sparsity parameter. Lumberjack is also able to trade off tree correlation for tree strength as $n$ increases, allowing it to win against other algs in both low $n$ and high $n$ settings. For smaller training sets, lumberjack wins through lower bias, while for larger sets it wins through lower variance.

#### Interpretability

Understanding the data is just as important as finding a good algorithm in many sattings. RFs are popular because one can learn good models that allow for extraction of suitable feature importance measures. One measure many use is the Gini importance, defined as the sum of reduction in gini impurity over all splits of all trees made on that feature. In normal RF, features with low marginal imporfation but high pairwise or higher-order joint distributional information will receive relatively low importance scores. In lumberjack, defining splits as linear combinations of features improves the chance of important higher-order distributional information is improved. In a simulation setting, lumberjacks top 10 splits contain more information than RFs, except for the very first.

It should be noted that the value of lambda affects the splits chosen - if the best projection is a vector of all ones but lambda is not close to 0, there is a low probability lumberjack would select that split.

### theoretical analysis of random projection forests

Given a training set $D_n$, we have a classifier $h_n$ trained on the data. The sequence of classifiers for the data is consistent for a distribution $F_{XY}$ if and only if L(h_n) converges to bayes optimal loss as $n \to \infty$. It is universally consistent iff $h_n$ is consistent for all possible distribbutions $f_{XY}$
Analysis is done on a simplified version of the RF procedure defined below.

The data-agnostic RPF is the original random projection forest with random partitions independent of class labels. The projection matrix A is also sampled independently.

We denote the number of partitions of a tree as $t_n$ The data-agnostic RPF is universally consistent for classification when $t_n\to\infty$, and $t_n/n \to 0$ as $n \to \infty$. This follows from Stone's theorem.

#### time complexity

Let $T$ be the number of trees, $n$ be the number of training samples, $p$ the number of features in the data, and $d$ the number of features sampled at each split.
The average case time complexity of constructing a RF is $O(Tdn\log^2(n))$. The $dn\log(n)$ sorts the $d$ features at neach node, and the additional $\log(n)$ is the reduction in node size at lower levels and avg number of nodes produced.
Lumberjack's average case time complexity is similar, with an additional term for sparse matrix multiplication at each node. This results in $O(Td\log(n)(\log(n)+\lambda p))$. Generally letting $\lambda \approx 1/p$ gives the same time complexity as RF.
Note that the $d$ in RF is $<= p$, while Lumberjack has no restriction on $d$. While a larger $d$ takes longer to train, it usually results in increased performance.

#### space complexity

Consider $c$ classes, and the same $T, p, n$. A single tree must store a data matrix in memory, $O(np)$. While splitting, two $c$-length arrays store the counts of each class to the left and right of a split point, used to evaluate Gini impurity. A series of random sparse projectio nvectors are sequentially assessed, with less than $p$ nonzeros. If we assume trees are fully grown (n leaf nodes, 2n total nodes), the space complexity to build a lumberjack is $O(T(np+c))$m the same as RFs.

#### storage complexity

the disk space required to store an RF is $O(Tn)$, as we have an $O(1)$ storage of a split or a class label for each node. For a lumberjack, a sparse vector is stored isntead of a split index. Thus, $z$ nonzero entries in a projection requires $O(z)$ memory. Storage of a lumberjack is thus $O(Tnz)$, while $z \approx 1$ when $\lambda = 1/p$.

#### empirical speed and scalability

Comparing RF, F-RC, and Ljack, RF is fastest, then Ljack, then F-RC (in the sparse parity and orthant problems). At similar $d$, training time for all is comparable. Additional training time with $d > p$ results in greater accuracy.

#### structured lumberjack

In CV tasks, good features exploit spatial relatinoships between pixels. These can be engineer using domain knowledge or leaned via CNN. One could propose a projection distribution which enables learning to exploit spatial structure.
This is referred to as S-Lumberjack, which samples $d$ rectangular patches of spatially contiguous pixels. For each patch, the split is optimized over the set of $d$ constructed features.
By constructing features from spatially-related data, features can represent low-level objects like edges, which can bbe used to create hierarchical decision rules combining patches.
S-lumberjack outperforms all other lumberjack methods and RF on image data. 
