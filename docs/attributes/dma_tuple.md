# DMA Tuple Metadata Specification

## Available Fields 

The metadata specification for a DIGITbrain DMA Tuple
has these sections:

- [Definition](#definition)


### Definition

An optional description for the Definition section may appear here. 

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

:   **Auto-generated**-*Integer*- Version number of the DMA Tuple
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

:   **Auto-generated**-*Text*- Short name to identify the DMA Tuple
    === "Example"
        ``` yaml     
        Name: Pressure drop for the injection in hall 3
        ```

`Scope`

:   **Auto-generated**-*Text*- Short description of the scope of the DMA Tuple (human readable)
    === "Example"
        ``` yaml     
        Scope: Effectiveness of the mold closing process
        ```

`IP Instance`

:   **Auto-generated**-*ID / URI*- Identifier of the IP Instance the DMA Tuple is valid for (NB: Entity for IP Instance is referenced)
    === "Example"
        ``` yaml     
        IP Instance: ip_instance_123e4567-e89b-12d3
        ```

`Namespace`

:   **Auto-generated**-*ID / URI?*- Context to interpret the associated information (optional?)
    === "Example"
        ``` yaml     
        Namespace: namespace_123e4567-e89b-12d3
        ```

`MA Pair`

:   **Auto-generated**-*ID / URI*- Identifier of the MA Pair associated to the DMA Tuple
    === "Example"
        ``` yaml     
        MA Pair: ma_pair_123e4567-e89b-12d3
        ```

`D Assets`

:   **Auto-generated**-*IDs / URIs*- Identifiers of the Data Assets associated to the DMA Tuple
    === "Example"
        ``` yaml     
        D Assets: data_123e4567-e89b-12d3
        ```

`Deployments`

:   **Auto-generated**-*See "Deployments"*- Characteristics of the Deployment for every Microservice associated to the DMA Tuple (NB: Entities for the available deployment infrastructures to be provided by DB Solution and selected for DMA Tuple. No deployment entity metadata structure currently exists)
    === "Example"
        ``` yaml     
        Deployments: deployments_123e4567-e89b-12d3
        ```

`Schedule`

:   **Auto-generated**-*Dates*- Days and hours the DMA Tuple will be active (optional)
    === "Example"
        ``` yaml     
        Schedule: R90/2021-05-01T00:00:00Z/PT48H
        ```

`Payload`

:   **Auto-generated**-*String*- User-defined key-value pairs: JSON string with additional information (optional)
    === "Example"
        ``` yaml     
        Payload: {‘injectionMold’: ‘Circuit Case’}
        ```
