<style>
  .md-content__button {
    display: none;
  }
</style>
# Microservice Fields


**For a more condensed summary this information is available in [table view](/tables/microservice/)**



The specification for Microservice
has these fields:


`name`{ #name }

:   **Required**-*string*<br>
    human readable short, yet descriptive name of the Microservice.


    === "Example"
        ``` yaml     
        "Object Detection for faulty parts"
        ```


`version`{ #version }

:   **Optional**-*string*<br>
    version as defined by the user.


    === "Example"
        ``` yaml     
        "1.0"
        ```


`description`{ #description }

:   **Required**-*string*<br>
    human readable short description of the Microservice's capabilities.


    === "Example"
        ``` yaml     
        "This microservices solves a certain problem using very specific methods…"
        ```


`classification_schema`{ #classification-schema }

:   **Required**-*enum [Simulation, ML, others]*<br>
    fine-granular classification of the Microservice


    === "Example"
        ``` yaml     
        "others"
        ```


`type`{ #type }

:   **Required**-*string[]*<br>
    detailed type of the microservice, list of keywords


    === "Example"
        ``` yaml     
        ["neural network", "deep learning", "convolutional neural network", "CNN"]
        ```


`deployment_format`{ #deployment-format }

:   **Required**-*enum [docker-compose, kubernetes-manifest]*<br>
    identifier of the deployment environment required to deploy the Microservice's container


    === "Example"
        ``` yaml     
        "docker-compose"
        ```


`deployment_data`{ #deployment-data }

:   **Required**-*string (YAML)*<br>
    DIGITbrain supports Microservices in containers. The platform aims
    to support any OCI-compliant container images, as mentioned in
    [pre-requisites](/start/microservice/#pre-requisites). Containers are 
    generally described in a variety of formats and the platform aims to
    support the most common kinds.

    We currently support the description of **one container** in either the *Docker-Compose*
    format or **one Pod or Deployment** in the *Kubernetes manifest* format.

    If you normally run your container with *docker run* we suggest using the online, open-source
    [Composerize](https://www.composerize.com/) tool, which can translate the command to a
    Docker-Compose file.




    === "Docker-Compose"
        ``` yaml     
        services:
          reverseproxy:
            image: nginx:latest
            ports:
              - '8080:8080'
            restart: always

        ```


    === "Kubernetes Manifest"
        ``` yaml     
        apiVersion: v1
        kind: Pod
        metadata:
          name: reverseproxy
        spec:
          containers:
            - name: reverseproxy
              image: nginx:latest
              ports:
                - containerPort: 8080

        ```



`configuration_data`{ #configuration-data }

:   **Optional**-*[ConfigurationData](../configuration_data.md)[]*<br>
    List of objects specifying configuration file(s) content required by the service


    === "Example"
        ``` yaml     
        file_path: /data/rclone.conf
        file_content: |
          [s3-server]
          access_key: 123abc
        mount_propagation: Bidirectional

        ```


`mounted_shared_directories`{ #mounted-shared-directories }

:   **Optional**-*string*<br>
    A note for developers of co-operating Microservices. Directories that should be shared to the host where this microservice can find required inputs / store outputs


    === "Example"
        ``` yaml     
        "/data and /cfg are mounted on the host for data and configuration sharing, respectively."
        ```


`recommended_number_of_gpus`{ #recommended-number-of-gpus }

:   **Optional**-*integer*<br>
    recommended number of GPUs


`recommended_gpu_ram`{ #recommended-gpu-ram }

:   **Optional**-*integer*<br>
    recommended amount of GPU memory in GB


`gpu_type`{ #gpu-type }

:   **Optional**-*string*<br>
    a description of the type of GPUs, and further specifications, to allow the execution of the Microservice



    === "Example"
        ``` yaml     
        "NVidia (compute capability >= 7.0)"
        ```


`hpc_required`{ #hpc-required }

:   **Optional**-*boolean*<br>
    whether this Microservice requires an HPC environment to be executed efficiently



    === "Example"
        ``` yaml     
        true
        ```


`edge_type`{ #edge-type }

:   **Optional**-*enum [TPU (Google), NPU (Qualcomm), FPGA, NVIDIA Jetson AGX]*<br>
    required type of edge device to allow the execution of the Microservice



    === "Example"
        ``` yaml     
        "NVIDIA Jetson AGX"
        ```


`recommended_ram`{ #recommended-ram }

:   **Optional**-*integer*<br>
    recommended amount of memory in GB



    === "Example"
        ``` yaml     
        16
        ```


`recommended_cpus`{ #recommended-cpus }

:   **Optional**-*integer*<br>
    recommended number of CPU cores



`required_disk_space`{ #required-disk-space }

:   **Optional**-*integer*<br>
    required amount of disk space in GB



    === "Example"
        ``` yaml     
        42
        ```


`os_arch`{ #os-arch }

:   **Optional**-*string*<br>
    supported os architecture. Defaults to x86



    === "Example"
        ``` yaml     
        "x86_64"
        ```


`os_type`{ #os-type }

:   **Optional**-*string*<br>
    supported os type. Defaults to Linux



    === "Example"
        ``` yaml     
        "linux"
        ```


`data_resource`{ #data-resource }

:   **Optional**-*[Data Resource](../data_resource.md)[]*<br>
    list of Data objects for each required data resource, specified using the "DATA" fields in the linked substructure



    === "Example"
        ``` yaml     
        kind: [FILE, STREAM]
        direction: [SOURCE]
        format: [application/zip, image/jpg]
        source_type: [MYSQL, KAFKA]
        auth_type: [userpass]
        schema: [jpg]
        aux_info:
          PROTOCOL: http
          MYSQL_DIALECT: mariadbdialect

        ```


`model_types`{ #model-types }

:   **Optional**-*string[]*<br>
    list of supported Model types



    === "Example"
        ``` yaml     
        ["SavedModel (Tensorflow)"]
        ```


`model_recommended_auth_tools`{ #model-recommended-auth-tools }

:   **Optional**-*string[]*<br>
    list of recommended AuthoringTools used to generate the Model



    === "Example"
        ``` yaml     
        ["PreSTRA"]
        ```


`parameters`{ #parameters }

:   **Optional**-*[Parameters](../parameters.md)[]*<br>
    list of Parameter objects for each possible parameters, to be specified before deployment



    === "Example"
        ``` yaml     
        parameters:
        - name: detection_threshold
          type: Integer
          mandatory: true
          defaultValue: 42
          description: This parameter is helpful

        ```


`metrics`{ #metrics }

:   **Optional**-*[Metrics](../metrics.md)[]*<br>
    list of Metric objects for each metric collected by the Microservice



    === "Example"
        ``` yaml     
        metrics:
        - name: meanTemperature
          correspondingMeasurement: temperature1
          function: arithmetic mean
          unit: degree celcius
          description: The metric is good

        ```

