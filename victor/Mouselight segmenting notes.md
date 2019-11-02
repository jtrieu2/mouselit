## Mouselight segmenting notes Nov. 2, 2019

[Spreadsheet keeping track of segmentation/annotation assignments](https://docs.google.com/spreadsheets/d/1bBpkcPXJaSh-qM9lJBJaXxclr6nMl43UpcVb8wGdydE/edit#gid=0)

[Level 7 octant images download link](https://my.pcloud.com/publink/show?code=kZID38kZxiYEOmuqIXjXzc1XG5syD7gYvPF7)

• The mouselight data is organized into an octree
octree diagram: [https://en.wikipedia.org/wiki/Octree#/media/File:Octree2.svg](https://slack-redir.net/link?url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FOctree%23%2Fmedia%2FFile%3AOctree2.svg)
• At each node the .tif image is called an octant
• Root (level 1) of octree contains the octant showing the entire mouselight, but is an image at the lowest resolution. Root has up to 8 level 2 child octants. Each Level 2 octant has double the resolution of previous level 1. Each level 2 octant has up to 8 level 3 child octant. Each level 3 octant has double the resolution of previous level 2. Each level 3 octant has up to 8 level 4 child octant...
• We are interested in octants are highest resolution, which are at the lowest level (level 7)
• Therefore, all of the .tif images we are segmenting are level 7 octants
• On the CIS computers, the mouselight data octree is implemented as a file directory
e.g. If the path from root to a level 7 octant is
lvl 1: root (path to root is cis/net/io50/data/janelia-data/2018-08-01/)
lvl 2: 1
lvl 3: 6
lvl 4: 8
lvl 5: 3
lvl 6: 8
lvl 7: 1the the path to the level 7 octant is
/cis/net/io50/data/janelia-data/2018-08-01/ **1/6/8/3/8/1/default.0.tif**
• Neurons are stored in swc files as a collection of points and straight lines in 3D space. Each swc file may span multiple level 7 octants
• We currently don't have a function to plot all the neurons that overlap a given level 7 octant. Therefore, you will have to segment by eyeballing anything that looks like a neuron.