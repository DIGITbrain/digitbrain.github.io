<style>
  .md-content__button {
    display: none;
  }
</style>
# Microservice Fields

**This information is also available in [table format](/tables/microservice/)**


## Available Fields 

The metadata specification for a DIGITbrain Microservice
has these sections:

- [Description](#description)
- [Service](#service)
- [Hardware Requirements](#hardware-requirements)
- [OS Requirements](#os-requirements)
- [Data Resources](#data-resources)
- [Model](#model)
- [Parameters](#parameters)
- [Metrics](#metrics)


### Description


`id`{ #id }
:   **Auto-generated**-*String*- unique DIGITbrain reference

    === "Example"
        ``` yaml     
        microservice_12312124
        ```

`name `{ #name- }
:   **Required**-*String*- human readable short, yet descriptive name of the Microservice

    === "Example"
        ``` yaml     
        Object Detection for faulty parts
        ```

`author `{ #author- }
:   **Required**-*String*- name of the authoring entity

    === "Example"
        ``` yaml     
        DFKI
        ```

`date`{ #date }
:   **Auto-generated**-*Date*- creation date

    === "Example"
        ``` yaml     
        06.04.2021
        ```

`version `{ #version- }
:   **Required**-*String*- version

    === "Example"
        ``` yaml     
        1.0
        ```

`description`{ #description }
:   **Required**-*String*- human readable short description of the Microservice's capabilities

    === "Example"
        ``` yaml     
        This microservices solves a certain problem using very specific methods...
        ```

`classificationSchema`{ #classificationschema }
:   **Required**-*Enumeration { Simulation, ML, others }*- fine-granular classification of the Microservice

    === "Example"
        ``` yaml     
        other
        ```

`type`{ #type }
:   **Required**-*List( String)*- detailed type of the microservice, list of keywords

    === "Example"
        ``` yaml     
        {neural network, deep learning, convolutional neural network, CNN}
        ```


### Service


`deploymentFormat`{ #deploymentformat }
:   **Required**-*Enumeration {docker-compose, kubernetes-manifest}*- identifier of the deployment environment required to deploy the Microservice's container

    === "Example"
        ``` yaml     
        docker-compose
        ```

`deploymentData`{ #deploymentdata }
:   **Required**-*JSON*- JSON of docker-compose or kubernetes manifest required to run the container

    === "Example"
        ``` yaml     
        See https://github.com/UoW-CPC/ADTGenerator/blob/main/examples/metadata_microservice.json#L30
        ```

`configurationData`{ #configurationdata }
:   **Optional**-*[ConfigurationData](../configurationdata.md)*- List of objects specifying configuration file(s) content required by the service

`mountedSharedDirectories`{ #mountedshareddirectories }
:   **Optional**-*String*- A note for developers of co-operating Microservices. Directories that should be shared to the host where this microservice can find required inputs / store outputs
    === "Example"
        ``` yaml     
        /data and /cfg are mounted on the host for data and configuration sharing, respectively.
        ```


### Hardware Requirements


`recommendedNumberOfGPUs`{ #recommendednumberofgpus }
:   **Optional**-*Int*- recommended number of GPUs
    === "Example"
        ``` yaml     
        2
        ```

`recommendedGPURAM`{ #recommendedgpuram }
:   **Optional**-*Int*- recommended amount of GPU memory in GB
    === "Example"
        ``` yaml     
        6
        ```

`gpuType`{ #gputype }
:   **Optional**-*String*- a description of the type of GPUs, and further specifications, to allow the execution of the Microservice
    === "Example"
        ``` yaml     
        NVidia (compute capability >= 7.0)
        ```

`hpcRequired`{ #hpcrequired }
:   **Optional**-*Bool*- whether this Microservice requires an HPC environment to be executed efficiently
    === "Example"
        ``` yaml     
        true
        ```

`edgeType`{ #edgetype }
:   **Optional**-*Enumeration {TPU (Google), NPU (Qualcomm), FPGA, NVIDIA Jetson AGX}*- required type of edge device to allow the execution of the Microservice
    === "Example"
        ``` yaml     
        NVIDIA Jetson AGX
        ```

`recommendedRAM`{ #recommendedram }
:   **Optional**-*String*- recommended amount of memory in GB
    === "Example"
        ``` yaml     
        16
        ```

`recommendedCPUs`{ #recommendedcpus }
:   **Optional**-*Int*- recommended number of CPU cores
    === "Example"
        ``` yaml     
        4
        ```

`requiredDiskSpace`{ #requireddiskspace }
:   **Optional**-*Int*- required amount of disk space in GB
    === "Example"
        ``` yaml     
        42
        ```


### OS Requirements


`osArch`{ #osarch }
:   **Optional**-*String*- supported os architecture. Defaults to x86
    === "Example"
        ``` yaml     
        x86_64
        ```

`osType`{ #ostype }
:   **Optional**-*String*- supported os type. Defaults to Linux
    === "Example"
        ``` yaml     
        linux
        ```


### Data Resources


`dataResource`{ #dataresource }
:   **Optional**-*[Data Resources](../data_resources.md)*- list of Data objects for each required data resource, specified using the "DATA" fields in the linked substructure


### Model


`model_types`{ #model_types }
:   **Optional**-*List( ModelTypes)*- list of supported Model types
    === "Example"
        ``` yaml     
        {SavedModel (Tensorflow)}
        ```

`model_recommendedAuthTools`{ #model_recommendedauthtools }
:   **Optional**-*List (AuthTools)*- list of recommended AuthoringTools used to generate the Model
    === "Example"
        ``` yaml     
        {PreSTRA}
        ```


### Parameters


`parameters`{ #parameters }
:   **Optional**-*List( Parameter)*- list of Parameter objects for each possible parameters, to be specified before deployment

    `name`{ #name }
:   **Required**-*String*- short name for this parameter (should be unique across the Microservice’s parameters)

        === "Example"
            ``` yaml     
            detection_threshold
            ```

    `type`{ #type }
:   **Required**-*Enumeration (xsd datatypes)*- expected input type (may be used to verify the input)

        === "Example"
            ``` yaml     
            Integer
            ```

    `mandatory`{ #mandatory }
:   **Optional**-*Boolean*- whether this parameter is mandatory (default: false)
        === "Example"
            ``` yaml     
            true
            ```

    `defaultValue`{ #defaultvalue }
:   **Optional**-*has to match "type"*- a default value, if the parameter is required but not provided
        === "Example"
            ``` yaml     
            42
            ```

    `description`{ #description }
:   **Required**-*String*- short description of the parameter and its possible values

        === "Example"
            ``` yaml     
            This parameter can be used to configure the included algorithm in a certain way, possible values: "A", "B", "Z"
            ```


### Metrics


`metrics`{ #metrics }
:   **Optional**-*List( Metrics)*- list of Metric objects for each metric collected by the Microservice

    `name`{ #name }
:   **Required**-*String*- short name (should be unique across the Microservice's metrics)

        === "Example"
            ``` yaml     
            meanTemperature
            ```

    `correspondingMeasurement`{ #correspondingmeasurement }
:   **Required**-*String*- identification of the corresponding measurement, i.e. output of the Model

        === "Example"
            ``` yaml     
            temperature1
            ```

    `function`{ #function }
:   **Required**-*String*- short description of the mathematical approach used to derive this value

        === "Example"
            ``` yaml     
            arithmetic mean
            ```

    `unit`{ #unit }
:   **Required**-*String*- the unit of the metric measurement

        === "Example"
            ``` yaml     
            degree celsius
            ```

    `description`{ #description }
:   **Required**-*String*- short description of the metric measurement

        === "Example"
            ``` yaml     
            This metric describes the arithmetic mean of the approximated temperatures of the fabricated part when it leaves station 4.
            ```
