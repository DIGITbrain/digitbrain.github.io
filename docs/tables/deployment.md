<style>
  .md-typeset h1,
  .md-content__button {
    display: none;
  }
</style>
| Concept             | Key                 | Subkey             | Type                              | Example Value | Comment                                                             | Condition |
| ------------------- | ------------------- | ------------------ | --------------------------------- | ------------- | ------------------------------------------------------------------- | --------- |
| Description         |                     |                    |                                   |               |                                                                     |           |
|                     | id                  |                    | UUID                              |               | DIGITbrain reference                                                | auto      |
|                     | name                |                    | String                            |               | Short name for the node/device                                      | mandatory |
|                     | author              |                    | String                            |               | Created by                                                          | mandatory |
|                     | date                |                    | Date                              |               | Created on                                                          | auto      |
| Deployments         |                     |                    |                                   |               |                                                                     |           |
|                     | type                |                    | Enumeration {cloudbroker, edge}   |               | computing centre                                                    | mandatory |
|                     | cloudbroker         |                    | Map of…                           |               | Configuration data for a CloudBroker instance                       |           |
|                     |                     | deployment_id      | UUID                              |               | ID of CloudBroker Deployment                                        |           |
|                     |                     | instance_type_id   | UUID                              |               | ID of CloudBroker InstanceType                                      |           |
|                     |                     | key_pair_id        | UUID                              |               | ID of CloudBroker Key Pair                                          |           |
|                     |                     | opened_port        | String (comma separated integers) |               | Ports to open at cloud side                                         |           |
|                     |                     | endpoint           | URL                               |               | Endpoint of the CB Platform                                         |           |
|                     | edge                |                    | Map of…                           |               | Connection data for a bring-your-own edge                           |           |
|                     |                     | endpoint           | URL                               |               | accesible IP or FQDN of edge device                                 |           |
| Data Source Mapping |                     |                    |                                   |               |                                                                     |           |
|                     | data_source_mapping |                    | Map of…                           |               | Mapping Microservices to Data assets, as available in the DMA Tuple | optional  |
|                     |                     | microserviceA_data | List of UUIDs                     |               | UUIDs of required data sources for MicroserviceA                    |           |
|                     |                     | microserviceB_data | List of UUIDs                     |               | UUIDs of required data sources for MicroserviceB                    |           |
|                     |                     | microserviceC_data | List of UUIDs                     |               | UUIDs of required data sources for MicroserviceC                    |           |
