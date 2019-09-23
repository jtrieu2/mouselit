**Introduction**
- RF often operate in a tabular setting i.e. the observation is not interpreted to have any structure
- this leads to weaknesses with data such as images or time series where there is structure
- MORF: at each node, randomly spatially contiguous features selected using knowledge of underlying structure

**Methods**
- SPORF uses a projection matrix A, but in MORF, this projection matrix is modified
- A = {a}
- each element of a maps to a location on the underlying manifold
- at each node, MF samples d atoms, which result in d features
- actual implementation: with a 2d array (such as an image), a rectangular patch is randomly selected and vectorizes
- patch is parameterized by upper-left corner location (u, v), height h, and width w
- u ~ unif{0, W - wmin}
- v ~ unif{0, H - hmin}
- w ~ unif{wmin, min(wmax, W - u)}
- h ~ unif{hmin, min(mhax, H - v)}
- with time series or 1 dimensional arrays, hmin = hmax = 1
- benefit of decision trees is that you can figure out the important features
- to determine important features in MORF, examined the number of times a given feature was used in projections

**Simulation Results**
- Evaluated performance against logistic regression, linear SVM, SVM, k nearest neighbors, RF, multi-layer perceptron, RPORF, CNN
- Experiments were tested on circle segments, orthogonal bars, and noisy impulse
- SPORF outperforms most algorithms in these settings

**Real Data Results**
- MF results in smoother pixel importance that is more localized on important areas
