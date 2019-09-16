Random Forests
Leo Breiman, 2001


- ensemble of trees have worked well for classification accuracy
- a random forest is a classifer consisting of a collection of trees where each tree casts a vote for the most popular class
- random forests do not overfit as more trees are added
- the generalization error of RF is dependent on the strength of individual classifiers in the forest and their correleation
- consequently, randomness added to an ensemble system must minimize correlation and maximize strength to improve accuracy


- Breiman's method: bagging (using random subset of the training set for an individual tree) and random feature selection are used
- each tree is grown and then not pruned
- bagging helps enhance accuracy as well as estimate generalization error (out-of-bag estimate)
- out-of-bag estimate: aggregate votes in which classifier is incorrect -> error rate
- more specifically, the out-of-bag estimate refers to the error rate of the classifiers on the parts of the training set that are not bagged with a given tree
- out-of-bag estimate is as accurate as using test set of same size as training set, so you do not need a test set
- in each bag, roughly 2/3 of training set 

- Forest-RI: at each node, select at random a small group of input variable to split on; grow using CART to max size and do not prune
- Breiman tested 2 input variables sizes: F=1 and F = log(2)(M) + 1, where M is # of input variables
- a single random variable random forest is enough to have comparable results to Adaboost; having more random input variable does not increase accuracy substantially, especially with smaller data sets
- Forest-RI can be much faster than Adaboost or Bagging


- Forest-RC: instead of just using random features, take a random linear combinations of some features
- this might be necessary because if there are not that many inputs, picking the number of random features to split on per node could lead to higher correlation etween the trees
- Forest-RC expands the possible ways to split
- 2 parameters: L -> number of variables to be combined (randomly selected than added with random coefficients [-1, 1]) and F: number of linear combinations generated per node
- on smaller data sets, you do not need a large F

- dealing with categorical variables: when they are elected, choose a random subset of the categories, then define sub. variable that is 1 if the value is within subset and 0 else

- with Forest-RI, as F increases, correlation will keep increasing, although strength will level out. Additionally, the error will decrease, then start increasing
- goal: maintain lower correlation but high strength

- RF are more immune to noise than Adaboost

- RF works well with weak inputs

- RF can also be used for regression
- correlation increases slowly relative to number of features
