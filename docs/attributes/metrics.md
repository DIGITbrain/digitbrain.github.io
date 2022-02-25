<style>
  .md-content__button {
    display: none;
  }
</style>
# Metrics Fields

**This information is also available in [table format](/tables/metrics/)**


## Available Fields 

The metadata specification for a DIGITbrain Metrics
has these sections:

- [Metrics](#metrics)


### Metrics


`name`{ #name }
:   **Required**-*String*- short name (should be unique across the Microservice's metrics)

    === "Example"
        ``` yaml     
        meanTemperature
        ```

`correspondingMeasurement`{ #correspondingmeasurement }
:   **Required**-*String*- identification of the corresponding measurement, i.e. output of the Model

    === "Example"
        ``` yaml     
        temperature1
        ```

`function`{ #function }
:   **Required**-*String*- short description of the mathematical approach used to derive this value

    === "Example"
        ``` yaml     
        arithmetic mean
        ```

`unit`{ #unit }
:   **Required**-*String*- the unit of the metric measurement

    === "Example"
        ``` yaml     
        degree celsius
        ```

`description`{ #description }
:   **Required**-*String*- short description of the metric measurement

    === "Example"
        ``` yaml     
        This metric describes the arithmetic mean of the approximated temperatures of the fabricated part when it leaves station 4.
        ```
