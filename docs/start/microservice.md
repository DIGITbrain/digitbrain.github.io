# Microservices in DIGITbrain

## Introduction

Microservices are the smallest building-block in DIGITbrain.
They are containerised applications that provide some required functionality.
Microservices can be composed together to create an Algorithm, which uses
the functionality of potentially multiple Microservices to realise some goal.

## Pre-requisites

Microservices in DIGITbrain must be containerised in an
[OCI-compliant](https://opencontainers.org/) image format.
The most common format for this is
[Docker](https://www.docker.com/resources/what-container)
but other formats are also suitable.

Once built, your container must be pushed to a Container Registry.
[DockerHub](https://docs.docker.com/docker-hub/repos/) offers
free public and paid private repositories, or the DIGITbrain platform
itself offers private repositories on a private registry.
Contact an administrator for access to the DIGITbrain private registry.

## Describing Microservices

For a closer look at the fields available for Microservices, use the following resources:

- [Microservices in Detail](/attributes/microservice) for an itemised listing of fields
- [Microservices Overview](/tables/microservice) for a table-formatted overview
