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

:   **Optional**-*string*- Name of the model

`Version`

:   **Optional**-*semver (if model only has revisions, use semver prerelease 0.1, 0.2, etc.)*- Version of the model

`License`

:   **Optional**-*enum tbd in SAD group*- License of the model

`Provider`

:   **Optional**-*string*- Provider name: Institution or Person

`Provider_contacts`

:   **Optional**-*obj*- OPTIONAL: Dictionary with keys being phone, email, address - Type takes into account co-simulation models, for which solver info is mandatory (next slide)

`AuthTool`

:   **Optional**-*enum*- Authoring Tool used to create the model

`Type`

:   **Optional**-*enum*- ML, LCA, 3D FEM and CFD, System simulation, discrete event simulation, co-simulation (it couples a model with specific algorithms) - The original term Path was proposed to be changed (SAD)

`Fidelity`

:   **Optional**-*number*- OPTIONAL: Error of the model’s prediction

`Model_URI`

:   **Optional**-*URI*- Where the model file is stored  Where the model file is stored DigitBrain certified external model repository - We could keep these fields into minimum and add further enums if needed, e.g. Linear_equations

`Model_FILENAME`

:   **Optional**-*string*- Name of the model file (if necessary) for example when MODEL_URI points to a repository and not a single file

`State_depend`

:   **Optional**-*bool*- stateful -> 1, stateless -> 0


### Parameters


`In-slots`

:   **Optional**-*array of obj  (key (group.key), name, dimensions (e.g. 2, 3, etc.), units (human-readable-name, exponents, offset, scale), default value, ranges, description)*- Values on which the model is evaluated (or parameters that might set before or during the evaluation) - Inputs and parameters together, although if needed we can still differentiate them internally in key field for each specific model.

`Outputs`

:   **Optional**-*nan*- Values that the model approximates

`CosimSolverInfo`

:   **Optional**-****- OPTIONAL (for co-simulation Type only)


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

