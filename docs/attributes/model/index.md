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


`ID`{ #id }
:   **Auto-generated**-*UUID*- Internal DigitBrain reference (automatically generated)


`Name`{ #name }
:   **Optional**-*string*- Name of the model

`Version`{ #version }
:   **Optional**-*semver*- Version of the model. If model only has revisions, use semver prerelease 0.1, 0.2, etc.

`License`{ #license }
:   **Optional**-*enum*- License of the model.  Type tbd in SAD group

`Provider`{ #provider }
:   **Optional**-*string*- Provider name: Institution or Person

`Provider_contacts`{ #provider_contacts }
:   **Optional**-*obj*- Dictionary with keys being phone, email, address - Type takes into account co-simulation models, for which solver info is mandatory (next slide)

`AuthTool`{ #authtool }
:   **Optional**-*enum*- Authoring Tool used to create the model

`Type`{ #type }
:   **Optional**-*enum*- ML, LCA, 3D FEM and CFD, System simulation, discrete event simulation, co-simulation (it couples a model with specific algorithms) - The original term Path was proposed to be changed (SAD)

`Fidelity`{ #fidelity }
:   **Optional**-*number*- Error of the model’s prediction

`REPOSITORY_URI`{ #repository_uri }
:   **Required**-*URI*- Where the model file is stored (usually the DigitBrain certified external model repository). The path and model filename are not provided via this field.

    === "Example"
        ``` yaml     
        https://www.myrepo.com
        ```

`PATH`{ #path }
:   **Required**-*string*- Path to the model file in the specified repository, not including the filename itself.

    === "Example"
        ``` yaml     
        input/models
        ```

`FILENAME`{ #filename }
:   **Required**-*string*- Name of the model file at the given path within the given repo, with a file extension if it exists.

    === "Example"
        ``` yaml     
        mymodel.pb
        ```

`State_depend`{ #state_depend }
:   **Optional**-*bool*- stateful -> 1, stateless -> 0


### Parameters


`In-slots`{ #in-slots }
:   **Optional**-*array of obj*- Values on which the model is evaluated (or parameters that might set before or during the evaluation) - Inputs and parameters together, although if needed we can still differentiate them internally in key field for each specific model.

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

    `Units.Unit`{ #units.unit }
:   **Optional**-*string*- Units of the in-slot (e.g Pa, m/s, etc…)

    `Units.Exponent`{ #units.exponent }
:   **Optional**-*array of number*- eg. exponents for kg (SI) {1, -2, 0, 0, 0, 0, 1}

    `Units.Offset`{ #units.offset }
:   **Optional**-*number*- scale offset if needed (e.g. K to C conversion)

    `Units.Scale`{ #units.scale }
:   **Optional**-*number*- Order of magnitude of the measurement unit scale e.g. Scale is equal to 10^-3 for values expressed in mm

    `Default-value`{ #default-value }
:   **Optional**-*number*- Default value for the in-slot

    `Ranges`{ #ranges }
:   **Optional**-*array of number*- Max and min value of the in-slot

`Outputs`{ #outputs }
:   **Optional**-*array of obj*- Values that the model approximates

    `Key`{ #key }
:   **Optional**-*string*- Group key (eg. type and name) of the output

    `Name`{ #name }
:   **Optional**-*string*- Human-readable name of the output

    `Dimensions`{ #dimensions }
:   **Optional**-*number*- Number of dimensions of the output (i.e. scalar, vector field)

    `Is-continuous`{ #is-continuous }
:   **Optional**-*boolean*- Continuous or discreet output

    `Units`{ #units }
:   **Optional**-*obj (see subkeys below)*- Values related to the output measurement units

    `Units.Unit`{ #units.unit }
:   **Optional**-*string*- Units of the output (e.g Pa, m/s, etc…)

    `Units.Exponent`{ #units.exponent }
:   **Optional**-*array of number*- eg. exponents for kg (SI) {1, -2, 0, 0, 0, 0, 1}

    `Units.Offset`{ #units.offset }
:   **Optional**-*number*- scale offset if needed (e.g. K to C conversion)

    `Units.Scale`{ #units.scale }
:   **Optional**-*number*- Order of magnitude of the measurement unit scale e.g. Scale is equal to 10^-3 for values expressed in mm

    `Default-value`{ #default-value }
:   **Optional**-*number*- Default value for the output

    `Ranges`{ #ranges }
:   **Optional**-*array of number*- Max and min value of the output

`CosimSolverInfo`{ #cosimsolverinfo }
:   **Optional**-*obj*- For co-simulation Type only


### Dependant FMUs


`Dependencies`{ #dependencies }
:   **Optional**-*array of URI*- Dependant FMUs for co-simulation


### OS Requirements


`osArch`{ #osarch }
:   **Optional**-*enum*- OS architecture type (e.g. x86_64)

`osType`{ #ostype }
:   **Optional**-*enum*- OS type (e.g. Windows, Linux)

`osDistribution`{ #osdistribution }
:   **Optional**-*enum*- OS distributun (e.g. Ubuntu, Fedora)


### Hardware Requirements 


`recommendedNumberOfGPUCores`{ #recommendednumberofgpucores }
:   **Optional**-*number*- Recommended number of GPU cores

`minimumNumberOfGPUCores`{ #minimumnumberofgpucores }
:   **Optional**-*number*- Minimum required number of GPU cores

`recommendedGPURAM`{ #recommendedgpuram }
:   **Optional**-*number*- Recommended GPU memory

`minimumGPURAM`{ #minimumgpuram }
:   **Optional**-*number*- Minimum required GPU memory

`recommendedRAM`{ #recommendedram }
:   **Optional**-*number*- Recommended Memory

`minimumRAM`{ #minimumram }
:   **Optional**-*number*- Minimum required memory

`recommendedCPUs`{ #recommendedcpus }
:   **Optional**-*number*- Recommended number of CPU cores

`minimumCPUs`{ #minimumcpus }
:   **Optional**-*number*- Minimum required number of CPU cores

`requiredDiskSpace`{ #requireddiskspace }
:   **Optional**-*number*- Required amount of disk space in GB


### Publishing


`Description`{ #description }
:   **Optional**-*string*- Model tag description Additional info about model files (e.g. versioning, scope, i.e. what is the model used for, e.g. simulation, control, etc.) - Human readable marketplace description
