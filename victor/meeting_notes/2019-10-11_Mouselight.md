  ## 3 Month milestones

* logistics
  * workstation software, collect annotations
  * where to host data/how to compute
* image processing

## Visualization

* Make neuroglancer work on mouselight data
  * put data on Amazon S3 for visualization purposes
  * tif files do not work, need to be in other format
  * standardized coordinates
    * z (anterior/posterior) 208
    * x (left/right) 528
    * y (inferior/superior) 400

## Segmentation Function

* normalize entire image first via whittening before converting swc to binary image

## TODO

* convert from swc to binary image
  * given a fragment, isolate a bounding box with some padding around the fragment in the subvolume
  * might need to do some manual segmentation on some neuron fragments to get ground truth
* data normalization on entire image (whitening)
  * Tommy is looking at Jeremiah's normalization resources