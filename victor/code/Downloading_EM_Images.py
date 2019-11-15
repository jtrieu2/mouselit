from cloudvolume import CloudVolume, view

# 1. Initialize a CloudVolume object which will know how to read from this dataset layer. 
cv = CloudVolume(
   'https://storage.googleapis.com/neuroglancer-public-data/kasthuri2011/image_color_corrected', 
    progress=True, # shows progress bar
    cache=True, # cache to disk to avoid repeated downloads
    # parallel=True, # uncomment to try parallel download!
)

# 2. Download context around the point in the Neuroglancer link above
#    into a numpy array.
# argument one is the (x,y,z) coordinate from neuroglancer
# mip=resolution level (smaller mips are higher resolution, highest is 0)
# size is in voxels
img = cv.download_point( (5188, 9096, 1198), mip=0, size=(512, 512, 64) )

# 3. Visualize the image! 
# Open your browser to https://localhost:8080 to view
# Press ctrl-C to continue script execution.
view(img)

# 4. When you're done experimenting, clean up the space we used on disk.
cv.cache.flush() 