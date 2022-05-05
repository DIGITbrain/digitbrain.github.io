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

- [Administrative Data](#administrative-data)
- [Definition](#definition)
- [Data Assets Mapping](#data-assets-mapping)
- [Deployments](#deployments)


### Administrative Data


`ID`{ #id }
:   **Auto-generated**-*ID*- Unique identifier of the asset.

    === "Example"
        ``` yaml     
        "DMAID_MYDMA"
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


### Definition


`Version`{ #version }
:   **Optional**-*Integer*- Version number of the DMA Tuple
    === "Example"
        ``` yaml     
        21
        ```

`Licensor`{ #licensor }
:   **Auto-generated**-*ID / URI*- Identifier of the Legal Entity licensing the the MA Pair (NB: Entity for Licensor is referenced)

    === "Example"
        ``` yaml     
        legal_entity_123e4567-e89b-12d3 (auto)
        ```

`Derivation`{ #derivation }
:   **Auto-generated**-*IDs / URIs*- In case of derivation, references to parent / child (optional)

    === "Example"
        ``` yaml     
        dma_tuple_123e4567-e89b-12d3 (auto)
        ```

`Name`{ #name }
:   **Required**-*Text*- Short name to identify the DMA Tuple

    === "Example"
        ``` yaml     
        Pressure drop for the injection in hall 3
        ```

`Scope`{ #scope }
:   **Required**-*Text*- Short description of the scope of the DMA Tuple (human readable)

    === "Example"
        ``` yaml     
        Effectiveness of the mold closing process
        ```

`IP Instance`{ #ip-instance }
:   **Required**-*ID / URI*- Identifier of the IP Instance the DMA Tuple is valid for (NB: Entity for IP Instance is referenced)

    === "Example"
        ``` yaml     
        ip_instance_123e4567-e89b-12d3
        ```

`Namespace`{ #namespace }
:   **Optional**-*ID / URI?*- Context to interpret the associated information (optional?)
    === "Example"
        ``` yaml     
        namespace_123e4567-e89b-12d3
        ```

`MA Pair`{ #ma-pair }
:   **Required**-*ID / URI*- Identifier of the MA Pair associated to the DMA Tuple

    === "Example"
        ``` yaml     
        "MAID_MYMA"
        ```

`Schedule`{ #schedule }
:   **Optional**-*Dates*- Days and hours the DMA Tuple will be active (optional)
    === "Example"
        ``` yaml     
        R90/2021-05-01T00:00:00Z/PT48H
        ```

`Payload`{ #payload }
:   **Optional**-*String*- User-defined key-value pairs: JSON string with additional information (optional)
    === "Example"
        ``` yaml     
        {‘injectionMold’: ‘Circuit Case’}
        ```


### Data Assets Mapping


`DataAssetsMapping`{ #dataassetsmapping }
:   **Required**-*[DataAssetsMapping](../dataassetsmapping.md)*- Mapping required Data assets to Microservices specified in the MA Pair. Not every Microservice needs a Data asset.

    === "Example"
        ``` yaml     
        {
              "MSID_MYMS_A": {
                "MY_SINK": "DATAID_MYDATA_A",
                "MY_STREAM": "DATAID_MYDATA_B"
              }
            }
        ```


### Deployments


`Deployments`{ #deployments }
:   **Required**-*[Deployment](../deployment.md)*- Mapping of characteristics of the Deployment (i.e. Cloud or Edge infrastructure) for every Microservice associated to the DMA Tuple

    === "Example"
        ``` yaml     
        {
             "A_RISTRA_HOST": {
               "name": "RISTRA_CPU_Deployment",
               "author": "Maxim Redkin",
               "type": "cloudbroker",
               "cloudbroker": {
                 "deployment_id": "16b1e2d4-3a2c-406e-8c45-5637099021f0",
                 "instance_type_id": "ca727925-a5ca-4697-b2c3-8788d82457d5",
                 "key_pair_id": "22873697-c9ec-4685-bddc-760436662bce",
                 "opened_port": "2379,4500,30010,8285,30012,443,10250,30888,30000,6443,22,500,8472,30012,4500,500",
                 "endpoint": "https://cloudsme-cbp.scaletools.com.ua"
              }
             }
            }
        ```
