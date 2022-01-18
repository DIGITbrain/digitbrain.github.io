<style>
  .md-content__button {
    display: none;
  }
</style>
# Deployment Metadata Fields

## Available Fields 

The metadata specification for a DIGITbrain Deployment
has these sections:

- [Description](#description)
- [Deployments](#deployments)
- [Data Source Mapping](#data-source-mapping)


### Description


`id`

:   **Auto-generated**-*UUID*- DIGITbrain reference


`name `

:   **Required**-*String*- Short name for the node/device


`author `

:   **Required**-*String*- Created by


`date`

:   **Auto-generated**-*Date*- Created on



### Deployments


`type`

:   **Required**-*Enumeration {cloudbroker, edge}*- computing centre


`cloudbroker`

:   **Optional**-*Map of…*- Configuration data for a CloudBroker instance

`deployment_id`

:   **Optional**-*UUID*- ID of CloudBroker Deployment

`instance_type_id`

:   **Optional**-*UUID*- ID of CloudBroker InstanceType

`key_pair_id`

:   **Optional**-*UUID*- ID of CloudBroker Key Pair

`opened_port`

:   **Optional**-*String (comma separated integers)*- Ports to open at cloud side

`endpoint`

:   **Optional**-*URL*- accesible IP or FQDN of edge device

`edge`

:   **Optional**-*Map of…*- Connection data for a bring-your-own edge


### Data Source Mapping


`data_source_mapping`

:   **Optional**-*Map of…*- Mapping Microservices to Data assets, as available in the DMA Tuple

`microserviceA_data`

:   **Optional**-*List of UUIDs*- UUIDs of required data sources for MicroserviceA

`microserviceB_data`

:   **Optional**-*List of UUIDs*- UUIDs of required data sources for MicroserviceB

`microserviceC_data`

:   **Optional**-*List of UUIDs*- UUIDs of required data sources for MicroserviceC
