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

## Metadata describing Microservices

For a closer look at this metadata, use the following resources:

- [Attribute Listing](/attributes/microservice) for an itemised listing of fields
- [Metadata Table](/tables/microservice) for a table-formatted overview
- Feel free to extend this list as desired

## Further reading...

This section takes an in-depth look at some of the more complex fields
required to describe this asset:

`deploymentData`

:   **Required** (*JSON*) <br>DIGITbrain supports Microservices in containers. The platform aims
to support any OCI-compliant container images, as mentioned above in the pre-requisites
section. Containers are generally described in a variety of formats and the platform
aims to support the most common kinds.<br>
We currently support the description of **one container** in either the *Docker-Compose*
format or **one Pod** in the *Kubernetes manifest* format. If you normally run your
container with *docker run* we suggest using the online, open-source
[Composerize](https://www.composerize.com/) tool, which can translate the command to a
Docker-Compose file. We require the *Docker-Compose* or *Kubernetes manifest* in JSON
format, so please use any YAML to JSON coverter - there are many
[online](https://www.google.com/search?q=yaml+to+json+online) to do so.

    === "Docker-Compose"

        ``` json
        {
          "services": {
            "reverseproxy": {
            "image": "nginx:latest",
            "ports": [
              "8080:8080"
            ],
            "restart": "always"
            }
          }
        }
        ```

    === "Kubernetes manifest"

        ``` json
        {
          "apiVersion": "v1",
          "kind": "Pod",
          "metadata": {
            "name": "reverseproxy"
          },
          "spec": {
            "containers": [
              {
                "name": "reverseproxy",
                "image": "nginx:latest",
                "ports": [
                  {
                    "containerPort": 8080
                  }
                ]
              }
            ]
          }
        }
        ```
