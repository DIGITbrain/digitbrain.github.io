# Algorithms in DIGITbrain

## Introduction

An Algorithm bundles one or more [Microservice(s)](microservices.md), that (toghether) enable the evaluation of a [Model](model.md) on [Data](data.md).
Within DIGITbrain, Algorithm shall be agnostic to IP instances (e.g. their application field or the context in which a model is being used). This context will be established later, when pairing the algorithm with a adequat [Model](model.md) as an [MA-Pair](ma_pair.md), and further when providing [Data](data.md) to form the [DMA-Tuple](dma_tuple.md).
The different Microservices within an Algorithm may be deployed on different resources (e.g. edge, cloud, HPC) depending on the individual mechanism of the Algorithm, and the needs of the Model.

## Pre-requisites

To construct an algorithm the required [Microservices](microservices.md) need to be registered with DIGITbrain.

## Metadata describing Algorithms

For a closer look at this metadata, use the following resources:

- [Attribute Listing](attributes/algorithm.md) for an itemised listing of fields
- [Metadata Table](tables/algorithm.md) for a table-formatted overview
- Feel free to extend this list as desired

## Further reading...

This space is for any other required documentation on this asset.
