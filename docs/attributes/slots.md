<style>
  .md-content__button {
    display: none;
  }
</style>
# Slots Fields




The specification for Slots
has these fields:


`key`{ #key }

:   **Optional**-*string*<br>
    unique (within a Model) machine-readable identifier matching [a-zA-Z_][a-zA-Z_0-9]*


    === "Example"
        ``` yaml     
        force_1
        ```


`name`{ #name }

:   **Optional**-*string*<br>
    Human-readable identifier


    === "Example"
        ``` yaml     
        Force at Boundary Condition 1
        ```


`dimensions`{ #dimensions }

:   **Optional**-*number (integer-valued) | array of integer-valued numbers, default is 1 (scalar)*<br>
    dimension of inputs to in-slot, array of dimensions for matrices / tensors


    === "Example"
        ``` yaml     
        1
        ```


`is_continuous`{ #is-continuous }

:   **Optional**-*bool, default is true (real)*<br>
    flag to indicate whether slot values are integer or real numbers



    === "Real Numbers"
        ``` yaml     
        True
        ```


    === "Integers"
        ``` yaml     
        False
        ```



`units`{ #units }

:   **Optional**-*[Units](units.md)*<br>
    Values related to the slot measurement units


`default_value`{ #default-value }

:   **Optional**-*number | null*<br>
    default value for in-slot, if null then the value for the in-slot
    needs to be set/fed at a later point in time.

    !!! warning
        
        Default value must not be set for out-slots!



`ranges`{ #ranges }

:   **Optional**-*array | null*<br>
    valid range of values (2-tuple array minimum maximum values OR array of discrete valid scalars).<br>If a valid range is not known a-priori: null / omitted

