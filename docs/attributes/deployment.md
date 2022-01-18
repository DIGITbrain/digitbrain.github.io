# Deployment Metadata Specification

## Available Fields 

The metadata specification for a DIGITbrain Deployment
has these sections:

- [Description](#description)
- [Deployments](#deployments)
- [Data Source Mapping](#data-source-mapping)


### Description

An optional description for the Description section may appear here. 

`id`

:   **Auto-generated**-*UUID*- DIGITbrain reference
    === "Example"
        ``` yaml     
        id: nan
        ```

`name `

:   **Required**-*String*- Short name for the node/device

    === "Example"
        ``` yaml     
        name : nan
        ```

`author `

:   **Required**-*String*- Created by

    === "Example"
        ``` yaml     
        author : nan
        ```

`date`

:   **Auto-generated**-*Date*- Created on
    === "Example"
        ``` yaml     
        date: nan
        ```


### Deployments

An optional description for the Deployments section may appear here. 

`type`

:   **Required**-*Enumeration {cloudbroker, edge}*- computing centre

    === "Example"
        ``` yaml     
        type: nan
        ```

`cloudbroker`

:   **Auto-generated**-*Map of…*- nan
    === "Example"
        ``` yaml     
        cloudbroker: nan
        ```

`deployment_id`

:   **Auto-generated**-*UUID*- ID of CloudBroker Deployment
    === "Example"
        ``` yaml     
        deployment_id: nan
        ```

`instance_type_id`

:   **Auto-generated**-*UUID*- ID of CloudBroker InstanceType
    === "Example"
        ``` yaml     
        instance_type_id: nan
        ```

`key_pair_id`

:   **Auto-generated**-*UUID*- ID of CloudBroker Key Pair
    === "Example"
        ``` yaml     
        key_pair_id: nan
        ```

`opened_port`

:   **Auto-generated**-*String (comma separated integers)*- Ports to open at cloud side
    === "Example"
        ``` yaml     
        opened_port: nan
        ```

`endpoint`

:   **Auto-generated**-*URL*- accesible IP or FQDN of edge device
    === "Example"
        ``` yaml     
        endpoint: nan
        ```

`edge`

:   **Auto-generated**-*Map of…*- nan
    === "Example"
        ``` yaml     
        edge: nan
        ```


### Data Source Mapping

An optional description for the Data Source Mapping section may appear here. 

`data_source_mapping`

:   **Optional**-*Map of…*- nan

    === "Example"
        ``` yaml     
        data_source_mapping: nan
        ```

`microserviceA_data`

:   **Auto-generated**-*List of UUIDs*- UUIDs of required data sources for MicroserviceA
    === "Example"
        ``` yaml     
        microserviceA_data: nan
        ```

`microserviceB_data`

:   **Auto-generated**-*List of UUIDs*- UUIDs of required data sources for MicroserviceB
    === "Example"
        ``` yaml     
        microserviceB_data: nan
        ```

`microserviceC_data`

:   **Auto-generated**-*List of UUIDs*- UUIDs of required data sources for MicroserviceC
    === "Example"
        ``` yaml     
        microserviceC_data: nan
        ```
