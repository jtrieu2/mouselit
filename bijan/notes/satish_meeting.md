CNNs win with $n>1000$, but before that point deef conv rf does better.

a typical CNN filter is learned through backpropagation

instead, we take the "window" the kernel is looking at and store that part of the image.
A 3x3 kernel would result in a 1x9 observation vector.

We stack all these patches aligned across images (let's say 10000 images) to get a
10000 x 9 data matrix $X$. We can directly feed this into the random(er) forest to
get posterior probabilities of classes, a 10000 x 1 label vector.
Going through the entire image like this is a single "layer", and would reduce
the dimension of the image by a factor of the kernel size * stride.

doing this for multiple layers, with a different forest for each layer, is what we have now.
it works for 2 class classification for 2d images.

it can be run on 3d volumes by flattening the volume into a vector, but performance does
not improve layer by layer as in the 2d case (?). Unsure why this is the case.

performance of the alg might be improved by adding more DL tools like nonlinear activations like ReLU
or by adding in pooling layers.

"shared" vs "unshared" forests depend on whether the forests are trained on different patches or all on the same patch
. it looks like shared outperforms unshared at the moment

the final layer stretches an image out and then feeds it into the forest to get a score.

Adding localization ability might work if you utilize region proposal networks (VGG, YOLOv3)
