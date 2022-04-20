
<style>
  .md-content__button {
    display: none;
  }
</style>


# Microservice_Flower

| Concept               | Key                        | Subkey   | Values                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|:----------------------|:---------------------------|:---------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description           |                            |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                       | id                         |          | "MSID_FLOWER"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                       | name                       |          | "Object Detection & Classification Network"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                       | author                     |          | "DFKI"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                       | date                       |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                       | version                    |          | "1.0.0"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                       | description                |          | "Detection and classification of objects from Images"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                       | classificationSchema       |          | "ML"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                       | type                       |          | ["neural network", "deep learning", "convolutional neural network", "CNN"]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Service               |                            |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                       | deploymentFormat           |          | "docker-compose"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                       | deploymentData             |          | {     "version": "3.9",     "services": {       "inf": {         "image": "dbs-container-repo.emgora.eu/dfki/ml/flower-inference:latest",         "environment": {             "TEST_MESSAGE": "This model was trained on pictures of flowers.",             "KAFKA_URI_IN": "{{DATA1.DATA_URI}}",             "KAFKA_URI_OUT": "kafka:193.225.250.14:9093:dfki-flower-result",             "CONSUMER_TIMEOUT": "3000",             "SSL_ACTIVE": "true",             "SLEEP_TIME": "10", "MODEL_PATH":"{{MODEL.PATH}}/{{MODEL.FILENAME}}"         }       }     }   } |
|                       | configurationData          |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                       | mountedSharedDirectories   |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Hardware Requirements |                            |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                       | recommendedNumberOfGPUs    |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                       | recommendedGPURAM          |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                       | gpuType                    |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                       | hpcRequired                |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                       | edgeType                   |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                       | recommendedRAM             |          | 2                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | recommendedCPUs            |          | 2                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | requiredDiskSpace          |          | 42GB                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| OS Requirements       |                            |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                       | osArch                     |          | "x86_64"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                       | osType                     |          | "linux"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Data Resources        |                            |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                       | dataResource               |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Model                 |                            |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                       | model_types                |          | SavedModel (Tensorflow)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                       | model_recommendedAuthTools |          | Tensorflow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Parameters            |                            |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                       | parameters                 |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Metrics               |                            |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                       | metrics                    |          | [<Metric-ID_ConfidenceScore>, <Metric-ID_DetectedClass>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

# Algorithm

| Concept     | Key                  | Subkey   | Values                                                                     |
|:------------|:---------------------|:---------|:---------------------------------------------------------------------------|
| Description |                      |          |                                                                            |
|             | id                   |          | "ALGID_FLOWER"                                                             |
|             | name                 |          | "DFKI Object Classification Algorithm"                                     |
|             | description          |          | "Algorithm for ML inferences based on tensorflow"                          |
|             | classificationSchema |          | "ML"                                                                       |
|             | type                 |          | ["neural network", "deep learning", "convolutional neural network", "CNN"] |
|             | author               |          | "Valerie Poser"                                                            |
|             | date                 |          |                                                                            |
|             | version              |          | "1.0.0"                                                                    |
| Algorithm   |                      |          |                                                                            |
|             | listOfMicroservices  |          | ["MSID_FLOWER"]                                                            |
|             | deploymentMapping    |          | {"MSID_FLOWER":"HOSTID_FLOWER"}                                            |

# Model

| Concept               | Key                         | Subkey   | Values                                                                                                                                                                                                       |
|:----------------------|:----------------------------|:---------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description           |                             |          |                                                                                                                                                                                                              |
|                       | ID                          |          | "MODELID_FLOWER"                                                                                                                                                                                             |
|                       | Name                        |          | Flower Classification                                                                                                                                                                                        |
|                       | Version                     |          | "1.0.0"                                                                                                                                                                                                      |
|                       | License                     |          | Public Domain                                                                                                                                                                                                |
|                       | Provider                    |          | DFKI                                                                                                                                                                                                         |
|                       | Provider_contacts           |          |                                                                                                                                                                                                              |
|                       | AuthTool                    |          |                                                                                                                                                                                                              |
|                       | Type                        |          | Tensorflow                                                                                                                                                                                                   |
|                       | Fidelity                    |          | SavedModel                                                                                                                                                                                                   |
|                       | REPOSITORY_URI              |          | "s3://dbrain-s3-test"                                                                                                                                                                                        |
|                       | PATH                        |          | "dfki/flower/model"                                                                                                                                                                                          |
|                       | FILENAME                    |          | "dfki_ml_flower-inference.zip"                                                                                                                                                                               |
|                       | State_depend                |          |                                                                                                                                                                                                              |
| Parameters            |                             |          |                                                                                                                                                                                                              |
|                       | In-slots                    |          |                                                                                                                                                                                                              |
|                       | Outputs                     |          | [detectedClass, confidenceScore]                                                                                                                                                                             |
|                       | CosimSolverInfo             |          |                                                                                                                                                                                                              |
| Dependant FMUs        |                             |          |                                                                                                                                                                                                              |
|                       | Dependencies                |          |                                                                                                                                                                                                              |
| OS Requirements       |                             |          |                                                                                                                                                                                                              |
|                       | osArch                      |          |                                                                                                                                                                                                              |
|                       | osType                      |          |                                                                                                                                                                                                              |
|                       | osDistribution              |          |                                                                                                                                                                                                              |
| Hardware Requirements |                             |          |                                                                                                                                                                                                              |
|                       | recommendedNumberOfGPUCores |          |                                                                                                                                                                                                              |
|                       | minimumNumberOfGPUCores     |          |                                                                                                                                                                                                              |
|                       | recommendedGPURAM           |          |                                                                                                                                                                                                              |
|                       | minimumGPURAM               |          |                                                                                                                                                                                                              |
|                       | recommendedRAM              |          |                                                                                                                                                                                                              |
|                       | minimumRAM                  |          |                                                                                                                                                                                                              |
|                       | recommendedCPUs             |          |                                                                                                                                                                                                              |
|                       | minimumCPUs                 |          |                                                                                                                                                                                                              |
|                       | requiredDiskSpace           |          |                                                                                                                                                                                                              |
| Publishing            |                             |          |                                                                                                                                                                                                              |
|                       | Description                 |          | "Model is based on a general imagenet model (https://tfhub.dev/google/imagenet/mobilenet_v3_small_100_224/classification/5) and has been fine-tuned on flower dataset, to classifiy different flower types." |

# Data

| Concept                             | Key              | Subkey   | Values                                                                                        |
|:------------------------------------|:-----------------|:---------|:----------------------------------------------------------------------------------------------|
| Administrative data                 |                  |          |                                                                                               |
|                                     | ID               |          | "DATAID_FLOWER"                                                                               |
|                                     | AUTHOR           |          |                                                                                               |
|                                     | PROVIDER         |          |                                                                                               |
|                                     | DATE             |          |                                                                                               |
| Description                         |                  |          |                                                                                               |
|                                     | DATA_NAME        |          | "DFKIFlowerStream"                                                                            |
|                                     | DATA_VERSION     |          | "1.0.0"                                                                                       |
|                                     | DATA_DESC        |          | This stream acts as a communication channel between an end user and an ML inference Algorithm |
|                                     | DATA_DESC_URL    |          |                                                                                               |
|                                     | DATA_SIZE        |          | 1m                                                                                            |
| Search support                      |                  |          |                                                                                               |
|                                     | DATA_TAGS        |          | ["jpg", "rgb"]                                                                                |
| Datakind specification              |                  |          |                                                                                               |
|                                     | DATA_KIND        |          | "STREAM"                                                                                      |
|                                     | DATA_DIRECTION   |          | "BIDIRECTIONAL"                                                                               |
|                                     | DATA_FORMAT      |          | ["text/plain", "application/octet-stream"]                                                    |
|                                     | DATA_STORE_TYPE  |          | "KAFKA"                                                                                       |
| Data access specification           |                  |          |                                                                                               |
|                                     | DATA_URI         |          | "kafka:193.225.250.14:9093:dfki-flower-in"                                                    |
|                                     | DATA_AUTH        |          | ["tls_manual"]                                                                                |
| Open parameters                     |                  |          |                                                                                               |
|                                     | DATA_CREDENTIALS |          |                                                                                               |
| Further access clauses (extensible) |                  |          |                                                                                               |
|                                     | DATA_AUX_INFO    |          | {"KAFKA_BROKER_VERSIOM":"2.7.0"}                                                              |
| Data content semantics              |                  |          |                                                                                               |
|                                     | DATA_SCHEMA      |          |                                                                                               |
|                                     | DATA_SCHEMA_URL  |          |                                                                                               |

# MA Pair

| Concept    | Key        | Subkey   | Values                              |
|:-----------|:-----------|:---------|:------------------------------------|
| Definition |            |          |                                     |
|            | ID         |          | "MAID_FLOWER"                       |
|            | Created at |          |                                     |
|            | Version    |          | 1.0.0                               |
|            | Author     |          |                                     |
|            | Licensor   |          |                                     |
|            | Derivation |          |                                     |
|            | Name       |          | DFKI Flower Classification          |
|            | Scope      |          | Classification of flowers in images |
|            | IP Family  |          | <IPF-ID_DFKI-Object-Detection>      |
|            | Namespace  |          |                                     |
|            | M Asset    |          | "MODELID_FLOWER"                    |
|            | A Asset    |          | "ALGID_FLOWER"                      |
|            | Rules      |          |                                     |
|            | Frequency  |          |                                     |
|            | Payload    |          |                                     |

# DMA Tuple

| Concept             | Key               | Subkey   | Values                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|:--------------------|:------------------|:---------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Definition          |                   |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                     | ID                |          | "DMAID_FLOWER"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                     | Created at        |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                     | Version           |          | 1.0.0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                     | Author            |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                     | Licensor          |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                     | Derivation        |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                     | Name              |          | Flower Classification for Valerie                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                     | Scope             |          | This DMA tuple contains all assets forming a complete object detection and classification (machine learning) stack, including in- and output streams, a trained model, as well as the inference algorithm.                                                                                                                                                                                                                                                                                                                                                              |
|                     | IP Instance       |          | 123e4567-e89b-12d3-a456-426614174000                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                     | Namespace         |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                     | MA Pair           |          | "MAID_FLOWER"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                     | Schedule          |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                     | Payload           |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Data Assets Mapping |                   |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                     | DataAssetsMapping |          | {"MSID_FLOWER": { "DATA1": "DATAID_FLOWER"}}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Deployments         |                   |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                     | Deployments       |          | {       "HOSTID_FLOWER": {         "name": "Object Detection",         "author": "Valerie Poser",         "type": "cloudbroker",         "cloudbroker": {           "deployment_id": "16b1e2d4-3a2c-406e-8c45-5637099021f0",           "instance_type_id": "ca727925-a5ca-4697-b2c3-8788d82457d5",           "key_pair_id": "22873697-c9ec-4685-bddc-760436662bce",           "opened_port": "2379,4500,30010,8285,30012,443,10250,30888,30000,6443,22,500,8472,30012,4500,500",           "endpoint": "https://cloudsme-cbp.scaletools.com.ua"         }       }     } |

# Deployment

| Concept     | Key         | Subkey           | Values                                 |
|:------------|:------------|:-----------------|:---------------------------------------|
| Description |             |                  |                                        |
|             | id          |                  | "HOSTID_FLOWER"                        |
|             | name        |                  | "DFKI object detection infrastructure" |
|             | author      |                  | "Valerie Poser"                        |
|             | date        |                  |                                        |
| Deployments |             |                  |                                        |
|             | type        |                  | "cloudbroker"                          |
|             | cloudbroker |                  |                                        |
|             |             | deployment_id    |                                        |
|             |             | instance_type_id |                                        |
|             |             | key_pair_id      |                                        |
|             |             | opened_port      |                                        |
|             |             | endpoint         |                                        |
|             |             | cloud_config     |                                        |
|             | edge        |                  |                                        |
|             |             | endpoint         |                                        |

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

# DataAssetsMapping

| Concept           | Key               | Subkey           | Values          |
|:------------------|:------------------|:-----------------|:----------------|
| DataAssetsMapping |                   |                  |                 |
|                   | *MICROSERVICE_ID* |                  | "MSID_FLOWER"   |
|                   |                   | *DATA_SOURCE_ID* | "DATAID_FLOWER" |

# ConfigurationData

| Concept           | Key              | Subkey   | Values                              |
|:------------------|:-----------------|:---------|:------------------------------------|
| ConfigurationData |                  |          |                                     |
|                   | filePath         |          | /data/rclone.conf                   |
|                   | fileContent      |          | [s3-server]\n    access_key: 123abc |
|                   | mountPropagation |          | Bidirectional                       |

# Data Resources

| Concept        | Key              | Subkey   | Values                       |
|:---------------|:-----------------|:---------|:-----------------------------|
| Data Resources |                  |          |                              |
|                | DATA_RESOURCE_ID |          | kafka_stream                 |
|                | DATA_KIND        |          | ["STREAM"]                   |
|                | DATA_DIRECTION   |          | ["BIDIRECTIONAL"]            |
|                | DATA_FORMAT      |          | ["image/jpeg", "text/plain"] |
|                | DATA_SOURCE_TYPE |          | ["KAFKA"]                    |
|                | DATA_AUTH_TYPE   |          | ["tls_manual"]               |
|                | DATA_SCHEMA      |          |                              |
|                | DATA_AUX_INFO    |          |                              |

# Parameters

| Concept    | Key          | Subkey   | Values                                                                                                             |
|:-----------|:-------------|:---------|:-------------------------------------------------------------------------------------------------------------------|
| Parameters |              |          |                                                                                                                    |
|            | name         |          | "detection_threshold"                                                                                              |
|            | type         |          | "Integer"                                                                                                          |
|            | mandatory    |          | True                                                                                                               |
|            | defaultValue |          | 42                                                                                                                 |
|            | description  |          | "This parameter can be used to configure the included algorithm in a certain way, possible values: 'A', 'B', 'Z'." |

# Metrics

| Concept   | Key                      | Subkey   | Values                                               |
|:----------|:-------------------------|:---------|:-----------------------------------------------------|
| Metrics   |                          |          |                                                      |
|           | name                     |          | "detectedClass"                                      |
|           | correspondingMeasurement |          | "detectedClass"                                      |
|           | function                 |          | "ML inference"                                       |
|           | unit                     |          | "enum"                                               |
|           | description              |          | "which classes has been detected in the input image" |

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
