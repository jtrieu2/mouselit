# get_coord_params(path):
    Arguments:
    path {string} -- path to highest level of octree
        E.g.  string = '/cis/net/io50/data/janelia-data/2018-08-01'
        highest level meaning the least resolution / most blurry

    Returns:
    origin {3-array} -- spatial location of origin in microns
        E.g. origin in spatial coords: [70093.0986804  15071.32671574 29306.18294772]
    size {3-array} -- voxel dimensions at finest level  # ??This concept is a little misleading, as it is not describing voxel spacing, nor the finest(most) dimension represented by 1 top level voxel, but simply the total dimension at finest level. Normally voxel should refer to 1 single voxel, not all voxels' total dimensions??
        E.g. voxel dimensions at finest level: [33792 25600 13312]
    spacing {3-array} -- spacing at finest resolution level in microns
        E.g. spacing at finest level in um (Actual spacing): [0.29875923 0.3044159  0.98840415]
    nl {int} -- number of levels in octree
        E.g. number of levels of octree: 7
### From transform.txt on the top level:
    # ox to sz are in unit nm
    ox: 70093276
    oy: 15071596
    oz: 29306737
    sx: 19120.59090909091
    sy: 19482.6175
    sz: 63257.86538461538
    nl: 7
###  Calculate 3rd RETURN VALUE spacing:
    Intermediate variable:
    values = [70093.276, 15071.596, 29306737, 19.12059, 19.4826175, 63.2578653, 7]  # Convert nm to um
    top_spacing = [19.12059, 19.4826175, 63.25786]  # In unit (um)
    num_voxels = 2 ^ (nl - 7)  # 2^(7-1)
    spacing = top_spacing / num_voxels # RETURN [0.29875923 0.3044159, 0.98840415]
###  Calculate 1st RETURN VALUE origin:
    Intermediate variable:
    origin = [70093.276, 15071.596, 29306.737]
    # The following modification is according to an email from Adam Taylor on 9/18/19
    # This origin shift is important when we decode the spatial locations of swc files
    # ??WHY??
    origin = spacing * floor(origin/spacing)
           = spacing * [234614.595, 49509.884, 29650.560]
           = [70093.0986804  15071.32671574 29306.18294772]  # RETURN
###  Calculate 2nd RETURN VALUE size (RETURN SIZE IS THE REVERSE OF IMG.SHAPE?):
    Intermediate variables:
    img_path = parent_path / 'default.0.tif'
    im = io.imread(str(img_path))
    dims = im.shape  # [208, 400, 528] ==> 208 Layers of scan of size 528*400
    size = np.array([dims[2],dims[1],dims[0]]) * 2^(7-1)
    size = size.astype(int)  
    # [33792 25600 13312] ==> 1st(33792) left to right
                              2nd(25600) superior to inferior
                              3rd(13312) anterior to posterior
    # Actual image shape**************************
    [528, 400, 208]


# space_to_vocel(spatial_coord, origin, spacing):
    Convert spatial location to voxel coordinates
    Arguments:
        spatial_coord {3-array} -- spatial coordinates in microns
            E.g. origin in spatial coords: [70093.0986804  15071.32671574 29306.18294772]
        origin {3-array} -- spatial coordinates of origin in microns
            E.g. origin in spatial coords: [70093.0986804  15071.32671574 29306.18294772]
        spacing {3-array} -- size of each voxel in microns
            E.g. spacing at finest level in um (Actual spacing): [0.29875923 0.3044159  0.98840415]
    Returns:
        voxel_coord {3-array of ints} -- voxel coordinate
            E.g. Test convert spatial to voxel coordinates [0 0 0]
###  Calculate RETURN VALUE voxel_coord:
    Intermediate variables:
    voxel_coord
    = np.round(np.divide(spatial_coord - origin, spacing))
    = round( ( [70093.0986804, 15071.32671574, 29306.18294772] - [70093.0986804, 15071.32671574, 29306.18294772] ) / 
             [0.29875923 0.3044159  0.98840415]
           )


# voxel_path(vox, tree_specifics):
    output the image path that contains the voxel and its coordinate in that file
    Arguments:
        vox {3-array of ints} -- voxel coordinates [0, sz-1]  # ??Rather [[0,0,0], sz-1], probably need exception??
            E.g. [5808, 5600, 2496]
        tree_specifics {list} -- path {string}, sz {3 array}, nl {int}, channel {0 or 1}
            Again, sz - voxel dimensions at finest level
            E.g. tree_specifics
                 = [parent_dir, sz, nl, 0]
                 = ['/cis/net/io50/data/janelia-data/2018-08-01', [33792 25600 13312], 7, 0]
    Returns:
        img_path -- path to the image that stores that voxel
            E.g. /cis/net/io50/data/janelia-data/2018-08-01/1/1/8/7/4/2/default.0.tif
        vox_cur -- coordinate of the voxel in that image
            E.g. [0 0 0]
    
###  Calculate RETURN VALUE img_path and vox_cur:
    Intermediate variables:
    path, sz, nl, channel = tree_specifics  # ['/cis/net/io50/data/janelia-data/2018-08-01', [33792 25600 13312], 7, 0]
    path_cur = Path(path)  # Path('/cis/net/io50/data/janelia-data/2018-08-01')
    sz_cur = sz  # sz_cur = [33792 25600 13312]
    vox_cur = vox  # vox_cur = [5808, 5600, 2496]
    for l in range(0, nl-1):  # 0, 1, 2, 3, 4, 5
        sz_cur = np.divide(sz_cur,2).astype(int)  # 1st iter: [16896, 12800, 6656]
        split = np.greater(vox_cur,sz_cur-1)  # 1st iter: [5808, 5600, 2496] > [16896-1, 12800-1, 6656-1] == False
        leaf = np.dot(split,np.array([1,2,4])) + 1  # 1st iter: np.dot([0, 0, 0], [1, 2, 4]) + 1
        path_cur = path_cur /  str(leaf)  # 1st iter: path_cur = path_cur/1
        vox_cur = vox_cur - np.multiply(sz_cur,split)  # 1st iter: [5808, 5600, 2496] - [16896, 12800, 6656]*[0, 0, 0]
    file =  'default.' + str(channel) + '.tif'
    img_path = path_cur / file

    return img_path, vox_cur
    
# get_intrarectangle_voxel(start,end, tree_specifics):
    Get a subvolume of image that is contained within a single tif image
    Arguments:
        start {3 array of ints} -- lower corner of rectangle
            E.g. [5807,5599,2495]
        end {3 array of ints} -- upper corner of rectangle (to be included)
            E.g. [5808,5600,2496]
        tree_specifics {list} -- path {string}, sz {3 array}, nl {int}, channel {0 or 1}
            E.g. tree_specifics
                 = [parent_dir, sz, nl, 0]
                 = ['/cis/net/io50/data/janelia-data/2018-08-01', [33792 25600 13312], 7, 0]
    
    ??Returns:
        volume {3 Dimensions array}
            E.g. [[[nan nan]
                  [nan  0.]]

                 [[nan nan]
                  [nan  0.]]]
    
###  Calculate RETURN VALUE volume:
    start_path, start_coord = voxel_path(start, tree_specifics)
        # start_path = /cis/net/io50/data/janelia-data/2018-08-01/1/1/8/3/6/7/default.0.tif
        # start_coord = [0 0 0]
    end_path, end_coord = voxel_path(end, tree_specifics)  
        # end_path = /cis/net/io50/data/janelia-data/2018-08-01/1/1/8/7/4/2/default.0.tif
        # end_coord = [0 0 0]
    end_coord = end_coord + 1  # end_coord = [1 1 1]

    if start_path != end_path:
         raise ValueError('Call to get_intrarectangle_voxel for coordinates that are in different files')
    try:
        im = io.imread(str(start_path))
        volume = im[start_coord[2]:end_coord[2],start_coord[1]:end_coord[1],start_coord[0]:end_coord[0]]
        volume = np.swapaxes(volume,0,2)
    except FileNotFoundError:
        volume = np.nan*np.zeros(end_coord - start_coord)
    return volume
