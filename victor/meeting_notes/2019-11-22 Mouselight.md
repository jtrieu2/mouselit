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

### Mouselit

* Visualization: need to be able to travel down the axon
  * have camera be on the axon
  * EyeWire
* 3D lcoal histogram equalization + thresholding + small object removal
  * good: amplifies dim signal
  * bad: results in very thick neurons
  * Give Tommy just the local hisogram equalization

* morphology on neurons
  * dendrites are supposed to be thicker than axons
  * develop a pipeline to manually label vertices as axons, soma, etc.



### Generating fragments

* dynamic programming algorithm to connect fragments and nodes
* restrict ourselves to close connections to optimally connect fragments