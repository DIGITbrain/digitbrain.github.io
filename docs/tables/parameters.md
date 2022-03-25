
<style>
  .md-content__button {
    display: none;
  }
</style>

**This information is also available in** **[list format](/attributes/parameters/)**

| Concept    | Key          | Subkey   | Type                        | Example Value                                                                                                     | Comment                                                                               | Condition   |
|:-----------|:-------------|:---------|:----------------------------|:------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------|:------------|
| Parameters |              |          |                             |                                                                                                                   |                                                                                       |             |
|            | name         |          | String                      | "detection_threshold"                                                                                             | short name for this parameter (should be unique across the Microservice’s parameters) | mandatory   |
|            | type         |          | Enumeration [xsd datatypes] | "Integer"                                                                                                         | expected input type (may be used to verify the input)                                 | mandatory   |
|            | mandatory    |          | Boolean                     | true                                                                                                              | whether this parameter is mandatory (default: false)                                  | optional    |
|            | defaultValue |          | has to match "type"         | 42                                                                                                                | a default value, if the parameter is required but not provided                        | optional    |
|            | description  |          | String                      | "This parameter can be used to configure the included algorithm in a certain way, possible values: 'A', 'B', 'Z'" | short description of the parameter and its possible values                            | mandatory   |
|            |              |          |                             |                                                                                                                   |                                                                                       |             |