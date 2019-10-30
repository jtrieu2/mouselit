import sys
sys.path.insert(0, '../../../savanna/')

from savanna.utils.dataset import *
from savanna.inference.conv_mf import ConvMF

import torch
import torch.nn as nn
import torch.nn.functional as F


class CustomNet(nn.Module):
    def __init__(self):
        super(CustomNet, self).__init__()
        self.fc1 = nn.Linear(25, 10, 250)
        self.fc2 = nn.Linear(250, 80)
        self.fc3 = nn.Linear(80, 10)

    def forward(self, b):
        b = F.relu(self.fc1(b))
        b = F.relu(self.fc2(b))
        b = self.fc3(b)
        return b







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



MorF = ConvMF(tree_type = "S-RerF", type = 'split_forest', num_trees = 25, num_split_trees = 1)
temp = MorF.fit(train_images, train_labels)
temp = torch.from_numpy(temp)
net = CustomNet()

import torch.optim as optim

criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)

for epoch in range(2):  # loop over the dataset multiple times

    running_loss = 0.0
    for i in range(len(train_images)):
        # get the inputs; data is a list of [inputs, labels]
        #inputs, labels = data

        # zero the parameter gradients
        optimizer.zero_grad()

        # forward + backward + optimize
        outputs = net(temp)
        loss = criterion(outputs, train_labels)
        loss.backward()
        optimizer.step()

        # print statistics
        running_loss += loss.item()
        if i % 2000 == 1999:    # print every 2000 mini-batches
            print('[%d, %5d] loss: %.3f' %
                  (epoch + 1, i + 1, running_loss / 2000))
            running_loss = 0.0

print('Finished Training')



temp = MorF.predict(test_images)


count = 0
for i in range(nsamples):
    output = net(temp[i])
    _, predicted = torch.max(outputs.data, 1)

    if predicted == test_labels[i]:
        count = count + 1

score = count/nsamples
print("MorF Accuracy")
print(score)
