<style>
  .md-content__button {
    display: none;
  }
</style>
# Model Fields


**For a more condensed summary this information is available in [table view](/tables/model/)**



The metadata specification for a DIGITbrain Model
has these fields:

`name`{ #name }

:   **Required**-*string*- Name of the model


`version`{ #version }

:   **Optional**-*string*- Version of the model, defined by the provider. 



    === "Example"
        ``` yaml     
        "0.1"
        ```

`license`{ #license }

:   **Optional**-*string*- License of the model.  Type tbd in SAD group


`provider_contacts`{ #provider_contacts }

:   **Optional**-*string*- Dictionary with keys being phone, email, address - Type takes into account co-simulation models, for which solver info is mandatory (next slide)


`marketplace_description`{ #marketplace_description }

:   **Optional**-*string*- Model tag description Additional info about model files (e.g. versioning, scope, i.e. what is the model used for, e.g. simulation, control, etc.) - Human readable marketplace description


`auth_tool`{ #auth_tool }

:   **Optional**-*string*- Authoring Tool used to create the model


`type`{ #type }

:   **Optional**-*string*- ML, LCA, 3D FEM and CFD, System simulation, discrete event simulation, co-simulation (it couples a model with specific algorithms) - The original term Path was proposed to be changed (SAD)


`fidelity`{ #fidelity }

:   **Optional**-*integer*- Error of the model’s prediction


`repository_uri`{ #repository_uri }

:   **Required**-*string*- Where the model file is stored (usually the DigitBrain certified external model repository). The path and model filename are not provided via this field.



    === "Example"
        ``` yaml     
        "https://www.myrepo.com"
        ```

`path`{ #path }

:   **Required**-*string*- Path to the model file in the specified repository, not including the filename itself.



    === "Example"
        ``` yaml     
        "input/models"
        ```

`filename`{ #filename }

:   **Required**-*string*- Name of the model file at the given path within the given repo, with a file extension if it exists.



    === "Example"
        ``` yaml     
        "mymodel.pb"
        ```

`state_depend`{ #state_depend }

:   **Optional**-*boolean*- stateful -> 1, stateless -> 0


`inslots`{ #inslots }

:   **Optional**-*[Slots](../slots.md)[]*- List of objects with values on which the model is evaluated (or parameters that might set before or during the evaluation) - Inputs and parameters together, although if needed we can still differentiate them internally in key field for each specific model.



    === "Example"
        ``` yaml     
        [
              { 
                "Key": "MY_INSLO_A",
                "Name": "ModelABin",
                "Dimensions": 112,
                "Is-continuous": true,
                "Units": {
                    "Unit": "Pa",
                    "Exponent": [1, -2, 0],
                    "Offset": 442,
                    "Scale": 10^-3
                },
                "Default-value": 55,
                "Ranges": [1,120]
              }
            ]  
        ```

`outslots`{ #outslots }

:   **Optional**-*[Slots](../slots.md)[]*- List of objects with values that the model approximates



    === "Example"
        ``` yaml     
        [
              { 
                "Key": "MY_OUTPUT_A",
                "Name": "ModelABout",
                "Dimensions": 112,
                "Is-continuous": true,
                "Units": {
                    "Unit": "Pa",
                    "Exponent": [1, -2, 0],
                    "Offset": 442,
                    "Scale": 10^-3
                },
                "Default-value": 55,
                "Ranges": [1,120]
              }
            ]  
        ```

`os_arch`{ #os_arch }

:   **Optional**-*string*- OS architecture type (e.g. x86_64)


`os_type`{ #os_type }

:   **Optional**-*string*- OS type (e.g. Windows, Linux)


`os_distribution`{ #os_distribution }

:   **Optional**-*string*- OS distributun (e.g. Ubuntu, Fedora)


`recommended_number_of_gpu_cores`{ #recommended_number_of_gpu_cores }

:   **Optional**-*integer*- Recommended number of GPU cores


`minimum_number_of_gpu_cores`{ #minimum_number_of_gpu_cores }

:   **Optional**-*integer*- Minimum required number of GPU cores


`recommended_gpu_ram`{ #recommended_gpu_ram }

:   **Optional**-*integer*- Recommended GPU memory


`minimum_gpu_ram`{ #minimum_gpu_ram }

:   **Optional**-*integer*- Minimum required GPU memory


`recommended_ram`{ #recommended_ram }

:   **Optional**-*integer*- Recommended Memory


`minimum_ram`{ #minimum_ram }

:   **Optional**-*integer*- Minimum required memory


`recommended_cpus`{ #recommended_cpus }

:   **Optional**-*integer*- Recommended number of CPU cores


`minimum_cpus`{ #minimum_cpus }

:   **Optional**-*integer*- Minimum required number of CPU cores


`required_disk_space`{ #required_disk_space }

:   **Optional**-*integer*- Required amount of disk space in GB


