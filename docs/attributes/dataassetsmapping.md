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


### DataAssetsMapping


`*MICROSERVICE_ID* `{ #microservice_id- }
:   **Required**-*Map[String, String]*- The key(s) here are UUID string(s) corresponding to the ID(s) of the Microservice(s) defined for this Algorithm. <br> The value for this key is a mapping of the logical IDs of Data Assets to the UUIDs of Data Assets.


    `*DATA_ID_LOGICAL* `{ #data_id_logical- }
:   **Required**-*String*- The key(s) here are logical IDs (string identifiers) of Data Assets that act as placeholders in the DeploymentData field of a Microservice. <br> The value for each key is the UUID of the Data Asset that should be substituted into the placeholders in the DeploymentData field.

        === "Example"
            ``` yaml     
            "DATAID_MYDATA_A"
            ```
