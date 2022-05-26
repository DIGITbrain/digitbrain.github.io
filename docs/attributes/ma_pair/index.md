<style>
  .md-content__button {
    display: none;
  }
</style>
# MA Pair Fields

**This information is also available in [table format](/tables/ma_pair/)**


## Available Fields 

The metadata specification for a DIGITbrain MA Pair
has these sections:

- [Administrative Data](#administrative-data)
- [Definition](#definition)


### Administrative Data


`ID`{ #id }
:   **Auto-generated**-*ID*- Unique identifier of the asset.

    === "Example"
        ``` yaml     
        "MAID_MYMA"
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

`BUILD`{ #build }
:   **Auto-generated**-*Integer*- Build number, incremented automatically to provide versioning for the asset

    === "Example"
        ``` yaml     
        21
        ```

`DATE`{ #date }
:   **Auto-generated**-*DATE (ISO 8601)*- Date of asset registration.

    === "Example"
        ``` yaml     
        2022-04-28T08:11:53+00:00
        ```


### Definition


`Version`{ #version }
:   **Optional**-*String*- Version number of the MA Pair, defined by the provider
    === "Example"
        ``` yaml     
        "0.21.0"
        ```

`Licensor`{ #licensor }
:   **Auto-generated**-*UUID*- Identifier of the Legal Entity licensing the MA Pair (NB: Entity for Licensor is referenced)

    === "Example"
        ``` yaml     
        legal_entity_123e4567-e89b-12d3 (auto)
        ```

`Derivation`{ #derivation }
:   **Auto-generated**-*UUID*- In case of derivation, references to parent / child (optional)

    === "Example"
        ``` yaml     
        ma_pair_123e4567-e89b-12d3 (auto)
        ```

`Name`{ #name }
:   **Required**-*Text*- Short name to identify the MA Pair

    === "Example"
        ``` yaml     
        Pressure drop
        ```

`Scope`{ #scope }
:   **Required**-*Text*- Short description of the scope of the MA Pair (human readable)

    === "Example"
        ``` yaml     
        Effectiveness of the mold closing process
        ```

`IP Family`{ #ip-family }
:   **Required**-*UUID*- Identifier of the IP Family the MA Pair is valid for

    === "Example"
        ``` yaml     
        ip_family_123e4567-e89b-12d3
        ```

`Namespace`{ #namespace }
:   **Optional**-*UUID?*- Context to interpret the associated information (optional?)
    === "Example"
        ``` yaml     
        namespace_123e4567-e89b-12d3
        ```

`M Asset`{ #m-asset }
:   **Required**-*UUID*- Identifier of the Model Asset associated to the MA Pair (NB: The corresponding model file is indicated in Model metadata (first tab) as Model_URI and the corresponding zip file needs to be served to the Algorithm to evaluate the Model by the Microservice (MODEL_FILENAME))

    === "Example"
        ``` yaml     
        "MODID_MYMODEL"
        ```

`A Asset`{ #a-asset }
:   **Required**-*UUID*- Identifiers of the Algorithm Asset associated to the MA Pair

    === "Example"
        ``` yaml     
        "ALGID_MYALG"
        ```

`Rules`{ #rules }
:   **Optional**-*UUIDs*- References to recommended Rules to be verified per Evaluation of the MA Pair
    === "Example"
        ``` yaml     
        rules_123e4567-e89b-12d3
        ```

`Frequency`{ #frequency }
:   **Optional**-*Integer*- Recommended number of evaluations conducted per hour for the MA Pair (optional)
    === "Example"
        ``` yaml     
        12
        ```

`Payload`{ #payload }
:   **Optional**-*String*- User-defined key-value pairs: JSON string with additional information (optional)
    === "Example"
        ``` yaml     
        {‘minPressure’: 90, ‘maxPressure’: 120}
        ```
