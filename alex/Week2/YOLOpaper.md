# YOLO Paper Summary: You Only Look Once

## Abstract + Intro
* As opposed to current object detection like R-CNN, YOLO does not use many classifiers to perform detection but reframes it as a single regression problem,
* With YOLO, single CNN predicts bounding boxes and object probabilities, resulting in fast and precise identification of images
* YOLO learns generalizable representations of objects and is then more robust to changes in domain or unexpected input
* Does lag behind state of the art systems in accuracy as it struggles to precisly localize small objects
* Totally open source!
## Methods - Unified Detection
* Image is divided into SxS grid, if an object is in the center of a cell, the cell should detect the object.
* Cell predicts bounding boxes and confidence for the boxes, and the conditional class probabilities.
* In the end, we get class probabilities for each box and how well the box fits the object
### Network Design
* Uses 24 convolutional layers and 2 fully connected layers
* Trained on imagenet using Darknet framework
* Bounding box width and height normalized by dividing by image width and height
* Leaky ReLU used for all besides final activation layer, where linear activation function is used
* Optimize for sum-squared error, but weight loss from confidence predictions for no objects lower than loss from Bounding box coordinate predictions
* Since YOLO predicts multiple boxes per grid cell, assign one predictor to predict based on the highest IOU (intersection over union) with the ground. This way, predictors get specialized and better at predicting certain sizes, aspect ratios, or classes.
## Limitations
* Strong spatial constraints mean that model struggles with many nearby, or small objects
* Struggles to generalize across aspect ratios
* Error weighted the same in loss function for small and large boxes, where small box error has a much greater impact on IOU

## Experiments
* In real time detection, YOLO outperforms only other algorithm they compare to (DPM)
* Results in worse localization performance than Fast R-CNN but much fewer background errors
