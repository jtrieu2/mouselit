### Intro
Region proposal computation is usually a bottleneck
in object detection networks.
They have their own network to calculate region proposals, which they combine with Fast R-CNN by sharing convolutional features ("attention" mechanisms).

An RPN simultaneously predicts object bounds and objectness scores at each position.
Convolutional feature maps used by region-based detectors can also be used for generating region proposals.

To unify RPNs with object detection networks, they designed a training scheme that alternates between fine-tuning region proposal and then fine-tuning object detection (keeping proposals fixed).

They evaluated their methods on the PASVAL VOC benchmarks, where RPNs with fast RNNs produce better detection accuracy than selective search + frcnn. The effective time for running proposals is just 10 milliseconds, so the frame rate is 5fps even while using expensive deep models. In COCO 2015 competitions faster RCNN is the bases of several 1st place entries.

### Related work
There is a large literature on both object proposal methods, including comprehensive surveys and comparisons of methods. Widely used methods include Selective Search, CPMC, MGC, and sliding-window based methods.

Deep networks can be trained to classify proposed regions into objects or background end-to-end. Accuraccy depends on performance of the region proposal module. Several papers have proposed ways of using them for predicting object bounding boxed. Shared computation of convolutions has been getting more and more attention.

### Faster R-CNN
There are 2 main modules - a deep fully connected conv netowrk, and the fast RCNN detector that uses proposed regions. The entire system is a single network for object detection. RPN basically tells fRCNN where to look.

#### Region proposal networks

An RPN takes an image of any size as input, and outputs a set of rectangular object proposals, each with an "object-ness" score. To generate proposals, slide a small network over the convolutional feature map output. This small network takes as input an nxn spatial window of the input feature map. Each sliding window is mapped to a lower d feature, which is fed into two sibling fully connected layers - a box regression layer and a box classification layer. The spatial window is suggested to be 3x3. 

At each sliding window location, predict multiple region proposals. Each proposal is a different box with an anchor point at their center (the anchor is in the center of the sliding window). With 3 scales and 3 aspect ratios for a 3x3 window, you have k=9 anchors at each position.

Since they use sliding windows, the anchors are translation invariant.

#### Loss function
They assign a class label (object or not) to each anchor. There is also a positive label for anchors with intersection over union (IoU) of at least .7 with any ground truth box. Ther loss function is a combination of classification and regression, comparing the difference in probability of an anchor being an object and the difference in coordinates of the predicted bounding box and the ground truth box. Regression loss is the smooth L1, and the classification loss is log loss over 2 classes. each term is normalized by Ncls and Nreg, and weighted by a balancing parameter lambda. normalize cls by mini-batch size, and reg by the number of anchor locations. lambda defaults to 10 to roughly equally weight each loss.

The RPN can be trained end-to-end by backprop with SGD.

The rest of the paper discusses benefits to sharing features with cnns to be faster, and goes over implementation details. They also show experiments discussing how good and fast their alg is. It is good and fast.
