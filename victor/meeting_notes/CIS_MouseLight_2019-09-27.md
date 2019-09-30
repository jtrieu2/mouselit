# CIS MouseLight Meeting 9/27/2019

* Goal: Make cell level atlas to answer questions like where do the neurons in this region project to

## Janelia Workstation Software
* operational on computers with 20GB+ of RAM
* windows version is maintained the most by Janelia
* Linux version may not be supported if we run into issues
* MacOS version does not work
* image format is tiff
* possible open source alternative to Workstation Software

Computers
  * CLark 318A - Windows
  * Daniel - Linux
  * Kwame - Linux

## We have ~250k fragments
* automatically generate fragments and then connect them manually
* sparsely labeled but still looks as dense as typical images
* see how to evaluate the automatically generated fragments
* are detected fragments lining up with the image?
  * yes but there is a lot of signal that is not being labeled
  * many false negatives, not many false positives

## We also have ~180 "Consensus" neurons
* two annotators connected fragments into neurons
* closest to ground truth to labeling of neurons
* ~180 neurons appears to cover the entirety of the brain

## Data we propose to get
* ~5 more (image, fragments, consensus neurons)
* Anthony: existing servers could hold 1 or 2 more
  * would take several weeks to open up space
  * then 1 week to upload
* or buy 100/200 TB server

## Software development
* Be neat when writing code (file organization and commenting style should be top quality)
* Start with basic data retrieval functions?
  * Done: parse **swc files** for fragments (pretty small)
  * Done: parse parameters of **octree**
  * Tommy has private repo with these functions
  * TODO: retrieve 3D rectangle around specified coordinate (Tommy is working on)

## Computational Timeline (logistics and training sets)
(insert image of timeline)

## Computational Timeline (traversal weight and connections)
(insert image of timeline)
