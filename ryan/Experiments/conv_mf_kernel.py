import sys
sys.path.insert(0, '../../../savanna/')

from savanna.utils.dataset import *
from savanna.inference.conv_mf import ConvMF


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
                        sub_train_indices = np.arange(59999)
                        )
train_images = trainset[0]
train_labels = trainset[1]
test_images = testset[0]
test_labels = testset[1]

nsamples = 10000

#(train_images, train_labels), (test_images, test_labels) = get_dataset("./FashionMNIST", dataset_name = "FashionMNIST")

#RerF
RerF = ConvMF(tree_type = "RerF", num_trees = 500)
RerF.fit(train_images, train_labels)
results = RerF.final_predict(test_images)
count = 0
for i in range(len(results)):
    if results[i] == testset[1][i]:
        count += 1
score = count/nsamples
print("RerF Accuracy")
print(score)

#RerF Convolve
RerF_Conv = ConvMF(type = "kernel_patches", tree_type = "RerF", num_trees = 10)
RerF_Conv.fit(train_images, train_labels)
results = RerF_Conv.final_predict(test_images)
count = 0
for i in range(len(results)):
    if results[i] == testset[1][i]:
        count += 1
score = count/nsamples
print("RerF Conv Accuracy")
print(score)

#MorF
MorF = ConvMF(tree_type = "S-RerF", num_trees = 500)
MorF.fit(train_images, train_labels)
results = MorF.final_predict(test_images)
count = 0
for i in range(len(results)):
    if results[i] == testset[1][i]:
        count += 1
score = count/nsamples
print("MorF Accuracy")
print(score)


#RerF Convolve
MorF_Conv = ConvMF(type = "kernel_patches", tree_type = "S-RerF", num_trees = 10)
MorF_Conv.fit(train_images, train_labels)
results = MorF_Conv.final_predict(test_images)
count = 0
for i in range(len(results)):
    if results[i] == testset[1][i]:
        count += 1
score = count/nsamples
print("MorF Conv Accuracy")
print(score)
