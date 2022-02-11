<style>
  .md-content__button {
    display: none;
  }
</style>
# Algorithm Fields

**This information is also available in [table format](/tables/algorithm/)**


## Available Fields 

The metadata specification for a DIGITbrain Algorithm
has these sections:

- [Description](#description)
- [Algorithm](#algorithm)


### Description


`id`
:   **Auto-generated**-*String*- a unique id to identify this asset

    === "Example"
        ``` yaml     
        id: algorithm_10824912410291
        ```

`name `
:   **Required**-*String*- a human-readable name to ease identification and discoverability for human users

    === "Example"
        ``` yaml     
        name : Object Detection Algorithm for detection of faulty weld seams
        ```

`description`
:   **Required**-*String*- a short, human-readable description of the Algorithm to aid a human user in analysing the Algorithm’s capabilities and its applicability to a certain problem

    === "Example"
        ``` yaml     
        description: This algorithm can be used to solve a specifc problem, and applies some fancy technologies.
        ```

`classificationSchema`
:   **Required**-*Enumeration { Simulation, ML, others }*- the classification of the Algorithm, to describe the specialization area

    === "Example"
        ``` yaml     
        classificationSchema: ML
        ```

`type`
:   **Required**-*List( String)*- a detailed list of attributes to describe the Algorithm’s field of application

    === "Example"
        ``` yaml     
        type: {neural network, deep learning, convolutional neural network, CNN}
        ```

`author `
:   **Required**-*String*- the authoring entity

    === "Example"
        ``` yaml     
        author : DFKI
        ```

`date`
:   **Auto-generated**-*Date*- the creation data

    === "Example"
        ``` yaml     
        date: 06.04.2021
        ```

`version `
:   **Required**-*String*- the version

    === "Example"
        ``` yaml     
        version : 1.0
        ```


### Algorithm


`listOfMicroservices`
:   **Required**-*List( String)*- a list of Microservice Asset IDs, which are contained in the algorithm

    === "Example"
        ``` yaml     
        listOfMicroservices: [microservice.microservice_id_A, microservice.microservice_id_B]
        ```

`deploymentMapping`
:   **Required**-*Map( String: String)*- a mapping specifying which microservice should run on which host. By default each microservice is assigned a respective host, but this behaviour is not always ideal (eg. when two or more Microservices may need to run on the same host)

    === "Example"
        ``` yaml     
        deploymentMapping: {microservice.microservice_id_A: deployment.microservice_id_B, microservice.microservice_id_B: deployment.microservice_id_B}
        ```
