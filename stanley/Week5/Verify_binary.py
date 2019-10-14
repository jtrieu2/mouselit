from skimage import io
from skimage.viewer import ImageViewer

if __name__ == '__main__':
    print(1)
    img = io.imread('/Users/apple/Desktop/2018-08-01/default.1.tif')
    print(img.shape)

    img1 = io.imread('/Users/apple/Desktop/2018-08-01/2/default.1_2.tif')
    slice = img[0]
    slice1 = img1[0]
    viewer = ImageViewer(slice)
    viewer1 = ImageViewer(slice1)
    viewer.show()
    viewer1.show()
