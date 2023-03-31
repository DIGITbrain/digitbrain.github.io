# Deployments in DIGITbrain

## Introduction

A deployment in DIGITbrain specifies the infrastructure that a desired DMA
Tuple will be deployed across. Here it is necessary to provide details on the
type of infrastructure that this deployment will define, along with all the
configuration details required by that infrastructure type.

## Pre-requisites

For most Processes in DIGITbrain, a common set of Deployments will be suitable.
Required IDs that describe that common set are available in the documentation
that follows below.

For some workloads with very specific hardware or software requirements, or
for those who require direct access to underlying virtual machines, it may
be necessary to raise a ticket with the administrator of your CloudBroker Platform.

Where bring-your-own edges are used, DIGITbrain currently supports the following

- ARM or x86 Architectures
- Common Linux Distributions
- Minimum 1 CPU, 1GB RAM and 5GB free disk space

## Describing Deployments

For a closer look at the fields available for Deployments, use the following resources:

- [Deployments in Detail](/attributes/deployment) for an itemised listing of fields
