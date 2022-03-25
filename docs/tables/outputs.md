
<style>
  .md-content__button {
    display: none;
  }
</style>

**This information is also available in** **[list format](/attributes/outputs/)**

| Concept   | Key           | Subkey   | Type                    | Example Value   | Comment                                                                                                  | Condition   |
|:----------|:--------------|:---------|:------------------------|:----------------|:---------------------------------------------------------------------------------------------------------|:------------|
| Outputs   |               |          |                         |                 |                                                                                                          |             |
|           | Key           |          | string                  | "MY_INSLO_A"    | Group key (eg. type and name) of the output                                                              | optional    |
|           | Name          |          | string                  | ModelABC        | Human-readable name of the output                                                                        | optional    |
|           | Dimensions    |          | number                  | 112             | Number of dimensions of the output (i.e. scalar, vector field)                                           | optional    |
|           | Is-continuous |          | boolean                 | true            | Continuous or discreet output                                                                            | optional    |
|           | Units         |          | obj (see subkeys below) |                 | Values related to the output measurement units                                                           | optional    |
|           |               | Unit     | string                  | "Pa"            | Units of the output (e.g Pa, m/s, etc…)                                                                  | optional    |
|           |               | Exponent | array of number         | [1, -2, 0, 0]   | eg. exponents for kg (SI) {1, -2, 0, 0, 0, 0, 1}                                                         | optional    |
|           |               | Offset   | number                  | 442             | scale offset if needed (e.g. K to C conversion)                                                          | optional    |
|           |               | Scale    | number                  | 10^-3           | Order of magnitude of the measurement unit scale e.g. Scale is equal to 10^-3 for values expressed in mm | optional    |
|           | Default-value |          | number                  | 55              | Default value for the output                                                                             | optional    |
|           | Ranges        |          | array of number         | [1,120]         | Max and min value of the output                                                                          | optional    |
|           |               |          |                         |                 |                                                                                                          |             |