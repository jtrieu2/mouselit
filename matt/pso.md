# Random Forest with Learned Representations for Semantic Segmentation
2019 Byeongkeun Kang and Truong Q. Nguyen, Fellow, IEEE
https://arxiv.org/pdf/1901.07828.pdf

## Abstract

Random forest frameework that learns weights, shapes, sparsities of feature representation in semantic segmentation
Typically, kernels have predetermined shape and sparsities so learn weights only
This unconstrained representation can learn the other things,  too
Demonstrated on hand segmentation data
Uses limited computational and memory resources for real-time semantic seg.

## Intro

Semeantic seg used for autonomous driving, robot navigation, human-machnine interaction
DL representations work well since they learn fine representations along with hieracrchiical structure and nonlinear activations
RFs and DNNs outperform most other methods
RFs more computational and memory efficient; DL higher acc.

## Proposed Method

In addition to bootstrapping and boosting,

1. Particle swarm optimization to learn splitting functions - learns weights, shapes, sparsities
2. Modifieed bilateral filter

## Experiments
30 v 60% accuracy, but 1992 instead of 58870 ms response time for proposed method v. OCNet
