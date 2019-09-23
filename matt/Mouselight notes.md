# Background

CIS server- 30tb complete mouse brain, open with janelia workstation
Highlight neurons with this software
analyze how long, where they go, fragment files

# Problem selection

random forest to have fragments -> many false positives
proofreader connects fragments - click on them
or other option - proofreader labels fragments from scratch

they say 7, we saw 1-2 with human annotation

we want to know how they got it
how they safelayer fragment, colume
how they work on workstation to manually annotate
they claim 4-5ppl label same vol. at once

Need annotation on Wednesday
Build an algorithm / new pipeline to mine data and apply to whole volume
2-3 kinds of labels 

# Pipeline for out algorithm / automatic neuron identification

0. need to preprocessed data (the data collectors know about it but our lab doesnt understand it yet)
1. from OG volume, how to get fragment (Random Forest ish)
2. given all the fragments, how to connect them (estimate scores/metric/probability that fragments are consecutively in same axon) (Neural Net)
3. Find min spanning tree to ensure morphology looks like a neuron. minimize loss function. given weights, how to connect fragments (Min. Spanning Tree for each neuron - cut it up)

Use novel DL net to approximate score between fragments

3y project; start with toy data set.

Generated fragments by extracting features from voxel and feed to RF

The atlas is the sum of ~25 mouse brains

The project goal is a roadmap not an atlas of every neuron in the brain
- see from region where do neurons go, how do axons project

# Goal is to know how each neuron projects in mouse brain

When registered together don't know which neuron is on top
Very unlikely to fire one neuron into the other

labelling hundreds - thousands of millions of neurons in mouse brain

Right now we have 0 annotated data, hope to get it on Monday. We're not labelling. 
May not get data within 3 months. Should get first annotation within 3 months.
Are we allowed to use data as project is debatable - depends on profs. - Miller, Jenelia (lab that collected data), Jovo

Update 9/20/19: The mouse light data will not be available for the next 3 months. Maybe we can work on it in Sprint 3.