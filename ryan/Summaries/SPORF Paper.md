# Sparse Projection Oblique Randomer Forest

**Introduction**
- typical random forests and other similar methods split along coordinate axis of features
- further developments, such as Forest-RC, created algorithms that split on linear compbinations of coordinates (oblique), which allow better learning at the expense of computational efficiency
- additionally, these methods occasionally do worse on some problems where axis aligned splitss are very informative
- SPORF uses sparse random projections for splits in order preserve the desirable properties of axis-aligned decision trees while mitigating the issues
 
**Background and Related Work**
- RF builds decision trees using recursive binary splits, try to maximize information gain, which is often measured by decrease in Gini impurity
- a random subset of features is chosen
- splitting continues until stopping criteria: common ones are max tree depth, min number of observations at node, or completely pure node
- oblique decision trees allow splits that aren't axis-aligned, several different methods including F-RC, RR-RF, CCF, and RBF
- projections -> random projection maxtrix X_ = XA, dimension reduction tool
- very sparse randomm projections can maintain high accuracy and speed up matric
- gradient boosted trees iteratively minimize cost function via gradient decent
- desirable properties:
	1. Random search for splits
	2. Flexible sparsity
		- RF searches over fully sparse, performs poorly if no single feature is informative
		- dense methods, such as RR-RF, do not do well in sparse scenarios
		- thus, you want to control sparsity
	3. Ease of tuning
	4. Data insight
	5. Expediency and Scalability

**Methods**
- sample lambda * p * d non-zero numbers from {-1, +1} and then distribute uniformly at random into projection matrix A
- in paper, each algorithm uses 500 trees, all unpruned
- some tuning of hyperparmeters (d number of candidate split directions at each node, and lamba, average sparsity in SPORF and F-RC)

**Simulated Data Empirical Performance**
- authors propose that oblique forests are more consistent than original RF
- certain problems, RF cannot get good results due to axis-aligned splitting
- simulated datasets:
	1. sparse parity (multivariate generalization of noisy XOR problem)
	2. orthant (class label determined by orthant)
	3 Trunk (balanced 2 class problem)
- SPORF performs as well or better than others on sparse barity and orthnant
- RF performs badly on sparse parity, F-RC on orthant
- F-RC requires hypermarameter to fix sparsity of sampled univariate projections, while SPORF uses sparsity on entire matrix A
- SPORF is more robust to sparsity hyperparameter than F-RC
- SPORF can find important features, and the features can be more informative than RF

**Real Data Empirical Performance**
- SPORF compares favorably to RF, XGBoost, RR-RF, and CCF on 105 benchmark datasets 
- SPORF outperforms RF all the time
- XGBoost and CCF outperform RF on numerica, but worse than RF on categorical
- default hyperparameters: d = p^2 and lambda = 4/p
- SPORF is robust to high dimensional noise ( comparable to XGBoost and RF but much better than RR-RF and CCF)
- Time complexity of RF is O(T dnlog(n)^2)
- SPORF's is O(Tdnlog(n)^2 + Tdnp lambda) due to sparse matrix multiplication, but since lamba is close to 1/p, complexity is generally the same as RF
- SPORF's space complexity is O(T(np + c)) which is the same as RF
- RF storage complexity is O(Tn)
- SPORF storage complexity is O(Tnz), but z is a RV whose prior dependent on lambda, which is uaully 1/p, and z is usually close to 1, to O(Tn) which is similar to RF
- empirically in terms of speed, RF > SPORF > F-RC
- SPORF generally is faster or comparable to existing algorithsm
