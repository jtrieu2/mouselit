## Mouselight data we have

* mouselight is cropped and organized into octree

* 7 levels in octree; at each node, there are 8 children (except leaf node)

* going down a level each voxel gets cut into 8 

* going down the tree doesn't change voxel size; it changes resolution

* 2 tiffs in each node, corresponding to the two channels

* transform.txt - sx = "size x" in nanometers; xo = "location of first x voxel in nano meters (origin)"

* brain is not perfect cube; some leaves don't have children

* each short fragment is saved in swc format (most likely in um)

  * haven't seen an swc that includes a branch?

* fully reconstructed neurons should also be swc files

  

## ideas for functions

* given fully reconstructed neuron (swc), grab the local subvolumes and visualize the neuron
  * may want to load a section or volume around fragment instead of entire projection neuron

## current functions

* test.py

## TODO

* check how octree organizes the sub-volumes (order of nodes from left to right)
  * i.e. for folders 1 to 8, subtract 1 to get numbers 0 - 7 to get octant
    * if octant 7 in binary in 111, where 0 = low, 1 = high for x y z
  * 7 is coordinate is farthest away from origin
* function to visualize small pieces of an image given a coordinate

* need to "snap" (register) verticies of the fragments to the path of continuous floursecnt signal 