# Data Assets Mapping in DIGITbrain

## Introduction

The Data Assets Mapping substructure in a DMA Tuple will map Data assets 
with Data Sources that have been specified for each Microservice that makes up
an Algorithm. Data Sources describe what type/kind of data the Microservice
expects (see the [Input Data](/attributes/microservice#inputdata) and
[Output Data](/attributes/microservice#outputdata) fields). This Data Assets
Mapping substructure will be used to connect those Data Sources to concrete Data
assets.

## Pre-requisites

Data Sources ([Input Data](/attributes/microservice#inputdata) and/or
[Output Data](/attributes/microservice#outputdata)) fields should be specified on
at least one of the Microservices that makes up the Algorithm in the DMA Tuple.
The Data Assets must already be published on the DIGITbrain platform.

## Metadata describing Deployment

For a closer look at this metadata, use the following resources:

- [Attribute Listing](attributes/dataassetmapping.md) for an itemised listing of fields
- [Metadata Table](tables/dataassetsmapping.md) for a table-formatted overview

## An example

See the below JSON for an example of how **Microservice**, **Data** and
**DataAssetsMapping** work together.

=== "Microservice"

    ```json
    {
      "Microservices": [
        {
          "id": "microservice_aaa_uuid",
          "deploymentData": "docker run -e STREAM={{ my_kafka_out.DATA_URI }} dfki/img",
          "outputData": [
            {
              "output_id": "my_kafka_out",
              "DATA_KIND": "stream",
              "DATA_SOURCE_TYPE": "kafka",
              //etc...
            },
            {
              "output_id": "my_file_out",
              //etc...
            }
          ],
        },
        {
          "id": "microservice_bbb_uuid",
          //etc...
          "inputData": [
            {
              "input_id": "my_stream_in",
              "DATA_KIND": "stream",
              "DATA_SOURCE_TYPE": "kafka",
              //etc...
            },
          ],
        }
      ],
    ```

=== "Data"

    ``` json
    "Data": [
      {
        "id": "data_zzz_uuid",
        "DATA_DESC": "This is some important data.",
        "DATA_URI": "kafka://host/topic#1",
        //etc...
      },
      {
        "id": "data_yyy_uuid",
        //etc...
      }
    ],
    ```

=== "DataAssetsMapping"

    ``` json
    "DMA Tuple": {
      "id": "dma_tuple_ggg_uuid",
      "DataAssetsMapping": {
        "microservice_aaa": {
          "my_kafka_out": "data_zzz_uuid",
          "my_file_out": "data_yyy_uuid"
        }
        "microservice_bbb_uuid": {
          "my_stream_in": "data_zzz_uuid"
        }
      }
      //etc...
    }
    ```