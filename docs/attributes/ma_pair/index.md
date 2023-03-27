<style>
  .md-content__button {
    display: none;
  }
</style>
# Behaviour Fields


**For a more condensed summary this information is available in [table view](/tables/ma_pair/)**



The specification for Behaviour
has these fields:

`version`{ #version }

:   **Optional**-*string*- Version number of the MA Pair, defined by the provider



    === "Example"
        ``` yaml     
        "0.21.0"
        ```

`licensor`{ #licensor }

:   **Required**-*string*- Identifier of the Legal Entity licensing the MA Pair (NB: Entity for Licensor is referenced)



    === "Example"
        ``` yaml     
        legal_entity_123e4567-e89b-12d3 (auto)
        ```

`derivation`{ #derivation }

:   **Required**-*string*- In case of derivation, references to parent / child (optional)



    === "Example"
        ``` yaml     
        ma_pair_123e4567-e89b-12d3 (auto)
        ```

`name`{ #name }

:   **Required**-*string*- Short name to identify the MA Pair



    === "Example"
        ``` yaml     
        Pressure drop
        ```

`scope`{ #scope }

:   **Required**-*string*- Short description of the scope of the MA Pair (human readable)



    === "Example"
        ``` yaml     
        Effectiveness of the mold closing process
        ```

`ip_family`{ #ip_family }

:   **Required**-*string*- Identifier of the IP Family the MA Pair is valid for



    === "Example"
        ``` yaml     
        ip_family_123e4567-e89b-12d3
        ```

`namespace`{ #namespace }

:   **Optional**-*string*- Context to interpret the associated information (optional?)



    === "Example"
        ``` yaml     
        namespace_123e4567-e89b-12d3
        ```

`m_asset`{ #m_asset }

:   **Required**-*string*- Identifier of the Model Asset associated to the MA Pair (NB: The corresponding model file is indicated in Model metadata (first tab) as Model_URI and the corresponding zip file needs to be served to the Algorithm to evaluate the Model by the Microservice (MODEL_FILENAME))


    Note:
    This is a Foreign Key to `microservice.id`.<fk table='microservice' column='id'/>


    === "Example"
        ``` yaml     
        "MODID_MYMODEL"
        ```

`a_asset`{ #a_asset }

:   **Required**-*string*- Identifiers of the Algorithm Asset associated to the MA Pair


    Note:
    This is a Foreign Key to `algorithm.id`.<fk table='algorithm' column='id'/>


    === "Example"
        ``` yaml     
        "ALGID_MYALG"
        ```

`rules`{ #rules }

:   **Optional**-*string[]*- References to recommended Rules to be verified per Evaluation of the MA Pair



    === "Example"
        ``` yaml     
        rules_123e4567-e89b-12d3
        ```

`frequency`{ #frequency }

:   **Optional**-*integer*- Recommended number of evaluations conducted per hour for the MA Pair (optional)



    === "Example"
        ``` yaml     
        12
        ```

`payload`{ #payload }

:   **Optional**-*string*- User-defined key-value pairs: JSON string with additional information (optional)



    === "Example"
        ``` yaml     
        {‘minPressure’: 90, ‘maxPressure’: 120}
        ```

