### Intro
Still has learnable weights and biases.
Netowrk has a loss function based on raw image pixels between classes on the last fully connected layer.

### Architecture Overview
Called "deep" when there are many hidden layers.
A regular neural network has layers which are just a set of neurons which function independently.
Regular NNs don't scale well to images. 32x32x3 images would need 3072 weights, which seems manageable, but a 200X200X3 image would have 120k. Lots of parameters as well, being very wasteful (and overfitting).

ConvNets have neurons arranged in 3D. Neurons in a layer will only be connected to a few neurons in the layer before and after them, to conserve spatial relationships.
The finail layer would be of shape 1x1x10, after all the compression metods, which is easily taken by softmax for classification.

### Different Layers
- convolutional layer
- pooling layer
- fully connected layer

The order matters, usually we have nonlinear activation functions operating a the end of a conv layer which get passed to a pooling layer. The fully connected layer is at the end for the sake of classification.

#### Convolutional Layer
Consists of a set of learnable filters. Each filter is small but gets used multiple times. E.g. a 5x5x3 filter gets slid through an image to produce a 2D activation map.
Each filter produces a separate activation map, which are stacked along the "depth" dimension to produce an output volume.
Some neurons/filters don't get passed along the whole image, and have a limited receptive field, affecting the depth.

The output volume is affected by 3 main params - depth, stride, and padding.
Depth is how many filters you are using.
Stride is how the filter gets passed along the image (1 pixel at a time? 2? etc.).
Zero-padding adds 0s to the outside of the input volume to control the width and height of the ouput volume.

example: an image of size 227x227x3. the first conv layer had receptive field size 11, size 4, and no padding. (227-11)/4 + 1 = 55. With 96 filters, the output volume is size 55x55x96. Each neuron is connected to a 11x11x3 region in the input.
This would result in 105,705,600 parameters in the first layer (a lot).
We made one BIG assumption that each slice gets weighted the same across its activations on a single slice (if a filter is useful at one spot in an image it might be useful in another).
Now instead of (11x11x3)x(55x55x96) params we have (11x11x3)x(96) params. Only 34,944 (+96 bias terms). This also allows us to compute the weights of a filter as a convolution over the image.

It is common to relax the parameter sharing scheme in images like faces where spatial location mateers a lot. These layers ware called locally connected.

#### Pooling Layer
People often put pooling layers between conv layers to reduce the spatial size of the representation, and number of parameters (and to control overfitting).
A pooling layer of size 2x2 with a stride of 2 discards 75% of the activations (since 4 values are converted to a single value, their max).
If the receptive field is too large, the pooling layer removes too much signal and performance does down, so F=2,3, S=2 is most comming.

Other than max pooling, other functions can also be done such as average pooling or l2-norm pooling.
A lot of papers don't like pooling and say that we should get rid of them, instaad controlling parameters with a larger stride.

#### Fully Connected Layer
All neurons in a Felly Connected layer have connections to all activations in the previous layer.
Activations can be computed by a matrix multiplication.

Note that the only difference between fully connected layers and convolutional layers is the fact that the filter size is not the entire image. Since dot products are still computed, you can convert between the two.

Any convolutional layer is equivalent to a fully connected layer with mostly zero values except for certain blocks, where weights in many blocks are equal.

### ConvNet architectures
The most common form stacks Conv-Relu layers, then a Pool layer. This is repeated until the image is transformed into a small enough shape. Then, the network transitions to fully connected layers, with the last one holding the output like class scores.

Input -> [[Conv -> Relu]xN -> Pool?]xM -> [FC -> Relu]xK -> FC

Usually 0 <= N <= 3, M >= 0, 0 <= K < 3

There is also some heuristic advice.
Prefer a stack of small filter Conv layers to one large receptive field conv layer. Whenever you stack conv layers on top of each other you must have nonlinearities in between! Insead of using a 7x7 filter, use 3 layers of 3x3 filters to sort through local patterns.

The linear pattern of convolutional layers has been surpassed by more complicated structures, such as Google's inception architectures and Residual Networks from Microsoft Research Asia. Other methods include utilizing dropout layers and batch normalization.
