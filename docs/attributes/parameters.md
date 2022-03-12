<style>
  .md-content__button {
    display: none;
  }
</style>
# Parameters Fields

**This information is also available in [table format](/tables/parameters/)**


## Available Fields 

The metadata specification for a DIGITbrain Parameters
has these sections:

- [Parameters](#parameters)


### Parameters


`name`{ #name }
:   **Required**-*String*- short name for this parameter (should be unique across the Microservice’s parameters)

    === "Example"
        ``` yaml     
        "detection_threshold"
        ```

`type`{ #type }
:   **Required**-*Enumeration [xsd datatypes]*- expected input type (may be used to verify the input)

    === "Example"
        ``` yaml     
        "Integer"
        ```

`mandatory`{ #mandatory }
:   **Optional**-*Boolean*- whether this parameter is mandatory (default: false)
    === "Example"
        ``` yaml     
        true
        ```

`defaultValue`{ #defaultvalue }
:   **Optional**-*has to match "type"*- a default value, if the parameter is required but not provided
    === "Example"
        ``` yaml     
        42
        ```

`description`{ #description }
:   **Required**-*String*- short description of the parameter and its possible values

    === "Example"
        ``` yaml     
        "This parameter can be used to configure the included algorithm in a certain way, possible values: 'A', 'B', 'Z'"
        ```
