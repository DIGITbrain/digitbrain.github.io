
<style>
  .md-content__button {
    display: none;
  }
</style>


# Microservice

| Concept               | Key                        | Subkey   | Values                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|:----------------------|:---------------------------|:---------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description           |                            |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                       | id                         |          | "MSID_DITAC_CABLE_PROBLEM"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                       | name                       |          | "DITAC Cable Problem Microservice"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                       | author                     |          | "Andrea Ranieri"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                       | date                       |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                       | version                    |          | "1.0.0"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                       | description                |          | "Microservice running the ML model for solving the DITAC analog cable problem"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                       | classificationSchema       |          | "Machine Learning"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                       | type                       |          | [ "ML model", "DL model", "Data Science"]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Service               |                            |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                       | deploymentFormat           |          | "docker-compose"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                       | deploymentData             |          | {         "version": "3.8",         "services": {           "ditac_cable_problem": {             "image": "python:3.8.13-slim-bullseye",             "entrypoint": "/bin/sh -c",             "command": "python app/server.py {{ PATH }}/{{ FILENAME }}",             "volumes": [               {                 "type": "bind",                 "source": "/data",                 "target": "/data",                 "bind": {                   "propagation": "rshared"                 }               }             ],             "privileged": true           }         }       } |
|                       | configurationData          |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                       | mountedSharedDirectories   |          | "/data is mounted on the host"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Hardware Requirements |                            |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                       | recommendedNumberOfGPUs    |          | 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                       | recommendedGPURAM          |          | 2                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                       | gpuType                    |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                       | hpcRequired                |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                       | edgeType                   |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                       | recommendedRAM             |          | 4                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                       | recommendedCPUs            |          | 2                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                       | requiredDiskSpace          |          | 10                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| OS Requirements       |                            |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                       | osArch                     |          | "x86_64"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                       | osType                     |          | "linux"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Data Resources        |                            |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                       | dataResource               |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Model                 |                            |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                       | model_types                |          | ["Fast.ai/Pytorch .pkl files"]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                       | model_recommendedAuthTools |          | ["Fast.ai/Pytorch"]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Parameters            |                            |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                       | parameters                 |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Metrics               |                            |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                       | metrics                    |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

# Algorithm

| Concept     | Key                  | Subkey   | Values                                                                      |
|:------------|:---------------------|:---------|:----------------------------------------------------------------------------|
| Description |                      |          |                                                                             |
|             | id                   |          | "ALGID_DITAC_CABLE_PROBLEM"                                                 |
|             | name                 |          | "DITAC Cable Problem Algorithm"                                             |
|             | description          |          | "Algorithm running the ML model for solving the DITAC analog cable problem" |
|             | classificationSchema |          | "Machine Learning"                                                          |
|             | type                 |          | [ "ML model", "DL model", "Data Science"]                                   |
|             | author               |          | "Andrea Ranieri"                                                            |
|             | date                 |          |                                                                             |
|             | version              |          | "1.0.0"                                                                     |
| Algorithm   |                      |          |                                                                             |
|             | listOfMicroservices  |          | ["MSID_DITAC_CABLE_PROBLEM"]                                                |
|             | deploymentMapping    |          | {"MSID_DITAC_CABLE_PROBLEM": "DITAC_CABLE_PROBLEM_HOST"}                    |

# Model

| Concept               | Key                         | Subkey   | Values                                                                                               |
|:----------------------|:----------------------------|:---------|:-----------------------------------------------------------------------------------------------------|
| Description           |                             |          |                                                                                                      |
|                       | ID                          |          | "MODID_DITAC_CABLE_PROBLEM"                                                                          |
|                       | Name                        |          | "DITAC Cable Problem model"                                                                          |
|                       | Version                     |          | "0.6.0"                                                                                              |
|                       | License                     |          | "LGPL"                                                                                               |
|                       | Provider                    |          | "Andrea Ranieri"                                                                                     |
|                       | Provider_contacts           |          |                                                                                                      |
|                       | AuthTool                    |          | "Fast.ai/Pytorch"                                                                                    |
|                       | Type                        |          | "ML"                                                                                                 |
|                       | Fidelity                    |          |                                                                                                      |
|                       | REPOSITORY_URI              |          | "http://deeplearning.ge.imati.cnr.it"                                                                |
|                       | PATH                        |          | "/ditac/models"                                                                                      |
|                       | FILENAME                    |          | "ditac-cable-problem-v0.6-endoftraining.pkl"                                                         |
|                       | State_depend                |          |                                                                                                      |
| Parameters            |                             |          |                                                                                                      |
|                       | In-slots                    |          |                                                                                                      |
|                       | Outputs                     |          |                                                                                                      |
|                       | CosimSolverInfo             |          |                                                                                                      |
| Dependant FMUs        |                             |          |                                                                                                      |
|                       | Dependencies                |          |                                                                                                      |
| OS Requirements       |                             |          |                                                                                                      |
|                       | osArch                      |          |                                                                                                      |
|                       | osType                      |          |                                                                                                      |
|                       | osDistribution              |          |                                                                                                      |
| Hardware Requirements |                             |          |                                                                                                      |
|                       | recommendedNumberOfGPUCores |          |                                                                                                      |
|                       | minimumNumberOfGPUCores     |          |                                                                                                      |
|                       | recommendedGPURAM           |          |                                                                                                      |
|                       | minimumGPURAM               |          |                                                                                                      |
|                       | recommendedRAM              |          |                                                                                                      |
|                       | minimumRAM                  |          |                                                                                                      |
|                       | recommendedCPUs             |          |                                                                                                      |
|                       | minimumCPUs                 |          |                                                                                                      |
|                       | requiredDiskSpace           |          |                                                                                                      |
| Publishing            |                             |          |                                                                                                      |
|                       | Description                 |          | "The ML model is able to predict whether a pressure anomaly is detected in the Kistler sensor graph" |

# Data

| Concept                             | Key              | Subkey   | Values                                       |
|:------------------------------------|:-----------------|:---------|:---------------------------------------------|
| Administrative data                 |                  |          |                                              |
|                                     | ID               |          | "DATAID_DITAC_CABLE_PROBLEM"                 |
|                                     | AUTHOR           |          |                                              |
|                                     | PROVIDER         |          |                                              |
|                                     | DATE             |          |                                              |
| Description                         |                  |          |                                              |
|                                     | DATA_NAME        |          | ?                                            |
|                                     | DATA_VERSION     |          |                                              |
|                                     | DATA_DESC        |          |                                              |
|                                     | DATA_DESC_URL    |          |                                              |
|                                     | DATA_SIZE        |          |                                              |
| Search support                      |                  |          |                                              |
|                                     | DATA_TAGS        |          | ["kistler files", "CSV", "pressure sensors"] |
| Datakind specification              |                  |          |                                              |
|                                     | DATA_KIND        |          | "STREAM"                                     |
|                                     | DATA_DIRECTION   |          | "SINK"                                       |
|                                     | DATA_FORMAT      |          | ["text/csv"]                                 |
|                                     | DATA_STORE_TYPE  |          | "POST"                                       |
| Data access specification           |                  |          |                                              |
|                                     | DATA_URI         |          |                                              |
|                                     | DATA_AUTH        |          |                                              |
| Open parameters                     |                  |          |                                              |
|                                     | DATA_CREDENTIALS |          |                                              |
| Further access clauses (extensible) |                  |          |                                              |
|                                     | DATA_AUX_INFO    |          |                                              |
| Data content semantics              |                  |          |                                              |
|                                     | DATA_SCHEMA      |          |                                              |
|                                     | DATA_SCHEMA_URL  |          |                                              |

# MA Pair

| Concept    | Key        | Subkey   | Values                                                                                               |
|:-----------|:-----------|:---------|:-----------------------------------------------------------------------------------------------------|
| Definition |            |          |                                                                                                      |
|            | ID         |          | "MAID_DITAC_CABLE_PROBLEM"                                                                           |
|            | Created at |          |                                                                                                      |
|            | Version    |          | "1.0.0"                                                                                              |
|            | Author     |          |                                                                                                      |
|            | Licensor   |          |                                                                                                      |
|            | Derivation |          |                                                                                                      |
|            | Name       |          | "DITAC Cable Problem ML model"                                                                       |
|            | Scope      |          | "The ML model is able to predict whether a pressure anomaly is detected in the Kistler sensor graph" |
|            | IP Family  |          | "IP_Familiy_ID_DITAC_CABLE_PROBLEM"                                                                  |
|            | Namespace  |          |                                                                                                      |
|            | M Asset    |          | "MODID_DITAC_CABLE_PROBLEM"                                                                          |
|            | A Asset    |          | "ALGID_DITAC_CABLE_PROBLEM"                                                                          |
|            | Rules      |          |                                                                                                      |
|            | Frequency  |          |                                                                                                      |
|            | Payload    |          |                                                                                                      |

# DMA Tuple

| Concept             | Key               | Subkey   | Values                                                                                |
|:--------------------|:------------------|:---------|:--------------------------------------------------------------------------------------|
| Definition          |                   |          |                                                                                       |
|                     | ID                |          | "DMAID_DITAC_CABLE_PROBLEM"                                                           |
|                     | Created at        |          |                                                                                       |
|                     | Version           |          |                                                                                       |
|                     | Author            |          |                                                                                       |
|                     | Licensor          |          |                                                                                       |
|                     | Derivation        |          |                                                                                       |
|                     | Name              |          | "RistraEngineMount"                                                                   |
|                     | Scope             |          | "Structural Simulation for Engine Mount of Fraunhofer's IP Family on moving machines" |
|                     | IP Instance       |          | "ID_IP_DITAC_CABLE_PROBLEM"                                                           |
|                     | Namespace         |          |                                                                                       |
|                     | MA Pair           |          | "MAID_DITAC_CABLE_PROBLEM"                                                            |
|                     | Schedule          |          |                                                                                       |
|                     | Payload           |          |                                                                                       |
| Data Assets Mapping |                   |          |                                                                                       |
|                     | DataAssetsMapping |          |                                                                                       |
| Deployments         |                   |          |                                                                                       |
|                     | Deployments       |          |                                                                                       |

# Supporting Metadata

| Concept                     | Key         | Subkey   | Values                                                                                                    |
|:----------------------------|:------------|:---------|:----------------------------------------------------------------------------------------------------------|
| Person                      |             |          |                                                                                                           |
|                             | ID          |          |                                                                                                           |
|                             | Created at  |          |                                                                                                           |
|                             | Version     |          |                                                                                                           |
|                             | First name  |          | Andrea                                                                                                    |
|                             | Last name   |          | Ranieri                                                                                                   |
|                             | Email       |          | andrea.ranieri@cnr.it                                                                                     |
|                             | CV          |          | Andrea Ranieri is a researcher at CNR-IMATI                                                               |
|                             | Image       |          |                                                                                                           |
|                             | Affiliation |          | CNR-IMATI                                                                                                 |
| Legal Entity (Organization) |             |          |                                                                                                           |
|                             | ID          |          |                                                                                                           |
|                             | Created at  |          |                                                                                                           |
|                             | Version     |          |                                                                                                           |
|                             | Author      |          | ID of CNR.IMATI.Ranieri.Andrea                                                                            |
|                             | Name        |          | Institute for Applied Mathematics and Information Technologies “Enrico Magenes”                           |
|                             | Description |          | IMATI is a cutting edge research institution in mathematics and computer science for applications at CNR. |
|                             | Logo        |          |                                                                                                           |
|                             | URL         |          | https://www.imati.cnr.it                                                                                  |
|                             | Location    |          | Genova                                                                                                    |
|                             | Phone       |          |                                                                                                           |
|                             | VAT ID No.  |          |                                                                                                           |
| IP Family                   |             |          |                                                                                                           |
|                             | ID          |          |                                                                                                           |
|                             | Created at  |          |                                                                                                           |
|                             | Version     |          |                                                                                                           |
|                             | Author      |          | Andrea Ranieri                                                                                            |
|                             | Manager     |          | Andrea Ranieri                                                                                            |
|                             | Name        |          | CNR-IMATI ML models                                                                                       |
|                             | Image       |          |                                                                                                           |
|                             | Model No.   |          |                                                                                                           |
|                             | Description |          |                                                                                                           |
|                             | Capacity    |          |                                                                                                           |
|                             | IP Man.     |          |                                                                                                           |
| IP Instance                 |             |          |                                                                                                           |
|                             | ID          |          |                                                                                                           |
|                             | Created at  |          |                                                                                                           |
|                             | Version     |          |                                                                                                           |
|                             | Author      |          | Andrea Ranieri                                                                                            |
|                             | Operator    |          | Andrea Ranieri                                                                                            |
|                             | IP Family   |          | ID_CNR_IMATI_ML_models                                                                                    |
|                             | Name        |          | CNR-IMATI ML model number 1                                                                               |
|                             | Image       |          |                                                                                                           |
|                             | Serial No.  |          |                                                                                                           |
|                             | Description |          |                                                                                                           |
|                             | Location    |          |                                                                                                           |

# Deployment

| Concept     | Key         | Subkey           | Values                     |
|:------------|:------------|:-----------------|:---------------------------|
| Description |             |                  |                            |
|             | id          |                  | "DITAC_CABLE_PROBLEM_HOST" |
|             | name        |                  | "Ubuntu small"             |
|             | author      |                  | "Andrea Ranieri"           |
|             | date        |                  |                            |
| Deployments |             |                  |                            |
|             | type        |                  | "cloudbroker"              |
|             | cloudbroker |                  |                            |
|             |             | deployment_id    |                            |
|             |             | instance_type_id |                            |
|             |             | key_pair_id      |                            |
|             |             | opened_port      | "55563,55564"              |
|             |             | endpoint         |                            |
|             |             | cloud_config     |                            |
|             | edge        |                  |                            |
|             |             | endpoint         |                            |

# DataAssetsMapping

| Concept           | Key               | Subkey           | Values   |
|:------------------|:------------------|:-----------------|:---------|
| DataAssetsMapping |                   |                  |          |
|                   | *MICROSERVICE_ID* |                  |          |
|                   |                   | *DATA_SOURCE_ID* |          |

# ConfigurationData

| Concept           | Key              | Subkey   | Values                                                                  |
|:------------------|:-----------------|:---------|:------------------------------------------------------------------------|
| ConfigurationData |                  |          |                                                                         |
|                   | filePath         |          |                                                                         |
|                   | fileContent      |          |                                                                         |
|                   | mountPropagation |          |                                                                         |
|                   |                  |          | {      "filePath":"",     "fileContent":"",     "mountPropagation":"" } |

# Data Resources

| Concept        | Key              | Subkey   | Values   |
|:---------------|:-----------------|:---------|:---------|
| Data Resources |                  |          |          |
|                | DATA_RESOURCE_ID |          |          |
|                | DATA_KIND        |          |          |
|                | DATA_DIRECTION   |          |          |
|                | DATA_FORMAT      |          |          |
|                | DATA_SOURCE_TYPE |          |          |
|                | DATA_AUTH_TYPE   |          |          |
|                | DATA_SCHEMA      |          |          |
|                | DATA_AUX_INFO    |          |          |

# Parameters

| Concept    | Key          | Subkey   | Values   |
|:-----------|:-------------|:---------|:---------|
| Parameters |              |          |          |
|            | name         |          |          |
|            | type         |          |          |
|            | mandatory    |          |          |
|            | defaultValue |          |          |
|            | description  |          |          |

# Metrics

| Concept   | Key                      | Subkey   | Values   |
|:----------|:-------------------------|:---------|:---------|
| Metrics   |                          |          |          |
|           | name                     |          |          |
|           | correspondingMeasurement |          |          |
|           | function                 |          |          |
|           | unit                     |          |          |
|           | description              |          |          |

# In-slots

| Concept   | Key           | Subkey   | Values   |
|:----------|:--------------|:---------|:---------|
| In-slots  |               |          |          |
|           | Key           |          |          |
|           | Name          |          |          |
|           | Dimensions    |          |          |
|           | Is-continuous |          |          |
|           | Units         |          |          |
|           |               | Unit     |          |
|           |               | Exponent |          |
|           |               | Offset   |          |
|           |               | Scale    |          |
|           | Default-value |          |          |
|           | Ranges        |          |          |

# Outputs

| Concept   | Key           | Subkey   | Values   |
|:----------|:--------------|:---------|:---------|
| Outputs   |               |          |          |
|           | Key           |          |          |
|           | Name          |          |          |
|           | Dimensions    |          |          |
|           | Is-continuous |          |          |
|           | Units         |          |          |
|           |               | Unit     |          |
|           |               | Exponent |          |
|           |               | Offset   |          |
|           |               | Scale    |          |
|           | Default-value |          |          |
|           | Ranges        |          |          |
