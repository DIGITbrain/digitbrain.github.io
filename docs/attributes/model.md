<style>
  .md-content__button {
    display: none;
  }
</style>
# Model Metadata Fields

## Available Fields 

The metadata specification for a DIGITbrain Model
has these sections:

- [Parameters](#parameters)
- [Dependant FMUs](#dependant-fmus)
- [OS Requirements](#os-requirements)
- [Hardware Requirements ](#hardware-requirements-)
- [Publishing](#publishing)

`Description`

:   **Optional**-*string*- Model tag description Additional info about model files (e.g. versioning, scope, i.e. what is the model used for, e.g. simulation, control, etc.) - Human readable marketplace description

`ID`

:   **Auto-generated**-*UUID*- Internal DigitBrain reference (automatically generated)


`Name`

:   **Optional**-*string*- Human-readable name of the output

`Version`

:   **Optional**-*semver*- Version of the model. If model only has revisions, use semver prerelease 0.1, 0.2, etc.

`License`

:   **Optional**-*enum*- License of the model.  Type tbd in SAD group

`Provider`

:   **Optional**-*string*- Provider name: Institution or Person

`Provider_contacts`

:   **Optional**-*obj*- Dictionary with keys being phone, email, address - Type takes into account co-simulation models, for which solver info is mandatory (next slide)

`AuthTool`

:   **Optional**-*enum*- Authoring Tool used to create the model

`Type`

:   **Optional**-*enum*- ML, LCA, 3D FEM and CFD, System simulation, discrete event simulation, co-simulation (it couples a model with specific algorithms) - The original term Path was proposed to be changed (SAD)

`Fidelity`

:   **Optional**-*number*- Error of the model’s prediction

`Model_URI`

:   **Optional**-*URI*- Where the model file is stored  Where the model file is stored DigitBrain certified external model repository - We could keep these fields into minimum and add further enums if needed, e.g. Linear_equations

`Model_FILENAME`

:   **Optional**-*string*- Name of the model file (if necessary) for example when MODEL_URI points to a repository and not a single file

`State_depend`

:   **Optional**-*bool*- stateful -> 1, stateless -> 0


### Parameters


`In-slots`

:   **Optional**-*array of obj*- Values on which the model is evaluated (or parameters that might set before or during the evaluation) - Inputs and parameters together, although if needed we can still differentiate them internally in key field for each specific model.

`Key`

:   **Optional**-*string*- Group key (eg. type and name) of the output

`Dimensions`

:   **Optional**-*number*- Number of dimensions of the output (i.e. scalar, vector field)

`Is-continuous`

:   **Optional**-*boolean*- Continuous or discreet output

`Units`

:   **Optional**-*obj (see subkeys below)*- Values related to the output measurement units

`Units.Unit`

:   **Optional**-*string*- Units of the output (e.g Pa, m/s, etc…)

`Units.Exponent`

:   **Optional**-*array of number*- eg. exponents for kg (SI) {1, -2, 0, 0, 0, 0, 1}

`Units.Offset`

:   **Optional**-*number*- scale offset if needed (e.g. K to C conversion)

`Units.Scale`

:   **Optional**-*number*- Order of magnitude of the measurement unit scale e.g. Scale is equal to 10^-3 for values expressed in mm

`Default-value`

:   **Optional**-*number*- Default value for the output

`Ranges`

:   **Optional**-*array of number*- Max and min value of the output

`Outputs`

:   **Optional**-*array of obj*- Values that the model approximates

`CosimSolverInfo`

:   **Optional**-*obj*- For co-simulation Type only


### Dependant FMUs


`Dependencies`

:   **Optional**-*array of URI*- Dependant FMUs for co-simulation


### OS Requirements


`osArch`

:   **Optional**-*enum*- OS architecture type (e.g. x86_64)

`osType`

:   **Optional**-*enum*- OS type (e.g. Windows, Linux)

`osDistribution`

:   **Optional**-*enum*- OS distributun (e.g. Ubuntu, Fedora)


### Hardware Requirements 


`recommendedNumberOfGPUCores`

:   **Optional**-*number*- Recommended number of GPU cores

`minimumNumberOfGPUCores`

:   **Optional**-*number*- Minimum required number of GPU cores

`recommendedGPURAM`

:   **Optional**-*number*- Recommended GPU memory

`minimumGPURAM`

:   **Optional**-*number*- Minimum required GPU memory

`recommendedRAM`

:   **Optional**-*number*- Recommended Memory

`minimumRAM`

:   **Optional**-*number*- Minimum required memory

`recommendedCPUs`

:   **Optional**-*number*- Recommended number of CPU cores

`minimumCPUs`

:   **Optional**-*number*- Minimum required number of CPU cores

`requiredDiskSpace`

:   **Optional**-*number*- Required amount of disk space in GB


### Publishing

