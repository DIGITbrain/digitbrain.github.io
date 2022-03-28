
<style>
  .md-content__button {
    display: none;
  }
</style>

**This information is also available in** **[list format](/attributes/metrics/)**

| Concept   | Key                      | Subkey   | Type   | Example Value                                                                                                                 | Comment                                                                   | Condition   |
|:----------|:-------------------------|:---------|:-------|:------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------|:------------|
| Metrics   |                          |          |        |                                                                                                                               |                                                                           |             |
|           | name                     |          | String | "meanTemperature"                                                                                                             | short name (should be unique across the Microservice's metrics)           | mandatory   |
|           | correspondingMeasurement |          | String | "temperature1"                                                                                                                | identification of the corresponding measurement, i.e. output of the Model | mandatory   |
|           | function                 |          | String | "arithmetic mean"                                                                                                             | short description of the mathematical approach used to derive this value  | mandatory   |
|           | unit                     |          | String | "degree celsius"                                                                                                              | the unit of the metric measurement                                        | mandatory   |
|           | description              |          | String | "This metric describes the arithmetic mean of the approximated temperatures of the fabricated part when it leaves station 4." | short description of the metric measurement                               | mandatory   |
|           |                          |          |        |                                                                                                                               |                                                                           |             |