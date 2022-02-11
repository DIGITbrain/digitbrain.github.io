<style>
  .md-content__button {
    display: none;
  }
</style>
# MA Pair Metadata Fields

**This information is also available in [table format](/tables/ma_pair/)**


## Available Fields 

The metadata specification for a DIGITbrain MA Pair
has these sections:

- [Definition](#definition)


### Definition


`ID`
:   **Auto-generated**-*UUID*- Unique identifier for the MA Pair

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
:   **Optional**-*Integer*- Version number of the MA Pair
    === "Example"
        ``` yaml     
        Version: 21
        ```

`Author`
:   **Auto-generated**-*UUID*- Identifier of the Author of the MA Pair (NB: Entity for author is referenced)

    === "Example"
        ``` yaml     
        Author: person_123e4567-e89b-12d3 (auto)
        ```

`Licensor`
:   **Auto-generated**-*UUID*- Identifier of the Legal Entity licensing the MA Pair (NB: Entity for Licensor is referenced)

    === "Example"
        ``` yaml     
        Licensor: legal_entity_123e4567-e89b-12d3 (auto)
        ```

`Derivation`
:   **Auto-generated**-*UUID*- In case of derivation, references to parent / child (optional)

    === "Example"
        ``` yaml     
        Derivation: ma_pair_123e4567-e89b-12d3 (auto)
        ```

`Name`
:   **Optional**-*Text*- Short name to identify the MA Pair
    === "Example"
        ``` yaml     
        Name: Pressure drop
        ```

`Scope`
:   **Optional**-*Text*- Short description of the scope of the MA Pair (human readable)
    === "Example"
        ``` yaml     
        Scope: Effectiveness of the mold closing process
        ```

`IP Family`
:   **Optional**-*UUID*- Identifier of the IP Family the MA Pair is valid for
    === "Example"
        ``` yaml     
        IP Family: ip_family_123e4567-e89b-12d3
        ```

`Namespace`
:   **Optional**-*UUID?*- Context to interpret the associated information (optional?)
    === "Example"
        ``` yaml     
        Namespace: namespace_123e4567-e89b-12d3
        ```

`M Asset`
:   **Optional**-*UUID*- Identifier of the Model Asset associated to the MA Pair (NB: The corresponding model file is indicated in Model metadata (first tab) as Model_URI and the corresponding zip file needs to be served to the Algorithm to evaluate the Model by the Microservice (MODEL_FILENAME))
    === "Example"
        ``` yaml     
        M Asset: model_123e4567-e89b-12d3
        ```

`A Asset`
:   **Optional**-*UUID*- Identifiers of the Algorithm Asset associated to the MA Pair
    === "Example"
        ``` yaml     
        A Asset: algorithm_123e4567-e89b-12d3
        ```

`Rules`
:   **Optional**-*UUIDs*- References to recommended Rules to be verified per Evaluation of the MA Pair
    === "Example"
        ``` yaml     
        Rules: rules_123e4567-e89b-12d3
        ```

`Frequency`
:   **Optional**-*Integer*- Recommended number of evaluations conducted per hour for the MA Pair (optional)
    === "Example"
        ``` yaml     
        Frequency: 12
        ```

`Payload`
:   **Optional**-*String*- User-defined key-value pairs: JSON string with additional information (optional)
    === "Example"
        ``` yaml     
        Payload: {‘minPressure’: 90, ‘maxPressure’: 120}
        ```
