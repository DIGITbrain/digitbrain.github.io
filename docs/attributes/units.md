<style>
  .md-content__button {
    display: none;
  }
</style>
# Units Fields




The specification for Units
has these fields:


`unit`{ #unit }

:   **Optional**-*string*<br>
    human readable unit symbol, here N for Newton


    === "Example"
        ``` yaml     
        N
        ```


`exponent`{ #exponent }

:   **Optional**-*number[]*<br>
    7-tuple of integer-valued exponents*- Ordered list of SI base units

    - 1st entry: Length - meter (m)
    - 2nd entry: Time - second (s)
    - 3rd entry: Amount of substance - mole (mol)
    - 4th entry: Electric current - ampere (A)
    - 5th entry: Temperature - kelvin (K)
    - 6th entry: Luminous intensity - candela (cd)
    - 7th entry: Mass - kilogram (kg)
      
    !!! note "Explanation"

        the exponents reference the above SI base units in the
        corresponding order to describe the unit w.r.t. the base SI units,
        the entries [1, -2, 0, 0, 0, 0, 1] thus denote m s⁻² kg, i.e., Newton



    === "Example"
        ``` yaml     
        [1, -2, 0, 0, 0, 0, 1]
        ```


`offset`{ #offset }

:   **Optional**-*number*<br>
    default value is 0*- allows to offset the values by adding a constant,
    e.g., Celsius is offset by 273.15 relative to Kelvin (C + 273.15 = K).
    !!! warning

        For absolute temperatures only! For temperature
        *differences*, this must be omitted!



`scale`{ #scale }

:   **Optional**-*number*<br>
    default value is 1*- allows to scale the values into base units,
    e.g., 1e-3 to describe mm (millimeters) in terms of m (meters)



    === "Example"
        ``` yaml     
        1
        ```

