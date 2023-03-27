<style>
  .md-content__button {
    display: none;
  }
</style>
# Slots Fields




The metadata specification for a DIGITbrain Slots
has these fields:

`key`{ #key }

:   **Optional**-*string*- unique (within a Model) machine-readable identifier matching [a-zA-Z_][a-zA-Z_0-9]*


    === "Example"
        ``` yaml     
        force_1
        ```

`name`{ #name }

:   **Optional**-*string*- Human-readable identifier


    === "Example"
        ``` yaml     
        Force at Boundary Condition 1
        ```

`dimensions`{ #dimensions }

:   **Optional**-*integer*- 

`is_continuous`{ #is_continuous }

:   **Optional**-*bool, default is true (real)*- flag to indicate whether slot values are integer or real numbers


    === "Example"
        ``` yaml     
        true
        ```

`units`{ #units }

:   **Optional**-*obj (see subkeys below)*- Values related to the slot measurement units

`default_value`{ #default_value }

:   **Optional**-*integer*- 

`ranges`{ #ranges }

:   **Optional**-*integer[]*- 

