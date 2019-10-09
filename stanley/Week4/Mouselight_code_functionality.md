# From src/image_getters.py

## Feature-based volume stitching

- Match descriptors between adjacent tiles in both x, y, and z directions. 

def stitch_images(segments, tree_specifics):

    """Stitch together image subvolumes
    
    Arguments:
        segments {3 list} -- segment locations as outputted by divide_voxel_bounds()
        tree_specifics {list} -- path {string}, sz {3 array}, nl {int}, channel {0 or 1}
    
    Returns:
        volume -- image subvolume
    """
which calls get_intrarectangle_voxel()

def get_intrarectangle_voxel(start,end, tree_specifics):

    """Get a subvolume of image that is contained within a single tif image
    
    Arguments:
        start {3 array of ints} -- lower corner of rectangle
        end {3 array of ints} -- upper corner of rectangle (to be included)
        tree_specifics {list} -- path {string}, sz {3 array}, nl {int}, channel {0 or 1}
    """

- Map voxel locations to a target coordinate space while preserving the spatial ordering. 

def space_to_voxel(spatial_coord, origin, spacing):

    """Convert spatial location to voxel coordinates
    
    Arguments:
        spatial_coord {3-array} -- spatial coordinates in microns
        origin {3-array} -- spatial coordinates of origin in microns
        spacing {3-array} -- size of each voxel in microns
    Returns:
        voxel_coord {3-array of ints} -- voxel coordinate
    """

## 3D visualization and reconstruction

- Back-projecting each voxel in each output tile to the nearest sampled voxel. In regions where two or more input tiles overlapped, the maximum intensity was used for the corresponding location in the output tile. 

def divide_voxel_bounds(start, end, tree_specifics):

    """If the corner coordinates of the desired subvolume span multiple tifs, then this function splits
    each dimension at the limits of the tifs
    
    Arguments:
        start {3-array of ints} -- start corner of rectangle
        end {3-array of ints} -- end corner of rectangle
        tree_specifics {list} -- path {string}, sz {3 array}, nl {int}, channel {0 or 1}
    Returns:
        segments {3-array} -- each element is a list of segments along the axis that lines up with the borders of the tif volumes
    """

- Data were resampled to 0.25x0.25x3x1 um voxels, and stored on disk along with downsampled octree representations of the same volume for visualization at different spatial scales.

Not sure
