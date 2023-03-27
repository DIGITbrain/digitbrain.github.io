<style>
  .md-content__button {
    display: none;
  }
</style>
# Slots Fields




The specification for Slots
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

:   **Optional**-*number (integer-valued) | array of integer-valued numbers, default is 1 (scalar)*- dimension of inputs to in-slot, array of dimensions for matrices / tensors


    === "Example"
        ``` yaml     
        1
        ```

`is_continuous`{ #is_continuous }

:   **Optional**-*bool, default is true (real)*- flag to indicate whether slot values are integer or real numbers


    === "Example"
        ``` yaml     
        true
        ```

`units`{ #units }

:   **Optional**-*obj (see subkeys below)*- Values related to the slot measurement units

`default_value`{ #default_value }

:   **Optional**-*number | null*- default value for in-slot, if null then the value for the in-slot needs
    to be set/fed at a later point in time.

    Default value must not be set for out-slots!


`ranges`{ #ranges }

:   **Optional**-*array | null*- valid range of values (2-tuple array minimum maximum values OR array of discrete valid scalars).<br>If a valid range is not known a-priori: null / omitted

