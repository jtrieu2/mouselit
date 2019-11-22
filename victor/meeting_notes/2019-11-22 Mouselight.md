## 2019-11-22 Mouselight

### Consensus points are sometimes "offset"

* computed signal-to-noise ratio
* assumption: singal-to-noise ratio is best indicator if point is on the neuron
* SNR < 2 means point is offset
* It is not common that consecutive points in a neuron are offset
* Is "tile" shifted? Does this explain why some points are offset?

### Snap points to signal

* move point to highest inensity within 3 voxel radius
* may move point to another neuron if it is close
* helps with seed-based segmentation algorithms because the points are no longer on background

### Next week

* start working on dimensionality reduction
  * image filters from points
  * meeting with Jeremias for feature extraction