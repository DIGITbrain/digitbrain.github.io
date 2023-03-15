<style>
  .md-content__button {
    display: none;
  }
</style>
# Slots Fields

**This information is also available in [table format](/tables/slots/)**


## Available Fields 

The metadata specification for a DIGITbrain Slots
has these sections:

- [Slots](#slots)


### Slots


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

`dimension`{ #dimension }
:   **Optional**-*number (integer-valued) | array of integer-valued numbers, default is 1 (scalar)*- dimension of inputs to in-slot, array of dimensions for matrices / tensors
    === "Example"
        ``` yaml     
        1
        ```

`dimension_names`{ #dimension_names }
:   **Optional**-*array of strings matching length of dimension | null*- optional list of concise names of each tensor dimension to indicate expected contents, e.g., "dimension_names": ["batch", "channels", "width", "height"]

`is-continuous`{ #is-continuous }
:   **Optional**-*bool, default is true (real)*- flag to indicate whether slot values are integer or real numbers
    === "Example"
        ``` yaml     
        true
        ```

`units`{ #units }
:   **Optional**-*obj (see subkeys below)*- Values related to the slot measurement units

    `name-of-unit`{ #name-of-unit }
:   **Optional**-*string*- human readable unit symbol, here N for Newton
        === "Example"
            ``` yaml     
            N
            ```

    `exponents`{ #exponents }
:   **Optional**-*array, 7-tuple of integer-valued exponents*- Ordered list of SI base units
          1st entry: Length - meter (m)
          2nd entry: Time - second (s)
          3rd entry: Amount of substance - mole (mol)
          4th entry: Electric current - ampere (A)
          5th entry: Temperature - kelvin (K)
          6th entry: Luminous intensity - candela (cd)
          7th entry: Mass - kilogram (kg)
Explanation: the exponents reference the above SI base units in the corresponding order to describe the unit w.r.t. the base SI units,
the entries [1, -2, 0, 0, 0, 0, 1] thus denote m s⁻² kg, i.e., Newton
        === "Example"
            ``` yaml     
            [1, -2, 0, 0, 0, 0, 1]
            ```

    `offset`{ #offset }
:   **Optional**-*number, default value is 0*- allows to offset the values by adding a constant, e.g., Celsius is offset by 273.15 relative to Kelvin (C + 273.15 = K).
For absolute temperatures only! For temperature *differences*, this must be omitted!

    `scale-factor`{ #scale-factor }
:   **Optional**-*number, default value is 1*- allows to scale the values into base units, e.g., 1e-3 to describe mm (millimeters) in terms of m (meters)
        === "Example"
            ``` yaml     
            1
            ```

`default`{ #default }
:   **Optional**-*number | null*- default value for in-slot, if null then the value for the in-slot needs to be set/fed at a later point in time.
Default value must not be set for out-slots!

`range`{ #range }
:   **Optional**-*array | null*- valid range of values (2-tuple array minimum maximum values OR array of discrete valid scalars).
If a valid range is not known a-priori: null / omitted
