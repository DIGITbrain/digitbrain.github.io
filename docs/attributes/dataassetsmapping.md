<style>
  .md-content__button {
    display: none;
  }
</style>
# DataAssetsMapping Fields

**This information is also available in [table format](/tables/dataassetsmapping/)**


## Available Fields 

The metadata specification for a DIGITbrain DataAssetsMapping
has these sections:

- [DataAssetsMapping](#dataassetsmapping)


### *This substructure is part of [DMA Tuple](dma_tuple.md)*



### DataAssetsMapping


`*MICROSERVICE_ID* `{ #microservice_id- }
:   **Required**-*Map<String, UUID>*- The key(s) in this substructure are UUID string(s) corresponding to the ID(s) of the Microservice(s)making up the included Algorithm. <br> The value for this key is a mapping of Data Resources to Data Assets.

    === "Example"
        ``` yaml     
        "microservice_0db_uuid": { 
              "my_dataresource": "data_9d8_uuid", 
              "new_dataresource": "data_aij_uuid" 
             }
        ```

    `*DATA_RESOURCE_ID* `{ #data_resource_id- }
:   **Required**-*UUID*- Nested below each Microservice, these key(s) are the String identifier(s) of the Data Resource(s) of each Microservice. <br> The value for each key is the UUID of the Data Asset that corresponds to it.

        === "Example"
            ``` yaml     
            See above
            ```
