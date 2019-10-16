### Intro

Not only do you have to segment, which requires pixel-wise analysis of
your data, but you also have to construct regions and label them.
RFs are more useful than deep learning in segmentaion since they are a bbig
speed up. Most previous work uses simple local features like pixel differences.
The big grok in this paper is to use "SCHM" which are single histogram class
models, and the paper uses RFs with the SCHMs (by KNN) to do segmentation.

They run experiments on the 9-class MSRC dataset
(https://www.microsoft.com/en-us/research/project/image-understanding/?from=http%3A%2F%2Fresearch.microsoft.com%2Fvision%2Fcambridge%2Frecognition%2F)
and the VOC2007 dataset
(http://host.robots.ox.ac.uk/pascal/VOC/voc2007/).

### Background

These lads claim that RFs are good because they (i) inject randomness into the
training of the trees and (ii) are an ensemble method, while still being
efficient. They are only using BINARY DECISION FORESTS for this paper. BUT,
they are very creative with the features that they use. They are concerned with
2 types of node functions, (1) "abstest" accumulates response in one feature in
a single rectangle and (2) "difftest" computes (1) on 2 nearby rectangles and
computes the difference.

### Fusing global and local cues into RF

The SHCM paper looks at random 5x5 patches in the training data, embedding each
patch into a point in 25-dimensional space. They get around 8000 patches, then
slide a 5x5 sliding window over the training data (the pixel to be labelled is
the one in the center) and use KNN on which textures are closer (or "textons").
These guys stress that this methods does not learn discriminatively and it
does not learn spatial information. It is just KL divergence on textons,

They combine two SHCMs qi and qj into wij = log(qi/qj). If there are n classes,
a tree of depth n-1 can compute the closest class by a series of test with
class ratios, which they call "fixed-tree". They say it is good because their
ratios can take values other than -1 and +1.

Thus they list 3 methods (i) fixed tree, basically computes the posterior, (ii)
learnt tree, selects the pair (i,j), and (iii) flexible rectangles where the
window is moved around and offset.

### Experiments

They all use RF of size 10 with a maximum depth of 15 (!!!).

Fixed tree: the sure a single fixed tree and learn the class posteriors by
applying the tree to each training point. This results in same performance as
in the original SHCM paper.

Learnt tree: Instead of using a single depth 8 tree, they allow selection of the
pair ij which improves performance by 1% (75 to 76).

Flexible rectangles: Allowing for different shapes/sizes of rectangles
as well as off center test pixels helps a lot (biggest made by the offset,
  which is around 15 +- 8 pixels in x and y direction, to 82%).

### More features

Introducing more features other than textons helps as well.
They include RGB differences with pixel-wise color histograms of size 8000.
Only using RGB gives a performance of 67% in fixed tree and 72% with offsetting.

HOG features (histogram oriented gradient) for the whole image, leading to
many cells with a feature vector for each cell (basically increasing the number
  of channels to 96 for each pixel). With HOG alone and offsetting you get 75%.

#### Combining features

You can easily combine RGB, HOG, and textons by stacking them. Using all
features and using offsetting gives a performance of 84%. Interestingly,
using textons seems redundant as only using RGB and HOG is also 84% acc.

### CRF stage

Once each pixel has a probability for each class (posteriors) from RF you can
do segmentation. Here they use the constrast sensitive potts model and a gmm
color model fit on each image.

### Conclusion

In general this paper talks about using RF to do segmentation and combining
different methods to improve performance.
