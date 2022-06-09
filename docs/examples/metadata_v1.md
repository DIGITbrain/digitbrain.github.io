
<style>
  .md-content__button {
    display: none;
  }
</style>


# Microservice

| Concept               | Key                        | Subkey   | Values                                                                                                                                                                                                                          |
|:----------------------|:---------------------------|:---------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description           |                            |          |                                                                                                                                                                                                                                 |
|                       | id                         |          | "MSID_OPDASH"                                                                                                                                                                                                                   |
|                       | name                       |          | "Production Optimizer"                                                                                                                                                                                                          |
|                       | author                     |          | "TEKNOPAR"                                                                                                                                                                                                                      |
|                       | date                       |          |                                                                                                                                                                                                                                 |
|                       | version                    |          | "1.0.0"                                                                                                                                                                                                                         |
|                       | description                |          | "Produces weekly optimal production planning using rule based algorithm. Predicts optimized energy consumption"                                                                                                                 |
|                       | classificationSchema       |          | "others"                                                                                                                                                                                                                        |
|                       | type                       |          | ["rule based algorithm", "machine learning"]                                                                                                                                                                                    |
| Service               |                            |          |                                                                                                                                                                                                                                 |
|                       | deploymentFormat           |          | "docker-compose"                                                                                                                                                                                                                |
|                       | deploymentData             |          | {   "version": "3.7",   "services": {     "production-planning": {       "ports": [         "5000:5000"       ],       "restart": "always",       "image": "dbs-container-repo.emgora.eu/production-planning:1.0.0"     }   } } |
|                       | configurationData          |          |                                                                                                                                                                                                                                 |
|                       | mountedSharedDirectories   |          |                                                                                                                                                                                                                                 |
| Hardware Requirements |                            |          |                                                                                                                                                                                                                                 |
|                       | recommendedNumberOfGPUs    |          |                                                                                                                                                                                                                                 |
|                       | recommendedGPURAM          |          |                                                                                                                                                                                                                                 |
|                       | gpuType                    |          |                                                                                                                                                                                                                                 |
|                       | hpcRequired                |          |                                                                                                                                                                                                                                 |
|                       | edgeType                   |          |                                                                                                                                                                                                                                 |
|                       | recommendedRAM             |          |                                                                                                                                                                                                                                 |
|                       | recommendedCPUs            |          |                                                                                                                                                                                                                                 |
|                       | requiredDiskSpace          |          |                                                                                                                                                                                                                                 |
| OS Requirements       |                            |          |                                                                                                                                                                                                                                 |
|                       | osArch                     |          | "x86_64"                                                                                                                                                                                                                        |
|                       | osType                     |          | "linux"                                                                                                                                                                                                                         |
| Data Resources        |                            |          |                                                                                                                                                                                                                                 |
|                       | dataResource               |          |                                                                                                                                                                                                                                 |
| Model                 |                            |          |                                                                                                                                                                                                                                 |
|                       | model_types                |          |                                                                                                                                                                                                                                 |
|                       | model_recommendedAuthTools |          |                                                                                                                                                                                                                                 |
| Parameters            |                            |          |                                                                                                                                                                                                                                 |
|                       | parameters                 |          |                                                                                                                                                                                                                                 |
| Metrics               |                            |          |                                                                                                                                                                                                                                 |
|                       | metrics                    |          |                                                                                                                                                                                                                                 |

# Algorithm

| Concept     | Key                  | Subkey   | Values                                                           |
|:------------|:---------------------|:---------|:-----------------------------------------------------------------|
| Description |                      |          |                                                                  |
|             | id                   |          | "ALGID_COATWIN"                                                  |
|             | name                 |          | "Production optimization with machine and sensor data"           |
|             | description          |          | "Computing optimal weekly production plan with analytical model" |
|             | classificationSchema |          | "ML"                                                             |
|             | type                 |          | ["ML", "Rule Based Algorithm"]                                   |
|             | author               |          | "TEKNOPAR"                                                       |
|             | date                 |          |                                                                  |
|             | version              |          | "1.0.0"                                                          |
| Algorithm   |                      |          |                                                                  |
|             | listOfMicroservices  |          | ["MSID_OPDASH"]                                                  |
|             | deploymentMapping    |          | {"MSID_OPDASH": "HOSTID_COATWIN" }                               |

# Model

| Concept               | Key                         | Subkey   | Values                   |
|:----------------------|:----------------------------|:---------|:-------------------------|
| Description           |                             |          |                          |
|                       | ID                          |          | "MODID_COATWIN"          |
|                       | Name                        |          | "Parameter Optimization" |
|                       | Version                     |          | "1.0.0"                  |
|                       | License                     |          |                          |
|                       | Provider                    |          |                          |
|                       | Provider_contacts           |          |                          |
|                       | Marketplace_description     |          |                          |
|                       | AuthTool                    |          | "scikit-learn"           |
|                       | Type                        |          | "ML"                     |
|                       | Fidelity                    |          |                          |
|                       | REPOSITORY_URI              |          | "s3://dbrain-s3-test"    |
|                       | PATH                        |          | "/data"                  |
|                       | FILENAME                    |          | "engine_mount.zip"       |
|                       | State_depend                |          |                          |
| Parameters            |                             |          |                          |
|                       | inSlots                     |          |                          |
|                       | outSlots                    |          |                          |
| OS Requirements       |                             |          |                          |
|                       | osArch                      |          |                          |
|                       | osType                      |          |                          |
|                       | osDistribution              |          |                          |
| Hardware Requirements |                             |          |                          |
|                       | recommendedNumberOfGPUCores |          |                          |
|                       | minimumNumberOfGPUCores     |          |                          |
|                       | recommendedGPURAM           |          |                          |
|                       | minimumGPURAM               |          |                          |
|                       | recommendedRAM              |          |                          |
|                       | minimumRAM                  |          |                          |
|                       | recommendedCPUs             |          |                          |
|                       | minimumCPUs                 |          |                          |
|                       | requiredDiskSpace           |          |                          |

# Data

| Concept                             | Key              | Subkey   | Values                             |
|:------------------------------------|:-----------------|:---------|:-----------------------------------|
| Administrative data                 |                  |          |                                    |
|                                     | ID               |          | "DATAID_MYDB"                      |
|                                     | AUTHOR           |          |                                    |
|                                     | PROVIDER         |          |                                    |
|                                     | DATE             |          |                                    |
| Description                         |                  |          |                                    |
|                                     | DATA_NAME        |          | "REPLASA MSSQL Server"             |
|                                     | DATA_VERSION     |          | "1.0.0"                            |
|                                     | DATA_DESC        |          | "Machine and sensor data from PLC" |
|                                     | DATA_DESC_URL    |          |                                    |
|                                     | DATA_SIZE        |          |                                    |
| Search support                      |                  |          |                                    |
|                                     | DATA_TAGS        |          | ["TBD"]                            |
| Datakind specification              |                  |          |                                    |
|                                     | DATA_KIND        |          | "DATABASE"                         |
|                                     | DATA_DIRECTION   |          | "SOURCE"                           |
|                                     | DATA_FORMAT      |          | [""]                               |
|                                     | DATA_STORE_TYPE  |          | "MSSQL"                            |
| Data access specification           |                  |          |                                    |
|                                     | DATA_URI         |          | "TBD"                              |
|                                     | DATA_AUTH        |          | ["VPN", "ssl_certificate"]         |
| Open parameters                     |                  |          |                                    |
|                                     | DATA_CREDENTIALS |          |                                    |
| Further access clauses (extensible) |                  |          |                                    |
|                                     | DATA_AUX_INFO    |          |                                    |
| Data content semantics              |                  |          |                                    |
|                                     | DATA_SCHEMA      |          |                                    |
|                                     | DATA_SCHEMA_URL  |          |                                    |

# MA Pair

| Concept    | Key        | Subkey   | Values                              |
|:-----------|:-----------|:---------|:------------------------------------|
| Definition |            |          |                                     |
|            | ID         |          | "MAID_COATWIN"                      |
|            | Created at |          |                                     |
|            | Version    |          | "1.0.0"                             |
|            | Author     |          |                                     |
|            | Licensor   |          |                                     |
|            | Derivation |          |                                     |
|            | Name       |          | "coatwinModelMount"                 |
|            | Scope      |          | "Analytical model for optimization" |
|            | IP Family  |          | "ip_family_id"                      |
|            | Namespace  |          |                                     |
|            | M Asset    |          | "MODID_COATWIN"                     |
|            | A Asset    |          | "ALGID_COATWIN"                     |
|            | Rules      |          |                                     |
|            | Frequency  |          |                                     |
|            | Payload    |          |                                     |

# DMA Tuple

| Concept             | Key               | Subkey   | Values                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|:--------------------|:------------------|:---------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Definition          |                   |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                     | ID                |          | "DMAID_COATWIN"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                     | Created at        |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                     | Version           |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                     | Author            |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                     | Licensor          |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                     | Derivation        |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                     | Name              |          | "coatwinModelMount"                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                     | Scope             |          | "Analytical model for optimization"                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                     | IP Instance       |          | ID_IP_INSTANCE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                     | Namespace         |          | ID_Namespace                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                     | MA Pair           |          | "MAID_COATWIN"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                     | Schedule          |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                     | Payload           |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Data Assets Mapping |                   |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                     | DataAssetsMapping |          | {"MSID_OPDASH": { "DATA1": "DATAID_MYDB"}}                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Deployments         |                   |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                     | Deployments       |          | { 	"HOSTID_COATWIN": { 		"name": "COATWIN_DEPLOYMENT", 		"author": "Ozan Ercan", 		"type": "cloudbroker", 		"cloudbroker": { 			"deployment_id": "16b1e2d4-3a2c-406e-8c45-5637099021f0", 			"instance_type_id": "ca727925-a5ca-4697-b2c3-8788d82457d5", 			"key_pair_id": "a4580fc3-f981-4279-98fa-eea142ecb511", 			"opened_port": "2379,4500,30010,8285,30012,443,10250,30888,30000,6443,22,500,8472,30012,4500,500, 5000", 			"endpoint": "https://cloudsme-cbp.scaletools.com.ua" 		} 	} } |

# Supporting Metadata

| Concept                     | Key         | Subkey   | Values   |
|:----------------------------|:------------|:---------|:---------|
| Person                      |             |          |          |
|                             | ID          |          |          |
|                             | Created at  |          |          |
|                             | Version     |          |          |
|                             | First name  |          | TBD      |
|                             | Last name   |          | TBD      |
|                             | Email       |          | TBD      |
|                             | CV          |          |          |
|                             | Image       |          |          |
|                             | Affiliation |          |          |
| Legal Entity (Organization) |             |          |          |
|                             | ID          |          |          |
|                             | Created at  |          |          |
|                             | Version     |          |          |
|                             | Author      |          | TBD      |
|                             | Name        |          | TBD      |
|                             | Description |          | TBD      |
|                             | Logo        |          |          |
|                             | URL         |          |          |
|                             | Location    |          |          |
|                             | Phone       |          |          |
|                             | VAT ID No.  |          |          |
| IP Family                   |             |          |          |
|                             | ID          |          |          |
|                             | Created at  |          |          |
|                             | Version     |          |          |
|                             | Author      |          | TBD      |
|                             | Manager     |          | TBD      |
|                             | Name        |          | TBD      |
|                             | Image       |          |          |
|                             | Model No.   |          |          |
|                             | Description |          |          |
|                             | Capacity    |          |          |
|                             | IP Man.     |          |          |
| IP Instance                 |             |          |          |
|                             | ID          |          |          |
|                             | Created at  |          |          |
|                             | Version     |          |          |
|                             | Author      |          | TBD      |
|                             | Operator    |          | TBD      |
|                             | IP Family   |          | TBD      |
|                             | Name        |          | TBD      |
|                             | Image       |          |          |
|                             | Serial No.  |          |          |
|                             | Description |          |          |
|                             | Location    |          |          |

# Deployment

| Concept     | Key         | Subkey           | Values                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|:------------|:------------|:-----------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description |             |                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|             | id          |                  | "HOSTID_COATWIN"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|             | name        |                  | "Ubuntu Coatwin"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|             | author      |                  | "Ozan Ercan"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|             | date        |                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Deployments |             |                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|             | type        |                  | "cloudbroker"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|             | cloudbroker |                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|             |             | deployment_id    | "16b1e2d4-3a2c-406e-8c45-5637099021f0"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|             |             | instance_type_id | "16b1e2d4-3a2c-406e-8c45-5637099021f0"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|             |             | key_pair_id      | "a4580fc3-f981-4279-98fa-eea142ecb511"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|             |             | opened_port      | "2379,4500,30010,8285,30012,443,10250,30888,30000,6443,22,500,8472,30012,4500,500, 5000"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|             |             | endpoint         | "https://cloudsme-cbp.scaletools.com.ua"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|             |             | cloud_config     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|             | edge        |                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|             |             | endpoint         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|             |             |                  | {      "HOSTID_COATWIN": {         "name": "Ubuntu Coatwin",         "author": "Ozan Ercan",         "type": "cloudbroker",         "cloudbroker": {             "deployment_id": "16b1e2d4-3a2c-406e-8c45-5637099021f0",             "instance_type_id": "16b1e2d4-3a2c-406e-8c45-5637099021f0",             "key_pair_id": "a4580fc3-f981-4279-98fa-eea142ecb511",             "opened_port": "2379,4500,30010,8285,30012,443,10250,30888,30000,6443,22,500,8472,30012,4500,500, 5000",             "endpoint": "https://cloudsme-cbp.scaletools.com.ua",         }     } } |

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

| Concept        | Key              | Subkey   | Values                                                                                                                                                                                                                 |
|:---------------|:-----------------|:---------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Data Resources |                  |          |                                                                                                                                                                                                                        |
|                | DATA_RESOURCE_ID |          | "USER_UI"                                                                                                                                                                                                              |
|                | DATA_KIND        |          | ["FILE"]                                                                                                                                                                                                               |
|                | DATA_DIRECTION   |          | ["SOURCE"]                                                                                                                                                                                                             |
|                | DATA_FORMAT      |          |                                                                                                                                                                                                                        |
|                | DATA_SOURCE_TYPE |          |                                                                                                                                                                                                                        |
|                | DATA_AUTH_TYPE   |          |                                                                                                                                                                                                                        |
|                | DATA_SCHEMA      |          |                                                                                                                                                                                                                        |
|                | DATA_AUX_INFO    |          |                                                                                                                                                                                                                        |
|                |                  |          | {      "DATA_RESOURCE_ID": "USER_UI",     "DATA_KIND": ["FILE"],     "DATA_DIRECTION": ["SOURCE"],     "DATA_FORMAT": ,     "DATA_SOURCE_TYPE": ,     "DATA_AUTH_TYPE": ,     "DATA_SCHEMA": ,     "DATA_AUX_INFO":  } |

# Parameters

| Concept    | Key          | Subkey   | Values                                                                                                          |
|:-----------|:-------------|:---------|:----------------------------------------------------------------------------------------------------------------|
| Parameters |              |          |                                                                                                                 |
|            | name         |          | "null"                                                                                                          |
|            | type         |          | "null"                                                                                                          |
|            | mandatory    |          |                                                                                                                 |
|            | defaultValue |          |                                                                                                                 |
|            | description  |          | "null"                                                                                                          |
|            |              |          | {      "name": "null",     "type": "null",     "mandatory": ,     "defaultValue": ,     "description": "null" } |

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
