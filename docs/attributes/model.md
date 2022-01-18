# Model Metadata Specification

## Available Fields 

The metadata specification for a DIGITbrain Model
has these sections:

- [Parameters](#parameters)
- [Dependant FMUs](#dependant-fmus)
- [OS Requirements](#os-requirements)
- [Hardware Requirements ](#hardware-requirements-)
- [Publishing](#publishing)

`Description`

:   **Auto-generated**-*string*- Model tag description Additional info about model files (e.g. versioning, scope, i.e. what is the model used for, e.g. simulation, control, etc.) - Human readable marketplace description
    === "Example"
        ``` yaml     
        Description: nan
        ```

`ID`

:   **Auto-generated**-*UUID*- Internal DigitBrain reference (automatically generated)
    === "Example"
        ``` yaml     
        ID: nan
        ```

`Name`

:   **Auto-generated**-*string*- Name of the model
    === "Example"
        ``` yaml     
        Name: nan
        ```

`Version`

:   **Auto-generated**-*semver (if model only has revisions, use semver prerelease 0.1, 0.2, etc.)*- Version of the model
    === "Example"
        ``` yaml     
        Version: nan
        ```

`License`

:   **Auto-generated**-*enum tbd in SAD group*- License of the model
    === "Example"
        ``` yaml     
        License: nan
        ```

`Provider`

:   **Auto-generated**-*string*- Provider name: Institution or Person
    === "Example"
        ``` yaml     
        Provider: nan
        ```

`Provider_contacts`

:   **Auto-generated**-*obj*- OPTIONAL: Dictionary with keys being phone, email, address - Type takes into account co-simulation models, for which solver info is mandatory (next slide)
    === "Example"
        ``` yaml     
        Provider_contacts: nan
        ```

`AuthTool`

:   **Auto-generated**-*enum*- Authoring Tool used to create the model
    === "Example"
        ``` yaml     
        AuthTool: nan
        ```

`Type`

:   **Auto-generated**-*enum*- ML, LCA, 3D FEM and CFD, System simulation, discrete event simulation, co-simulation (it couples a model with specific algorithms) - The original term Path was proposed to be changed (SAD)
    === "Example"
        ``` yaml     
        Type: nan
        ```

`Fidelity`

:   **Auto-generated**-*number*- OPTIONAL: Error of the model’s prediction
    === "Example"
        ``` yaml     
        Fidelity: nan
        ```

`Model_URI`

:   **Auto-generated**-*URI*- Where the model file is stored  Where the model file is stored DigitBrain certified external model repository - We could keep these fields into minimum and add further enums if needed, e.g. Linear_equations
    === "Example"
        ``` yaml     
        Model_URI: nan
        ```

`Model_FILENAME`

:   **Optional**-*string*- Name of the model file (if necessary) for example when MODEL_URI points to a repository and not a single file

    === "Example"
        ``` yaml     
        Model_FILENAME: nan
        ```

`State_depend`

:   **Auto-generated**-*bool*- stateful -> 1, stateless -> 0
    === "Example"
        ``` yaml     
        State_depend: nan
        ```


### Parameters

An optional description for the Parameters section may appear here. 

`In-slots`

:   **Auto-generated**-*array of obj  (key (group.key), name, dimensions (e.g. 2, 3, etc.), units (human-readable-name, exponents, offset, scale), default value, ranges, description)*- Values on which the model is evaluated (or parameters that might set before or during the evaluation) - Inputs and parameters together, although if needed we can still differentiate them internally in key field for each specific model.
    === "Example"
        ``` yaml     
        In-slots: nan
        ```

`Outputs`

:   **Auto-generated**-*nan*- Values that the model approximates
    === "Example"
        ``` yaml     
        Outputs: nan
        ```

`CosimSolverInfo`

:   **Auto-generated**-****- OPTIONAL (for co-simulation Type only)
    === "Example"
        ``` yaml     
        CosimSolverInfo: nan
        ```


### Dependant FMUs

An optional description for the Dependant FMUs section may appear here. 

`Dependencies`

:   **Auto-generated**-*array of URI*- Dependant FMUs for co-simulation
    === "Example"
        ``` yaml     
        Dependencies: nan
        ```


### OS Requirements

An optional description for the OS Requirements section may appear here. 

`osArch`

:   **Auto-generated**-*enum*- OS architecture type (e.g. x86_64)
    === "Example"
        ``` yaml     
        osArch: nan
        ```

`osType`

:   **Auto-generated**-*enum*- OS type (e.g. Windows, Linux)
    === "Example"
        ``` yaml     
        osType: nan
        ```

`osDistribution`

:   **Auto-generated**-*enum*- OS distributun (e.g. Ubuntu, Fedora)
    === "Example"
        ``` yaml     
        osDistribution: nan
        ```


### Hardware Requirements 

An optional description for the Hardware Requirements  section may appear here. 

`recommendedNumberOfGPUCores`

:   **Optional**-*number*- Recommended number of GPU cores

    === "Example"
        ``` yaml     
        recommendedNumberOfGPUCores: nan
        ```

`minimumNumberOfGPUCores`

:   **Optional**-*number*- Minimum required number of GPU cores

    === "Example"
        ``` yaml     
        minimumNumberOfGPUCores: nan
        ```

`recommendedGPURAM`

:   **Optional**-*number*- Recommended GPU memory

    === "Example"
        ``` yaml     
        recommendedGPURAM: nan
        ```

`minimumGPURAM`

:   **Optional**-*number*- Minimum required GPU memory

    === "Example"
        ``` yaml     
        minimumGPURAM: nan
        ```

`recommendedRAM`

:   **Optional**-*number*- Recommended Memory

    === "Example"
        ``` yaml     
        recommendedRAM: nan
        ```

`minimumRAM`

:   **Optional**-*number*- Minimum required memory

    === "Example"
        ``` yaml     
        minimumRAM: nan
        ```

`recommendedCPUs`

:   **Optional**-*number*- Recommended number of CPU cores

    === "Example"
        ``` yaml     
        recommendedCPUs: nan
        ```

`minimumCPUs`

:   **Optional**-*number*- Minimum required number of CPU cores

    === "Example"
        ``` yaml     
        minimumCPUs: nan
        ```

`requiredDiskSpace`

:   **Optional**-*number*- Required amount of disk space in GB

    === "Example"
        ``` yaml     
        requiredDiskSpace: nan
        ```


### Publishing

An optional description for the Publishing section may appear here. 
