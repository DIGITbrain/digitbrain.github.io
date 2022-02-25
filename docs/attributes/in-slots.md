<style>
  .md-content__button {
    display: none;
  }
</style>
# In-slots Fields

**This information is also available in [table format](/tables/in-slots/)**


## Available Fields 

The metadata specification for a DIGITbrain In-slots
has these sections:

- [In-slots](#in-slots)


### In-slots


`Key`{ #key }
:   **Optional**-*string*- Group key (eg. type and name) of the in-slot

`Name`{ #name }
:   **Optional**-*string*- Human-readable name of the in-slot

`Dimensions`{ #dimensions }
:   **Optional**-*number*- Number of dimensions of the in-slot (i.e. scalar, vector field)

`Is-continuous`{ #is-continuous }
:   **Optional**-*boolean*- continuous or discreet in-slot

`Units`{ #units }
:   **Optional**-*obj (see subkeys below)*- Values related to the in-slot measurement units

    `Unit`{ #unit }
:   **Optional**-*string*- Units of the in-slot (e.g Pa, m/s, etc…)

    `Exponent`{ #exponent }
:   **Optional**-*array of number*- eg. exponents for kg (SI) {1, -2, 0, 0, 0, 0, 1}

    `Offset`{ #offset }
:   **Optional**-*number*- scale offset if needed (e.g. K to C conversion)

    `Scale`{ #scale }
:   **Optional**-*number*- Order of magnitude of the measurement unit scale e.g. Scale is equal to 10^-3 for values expressed in mm

`Default-value`{ #default-value }
:   **Optional**-*number*- Default value for the in-slot

`Ranges`{ #ranges }
:   **Optional**-*array of number*- Max and min value of the in-slot
