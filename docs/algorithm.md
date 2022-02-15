# Algorithms in DIGITbrain

## Introduction

In DIGITbrain an Algorithm is handled as a preconfigured black box
software (SW) component, providing only a description of its capabilities.
The DIGITbrain approach enables users with low experience to easily make
use of complex algorithms by simply providing the required inputs
(i.e., data, model).

An Algorithm is a set of one or multiple [Microservices](microservice.md),
bundling the required tools to evaluate a Model with the associated Data.

## Pre-requisites

To integrate an Algorithm within the DIGITbrain Solution, the following steps need to be performed:

- **Authoring:** preparation and pre-configuration of Microservices using Authoring Tools.
- **Packaging:** the authored Microservice is packaged following the Asset guidelines of the DIGITbrain Solution (i.e., Docker containers).
- **Publishing:** definition and provision of metadata description for Microservices together with their publication in the DIGITbrain Asset Metadata Registry. Additionally, the different Microservices need to be linked to an Algorithm, defining its metadata, and publishing it as a new Algorithm Asset to the DIGITbrain Asset Metadata Registry using the respective Publishing Interface.

## Metadata describing Algorithms

For a closer look at this metadata, use the following resources:

- [Attribute Listing](attributes/algorithm.md) for an itemised listing of fields
- [Metadata Table](tables/algorithm.md) for a table-formatted overview
- Feel free to extend this list as desired

## Further reading...

This space is for any other required documentation on this asset.