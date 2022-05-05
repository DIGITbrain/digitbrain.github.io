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

- [Administrative Data](#administrative-data)
- [Description](#description)
- [Service](#service)
- [Hardware Requirements](#hardware-requirements)
- [OS Requirements](#os-requirements)
- [Data Resources](#data-resources)
- [Model](#model)
- [Parameters](#parameters)
- [Metrics](#metrics)


### Administrative Data


`ID`{ #id }
:   **Auto-generated**-*ID*- Unique identifier of the asset.

    === "Example"
        ``` yaml     
        "MSID_MYMS_A"
        ```

`AUTHOR`{ #author }
:   **Auto-generated**-*ID*- Unique identifier of the user who created this record

    === "Example"
        ``` yaml     
        UUID
        ```

`PROVIDER`{ #provider }
:   **Auto-generated**-*ID*- Legal entity who provides the asset (owner). It is the affiliation of the author by default.

    === "Example"
        ``` yaml     
        UUID
        ```

`DATE`{ #date }
:   **Auto-generated**-*DATE (ISO 8601)*- Date of asset registration.

    === "Example"
        ``` yaml     
        2022-04-28T08:11:53+00:00
        ```


### Description


`name `{ #name- }
:   **Required**-*String*- human readable short, yet descriptive name of the Microservice

    === "Example"
        ``` yaml     
        "Object Detection for faulty parts"
        ```

`version `{ #version- }
:   **Required**-*String*- version

    === "Example"
        ``` yaml     
        "1.0"
        ```

`description`{ #description }
:   **Required**-*String*- human readable short description of the Microservice's capabilities

    === "Example"
        ``` yaml     
        "This microservices solves a certain problem using very specific methods…"
        ```

`classificationSchema`{ #classificationschema }
:   **Required**-*Enumeration ["Simulation", "ML", "others"]*- fine-granular classification of the Microservice

    === "Example"
        ``` yaml     
        "others"
        ```

`type`{ #type }
:   **Required**-*List[String]*- detailed type of the microservice, list of keywords

    === "Example"
        ``` yaml     
        ["neural network", "deep learning", "convolutional neural network", "CNN"]
        ```


### Service


`deploymentFormat`{ #deploymentformat }
:   **Required**-*Enumeration ["docker-compose", "kubernetes-manifest"]*- identifier of the deployment environment required to deploy the Microservice's container

    === "Example"
        ``` yaml     
        "docker-compose"
        ```

`deploymentData`{ #deploymentdata }
:   **Required**-*JSON*- JSON of docker-compose or kubernetes manifest required to run the container

    === "Example"
        ``` yaml     
        "version": "3.7",
            "services": {
              "ristra": {
                "image": "dbs-container-repo.emgora.eu/db-ristra-cli-cpu:1.0.0",
                "entrypoint": "/bin/sh -c",
                "command": "python3 start.py {{ MODEL_PATH }}/{{ MODEL_FILE }}",
                "volumes": [{
                  "type": "bind",
                  "source": "/data",
                  "target": "/data",
                  "bind": {
                     "propagation": "rshared"
            	      }
                }],
                "privileged": true
              }
            }
        ```

`configurationData`{ #configurationdata }
:   **Optional**-*[ConfigurationData](../configurationdata.md)*- List of objects specifying configuration file(s) content required by the service
    === "Example"
        ``` yaml     
        [ {
                "filePath": "/data/rclone.conf",
                "fileContent": "[s3-server]\n    access_key: 123abc",
                "mountPropagation": "Bidirectional"
            } ]
        ```

`mountedSharedDirectories`{ #mountedshareddirectories }
:   **Optional**-*String*- A note for developers of co-operating Microservices. Directories that should be shared to the host where this microservice can find required inputs / store outputs
    === "Example"
        ``` yaml     
        "/data and /cfg are mounted on the host for data and configuration sharing, respectively."
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
        "NVidia (compute capability >= 7.0)"
        ```

`hpcRequired`{ #hpcrequired }
:   **Optional**-*Bool*- whether this Microservice requires an HPC environment to be executed efficiently
    === "Example"
        ``` yaml     
        true
        ```

`edgeType`{ #edgetype }
:   **Optional**-*Enumeration ["TPU (Google)", "NPU (Qualcomm)", "FPGA", "NVIDIA Jetson AGX"]*- required type of edge device to allow the execution of the Microservice
    === "Example"
        ``` yaml     
        "NVIDIA Jetson AGX"
        ```

`recommendedRAM`{ #recommendedram }
:   **Optional**-*Int*- recommended amount of memory in GB
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
        "x86_64"
        ```

`osType`{ #ostype }
:   **Optional**-*String*- supported os type. Defaults to Linux
    === "Example"
        ``` yaml     
        "linux"
        ```


### Data Resources


`dataResource`{ #dataresource }
:   **Optional**-*[Data Resources](../data_resources.md)*- list of Data objects for each required data resource, specified using the "DATA" fields in the linked substructure
    === "Example"
        ``` yaml     
        [{
                "DATA_RESOURCE_ID": "MY_SINK",
                "DATA_KIND": ["FILE", "STREAM"],
                "DATA_DIRECTION": ["SOURCE"],
                "DATA_FORMAT": ["image/jpg"],
                "DATA_SOURCE_TYPE": ["KAFKA"],
                "DATA_SCHEMA": ["jpg"],
                "DATA_AUX_INFO": {"PROTOCOL": "https", "S3_REGION": "eu-west-1"}
            }]
        ```


### Model


`model_types`{ #model_types }
:   **Optional**-*List[String]*- list of supported Model types
    === "Example"
        ``` yaml     
        ["SavedModel (Tensorflow)"]
        ```

`model_recommendedAuthTools`{ #model_recommendedauthtools }
:   **Optional**-*List[String]*- list of recommended AuthoringTools used to generate the Model
    === "Example"
        ``` yaml     
        ["PreSTRA"]
        ```


### Parameters


`parameters`{ #parameters }
:   **Optional**-*[Parameters](../parameters.md)*- list of Parameter objects for each possible parameters, to be specified before deployment
    === "Example"
        ``` yaml     
        [{
                "name": "detection_threshold",
                "type": "Integer",
                "mandatory": true,
                "defaultValue": 42,
                "description": "This parameter is helpful"
            }]
        ```


### Metrics


`metrics`{ #metrics }
:   **Optional**-*[Metrics](../metrics.md)*- list of Metric objects for each metric collected by the Microservice
    === "Example"
        ``` yaml     
        [{
                "name": "meanTemperature",
                "correspondingMeasurement": "temperature1",
                "function": "arithmetic mean",
                "unit": "degree celcius",
                "description": "The metric is good"
            } ]
        ```
