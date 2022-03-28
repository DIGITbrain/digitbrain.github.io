<style>
  .md-content__button {
    display: none;
  }
</style>
# Outputs Fields

**This information is also available in [table format](/tables/outputs/)**


## Available Fields 

The metadata specification for a DIGITbrain Outputs
has these sections:

- [Outputs](#outputs)


### Outputs


`Key`{ #key }
:   **Optional**-*string*- Group key (eg. type and name) of the output
    === "Example"
        ``` yaml     
        "MY_INSLO_A"
        ```

`Name`{ #name }
:   **Optional**-*string*- Human-readable name of the output
    === "Example"
        ``` yaml     
        ModelABC
        ```

`Dimensions`{ #dimensions }
:   **Optional**-*number*- Number of dimensions of the output (i.e. scalar, vector field)
    === "Example"
        ``` yaml     
        112
        ```

`Is-continuous`{ #is-continuous }
:   **Optional**-*boolean*- Continuous or discreet output
    === "Example"
        ``` yaml     
        true
        ```

`Units`{ #units }
:   **Optional**-*obj (see subkeys below)*- Values related to the output measurement units

    `Unit`{ #unit }
:   **Optional**-*string*- Units of the output (e.g Pa, m/s, etc…)
        === "Example"
            ``` yaml     
            "Pa"
            ```

    `Exponent`{ #exponent }
:   **Optional**-*array of number*- eg. exponents for kg (SI) {1, -2, 0, 0, 0, 0, 1}
        === "Example"
            ``` yaml     
            [1, -2, 0, 0]
            ```

    `Offset`{ #offset }
:   **Optional**-*number*- scale offset if needed (e.g. K to C conversion)
        === "Example"
            ``` yaml     
            442
            ```

    `Scale`{ #scale }
:   **Optional**-*number*- Order of magnitude of the measurement unit scale e.g. Scale is equal to 10^-3 for values expressed in mm
        === "Example"
            ``` yaml     
            10^-3
            ```

`Default-value`{ #default-value }
:   **Optional**-*number*- Default value for the output
    === "Example"
        ``` yaml     
        55
        ```

`Ranges`{ #ranges }
:   **Optional**-*array of number*- Max and min value of the output
    === "Example"
        ``` yaml     
        [1,120]
        ```
