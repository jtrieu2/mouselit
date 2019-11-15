## 2019-11-08 Mouselight

* Convert ground truth points to masks
  * 1) threshold at min intenisty of points
  * 2) create thick skeleton from points
  * find intersection of 1) and 2
  * closing operation
* works ok sometimes
* Problem 1: threshold too low
  * point is not actually on neuron so the min intensity becomes the background intensity
  * will address by computing threshold from small sphere around the point
* Problem 2: too many axons close together
* Problem 3: low signal/noise ratio
* suggestions: look at ~30 degrees in direction of moving from one point to point instead of growing in 360 degrees
* statistics on neuron 1 to explain problems
  * percentile of dimmest point: majority are > 95th percentile
* To-do (Tommy)
  * improve sw2pixel
    * smoothing
    * directional closing
  * local signal to noise ratio along with axon



## swc2stat

* Natverse: http://natverse.org/gallery/
  * look for possible features/metrics that are useful
  * check in with Solange's group for tools that are useful for quality control on traces