# A Survey of Semantic Segmentation
## Intro
The task is to cluster parts of an image together if they belong to the same class. Non-semantic segmentation clusters pixels together based on general characteristics.

Object detection has to distinguish different instances of the same object.

The classes that the alg is trained on is a central design decision.
But, there are also unsupervised segmentation algs as well.

The data that can be used for inference varies by application:
grayscale, colored, including depth, stereo images, or 3d.

Segmentation algs can also be passive, automatic, or interactive.
Performance is measured in a few ways:
 - Accuracy, which can be pixel-wise accuracy (which has drawbacks), mean accuracy, mean intersection over union, and frequency weighted intersection over union.
 - Speed, which on a per-image basis is called latency. Most wall times are hardware-specific, sometimes even data-specific. Besides latency, throughput is also relevant for different applications.
  - Stability, over slight changes in the input image like being blurred by smoke.
  - Memory usage, which matter if a smartphone or camera would use it.

The computer vision community produced a couple public datasets.
 - PASCAL VOC, each year from 2005-2012. In 2007 segmentation was added. It contains annotated photos from www.flicker.com. The 2012 competition had 5 challenges, of which one was segmentation with pixel-wise class labels. The classes are: aeroplane, bicycle, bird, ... They use segmentation over union
 - MSRCv2, 591 photographs with pixel-level annotation of 21 classes: aeroplane, bike, bird... as well as a VOID label for pixels which don't belong to any of the 21 classes or close to the segmentation boundary.
 - Warwick-QU dataset, 165  images with pixel-level annotations of 5 classes: healthy, adenomatous, moderately differentiated, moderately-to-poorly differentiated, and poorly differentiated. It is part of the gland segmentation challenge.
 - DIARETDB1, 89 images showing interior of the eye

## Segmentation pipeline
Typically semantic seg is done with a classifier which operates on fixed-size features and a sliding-window approach. Your classifier is trained on images of a fixed size and fed rectangular regions of that image, and classifies the center pixel of that window. Techniques to speed this up include applying a stride and interpolating results. Neural networks can do this efficiently by applying a trained network to an image as a convolution.

Markov random fiels and conditional random fields take the complete image and segment it holistically.

## Traditional approach (no neural nets or heavy domain knowledge)
### Features and preprocessing
Note that auto encoders can be used to learn features which can be used by any classifier. Commonly used features include:
  - Pixel color, either in RGB or HSV or gray-value. Most dominant are RGB for simplicity and HSI which might make illumination invariance simpler. One can use histogram equalization can be used to improve contrast.
  - Histogram of oriented gradients, interpret the image as a discrete function which maps position to a color. Each pixel has a derivative of x and y, and the original image is transformed to two feature maps of equal size which represents the gradient. This is split into patches and histograms are calculated for each patch.
  - SIFT (scale invariant feature transform), describe keypoints in an image. Each keypoint generates a 128-dimensional feature vector from a 16x16 patch around it.
  - BOV (bag of visual words), similar to keypoints and HOG features, historgrams counting occurrences of certain patterns in an image.
  - Poselets, rely on manually added keypoints such as "left shoulder" originally used for pose estimation. Difficult to use for non-human data.
  - Textons are base-level patterns such as edge detectors
  - Dim reduction, down sampling the image or running pca

### Unsupervised methods
These can be used as another source of information in supervised algorithms or to refine a segmentation. They are never semantic. These algs try to detect consistent regions or region boundaries.
 - Clustering algs, you can directly cluster pixels such as with k-means or mean-shift algorithm
 - Graph-based image segmentation, interpret pixels as vertices and edges as a difference in color. you can use the 4-neighborhood or 8-neighborhood versions. You can build a MST and remove edges above a threshold, and connected components are segments. Pascal VOC 2010 2nd place was a graph alg.
 - Random walks, select seed points on the image and each pixel has a probability of beng reached by random walk from the seed point. The walk probabilities are exactly the HOG features in x and y. It in interactive unless you use another method to generate seeds.
 - Active contour models, find edges and smooth borders. They create an energy function and minimize it, used either to segment itself or to refine segmentation.
 - Watershed segmentation, takes a grayscale and interprets it as a height map. Low values are basins and high values are the watershed, and the basins should capture what you want. You fill basins from the bottom and a watershed is found when two basins connect. There are two flaws, over-segmentation due to local minima and thick watersheds due to plateaus.

### Random decision forests
Measure of features can be arbitrary, and are faster than SVMs. The training modes are central axis projection and perceptron training. In training, each node searches a hyperplane (MORF falls into this category). Random forests with texton features are applied for segmentation and have a per-pixel accuracy of 66.9%. An excellent introduction is given by Object class segmentation using random forests.

The rest of the methods include SVMs, markov random fields, conditional random fields, and neural networks.

### Post processing methods
morphological "opening" and "closing" operations can remove noise. Which are dilation and erosion. Another way to refine is to match close edges, one way of doing this is with an ultra-metric contour map.
Active contour models are another example we reviewed before.

### Possible problems
 - lens flare
 - vignetting, photograph gets darker in the corners due to filters
 - blurred images, either through camera shake or smoke
 - partial occlusions, if there is something in front of your class partially
 - camouflage, where your object has similar texture to bbackground.
