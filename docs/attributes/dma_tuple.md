<style>
  .md-content__button {
    display: none;
  }
</style>
# DMA Tuple Fields

**This information is also available in [table format](/tables/dma_tuple/)**


## Available Fields 

The metadata specification for a DIGITbrain DMA Tuple
has these sections:

- [Definition](#definition)


### Definition


`ID`
:   **Auto-generated**-*ID / URI*- Unique identifier for the DMA Tuple

    === "Example"
        ``` yaml     
        ID: 123e4567-e89b-12d3-a456-426614174000
        ```

`Created at`
:   **Auto-generated**-*ISO 8601*- Date of creation

    === "Example"
        ``` yaml     
        Created at: 2021-05-01T00:00:00Z
        ```

`Version`
:   **Optional**-*Integer*- Version number of the DMA Tuple
    === "Example"
        ``` yaml     
        Version: 21
        ```

`Author`
:   **Auto-generated**-*ID / URI*- Identifier of the Author of the MA Pair (NB: Entity for author is referenced)

    === "Example"
        ``` yaml     
        Author: person_123e4567-e89b-12d3 (auto)
        ```

`Licensor`
:   **Auto-generated**-*ID / URI*- Identifier of the Legal Entity licensing the the MA Pair (NB: Entity for Licensor is referenced)

    === "Example"
        ``` yaml     
        Licensor: legal_entity_123e4567-e89b-12d3 (auto)
        ```

`Derivation`
:   **Auto-generated**-*IDs / URIs*- In case of derivation, references to parent / child (optional)

    === "Example"
        ``` yaml     
        Derivation: dma_tuple_123e4567-e89b-12d3 (auto)
        ```

`Name`
:   **Optional**-*Text*- Short name to identify the DMA Tuple
    === "Example"
        ``` yaml     
        Name: Pressure drop for the injection in hall 3
        ```

`Scope`
:   **Optional**-*Text*- Short description of the scope of the DMA Tuple (human readable)
    === "Example"
        ``` yaml     
        Scope: Effectiveness of the mold closing process
        ```

`IP Instance`
:   **Optional**-*ID / URI*- Identifier of the IP Instance the DMA Tuple is valid for (NB: Entity for IP Instance is referenced)
    === "Example"
        ``` yaml     
        IP Instance: ip_instance_123e4567-e89b-12d3
        ```

`Namespace`
:   **Optional**-*ID / URI?*- Context to interpret the associated information (optional?)
    === "Example"
        ``` yaml     
        Namespace: namespace_123e4567-e89b-12d3
        ```

`MA Pair`
:   **Optional**-*ID / URI*- Identifier of the MA Pair associated to the DMA Tuple
    === "Example"
        ``` yaml     
        MA Pair: ma_pair_123e4567-e89b-12d3
        ```

`DataAssetsMapping`
:   **Optional**-*Map*- Mapping the available Data assets in this DMA Tuple to available Microservices. Required if Data assets are required. Not all microservices need a Data asset.
    === "Example"
        ``` yaml     
        DataAssetsMapping: { "microserviceA_ID": "data_123e4567-e89b-12d3", "microserviceB_ID": "data_234e4567-e89b-23d4"}
        ```

    `microserviceA_ID`
:   **Optional**-*nan*- 1:1 relationship between a Microservice and a Data asset, specified by their IDs
        === "Example"
            ``` yaml     
            microserviceA_ID: data_123e4567-e89b-12d3
            ```

`Deployments`
:   **Optional**-*See "Deployments"*- Characteristics of the Deployment for every Microservice associated to the DMA Tuple (NB: Entities for the available deployment infrastructures to be provided by DB Solution and selected for DMA Tuple. No deployment entity metadata structure currently exists)
    === "Example"
        ``` yaml     
        Deployments: deployments_123e4567-e89b-12d3
        ```

`Schedule`
:   **Optional**-*Dates*- Days and hours the DMA Tuple will be active (optional)
    === "Example"
        ``` yaml     
        Schedule: R90/2021-05-01T00:00:00Z/PT48H
        ```

`Payload`
:   **Optional**-*String*- User-defined key-value pairs: JSON string with additional information (optional)
    === "Example"
        ``` yaml     
        Payload: {‘injectionMold’: ‘Circuit Case’}
        ```
