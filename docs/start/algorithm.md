# Algorithms in DIGITbrain

## Introduction

In DIGITbrain an Algorithm is handled as a preconfigured black box
software (SW) component, providing only a description of its capabilities.
The DIGITbrain approach enables users with low experience to easily make
use of complex algorithms by simply providing the required inputs
(i.e., data, model).

An Algorithm bundles one or more [Microservice(s)](microservice.md), that (together)
enable the evaluation of a [Model](model.md) on [Data](data.md).
Within DIGITbrain, Algorithm shall be agnostic to IP instances (e.g. their application
field or the context in which a model is being used). This context will be established
later, when pairing the algorithm with a adequat [Model](model.md) as an [MA-Pair](ma_pair.md),
and further when providing [Data](data.md) to form the [DMA-Tuple](../dma_tuple).
The different Microservices within an Algorithm may be deployed on different resources
(e.g. edge, cloud, HPC) depending on the individual mechanism of the Algorithm, and the
needs of the Model.

## Pre-requisites

To integrate an Algorithm within the DIGITbrain Solution, the following steps need to be performed:

- **Authoring:** preparation and pre-configuration of Microservices using Authoring Tools.
- **Packaging:** the authored Microservice is packaged following the Asset guidelines of the DIGITbrain Solution (i.e., Docker containers).
- **Publishing:** definition and provision of metadata description for Microservices together with their publication in the DIGITbrain Asset Metadata Registry. Additionally, the different Microservices need to be linked to an Algorithm, defining its metadata, and publishing it as a new Algorithm Asset to the DIGITbrain Asset Metadata Registry using the respective Publishing Interface.

## Metadata describing Algorithms

For a closer look at this metadata, use the following resources:

- [Attribute Listing](/attributes/algorithm) for an itemised listing of fields
- [Metadata Table](/tables/algorithm) for a table-formatted overview
- Feel free to extend this list as desired

## Further reading...

This space is for any other required documentation on this asset.
