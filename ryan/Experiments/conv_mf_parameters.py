import sys
sys.path.insert(0, '../../../savanna/')

from savanna.utils.dataset import *
from savanna.inference.conv_mf import ConvMF
import matplotlib
import matplotlib.pyplot as plt

numpy_data = dict()
(numpy_data["train_images"], numpy_data["train_labels"]), (
    numpy_data["test_images"],
    numpy_data["test_labels"],
) = get_dataset("./FashionMNIST", "FashionMNIST", is_numpy=True)
#trainset, testset = get_dataset("../savanna/data", "FashionMNIST", is_numpy=True)

trainset, testset = get_subset_data(
                        dataset_name = "FashionMNIST",
                        data=numpy_data,
                        choosen_classes= np.arange(10),
                        sub_train_indices = np.arange(10000)
                        )
train_images = trainset[0]
train_labels = trainset[1]
test_images = testset[0]
test_labels = testset[1]

nsamples = 10000


#kernel_patch
"""
sizes = [5, 7, 9, 11, 13, 15, 17, 19, 21]
accuracy = []

for i in sizes:
    MorF_Conv = ConvMF(type = "kernel_patches", tree_type = "S-RerF", num_trees = 10, kernel_size = i)
    MorF_Conv.fit(train_images, train_labels)
    results = MorF_Conv.final_predict(test_images)
    count = 0
    for i in range(len(results)):
        if results[i] == testset[1][i]:
            count += 1
    score = count/nsamples
    accuracy.append(score)

plt.plot(sizes, accuracy)
plt.title("Kernel Size vs. Accuracy")
plt.xlabel("Kernel Size")
plt.ylabel("Accuracy")
plt.show()
"""


sizes = [3, 4, 5, 6, 7, 8, 9]
accuracy = []

for i in sizes:
    MorF_Conv = ConvMF(type = "kernel_patches", tree_type = "S-RerF", num_trees = 10, kernel_size = 9, patch_height_max = i, patch_width_max = i)
    MorF_Conv.fit(train_images, train_labels)
    results = MorF_Conv.final_predict(test_images)
    count = 0
    for i in range(len(results)):
        if results[i] == testset[1][i]:
            count += 1
    score = count/nsamples
    accuracy.append(score)

plt.plot(sizes, accuracy)
plt.title("Max Patch Size vs. Accuracy")
plt.xlabel("Max Patch Size")
plt.ylabel("Accuracy")
plt.show()
