#Spatial decision forests for MS lesion segmentation in multi-channel magnetic resonance images

## Introduction
* Multiple Sclerosis (MS) is a chronic disease that affects white matter (WM) of central nervous system
* automatic segmentation (locating) of lesions can help diagnosis and patient follow up

### past automatic segmentation methods
* Anbeek et al.(March, 2004) and Admiraal-Behloul et al.(2005) -> intensity based k-nearest neighbors with spatial prior and a fuzzy inference system
* unsupervised learning based on hidden markov chains that estimates proportion of white matter (WM), gray matter (GM), and cerebro-spinal fluid (CSF) in each voxel
* Expectation maximization (EM) combined with Mahalanobis thresholding to highlight lesions

### proposed method
* random forest with spatial, multi-channel features, and symmetry features
* assumption that healthy brain is approximately symmetric with respect to mid-sagittal plane and that MS lesions develop asymmetrically
