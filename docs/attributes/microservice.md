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
- [Input Data(WP4)](#input-datawp4)
- [Output Data (WP4)](#output-data-wp4)
- [Model(WP5)](#modelwp5)
- [Parameters](#parameters)
- [Metrics](#metrics)


### Description


`id`
:   **Auto-generated**-*String*- unique DIGITbrain reference

    === "Example"
        ``` yaml     
        microservice_12312124
        ```

`name `
:   **Required**-*String*- human readable short, yet descriptive name of the Microservice

    === "Example"
        ``` yaml     
        Object Detection for faulty parts
        ```

`author `
:   **Required**-*String*- name of the authoring entity

    === "Example"
        ``` yaml     
        DFKI
        ```

`date`
:   **Auto-generated**-*Date*- creation date

    === "Example"
        ``` yaml     
        06.04.2021
        ```

`version `
:   **Required**-*String*- version

    === "Example"
        ``` yaml     
        1.0
        ```

`description`
:   **Required**-*String*- human readable short description of the Microservice's capabilities

    === "Example"
        ``` yaml     
        This microservices solves a certain problem using very specific methods...
        ```

`classificationSchema`
:   **Required**-*Enumeration { Simulation, ML, others }*- fine-granular classification of the Microservice

    === "Example"
        ``` yaml     
        other
        ```

`type`
:   **Required**-*List( String)*- detailed type of the microservice, list of keywords

    === "Example"
        ``` yaml     
        {neural network, deep learning, convolutional neural network, CNN}
        ```


### Service


`deploymentFormat`
:   **Required**-*Enumeration {docker-compose, kubernetes-manifest}*- identifier of the deployment environment required to deploy the Microservice's container

    === "Example"
        ``` yaml     
        docker-compose
        ```

`deploymentData`
:   **Required**-*JSON*- JSON of docker-compose or kubernetes manifest required to run the container

    === "Example"
        ``` yaml     
        See https://github.com/UoW-CPC/ADTGenerator/blob/main/examples/metadata_microservice.json#L30
        ```

`configurationData`
:   **Optional**-*List(Map)*- configuration file(s) required by the service
    === "Example"
        ``` yaml     
        https://github.com/UoW-CPC/ADTGenerator/blob/main/examples/metadata_RISTRA.json#L101
        ```

    `filePath`
:   **Optional**-*String*- full path to file including file name
        === "Example"
            ``` yaml     
            /data/rclone.conf
            ```

    `fileContent`
:   **Optional**-*String*- file content (not binary)
        === "Example"
            ``` yaml     
            [s3-server]\n    access_key: 123abc
            ```

    `mountPropagation`
:   **Optional**-*boolean*- Enable mountPropagation https://kubernetes.io/docs/concepts/storage/volumes/#mount-propagation . Default: False
        === "Example"
            ``` yaml     
            True
            ```

`mountedInputDirectories`
:   **Optional**-*List(String)*- A note for developers of co-operating Microservices. A list of directories that should be shared to the host by where this microservice can find required inputs
    === "Example"
        ``` yaml     
        ["/data", "/cfg"]
        ```

`mountedOutputDirectories`
:   **Optional**-*List(String)*- A note for developers of co-operating Microservices.  A list of directories that are shared on the host where this microservice will store its outputs
    === "Example"
        ``` yaml     
        ["/data_out", "/results"]
        ```


### Hardware Requirements


`recommendedNumberOfGPUs`
:   **Optional**-*Int*- recommended number of GPUs
    === "Example"
        ``` yaml     
        2
        ```

`minimumNumberOfGPUs`
:   **Optional**-*Int*- minimum required number of GPUs
    === "Example"
        ``` yaml     
        1
        ```

`recommendedGPURAM`
:   **Optional**-*Int*- recommended amount of GPU memory in GB
    === "Example"
        ``` yaml     
        6
        ```

`minimumGPURAM`
:   **Optional**-*Int*- minimum required amount of GPU memory in GB
    === "Example"
        ``` yaml     
        1
        ```

`gpuType`
:   **Optional**-*String*- a description of the type of GPUs, and further specifications, to allow the execution of the Microservice
    === "Example"
        ``` yaml     
        NVidia (compute capability >= 7.0)
        ```

`hpcRequired`
:   **Optional**-*Bool*- whether this Microservice requires an HPC environment to be executed efficiently
    === "Example"
        ``` yaml     
        true
        ```

`edgeType`
:   **Optional**-*Enumeration {TPU (Google), NPU (Qualcomm), FPGA, NVIDIA Jetson AGX}*- required type of edge device to allow the execution of the Microservice
    === "Example"
        ``` yaml     
        NVIDIA Jetson AGX
        ```

`recommendedRAM`
:   **Optional**-*String*- recommended amount of memory in GB
    === "Example"
        ``` yaml     
        16
        ```

`minimumRAM`
:   **Optional**-*String*- minimum required amount memory in GB
    === "Example"
        ``` yaml     
        2
        ```

`recommendedCPUs`
:   **Optional**-*Int*- recommended number of CPU cores
    === "Example"
        ``` yaml     
        4
        ```

`minimumCPUs`
:   **Optional**-*Int*- minimum required number of CPU cores
    === "Example"
        ``` yaml     
        2
        ```

`requiredDiskSpace`
:   **Optional**-*Int*- required amount of disk space in GB
    === "Example"
        ``` yaml     
        42
        ```


### OS Requirements


`osArch`
:   **Required**-*String*- supported os architecture

    === "Example"
        ``` yaml     
        x86_64
        ```

`osType`
:   **Optional**-*String*- supported os type
    === "Example"
        ``` yaml     
        linux
        ```

`osDistribution`
:   **Optional**-*String*- supported os distribution
    === "Example"
        ``` yaml     
        ubuntu
        ```

`osVersion`
:   **Optional**-*String*- description of supported os version
    === "Example"
        ``` yaml     
        20.04
        ```


### Input Data(WP4)


`inputData`
:   **Optional**-*List( Data Objects)*- list of Data objects for each required input, specified using the "DATA" fields listed below
    === "Example"
        ``` yaml     
        {{DATA_KIND = {FILE, STREAM}, DATA_DIRECTION = {SOURCE}} 
        ```

    `input_id`
:   **Required**-*String*- human-readable identifier, unique within a Microservice

        === "Example"
            ``` yaml     
            file1
            ```

    `DATA_KIND`
:   **Required**-*List( DATA_KIND)*- supported types of the data resource (e.g. file/object storage, database management system, streaming broker). FILE can mean a single file or a folder.

        === "Example"
            ``` yaml     
            {FILE, STREAM}
            ```

    `DATA_DIRECTION`
:   **Required**-*List( DATA_DIRECTION)*- supported direction of data flow (source: data provider, sink: data consumer/storage)

        === "Example"
            ``` yaml     
            {SINK, BIDIRECTIONAL}
            ```

    `DATA_FORMAT`
:   **Optional**-*List( DATA_FORMAT)*- supported format/encoding of the data produced or consumed by the data resource as a MIME type (IETF RFC 6838 https://www.sitepoint.com/mime-types-complete-list/). More than one can appear here (remote directory with several files).
        === "Example"
            ``` yaml     
            {application/zip, image/jpg}
            ```

    `DATA_SOURCE_TYPE`
:   **Optional**-*List( DATA_SOURCE_TYPE)*- supported exact type of the data resource. Typically corresponds to the scheme part (protocol://) of DATA_URI
        === "Example"
            ``` yaml     
            {MYSQL, KAFKA}
            ```

    `DATA_PROTOCOL`
:   **Optional**-*List( DATA_PROTOCOL)*- supported protocols
        === "Example"
            ``` yaml     
            {HTTP}
            ```

    `DATA_AUTH_TYPE`
:   **Optional**-*List( DATA_AUTH_TYPE)*- supported authentication type
        === "Example"
            ``` yaml     
            {tls_mutual, userpass}
            ```

    `DATA_MYSQL_DIALECT`
:   **Optional**-*List( DATA_MYSQL_DIALECT)*- supported MYSQL dialect
        === "Example"
            ``` yaml     
            {mariadbdialect}
            ```

    `DATA_MQTT_PROTOCOL_VERSION`
:   **Optional**-*List( DATA_MQTT_PROTOCOL_VERSION)*- supported MQTT protocol version
        === "Example"
            ``` yaml     
            {2.3.1}
            ```

    `DATA_KAFKA_BROKER_VERSION`
:   **Optional**-*List( DATA_KAFKA_BROKER_VERSION)*- supported Kafka broker version
        === "Example"
            ``` yaml     
            {2.7.1, 2.5}
            ```

    `DATA_S3_REGION`
:   **Optional**-*List( DATA_S3_REGION)*- supported S3 region
        === "Example"
            ``` yaml     
            {eu-central-1}
            ```

    `DATA_SCHEMA`
:   **Optional**-*List( DATA_SCHEMA)*- supported internal message structure, semantics, ontology. It can be any file (doc, rdf, owl, etc.). Asset Administration Shell, IEC 61360 - Common Data Dictionary, …
        === "Example"
            ``` yaml     
            {jpg}
            ```


### Output Data (WP4)


`outputData`
:   **Optional**-*List( Data Objects)*- list of Data objects for each generated output, specified using the "DATA" fields listed below
    === "Example"
        ``` yaml     
        {{DATA_KIND = {FILE, STREAM}, DATA_DIRECTION = {SINK}} 
        ```

    `output_id`
:   **Required**-*String*- human-readable identifier, unique within a Microservice

        === "Example"
            ``` yaml     
            file1
            ```

    `DATA_KIND`
:   **Required**-*List( DATA_KIND)*- supported types of the data resource (e.g. file/object storage, database management system, streaming broker). FILE can mean a single file or a folder.

        === "Example"
            ``` yaml     
            {FILE, STREAM}
            ```

    `DATA_DIRECTION`
:   **Required**-*List( DATA_DIRECTION)*- supported direction of data flow (source: data provider, sink: data consumer/storage)

        === "Example"
            ``` yaml     
            {SINK, BIDIRECTIONAL}
            ```

    `DATA_FORMAT`
:   **Optional**-*List( DATA_FORMAT)*- supported format/encoding of the data produced or consumed by the data resource as a MIME type (IETF RFC 6838 https://www.sitepoint.com/mime-types-complete-list/). More than one can appear here (remote directory with several files)
        === "Example"
            ``` yaml     
            {application/zip, image/jpg}
            ```

    `DATA_SOURCE_TYPE`
:   **Optional**-*List( DATA_SOURCE_TYPE)*- supported exact type of the data resource. Typically corresponds to the scheme part (protocol://) of DATA_URI.
        === "Example"
            ``` yaml     
            {MYSQL, KAFKA}
            ```

    `DATA_PROTOCOL`
:   **Optional**-*List( DATA_PROTOCOL)*- supported protocols
        === "Example"
            ``` yaml     
            {HTTP}
            ```

    `DATA_AUTH_TYPE`
:   **Optional**-*List( DATA_AUTH_TYPE)*- supported authentication type
        === "Example"
            ``` yaml     
            {tls_mutual, userpass}
            ```

    `DATA_MYSQL_DIALECT`
:   **Optional**-*List( DATA_MYSQL_DIALECT)*- supported MYSQL dialect, for each generated output
        === "Example"
            ``` yaml     
            {mariadbdialect}
            ```

    `DATA_MQTT_PROTOCOL_VERSION`
:   **Optional**-*List( DATA_MQTT_PROTOCOL_VERSION)*- supported MQTT protocol version
        === "Example"
            ``` yaml     
            {2.3.1}
            ```

    `DATA_KAFKA_BROKER_VERSION`
:   **Optional**-*List( DATA_KAFKA_BROKER_VERSION)*- supported Kafka broker version
        === "Example"
            ``` yaml     
            {2.7.1, 2.5}
            ```

    `DATA_S3_REGION`
:   **Optional**-*List( DATA_S3_REGION)*- supported S3 region
        === "Example"
            ``` yaml     
            {eu-central-1}
            ```

    `DATA_SCHEMA`
:   **Optional**-*List( DATA_SCHEMA)*- supported internal message structure, semantics, ontology. It can be any file (doc, rdf, owl, etc.). Asset Administration Shell, IEC 61360 - Common Data Dictionary, …
        === "Example"
            ``` yaml     
            {jpg}
            ```


### Model(WP5)


`model_types`
:   **Optional**-*List( ModelTypes)*- list of supported Model types
    === "Example"
        ``` yaml     
        {SavedModel (Tensorflow)}
        ```

`model_recommendedAuthTools`
:   **Optional**-*List (AuthTools)*- list of recommended AuthoringTools used to generate the Model
    === "Example"
        ``` yaml     
        {PreSTRA}
        ```


### Parameters


`parameters`
:   **Optional**-*List( Parameter)*- list of Parameter objects for each possible parameters, to be specified before deployment

    `name`
:   **Required**-*String*- short name for this parameter (should be unique across the Microservice’s parameters)

        === "Example"
            ``` yaml     
            detection_threshold
            ```

    `type`
:   **Required**-*Enumeration (xsd datatypes)*- expected input type (may be used to verify the input)

        === "Example"
            ``` yaml     
            Integer
            ```

    `mandatory`
:   **Optional**-*Boolean*- whether this parameter is mandatory (default: false)
        === "Example"
            ``` yaml     
            true
            ```

    `defaultValue`
:   **Optional**-*has to match "type"*- a default value, if the parameter is required but not provided
        === "Example"
            ``` yaml     
            42
            ```

    `description`
:   **Required**-*String*- short description of the parameter and its possible values

        === "Example"
            ``` yaml     
            This parameter can be used to configure the included algorithm in a certain way, possible values: "A", "B", "Z"
            ```


### Metrics


`metrics`
:   **Optional**-*List( Metrics)*- list of Metric objects for each metric collected by the Microservice

    `name`
:   **Required**-*String*- short name (should be unique across the Microservice's metrics)

        === "Example"
            ``` yaml     
            meanTemperature
            ```

    `correspondingMeasurement`
:   **Required**-*String*- identification of the corresponding measurement, i.e. output of the Model

        === "Example"
            ``` yaml     
            temperature1
            ```

    `function`
:   **Required**-*String*- short description of the mathematical approach used to derive this value

        === "Example"
            ``` yaml     
            arithmetic mean
            ```

    `unit`
:   **Required**-*String*- the unit of the metric measurement

        === "Example"
            ``` yaml     
            degree celsius
            ```

    `description`
:   **Required**-*String*- short description of the metric measurement

        === "Example"
            ``` yaml     
            This metric describes the arithmetic mean of the approximated temperatures of the fabricated part when it leaves station 4.
            ```
