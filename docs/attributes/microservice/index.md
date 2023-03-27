<style>
  .md-content__button {
    display: none;
  }
</style>
# Microservice Fields


**For a more condensed summary this information is available in [table view](/tables/microservice/)**



The metadata specification for a DIGITbrain Microservice
has these fields:

`name`{ #name }

:   **Required**-*string*- human readable short, yet descriptive name of the Microservice.


    === "Example"
        ``` yaml     
        "Object Detection for faulty parts"
        ```

`version`{ #version }

:   **Optional**-*string*- version as defined by the user.


    === "Example"
        ``` yaml     
        "1.0"
        ```

`description`{ #description }

:   **Required**-*string*- human readable short description of the Microservice's capabilities.


    === "Example"
        ``` yaml     
        "This microservices solves a certain problem using very specific methods…"
        ```

`classification_schema`{ #classification_schema }

:   **Required**-*enum [Simulation, ML, others]*- fine-granular classification of the Microservice


    === "Example"
        ``` yaml     
        "others"
        ```

`type`{ #type }

:   **Required**-*string*- detailed type of the microservice, list of keywords


    === "Example"
        ``` yaml     
        ["neural network", "deep learning", "convolutional neural network", "CNN"]
        ```

`deployment_format`{ #deployment_format }

:   **Required**-*enum [docker-compose, kubernetes-manifest]*- identifier of the deployment environment required to deploy the Microservice's container


    === "Example"
        ``` yaml     
        "docker-compose"
        ```

`deployment_data`{ #deployment_data }

:   **Required**-*string*- JSON of docker-compose or kubernetes manifest required to run the container


    === "Example"
        ``` yaml     
        "version": "3.7",
            "services": {
              "ristra": {
                "image": "dbs-container-repo.emgora.eu/db-ristra-cli-cpu:1.0.0",
                "entrypoint": "/bin/sh -c",
                "command": "python3 start.py {{ MODEL.PATH }}/{{ MODEL.FILE }}",
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

`configuration_data`{ #configuration_data }

:   **Optional**-*[ConfigurationData](../configurationdata.md)*- List of objects specifying configuration file(s) content required by the service


    === "Example"
        ``` yaml     
        [ {
                "filePath": "/data/rclone.conf",
                "fileContent": "[s3-server]\n    access_key: 123abc",
                "mountPropagation": "Bidirectional"
            } ]
        ```

`mounted_shared_directories`{ #mounted_shared_directories }

:   **Optional**-*string*- A note for developers of co-operating Microservices. Directories that should be shared to the host where this microservice can find required inputs / store outputs


    === "Example"
        ``` yaml     
        "/data and /cfg are mounted on the host for data and configuration sharing, respectively."
        ```

`recommended_number_of_gpus`{ #recommended_number_of_gpus }

:   **Optional**-*integer*- recommended number of GPUs

`recommended_gpu_ram`{ #recommended_gpu_ram }

:   **Optional**-*integer*- recommended amount of GPU memory in GB

`gpu_type`{ #gpu_type }

:   **Optional**-*string*- a description of the type of GPUs, and further specifications, to allow the execution of the Microservice



    === "Example"
        ``` yaml     
        "NVidia (compute capability >= 7.0)"
        ```

`hpc_required`{ #hpc_required }

:   **Optional**-*boolean*- whether this Microservice requires an HPC environment to be executed efficiently



    === "Example"
        ``` yaml     
        true
        ```

`edge_type`{ #edge_type }

:   **Optional**-*enum [TPU (Google), NPU (Qualcomm), FPGA, NVIDIA Jetson AGX]*- required type of edge device to allow the execution of the Microservice



    === "Example"
        ``` yaml     
        "NVIDIA Jetson AGX"
        ```

`recommended_ram`{ #recommended_ram }

:   **Optional**-*integer*- recommended amount of memory in GB



    === "Example"
        ``` yaml     
        16
        ```

`recommended_cpus`{ #recommended_cpus }

:   **Optional**-*integer*- recommended number of CPU cores


`required_disk_space`{ #required_disk_space }

:   **Optional**-*integer*- required amount of disk space in GB



    === "Example"
        ``` yaml     
        42
        ```

`os_arch`{ #os_arch }

:   **Optional**-*string*- supported os architecture. Defaults to x86



    === "Example"
        ``` yaml     
        "x86_64"
        ```

`os_type`{ #os_type }

:   **Optional**-*string*- supported os type. Defaults to Linux



    === "Example"
        ``` yaml     
        "linux"
        ```

`data_resource`{ #data_resource }

:   **Optional**-*[Data Resources](../data_resources.md)*- list of Data objects for each required data resource, specified using the "DATA" fields in the linked substructure



    === "Example"
        ``` yaml     
        [{
                "ID": "MY_SINK",
                "KIND": "STREAM",
                "DIRECTION": "SOURCE",
                "FORMAT": ["image/jpg"],
                "SOURCE_TYPE": "KAFKA",
                "SCHEMA": ["jpeg image"],
                "AUX_INFO": {"PROTOCOL": "https", "S3_REGION": "eu-west-1"}
            }]
        ```

`model_types`{ #model_types }

:   **Optional**-*string*- list of supported Model types



    === "Example"
        ``` yaml     
        ["SavedModel (Tensorflow)"]
        ```

`model_recommended_auth_tools`{ #model_recommended_auth_tools }

:   **Optional**-*string*- list of recommended AuthoringTools used to generate the Model



    === "Example"
        ``` yaml     
        ["PreSTRA"]
        ```

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

