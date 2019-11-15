from cloudvolume import CloudVolume, view 

cv = CloudVolume(
    'https://storage.googleapis.com/neuroglancer-public-data/kasthuri2011/ground_truth',
    progress=True, # shows progress bar
    cache=True, # cache to disk to avoid repeated downloads
    # parallel=True, # uncomment to try parallel download!
)

img = cv.download_point( (5188, 9096, 1198), mip=0, size=(512, 512, 64) )

# segmentation=True activates the segmentation mode
# of the microviewer. If it was False, it would display
# as a raw image, which might be very dark if the label
# values are small.
view(img, segmentation=True)

# Get as mesh object
mesh = cv.mesh.get(13)
# Save to disk at ./13.obj which can be visualized in MeshLab or Blender
cv.mesh.save(13, file_format='obj')

cv.cache.flush()
