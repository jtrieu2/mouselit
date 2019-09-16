#BOHB Paper Summary
* Baynesian Hyperparameter tuning sucks, not feasible for long training times and bandit-based methods alone do not converge quickly enough.
* Try a combination of the 2 instead

## Introduction
* Good Hyperparameters have the following criteria:
  * Strong Anytime Performance -
  * Strong Final Performance - works well given the time and resource constraints
  * Effective Use of Parallel resources - good use of parallel computing
  * Scalability - should work with lots of hyperparameters
  * Robustness and Flexibility - should work with many types of hyperparameters and HPO problems
## Background
* Baynesian Hyperparameter optimization has worked well in the past, mostly commonly Gaussian processes. These don't scale well and require special kernels to be effective.
* Hyperband is the bandit strategy that allocates resources to set of random configurations. Has better anytime performance compared to Gaussian processes and scales better into high dimensions but does not learn from previous configurations and creates random configuration samples. Possibly has worse performance due to random elements.
## BO and HB
* Aim to minimize function of validation performance for ML algorithms, where function is generally observed through noise.
* BO uses probabilistic model based on conditional probs with existing data points.
  * Uses acquisition function that trades off exploration and exploitation
  * Iterates through maximizing acquisition function, evaluation of the probabilistic objective function , and augments data with point that maximizes acquisition function
* HB works by taking budgets of approximations for the objective function. Uses successive halving to reduce sample size while  
* BOHB extends HB by taking strong final performance from BO.
* Additionally, BOHB leverages HB simplicity and computational efficiency from carrying out small functions at smaller budgets.
* The algorithm uses HB to determine how many configurations to use, replacing a random sample with a model-based search (BO)
  * Uses multidimensional KDE to better handle interaction in input space, requiring a minimum number of data points
  * Gradually move from smaller to larger budgets as optimization progresses, beginning with best and worst configurations to model two initial densities
  * BOHB generally insensitive to its hyperparameters
## Experiments and Benchmarks
* Optimized hyperparameters of a high dimensional toy function, a SVM, and feed forward neural network.
* For 16 dim function, BOHB converged the fastest to the time budget and minimal regret
* In neural network, BOHB found optimal initial learning rate, batch size, dropout, decay factor, number of layers, and units per layer.
* Also optimized hyperparameters on CNN trained on CIFAR-10, taking significantly fewer "days" of GPU training than the models that outperform it.
