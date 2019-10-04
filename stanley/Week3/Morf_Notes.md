# Background

Naïve DF implementations fail to explicitly consider feature indices. 

Here, we build on that to show that one can choose distributions in a manifold aware fashion. For example, for image classification, rather than randomly selecting pixels, one can randomly select contiguous patches.

We demonstrate the empirical performance of data living on three different manifolds: images, time-series, and a torus.

Inspired by Sporf, we propose a projection distribution that takes into account continuity between neighboring features while incorporating enough randomness to learn relevant projections. At each node in the decision tree, sets of random spatially contiguous features are randomly selected using knowledge of the underlying manifold. Summing the intensities of the sampled features yields a set of projections which can then be evaluated to partition the observations. 

## Desirable Properties
In the structured setting, the dictionary of projection vectors A = {a} is modified to take advantage of the underlying manifold on which the data lies. We term this method the Manifold Forest (Mf).

Each atom a projects an observation to a real number and is designed with respect to prior knowledge of the data manifold. Nonzero elements of a effectively select and weight features. Since the feature space is structured, each element of a maps to a location on the underlying manifold. 

