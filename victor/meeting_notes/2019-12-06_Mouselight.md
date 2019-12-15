## 2019-12-06 Mouselight

### this week

* SNR on preprocessing
* gaussian filter with signma=1.5, snap point to highest intensity within cube of radius 3
* only showign points with SNR < 2
* SNR increased after gaussian filtering **and** snapping the points
* skimage histogram equalization has poor effect on SNR

<img src="/Users/victor/Library/Application Support/typora-user-images/image-20191206154058798.png" alt="image-20191206154058798" style="zoom:50%;" />

* suggested to move on to other preprocessing methods
* Image whitening
  * image patch is a random vector
  * Different image patches are different observations of the random vector
  * Transform covariance of the random vector to identity
* Whitening with (9x9x3) patches on MIP of neurons doesn't seem to work
  * no change - Bug? or wrong implementation of algorithm?
  * check if image is already very decorrelated; check eigenvalues

### existing pipeline 

1. random forest binary classifier (Ilastik, Sommer, 2011)
   1. features - gaussian, laplacian, gradient magnitude, DoG, structure tensor eigenvalues, hessian of gaussian eigenvalues
2. theshold at 0.5
3. Skeletonize (Lee, 1994)
   1. thinning procedure
   2. preserve number of connected objects, cavities and holes
4. Downsample to 20um spacing
5. split at branch points
6. remvoe small segments etc
7. manual annotation

### Question from Dr. Miller

* is it possible to train random forest on 7 features per voxel for entire image? (gaussian, laplacian, gradient magnitude, DoG, structure tensor eigenvalues, hessian of gaussian eigenvalues)