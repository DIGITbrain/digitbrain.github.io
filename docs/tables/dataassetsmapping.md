
<style>
  .md-content__button {
    display: none;
  }
</style>

**This information is also available in** **[list format](/attributes/dataassetsmapping/)**

| Concept           | Key               | Subkey           | Type              | Example Value                                                                                                      | Comment                                                                                                                                                                                                        | Condition   |
|:------------------|:------------------|:-----------------|:------------------|:-------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------|
| DataAssetsMapping |                   |                  |                   |                                                                                                                    |                                                                                                                                                                                                                |             |
|                   | *MICROSERVICE_ID* |                  | Map<String, UUID> | "microservice_0db_uuid": { <br>  "datasource_89d": "data_9d8_uuid", <br>  "datasource_dlo": "data_aij_uuid" <br> } | The key(s) in this substructure are UUID string(s) corresponding to the ID(s) of the Microservice(s)making up the included Algorithm. <br> The value for this key is a mapping of Data Sources to Data Assets. | mandatory   |
|                   |                   | *DATA_SOURCE_ID* | UUID              | See above                                                                                                          | Nested below each Microservice, these key(s) are the String identifier(s) of the Data Source(s) of each Microservice. <br> The value for each key is the UUID of the Data Asset that corresponds to it.        | mandatory   |