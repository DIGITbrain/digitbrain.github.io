<style>
  .md-content__button {
    display: none;
  }
</style>
# Metrics Fields




The specification for Metrics
has these fields:


`name`{ #name }

:   **Optional**-*String*<br>
    short name (should be unique across the Microservice's metrics)


    === "Example"
        ``` yaml     
        "meanTemperature"
        ```


`corresponding_measurement`{ #corresponding-measurement }

:   **Optional**-*String*<br>
    identification of the corresponding measurement, i.e. output of the Model


    === "Example"
        ``` yaml     
        "temperature1"
        ```


`function`{ #function }

:   **Optional**-*String*<br>
    short description of the mathematical approach used to derive this value


    === "Example"
        ``` yaml     
        "arithmetic mean"
        ```


`unit`{ #unit }

:   **Optional**-*String*<br>
    the unit of the metric measurement


    === "Example"
        ``` yaml     
        "degree celsius"
        ```


`description`{ #description }

:   **Optional**-*String*<br>
    short description of the metric measurement


    === "Example"
        ``` yaml     
        "This metric describes the arithmetic mean of the approximated temperatures of the fabricated part when it leaves station 4."
        ```

