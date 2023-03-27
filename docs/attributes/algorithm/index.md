<style>
  .md-content__button {
    display: none;
  }
</style>
# Algorithm Fields


**For a more condensed summary this information is available in [table view](/tables/algorithm/)**



The metadata specification for a DIGITbrain Algorithm
has these fields:

`name`{ #name }

:   **Required**-*string*- a human-readable name to ease identification and discoverability for human users



    === "Example"
        ``` yaml     
        "Object Detection Algorithm for detection of faulty weld seams"
        ```

`description`{ #description }

:   **Required**-*string*- a short, human-readable description of the Algorithm to aid a human user in analysing the Algorithm’s capabilities and its applicability to a certain problem



    === "Example"
        ``` yaml     
        "This algorithm can be used to solve a specifc problem, and applies some fancy technologies."
        ```

`classification_schema`{ #classification_schema }

:   **Required**-*enum [Simulation, ML, others]*- the classification of the Algorithm, to describe the specialization area



    === "Example"
        ``` yaml     
        "ML"
        ```

`type`{ #type }

:   **Required**-*string*- a detailed list of attributes to describe the Algorithm’s field of application



    === "Example"
        ``` yaml     
        ["neural network", "deep learning", "convolutional neural network", "CNN"]
        ```

`version`{ #version }

:   **Optional**-*string*- the version, as defined by the provider



    === "Example"
        ``` yaml     
        "1.0"
        ```

`list_of_microservices`{ #list_of_microservices }

:   **Required**-*string*- a list of Microservice Asset IDs, which are contained in the algorithm



    === "Example"
        ``` yaml     
        ["MSID_MYMS_A", "MSID_MYMS_B"]
        ```

`deployment_mapping`{ #deployment_mapping }

:   **Required**-*string*- a mapping specifying which microservice should run on which host. By default each microservice is assigned a respective host, but this behaviour is not always ideal (eg. when two or more Microservices may need to run on the same host)



    === "Example"
        ``` yaml     
        {"MSID_MYMS_A": "HOSTID_MYHOST_A", "MSID_MYMS_B": "HOSTID_MYHOST_A"}
        ```

