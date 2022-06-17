
<style>
  .md-content__button {
    display: none;
  }
</style>


# Microservice

| Concept               | Key                        | Subkey   | Values                                                                                                                                                                                                                                                                                                                                                                               |
|:----------------------|:---------------------------|:---------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Administrative Data   |                            |          |                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | ID                         |          | "MSID_MAESTRO"                                                                                                                                                                                                                                                                                                                                                                       |
|                       | AUTHOR                     |          |                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | PROVIDER                   |          |                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | DATE                       |          |                                                                                                                                                                                                                                                                                                                                                                                      |
| Description           |                            |          |                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | name                       |          | "Co-simulation"                                                                                                                                                                                                                                                                                                                                                                      |
|                       | version                    |          | "2.2.0"                                                                                                                                                                                                                                                                                                                                                                              |
|                       | description                |          | "Maestro microservice for co-simulation use cases"                                                                                                                                                                                                                                                                                                                                   |
|                       | classificationSchema       |          | "Co-simulation"                                                                                                                                                                                                                                                                                                                                                                      |
|                       | type                       |          | ["Co-simulation",  "Maestro"]                                                                                                                                                                                                                                                                                                                                                        |
| Service               |                            |          |                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | deploymentFormat           |          | "docker-compose"                                                                                                                                                                                                                                                                                                                                                                     |
|                       | deploymentData             |          | {     "version": "3.7",     "services": {       "maestro": {         "image": "prasadtalasila/maestro-openjdk13",         "entrypoint": "bash -c \"wget -P /home/model {{MODEL.REPOSITORY_URI}}  && /home/cosim/entrypoint.sh\"",         "restart": "on-failure",         "volumes": [           "/model:/home/model",           "/output:/home/output"         ]       }     }   } |
|                       | configurationData          |          |                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | mountedSharedDirectories   |          | "/model and /output are mounted to the host"                                                                                                                                                                                                                                                                                                                                         |
| Hardware Requirements |                            |          |                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | recommendedNumberOfGPUs    |          |                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | recommendedGPURAM          |          |                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | gpuType                    |          |                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | hpcRequired                |          |                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | edgeType                   |          |                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | recommendedRAM             |          |                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | recommendedCPUs            |          |                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | requiredDiskSpace          |          |                                                                                                                                                                                                                                                                                                                                                                                      |
| OS Requirements       |                            |          |                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | osArch                     |          | "x86_64"                                                                                                                                                                                                                                                                                                                                                                             |
|                       | osType                     |          |                                                                                                                                                                                                                                                                                                                                                                                      |
| Data Resources        |                            |          |                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | dataResource               |          |                                                                                                                                                                                                                                                                                                                                                                                      |
| Model                 |                            |          |                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | model_types                |          | ["Co-simulation"]                                                                                                                                                                                                                                                                                                                                                                    |
|                       | model_recommendedAuthTools |          | ["INTO-CPS"," Modelica", "SysML"]                                                                                                                                                                                                                                                                                                                                                    |
| Parameters            |                            |          |                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | parameters                 |          |                                                                                                                                                                                                                                                                                                                                                                                      |
| Metrics               |                            |          |                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | metrics                    |          |                                                                                                                                                                                                                                                                                                                                                                                      |

# Algorithm

| Concept             | Key                  | Subkey   | Values                           |
|:--------------------|:---------------------|:---------|:---------------------------------|
| Administrative Data |                      |          |                                  |
|                     | ID                   |          | "ALGID_MAESTRO"                  |
|                     | AUTHOR               |          |                                  |
|                     | PROVIDER             |          |                                  |
|                     | DATE                 |          |                                  |
| Description         |                      |          |                                  |
|                     | name                 |          | "Co-simulation Algorithm"        |
|                     | description          |          | "Co-simulation experiments"      |
|                     | classificationSchema |          | "Co-Simulation"                  |
|                     | type                 |          | ["Co-Simulation"]                |
|                     | version              |          | "1.0"                            |
| Algorithm           |                      |          |                                  |
|                     | listOfMicroservices  |          | ["MSID_MAESTRO"]                 |
|                     | deploymentMapping    |          | {"MSID_MAESTRO": "MAESTRO_HOST"} |

# Model

| Concept               | Key                         | Subkey   | Values                                                                                         |
|:----------------------|:----------------------------|:---------|:-----------------------------------------------------------------------------------------------|
| Administrative Data   |                             |          |                                                                                                |
|                       | ID                          |          | "MODID_MAESTRO"                                                                                |
|                       | AUTHOR                      |          |                                                                                                |
|                       | PROVIDER                    |          |                                                                                                |
|                       | DATE                        |          |                                                                                                |
| Description           |                             |          |                                                                                                |
|                       | Name                        |          | "Mass-string-dampner"                                                                          |
|                       | Version                     |          | "1.0"                                                                                          |
|                       | License                     |          |                                                                                                |
|                       | Provider_contacts           |          |                                                                                                |
|                       | Marketplace_description     |          |                                                                                                |
|                       | AuthTool                    |          |                                                                                                |
|                       | Type                        |          |                                                                                                |
|                       | Fidelity                    |          |                                                                                                |
|                       | REPOSITORY_URI              |          | "https://github.com/prasadtalasila/digitbrain-example/raw/main/example1/model/cosim-model.zip" |
|                       | PATH                        |          | "https://github.com/prasadtalasila/digitbrain-example/raw/main/example1/model/"                |
|                       | FILENAME                    |          | "cosim-model.zip"                                                                              |
|                       | State_depend                |          |                                                                                                |
| Parameters            |                             |          |                                                                                                |
|                       | inSlots                     |          |                                                                                                |
|                       | outSlots                    |          |                                                                                                |
| OS Requirements       |                             |          |                                                                                                |
|                       | osArch                      |          |                                                                                                |
|                       | osType                      |          |                                                                                                |
|                       | osDistribution              |          |                                                                                                |
| Hardware Requirements |                             |          |                                                                                                |
|                       | recommendedNumberOfGPUCores |          |                                                                                                |
|                       | minimumNumberOfGPUCores     |          |                                                                                                |
|                       | recommendedGPURAM           |          |                                                                                                |
|                       | minimumGPURAM               |          |                                                                                                |
|                       | recommendedRAM              |          |                                                                                                |
|                       | minimumRAM                  |          |                                                                                                |
|                       | recommendedCPUs             |          |                                                                                                |
|                       | minimumCPUs                 |          |                                                                                                |
|                       | requiredDiskSpace           |          |                                                                                                |

# Data

| Concept                             | Key              | Subkey   | Values         |
|:------------------------------------|:-----------------|:---------|:---------------|
| Administrative Data                 |                  |          |                |
|                                     | ID               |          | "DATAID_OUT"   |
|                                     | AUTHOR           |          |                |
|                                     | PROVIDER         |          |                |
|                                     | DATE             |          |                |
| Description                         |                  |          |                |
|                                     | DATA_NAME        |          | "output"       |
|                                     | DATA_VERSION     |          |                |
|                                     | DATA_DESC        |          |                |
|                                     | DATA_DESC_URL    |          |                |
|                                     | DATA_SIZE        |          |                |
| Search support                      |                  |          |                |
|                                     | DATA_TAGS        |          |                |
| Datakind specification              |                  |          |                |
|                                     | DATA_KIND        |          | "FILE"         |
|                                     | DATA_DIRECTION   |          | "SINK"         |
|                                     | DATA_FORMAT      |          | ["text/plain"] |
|                                     | DATA_STORE_TYPE  |          | "LOCAL"        |
| Data access specification           |                  |          |                |
|                                     | DATA_URI         |          |                |
|                                     | DATA_AUTH        |          |                |
| Open parameters                     |                  |          |                |
|                                     | DATA_CREDENTIALS |          |                |
| Further access clauses (extensible) |                  |          |                |
|                                     | DATA_AUX_INFO    |          |                |
| Data content semantics              |                  |          |                |
|                                     | DATA_SCHEMA      |          |                |
|                                     | DATA_SCHEMA_URL  |          |                |

# MA Pair

| Concept             | Key        | Subkey   | Values                                                                 |
|:--------------------|:-----------|:---------|:-----------------------------------------------------------------------|
| Administrative Data |            |          |                                                                        |
|                     | ID         |          | "MAID_MAESTRO"                                                         |
|                     | AUTHOR     |          |                                                                        |
|                     | PROVIDER   |          |                                                                        |
|                     | DATE       |          |                                                                        |
| Definition          |            |          |                                                                        |
|                     | Version    |          | "1.0.0"                                                                |
|                     | Licensor   |          |                                                                        |
|                     | Derivation |          |                                                                        |
|                     | Name       |          | "Maestro-spring-dampner"                                               |
|                     | Scope      |          | "Mass Spring Dampner model to be evaluated by co-simulation algorithm" |
|                     | IP Family  |          | "IP_Familiy_ID"                                                        |
|                     | Namespace  |          |                                                                        |
|                     | M Asset    |          | "MODID_MAESTRO"                                                        |
|                     | A Asset    |          | "ALGID_MAESTRO"                                                        |
|                     | Rules      |          |                                                                        |
|                     | Frequency  |          |                                                                        |
|                     | Payload    |          |                                                                        |

# DMA Tuple

| Concept             | Key               | Subkey   | Values                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|:--------------------|:------------------|:---------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Administrative Data |                   |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                     | ID                |          | "DMAID_MAESTRO"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                     | AUTHOR            |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                     | PROVIDER          |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                     | DATE              |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Definition          |                   |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                     | Version           |          | "1.0.0"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                     | Licensor          |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                     | Derivation        |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                     | Name              |          | "Mass Spring Dampner"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                     | Scope             |          | "Mass Spring Dampner example"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                     | IP Instance       |          | "ID_IP_Instance"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                     | Namespace         |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                     | MA Pair           |          | "MAID_MAESTRO"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                     | Schedule          |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                     | Payload           |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Data Assets Mapping |                   |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                     | DataAssetsMapping |          | { "MSID_MAESTRO": { "DATA1": "DATAID_OUT"}}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Deployments         |                   |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                     | Deployments       |          | {     "MAESTRO_HOST": {       "name": "Co-simulation-Deployment",       "author": "Resmi Arjun",       "type": "cloudbroker",       "cloudbroker": {         "deployment_id": "16b1e2d4-3a2c-406e-8c45-5637099021f0",         "instance_type_id": "ca727925-a5ca-4697-b2c3-8788d82457d5",         "key_pair_id": "4380605a-c24f-4dec-b234-32b3f72eb94c",         "opened_port": "1-65535",         "cloud_config": "#cloud-config\nruncmd:\n- [\"ipsec stop\"]",         "endpoint": "https://cloudsme-cbp.scaletools.com.ua"       }     }   } |

# Supporting Metadata

| Concept                     | Key         | Subkey   | Values                    |
|:----------------------------|:------------|:---------|:--------------------------|
| Person                      |             |          |                           |
|                             | ID          |          |                           |
|                             | Created at  |          |                           |
|                             | Version     |          |                           |
|                             | First name  |          | Prasad                    |
|                             | Last name   |          | Talasila                  |
|                             | Email       |          | prasad.talasila@ece.au.dk |
|                             | CV          |          |                           |
|                             | Image       |          |                           |
|                             | Affiliation |          |                           |
| Legal Entity (Organization) |             |          |                           |
|                             | ID          |          |                           |
|                             | Created at  |          |                           |
|                             | Version     |          |                           |
|                             | Author      |          |                           |
|                             | Name        |          | AU                        |
|                             | Description |          | Aarhus University         |
|                             | Logo        |          |                           |
|                             | URL         |          |                           |
|                             | Location    |          |                           |
|                             | Phone       |          |                           |
|                             | VAT ID No.  |          |                           |
| IP Family                   |             |          |                           |
|                             | ID          |          |                           |
|                             | Created at  |          |                           |
|                             | Version     |          |                           |
|                             | Author      |          |                           |
|                             | Manager     |          |                           |
|                             | Name        |          |                           |
|                             | Image       |          |                           |
|                             | Model No.   |          |                           |
|                             | Description |          |                           |
|                             | Capacity    |          |                           |
|                             | IP Man.     |          |                           |
| IP Instance                 |             |          |                           |
|                             | ID          |          |                           |
|                             | Created at  |          |                           |
|                             | Version     |          |                           |
|                             | Author      |          |                           |
|                             | Operator    |          |                           |
|                             | IP Family   |          |                           |
|                             | Name        |          |                           |
|                             | Image       |          |                           |
|                             | Serial No.  |          |                           |
|                             | Description |          |                           |
|                             | Location    |          |                           |

# Deployment

| Concept     | Key         | Subkey           | Values                                                                                                                                                                                                                                                             |
|:------------|:------------|:-----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description |             |                  |                                                                                                                                                                                                                                                                    |
|             | id          |                  |                                                                                                                                                                                                                                                                    |
|             | name        |                  |                                                                                                                                                                                                                                                                    |
|             | author      |                  |                                                                                                                                                                                                                                                                    |
|             | date        |                  |                                                                                                                                                                                                                                                                    |
| Deployments |             |                  |                                                                                                                                                                                                                                                                    |
|             | type        |                  |                                                                                                                                                                                                                                                                    |
|             | cloudbroker |                  |                                                                                                                                                                                                                                                                    |
|             |             | deployment_id    |                                                                                                                                                                                                                                                                    |
|             |             | instance_type_id |                                                                                                                                                                                                                                                                    |
|             |             | key_pair_id      |                                                                                                                                                                                                                                                                    |
|             |             | opened_port      |                                                                                                                                                                                                                                                                    |
|             |             | endpoint         |                                                                                                                                                                                                                                                                    |
|             |             | cloud_config     |                                                                                                                                                                                                                                                                    |
|             | edge        |                  |                                                                                                                                                                                                                                                                    |
|             |             | endpoint         |                                                                                                                                                                                                                                                                    |
|             |             |                  | {      : {         "name": ,         "author": ,         "type": ,         "cloudbroker": {             "deployment_id": ,             "instance_type_id": ,             "key_pair_id": ,             "opened_port": ,             "endpoint": ,         }     } } |

# DataAssetsMapping

| Concept           | Key               | Subkey           | Values                                                                                      |
|:------------------|:------------------|:-----------------|:--------------------------------------------------------------------------------------------|
| DataAssetsMapping |                   |                  |                                                                                             |
|                   | *MICROSERVICE_ID* |                  |                                                                                             |
|                   |                   | *DATA_SOURCE_ID* |                                                                                             |
|                   |                   |                  |                                                                                             |
|                   |                   |                  |                                                                                             |
|                   |                   |                  | {      "*MICROSERVICE_ID* ": {         "*DATA_SOURCE_ID* ": ,         "": ,         "": , } |

# ConfigurationData

| Concept           | Key              | Subkey   | Values                                                               |
|:------------------|:-----------------|:---------|:---------------------------------------------------------------------|
| ConfigurationData |                  |          |                                                                      |
|                   | filePath         |          |                                                                      |
|                   | fileContent      |          |                                                                      |
|                   | mountPropagation |          |                                                                      |
|                   |                  |          | {      "filePath": ,     "fileContent": ,     "mountPropagation":  } |

# Data Resources

| Concept        | Key              | Subkey   | Values                                                                                                                                                                                      |
|:---------------|:-----------------|:---------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Data Resources |                  |          |                                                                                                                                                                                             |
|                | DATA_RESOURCE_ID |          |                                                                                                                                                                                             |
|                | DATA_KIND        |          |                                                                                                                                                                                             |
|                | DATA_DIRECTION   |          |                                                                                                                                                                                             |
|                | DATA_FORMAT      |          |                                                                                                                                                                                             |
|                | DATA_SOURCE_TYPE |          |                                                                                                                                                                                             |
|                | DATA_AUTH_TYPE   |          |                                                                                                                                                                                             |
|                | DATA_SCHEMA      |          |                                                                                                                                                                                             |
|                | DATA_AUX_INFO    |          |                                                                                                                                                                                             |
|                |                  |          | {      "DATA_RESOURCE_ID": ,     "DATA_KIND": ,     "DATA_DIRECTION": ,     "DATA_FORMAT": ,     "DATA_SOURCE_TYPE": ,     "DATA_AUTH_TYPE": ,     "DATA_SCHEMA": ,     "DATA_AUX_INFO":  } |

# Parameters

| Concept    | Key          | Subkey   | Values                                                                                        |
|:-----------|:-------------|:---------|:----------------------------------------------------------------------------------------------|
| Parameters |              |          |                                                                                               |
|            | name         |          |                                                                                               |
|            | type         |          |                                                                                               |
|            | mandatory    |          |                                                                                               |
|            | defaultValue |          |                                                                                               |
|            | description  |          |                                                                                               |
|            |              |          | {      "name": ,     "type": ,     "mandatory": ,     "defaultValue": ,     "description":  } |

# Metrics

| Concept   | Key                      | Subkey   | Values                                                                                                   |
|:----------|:-------------------------|:---------|:---------------------------------------------------------------------------------------------------------|
| Metrics   |                          |          |                                                                                                          |
|           | name                     |          |                                                                                                          |
|           | correspondingMeasurement |          |                                                                                                          |
|           | function                 |          |                                                                                                          |
|           | unit                     |          |                                                                                                          |
|           | description              |          |                                                                                                          |
|           |                          |          | {      "name": ,     "correspondingMeasurement": ,     "function": ,     "unit": ,     "description":  } |

# Slots

| Concept   | Key           | Subkey   | Values                                                                                                                                                                                                               |
|:----------|:--------------|:---------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Slots     |               |          |                                                                                                                                                                                                                      |
|           | Key           |          |                                                                                                                                                                                                                      |
|           | Name          |          |                                                                                                                                                                                                                      |
|           | Dimensions    |          |                                                                                                                                                                                                                      |
|           | Is-continuous |          |                                                                                                                                                                                                                      |
|           | Units         |          |                                                                                                                                                                                                                      |
|           |               | Unit     |                                                                                                                                                                                                                      |
|           |               | Exponent |                                                                                                                                                                                                                      |
|           |               | Offset   |                                                                                                                                                                                                                      |
|           |               | Scale    |                                                                                                                                                                                                                      |
|           | Default-value |          |                                                                                                                                                                                                                      |
|           | Ranges        |          |                                                                                                                                                                                                                      |
|           |               |          | {      "Key": ,     "Name": ,     "Dimensions": ,     "Is-continuous": ,     "Units": {         "Unit": ,         "Exponent": ,         "Offset": ,         "Scale":      },     "Default-value": ,     "Ranges":  } |
