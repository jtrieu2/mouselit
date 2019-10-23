## Mouselight data we have

* mouselight is cropped and organized into octree
* 7 levels in octree; each node has 8 children 
  * going down a level each voxel gets cut into 8 smaller voxels (spacing/2)
  * going down the tree doesn't change voxel size; it changes resolution
* 2 tiffs in each node, corresponding to the two channels
* transform.txt:
  * sx = "size x in nanometers"
  * xo = "location of first x voxel in nano meters (origin)"
* brain is not perfect cube; some nodes don't have children
* each short fragment is saved in swc format (most likely in mircons)
* fully reconstructed neurons should also be swc files

## ideas for functions

* given fully reconstructed neuron (swc), grab the local subvolumes and visualize the neuron
  * may want to load a section or volume around fragment instead of entire projection neuron

## current functions

* as of 2019-10-04: located in test.py and most work

## tasks for near future

* check how octree organizes the sub-volumes (order of nodes from left to right)
  * i.e. for folders 1 to 8, subtract 1 to get numbers 0 - 7 to get octant
    * if octant 7 in binary in 111, where 0 = low, 1 = high for x y z
  * 7 is coordinate is farthest away from origin
* function to visualize small pieces of an image given a coordinate

* need to "snap" (register) verticies of the fragments to the path of continuous floursecnt signal 
  * worried that not all vertices of fragments actually overlap with the neuron its suppoed to annotate