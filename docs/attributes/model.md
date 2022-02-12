<style>
  .md-content__button {
    display: none;
  }
</style>
# Model Fields

**This information is also available in [table format](/tables/model/)**


## Available Fields 

The metadata specification for a DIGITbrain Model
has these sections:

- [Description](#description)
- [Parameters](#parameters)
- [Dependant FMUs](#dependant-fmus)
- [OS Requirements](#os-requirements)
- [Hardware Requirements ](#hardware-requirements-)
- [Publishing](#publishing)


### Description


`ID`{ #ID }
:   **Auto-generated**-*UUID*- Internal DigitBrain reference (automatically generated)


`Name`{ #Name }
:   **Optional**-*string*- Name of the model

`Version`{ #Version }
:   **Optional**-*semver*- Version of the model. If model only has revisions, use semver prerelease 0.1, 0.2, etc.

`License`{ #License }
:   **Optional**-*enum*- License of the model.  Type tbd in SAD group

`Provider`{ #Provider }
:   **Optional**-*string*- Provider name: Institution or Person

`Provider_contacts`{ #Provider_contacts }
:   **Optional**-*obj*- Dictionary with keys being phone, email, address - Type takes into account co-simulation models, for which solver info is mandatory (next slide)

`AuthTool`{ #AuthTool }
:   **Optional**-*enum*- Authoring Tool used to create the model

`Type`{ #Type }
:   **Optional**-*enum*- ML, LCA, 3D FEM and CFD, System simulation, discrete event simulation, co-simulation (it couples a model with specific algorithms) - The original term Path was proposed to be changed (SAD)

`Fidelity`{ #Fidelity }
:   **Optional**-*number*- Error of the model’s prediction

`REPOSITORY_URI`{ #REPOSITORY_URI }
:   **Required**-*URI*- Where the model file is stored (usually the DigitBrain certified external model repository). The path and model filename are not provided via this field.

    === "Example"
        ``` yaml     
        https://www.myrepo.com
        ```

`PATH`{ #PATH }
:   **Required**-*string*- Path to the model file in the specified repository, not including the filename itself.

    === "Example"
        ``` yaml     
        input/models
        ```

`FILENAME`{ #FILENAME }
:   **Required**-*string*- Name of the model file at the given path within the given repo, with a file extension if it exists.

    === "Example"
        ``` yaml     
        mymodel.pb
        ```

`State_depend`{ #State_depend }
:   **Optional**-*bool*- stateful -> 1, stateless -> 0


### Parameters


`In-slots`{ #In-slots }
:   **Optional**-*array of obj*- Values on which the model is evaluated (or parameters that might set before or during the evaluation) - Inputs and parameters together, although if needed we can still differentiate them internally in key field for each specific model.

    `Key`{ #Key }
:   **Optional**-*string*- Group key (eg. type and name) of the in-slot

    `Name`{ #Name }
:   **Optional**-*string*- Human-readable name of the in-slot

    `Dimensions`{ #Dimensions }
:   **Optional**-*number*- Number of dimensions of the in-slot (i.e. scalar, vector field)

    `Is-continuous`{ #Is-continuous }
:   **Optional**-*boolean*- continuous or discreet in-slot

    `Units`{ #Units }
:   **Optional**-*obj (see subkeys below)*- Values related to the in-slot measurement units

    `Units.Unit`{ #Units.Unit }
:   **Optional**-*string*- Units of the in-slot (e.g Pa, m/s, etc…)

    `Units.Exponent`{ #Units.Exponent }
:   **Optional**-*array of number*- eg. exponents for kg (SI) {1, -2, 0, 0, 0, 0, 1}

    `Units.Offset`{ #Units.Offset }
:   **Optional**-*number*- scale offset if needed (e.g. K to C conversion)

    `Units.Scale`{ #Units.Scale }
:   **Optional**-*number*- Order of magnitude of the measurement unit scale e.g. Scale is equal to 10^-3 for values expressed in mm

    `Default-value`{ #Default-value }
:   **Optional**-*number*- Default value for the in-slot

    `Ranges`{ #Ranges }
:   **Optional**-*array of number*- Max and min value of the in-slot

`Outputs`{ #Outputs }
:   **Optional**-*array of obj*- Values that the model approximates

    `Key`{ #Key }
:   **Optional**-*string*- Group key (eg. type and name) of the output

    `Name`{ #Name }
:   **Optional**-*string*- Human-readable name of the output

    `Dimensions`{ #Dimensions }
:   **Optional**-*number*- Number of dimensions of the output (i.e. scalar, vector field)

    `Is-continuous`{ #Is-continuous }
:   **Optional**-*boolean*- Continuous or discreet output

    `Units`{ #Units }
:   **Optional**-*obj (see subkeys below)*- Values related to the output measurement units

    `Units.Unit`{ #Units.Unit }
:   **Optional**-*string*- Units of the output (e.g Pa, m/s, etc…)

    `Units.Exponent`{ #Units.Exponent }
:   **Optional**-*array of number*- eg. exponents for kg (SI) {1, -2, 0, 0, 0, 0, 1}

    `Units.Offset`{ #Units.Offset }
:   **Optional**-*number*- scale offset if needed (e.g. K to C conversion)

    `Units.Scale`{ #Units.Scale }
:   **Optional**-*number*- Order of magnitude of the measurement unit scale e.g. Scale is equal to 10^-3 for values expressed in mm

    `Default-value`{ #Default-value }
:   **Optional**-*number*- Default value for the output

    `Ranges`{ #Ranges }
:   **Optional**-*array of number*- Max and min value of the output

`CosimSolverInfo`{ #CosimSolverInfo }
:   **Optional**-*obj*- For co-simulation Type only


### Dependant FMUs


`Dependencies`{ #Dependencies }
:   **Optional**-*array of URI*- Dependant FMUs for co-simulation


### OS Requirements


`osArch`{ #osArch }
:   **Optional**-*enum*- OS architecture type (e.g. x86_64)

`osType`{ #osType }
:   **Optional**-*enum*- OS type (e.g. Windows, Linux)

`osDistribution`{ #osDistribution }
:   **Optional**-*enum*- OS distributun (e.g. Ubuntu, Fedora)


### Hardware Requirements 


`recommendedNumberOfGPUCores`{ #recommendedNumberOfGPUCores }
:   **Optional**-*number*- Recommended number of GPU cores

`minimumNumberOfGPUCores`{ #minimumNumberOfGPUCores }
:   **Optional**-*number*- Minimum required number of GPU cores

`recommendedGPURAM`{ #recommendedGPURAM }
:   **Optional**-*number*- Recommended GPU memory

`minimumGPURAM`{ #minimumGPURAM }
:   **Optional**-*number*- Minimum required GPU memory

`recommendedRAM`{ #recommendedRAM }
:   **Optional**-*number*- Recommended Memory

`minimumRAM`{ #minimumRAM }
:   **Optional**-*number*- Minimum required memory

`recommendedCPUs`{ #recommendedCPUs }
:   **Optional**-*number*- Recommended number of CPU cores

`minimumCPUs`{ #minimumCPUs }
:   **Optional**-*number*- Minimum required number of CPU cores

`requiredDiskSpace`{ #requiredDiskSpace }
:   **Optional**-*number*- Required amount of disk space in GB


### Publishing


`Description`{ #Description }
:   **Optional**-*string*- Model tag description Additional info about model files (e.g. versioning, scope, i.e. what is the model used for, e.g. simulation, control, etc.) - Human readable marketplace description
