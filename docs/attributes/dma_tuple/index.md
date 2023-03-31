<style>
  .md-content__button {
    display: none;
  }
</style>
# Process Fields




The specification for Process
has these fields:


`name`{ #name }

:   **Required**-*string*<br>
    Short name to identify the Process


    === "Example"
        ``` yaml     
        Pressure drop for the injection in hall 3
        ```


`scope`{ #scope }

:   **Required**-*string*<br>
    Short description of the scope of the Process (human readable)


    === "Example"
        ``` yaml     
        Effectiveness of the mold closing process
        ```


`version`{ #version }

:   **Required**-*string*<br>
    Version number of the Process, defined by the provider


    === "Example"
        ``` yaml     
        0.21.0
        ```


`ip_instance`{ #ip-instance }

:   **Required**-*string*<br>
    Identifier of the IP Instance the Process is valid for (NB: Entity for IP Instance is referenced)


    === "Example"
        ``` yaml     
        ip_instance_123e4567-e89b-12d3
        ```


`provider`{ #provider }

:   **Required**-*string*<br>
    Legal entity who provides the asset (owner). It is the affiliation of the author by default.


    === "Example"
        ``` yaml     
        cabd945f-4085-4e34-becd-45ec5a851a9b
        ```


`ma_pair`{ #ma-pair }

:   **Required**-*string*<br>
    Identifier of the Behaviour (MA Pair) associated to the Process


    === "Example"
        ``` yaml     
        MAID_MYMA
        ```


`deployments`{ #deployments }

:   **Required**-*[Deployment](../deployment.md)*<br>
    Mapping of characteristics of the Deployment (i.e. Cloud or Edge infrastructure) for every Microservice associated to the Process


`data_assets_mapping`{ #data-assets-mapping }

:   **Optional**-*[DataAssetsMapping](../dataassetsmapping.md)*<br>
    Mapping required Data assets to Microservices specified in the Behaviour (MA Pair). Not every Microservice needs a Data asset.


`namespace`{ #namespace }

:   **Optional**-*string*<br>
    Context to interpret the associated information


    === "Example"
        ``` yaml     
        namespace_123e4567-e89b-12d3
        ```


`payload`{ #payload }

:   **Optional**-*string (JSON)*<br>
    User-defined key-value pairs with additional information


    === "Example"
        ``` yaml     
        {"injectionMold": "Circuit Case"}

        ```


`schedule`{ #schedule }

:   **Optional**-*string*<br>
    Days and hours the Process will be active


    === "Example"
        ``` yaml     
        R90/2021-05-01T00:00:00Z/PT48H
        ```

