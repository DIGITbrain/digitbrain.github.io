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

- [Administrative Data](#administrative-data)
- [Description](#description)
- [Algorithm](#algorithm)


### Administrative Data


`ID`{ #id }
:   **Auto-generated**-*ID*- Unique identifier of the asset.

    === "Example"
        ``` yaml     
        "ALGID_MYALG"
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

`BUILD`{ #build }
:   **Auto-generated**-*Integer*- Build number, incremented automatically to provide versioning for the asset

    === "Example"
        ``` yaml     
        21
        ```

`DATE`{ #date }
:   **Auto-generated**-*DATE (ISO 8601)*- Date of asset registration.

    === "Example"
        ``` yaml     
        2022-04-28T08:11:53+00:00
        ```


### Description


`name `{ #name- }
:   **Required**-*String*- a human-readable name to ease identification and discoverability for human users

    === "Example"
        ``` yaml     
        "Object Detection Algorithm for detection of faulty weld seams"
        ```

`description`{ #description }
:   **Required**-*String*- a short, human-readable description of the Algorithm to aid a human user in analysing the Algorithm’s capabilities and its applicability to a certain problem

    === "Example"
        ``` yaml     
        "This algorithm can be used to solve a specifc problem, and applies some fancy technologies."
        ```

`classificationSchema`{ #classificationschema }
:   **Required**-*Enumeration ["Simulation", "ML", "others"]*- the classification of the Algorithm, to describe the specialization area

    === "Example"
        ``` yaml     
        "ML"
        ```

`type`{ #type }
:   **Required**-*List[String]*- a detailed list of attributes to describe the Algorithm’s field of application

    === "Example"
        ``` yaml     
        ["neural network", "deep learning", "convolutional neural network", "CNN"]
        ```

`version `{ #version- }
:   **Optional**-*String*- the version, as defined by the provider
    === "Example"
        ``` yaml     
        "1.0"
        ```


### Algorithm


`listOfMicroservices`{ #listofmicroservices }
:   **Required**-*List[String]*- a list of Microservice Asset IDs, which are contained in the algorithm

    === "Example"
        ``` yaml     
        ["MSID_MYMS_A", "MSID_MYMS_B"]
        ```

`deploymentMapping`{ #deploymentmapping }
:   **Required**-*Map[String, String]*- a mapping specifying which microservice should run on which host. By default each microservice is assigned a respective host, but this behaviour is not always ideal (eg. when two or more Microservices may need to run on the same host)

    === "Example"
        ``` yaml     
        {"MSID_MYMS_A": "HOSTID_MYHOST_A", "MSID_MYMS_B": "HOSTID_MYHOST_A"}
        ```
