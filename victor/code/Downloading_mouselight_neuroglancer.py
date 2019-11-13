from cloudvolume import CloudVolume, view

# 1. Initialize a CloudVolume object which will know how to read from this dataset layer.
cv = CloudVolume(
    's3://https://d2zu5izn76slwn.cloudfront.net/precomputed_volumes/brain1',
    progress=True, # shows progress bar
    cache=True, # cache to disk to avoid repeated downloads
    # parallel=True, # uncomment to try parallel download!
)

# 2. Download context around the point in the Neuroglancer link above
#    into a numpy array.
# argument one is the (x,y,z) coordinate from neuroglancer
# mip=resolution level (smaller mips are higher resolution, highest is 0)
# size is in voxels
img = cv.download_point( (2054, 1227, 1131), mip=1, size=(500,500,500) )

# 3. Visualize the image!
# Open your browser to https://localhost:8080 to view
# Press ctrl-C to continue script execution.
view(img)

# 4. When you're done experimenting, clean up the space we used on disk.
cv.cache.flush()
