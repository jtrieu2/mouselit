Residual and Plain Convolutional Neural Networks for 3D Brain MRI Classification
Korolev, Safiullin, Belyaev, and Dodonova

Introduction
- develop a deep learning based algo. to simplify MRI classification pipeline
- neuroimaging datasets are very small; try to overcome with oversampling, but still in general need network architecture that can learn fro small datasets
- in the paper, propose 2 different 3D conv. network architectures
- networks can generalize local features, using batch normalization technique and residual network archi. to compensate for small training dataset
- tested on Alzheimer's Disease Neuroimaging Initiative, tries to classify stage of dementia

Method
- first architecture is common feedforward network with conv. and pooling layers
- VoxCNN, similar to VGG
- second is modern residual neural network
- derived from ResNet
- 5 fold corss-validations

Results 
- both networks show simliar results, and are comparable to previous results
- authors claim their pipeline is eaier to use and does not need handcrated features