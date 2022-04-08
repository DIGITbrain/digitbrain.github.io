
<style>
  .md-content__button {
    display: none;
  }
</style>


# Data

| Concept                             | Key              | Subkey   | Values                                                                                        |
|:------------------------------------|:-----------------|:---------|:----------------------------------------------------------------------------------------------|
| Administrative data                 |                  |          |                                                                                               |
|                                     | ID               |          | <D-ID_DFKI-Flower-Stream>                                                                     |
|                                     | AUTHOR           |          |                                                                                               |
|                                     | PROVIDER         |          |                                                                                               |
|                                     | DATE             |          |                                                                                               |
| Description                         |                  |          |                                                                                               |
|                                     | DATA_NAME        |          | DFKIFlowerStream                                                                              |
|                                     | DATA_VERSION     |          | 1.0.0                                                                                         |
|                                     | DATA_DESC        |          | This stream acts as a communication channel between an end user and an ML inference Algorithm |
|                                     | DATA_DESC_URL    |          |                                                                                               |
|                                     | DATA_SIZE        |          | 1m                                                                                            |
| Search support                      |                  |          |                                                                                               |
|                                     | DATA_TAGS        |          | [jpg, rgb]                                                                                    |
| Datakind specification              |                  |          |                                                                                               |
|                                     | DATA_KIND        |          | STREAM                                                                                        |
|                                     | DATA_DIRECTION   |          | BIDIRECTIONAL                                                                                 |
|                                     | DATA_FORMAT      |          | [{text/plain, application/octet-stream}]                                                      |
|                                     | DATA_STORE_TYPE  |          | KAFKA                                                                                         |
| Data access specification           |                  |          |                                                                                               |
|                                     | DATA_URI         |          | kafka://193.225.250.14:9093/dfki-flowers                                                      |
|                                     | DATA_AUTH        |          | [tls_mutual]                                                                                  |
| Open parameters                     |                  |          |                                                                                               |
|                                     | DATA_CREDENTIALS |          |                                                                                               |
| Further access clauses (extensible) |                  |          |                                                                                               |
|                                     | DATA_AUX_INFO    |          | {KAFKA_BROKER_VERSION: 2.7.0}                                                                 |
| Data content semantics              |                  |          |                                                                                               |
|                                     | DATA_SCHEMA      |          |                                                                                               |
|                                     | DATA_SCHEMA_URL  |          |                                                                                               |

# Microservice_ML-Inference

| Concept               | Key                        | Subkey   | Values                                                                                                                                                                                         |
|:----------------------|:---------------------------|:---------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description           |                            |          |                                                                                                                                                                                                |
|                       | id                         |          | <MS-ID_Microservice_ML-Inference>                                                                                                                                                              |
|                       | name                       |          | Object Detection & Classification Network                                                                                                                                                      |
|                       | author                     |          | Valerie Poser                                                                                                                                                                                  |
|                       | date                       |          |                                                                                                                                                                                                |
|                       | version                    |          | 1.0.0                                                                                                                                                                                          |
|                       | description                |          | Detection and classification of objects from Images                                                                                                                                            |
|                       | classificationSchema       |          | ML                                                                                                                                                                                             |
|                       | type                       |          | {neural network, deep learning, convolutional neural network, CNN}                                                                                                                             |
| Service               |                            |          |                                                                                                                                                                                                |
|                       | deploymentFormat           |          | docker-compose                                                                                                                                                                                 |
|                       | deploymentData             |          | {     "version": "3.9",     "services": {         "inference": {             "image": "dfki/ml/flower-inference:latest",             "env_file": {                 "inf.env"}         }    } } |
|                       | configurationData          |          | inf.enf: inf.env                                                                                                                                                                               |
|                       | mountedSharedDirectories   |          |                                                                                                                                                                                                |
| Hardware Requirements |                            |          |                                                                                                                                                                                                |
|                       | recommendedNumberOfGPUs    |          |                                                                                                                                                                                                |
|                       | recommendedGPURAM          |          |                                                                                                                                                                                                |
|                       | gpuType                    |          |                                                                                                                                                                                                |
|                       | hpcRequired                |          |                                                                                                                                                                                                |
|                       | edgeType                   |          |                                                                                                                                                                                                |
|                       | recommendedRAM             |          | 2                                                                                                                                                                                              |
|                       | recommendedCPUs            |          | 2                                                                                                                                                                                              |
|                       | requiredDiskSpace          |          | 42GB                                                                                                                                                                                           |
| OS Requirements       |                            |          |                                                                                                                                                                                                |
|                       | osArch                     |          | x86_64                                                                                                                                                                                         |
|                       | osType                     |          | linux                                                                                                                                                                                          |
| Data Resources        |                            |          |                                                                                                                                                                                                |
|                       | dataResource               |          |                                                                                                                                                                                                |
| Model                 |                            |          |                                                                                                                                                                                                |
|                       | model_types                |          | SavedModel (Tensorflow)                                                                                                                                                                        |
|                       | model_recommendedAuthTools |          | Tensorflow                                                                                                                                                                                     |
| Parameters            |                            |          |                                                                                                                                                                                                |
|                       | parameters                 |          | [<P-ID_DetectionThreshold>]                                                                                                                                                                    |
| Metrics               |                            |          |                                                                                                                                                                                                |
|                       | metrics                    |          | [<Metric-ID_ConfidenceScore>, <Metric-ID_DetectedClass>]                                                                                                                                       |

# Data Resources

| Concept        | Key                        | Subkey   | Values                   |
|:---------------|:---------------------------|:---------|:-------------------------|
| Data Resources |                            |          |                          |
|                | DATA_RESOURCE_ID           |          | kafka_stream             |
|                | DATA_KIND                  |          | STREAM                   |
|                | DATA_DIRECTION             |          | BIDIRECTIONAL            |
|                | DATA_FORMAT                |          | {image/jpeg, text/plain} |
|                | DATA_SOURCE_TYPE           |          | {KAFKA}                  |
|                | DATA_AUTH_TYPE             |          |                          |
|                | DATA_MYSQL_DIALECT         |          |                          |
|                | DATA_MQTT_PROTOCOL_VERSION |          |                          |
|                | DATA_KAFKA_BROKER_VERSION  |          | 2.7.0                    |
|                | DATA_S3_REGION             |          |                          |
|                | DATA_SCHEMA                |          |                          |

# Metrics-detectedClass

| Concept   | Key                      | Subkey   | Values                                             |
|:----------|:-------------------------|:---------|:---------------------------------------------------|
| Metrics   |                          |          |                                                    |
|           | name                     |          | detectedClass                                      |
|           | correspondingMeasurement |          | detectedClass                                      |
|           | function                 |          | ML inference                                       |
|           | unit                     |          | enum                                               |
|           | description              |          | which classes has been detected in the input image |

# Metrics-confidenceScore

| Concept   | Key                      | Subkey   | Values                                                                             |
|:----------|:-------------------------|:---------|:-----------------------------------------------------------------------------------|
| Metrics   |                          |          |                                                                                    |
|           | name                     |          | confidenceScore                                                                    |
|           | correspondingMeasurement |          | confidenceScore                                                                    |
|           | function                 |          | ML inference                                                                       |
|           | unit                     |          | %                                                                                  |
|           | description              |          | how confident the model is that the detected class matches the object in the image |

# Parameters-detectionThreshold

| Concept    | Key          | Subkey   | Values                                                                                                          |
|:-----------|:-------------|:---------|:----------------------------------------------------------------------------------------------------------------|
| Parameters |              |          |                                                                                                                 |
|            | name         |          | detection_threshold                                                                                             |
|            | type         |          | Integer                                                                                                         |
|            | mandatory    |          | true                                                                                                            |
|            | defaultValue |          | 42                                                                                                              |
|            | description  |          | This parameter can be used to configure the included algorithm in a certain way, possible values: "A", "B", "Z" |

# Model

| Concept               | Key                         | Subkey   | Values                                                                                                                                                                                                     |
|:----------------------|:----------------------------|:---------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description           |                             |          |                                                                                                                                                                                                            |
|                       | ID                          |          | <M-ID_Flower-Classification>                                                                                                                                                                               |
|                       | Name                        |          | Flower Classification                                                                                                                                                                                      |
|                       | Version                     |          | 1.0.0                                                                                                                                                                                                      |
|                       | License                     |          | Public Domain                                                                                                                                                                                              |
|                       | Provider                    |          | DFKI                                                                                                                                                                                                       |
|                       | Provider_contacts           |          |                                                                                                                                                                                                            |
|                       | AuthTool                    |          |                                                                                                                                                                                                            |
|                       | Type                        |          | Tensorflow                                                                                                                                                                                                 |
|                       | Fidelity                    |          | SavedModel                                                                                                                                                                                                 |
|                       | REPOSITORY_URI              |          | s3://dbrain-s3-test                                                                                                                                                                                        |
|                       | PATH                        |          | dfki/flower/model                                                                                                                                                                                          |
|                       | FILENAME                    |          | dfki_ml_flower-inference.zip                                                                                                                                                                               |
|                       | State_depend                |          |                                                                                                                                                                                                            |
| Parameters            |                             |          |                                                                                                                                                                                                            |
|                       | In-slots                    |          |                                                                                                                                                                                                            |
|                       | Outputs                     |          | {detectedClass, confidenceScore}                                                                                                                                                                           |
|                       | CosimSolverInfo             |          |                                                                                                                                                                                                            |
| Dependant FMUs        |                             |          |                                                                                                                                                                                                            |
|                       | Dependencies                |          |                                                                                                                                                                                                            |
| OS Requirements       |                             |          |                                                                                                                                                                                                            |
|                       | osArch                      |          |                                                                                                                                                                                                            |
|                       | osType                      |          |                                                                                                                                                                                                            |
|                       | osDistribution              |          |                                                                                                                                                                                                            |
| Hardware Requirements |                             |          |                                                                                                                                                                                                            |
|                       | recommendedNumberOfGPUCores |          |                                                                                                                                                                                                            |
|                       | minimumNumberOfGPUCores     |          |                                                                                                                                                                                                            |
|                       | recommendedGPURAM           |          |                                                                                                                                                                                                            |
|                       | minimumGPURAM               |          |                                                                                                                                                                                                            |
|                       | recommendedRAM              |          |                                                                                                                                                                                                            |
|                       | minimumRAM                  |          |                                                                                                                                                                                                            |
|                       | recommendedCPUs             |          |                                                                                                                                                                                                            |
|                       | minimumCPUs                 |          |                                                                                                                                                                                                            |
|                       | requiredDiskSpace           |          |                                                                                                                                                                                                            |
| Publishing            |                             |          |                                                                                                                                                                                                            |
|                       | Description                 |          | Model is based on a general imagenet model (https://tfhub.dev/google/imagenet/mobilenet_v3_small_100_224/classification/5) and has been fine-tuned on flower dataset, to classifiy different flower types. |

# Algorithm

| Concept     | Key                  | Subkey   | Values                                                             |
|:------------|:---------------------|:---------|:-------------------------------------------------------------------|
| Description |                      |          |                                                                    |
|             | id                   |          | <A-ID_DFKI-Object-Classification-Algorithm>                        |
|             | name                 |          | DFKI Object Classification Algorithm                               |
|             | description          |          | Algorithm for ML inferences based on tensorflow                    |
|             | classificationSchema |          | ML                                                                 |
|             | type                 |          | {neural network, deep learning, convolutional neural network, CNN} |
|             | author               |          | Valerie Poser                                                      |
|             | date                 |          |                                                                    |
|             | version              |          | 1.0.0                                                              |
| Algorithm   |                      |          |                                                                    |
|             | listOfMicroservices  |          | [<MS-ID_Microservice_ML-Inference>]                                |
|             | deploymentMapping    |          | [<MS-ID_Microservice_ML-Inference>:hostA]                          |

# MA Pair

| Concept    | Key        | Subkey   | Values                                      |
|:-----------|:-----------|:---------|:--------------------------------------------|
| Definition |            |          |                                             |
|            | ID         |          | <MA-ID_DFKI-Flower-Classification>          |
|            | Created at |          |                                             |
|            | Version    |          | 1.0.0                                       |
|            | Author     |          |                                             |
|            | Licensor   |          |                                             |
|            | Derivation |          |                                             |
|            | Name       |          | DFKI Flower Classification                  |
|            | Scope      |          | Classification of flowers in images         |
|            | IP Family  |          | <IPF-ID_DFKI-Object-Detection>              |
|            | Namespace  |          |                                             |
|            | M Asset    |          | <M-ID_Flower-Classification>                |
|            | A Asset    |          | <A-ID_DFKI-Object-Classification-Algorithm> |
|            | Rules      |          |                                             |
|            | Frequency  |          |                                             |
|            | Payload    |          |                                             |

# DMA Tuple

| Concept             | Key               | Subkey   | Values                              |
|:--------------------|:------------------|:---------|:------------------------------------|
| Definition          |                   |          |                                     |
|                     | ID                |          | <DMA-ID_DFKI-Flower-Classification> |
|                     | Created at        |          |                                     |
|                     | Version           |          | 1.0.0                               |
|                     | Author            |          |                                     |
|                     | Licensor          |          |                                     |
|                     | Derivation        |          |                                     |
|                     | Name              |          | Flower Classification for Valerie   |
|                     | Scope             |          |                                     |
|                     | IP Instance       |          |                                     |
|                     | Namespace         |          |                                     |
|                     | MA Pair           |          | <MA-ID_DFKI-Flower-Classification>  |
|                     | Schedule          |          |                                     |
|                     | Payload           |          |                                     |
| Data Assets Mapping |                   |          |                                     |
|                     | DataAssetsMapping |          | <DAM-ID_DFKI-Flower-Classification> |
| Deployments         |                   |          |                                     |
|                     | Deployments       |          | <DEP-ID_DFKI-Flower-Classification> |

# DataAssetsMapping

| Concept           | Key               | Subkey           | Values                       |
|:------------------|:------------------|:-----------------|:-----------------------------|
| DataAssetsMapping |                   |                  |                              |
|                   | *MICROSERVICE_ID* |                  | <M-ID_Flower-Classification> |
|                   |                   | *DATA_SOURCE_ID* | <D-ID_DFKI-Flower-Stream>    |

# Supporting Metadata

| Concept                     | Key         | Subkey   | Values   |
|:----------------------------|:------------|:---------|:---------|
| Person                      |             |          |          |
|                             | ID          |          |          |
|                             | Created at  |          |          |
|                             | Version     |          |          |
|                             | First name  |          |          |
|                             | Last name   |          |          |
|                             | Email       |          |          |
|                             | CV          |          |          |
|                             | Image       |          |          |
|                             | Affiliation |          |          |
| Legal Entity (Organization) |             |          |          |
|                             | ID          |          |          |
|                             | Created at  |          |          |
|                             | Version     |          |          |
|                             | Author      |          |          |
|                             | Name        |          |          |
|                             | Description |          |          |
|                             | Logo        |          |          |
|                             | URL         |          |          |
|                             | Location    |          |          |
|                             | Phone       |          |          |
|                             | VAT ID No.  |          |          |
| IP Family                   |             |          |          |
|                             | ID          |          |          |
|                             | Created at  |          |          |
|                             | Version     |          |          |
|                             | Author      |          |          |
|                             | Manager     |          |          |
|                             | Name        |          |          |
|                             | Image       |          |          |
|                             | Model No.   |          |          |
|                             | Description |          |          |
|                             | Capacity    |          |          |
|                             | IP Man.     |          |          |
| IP Instance                 |             |          |          |
|                             | ID          |          |          |
|                             | Created at  |          |          |
|                             | Version     |          |          |
|                             | Author      |          |          |
|                             | Operator    |          |          |
|                             | IP Family   |          |          |
|                             | Name        |          |          |
|                             | Image       |          |          |
|                             | Serial No.  |          |          |
|                             | Description |          |          |
|                             | Location    |          |          |

# Deployment

| Concept     | Key         | Subkey           | Values                              |
|:------------|:------------|:-----------------|:------------------------------------|
| Description |             |                  |                                     |
|             | id          |                  | <DEP-ID_DFKI-Flower-Classification> |
|             | name        |                  |                                     |
|             | author      |                  |                                     |
|             | date        |                  |                                     |
| Deployments |             |                  |                                     |
|             | type        |                  |                                     |
|             | cloudbroker |                  |                                     |
|             |             | deployment_id    |                                     |
|             |             | instance_type_id |                                     |
|             |             | key_pair_id      |                                     |
|             |             | opened_port      |                                     |
|             |             | endpoint         |                                     |
|             |             | cloud_config     |                                     |
|             | edge        |                  |                                     |
|             |             | endpoint         |                                     |

# ConfigurationData

| Concept           | Key              | Subkey   | Values   |
|:------------------|:-----------------|:---------|:---------|
| ConfigurationData |                  |          |          |
|                   | filePath         |          |          |
|                   | fileContent      |          |          |
|                   | mountPropagation |          |          |

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
