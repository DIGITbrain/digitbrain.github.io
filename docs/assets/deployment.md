| Concept             | Key                 | sub key            | Type                              | Example Value | Comment                                          | condition |
| ------------------- | ------------------- | ------------------ | --------------------------------- | ------------- | ------------------------------------------------ | --------- |
| Description         |                     |                    |                                   |               |                                                  |           |
|                     | id                  |                    | UUID                              |               | DIGITbrain reference                             | AUTO      |
|                     | name                |                    | String                            |               | Short name for the node/device                   | Mandatory |
|                     | author              |                    | String                            |               | Created by                                       | Mandatory |
|                     | date                |                    | Date                              |               | Created on                                       | AUTO      |
| Deployments         |                     |                    |                                   |               |                                                  |           |
|                     | type                |                    | Enumeration {cloudbroker, edge}   |               | computing centre                                 | Mandatory |
|                     | cloudbroker         |                    | Map of…                           |               |                                                  |           |
|                     |                     | deployment_id      | UUID                              |               | ID of CloudBroker Deployment                     |           |
|                     |                     | instance_type_id   | UUID                              |               | ID of CloudBroker InstanceType                   |           |
|                     |                     | key_pair_id        | UUID                              |               | ID of CloudBroker Key Pair                       |           |
|                     |                     | opened_port        | String (comma separated integers) |               | Ports to open at cloud side                      |           |
|                     |                     | endpoint           | URL                               |               | Endpoint of the CB Platform                      |           |
|                     | edge                |                    | Map of…                           |               |                                                  |           |
|                     |                     | endpoint           | URL                               |               | accesible IP or FQDN of edge device              |           |
| Data Source Mapping |                     |                    |                                   |               |                                                  |           |
|                     | data_source_mapping |                    | Map of…                           |               |                                                  | Optional  |
|                     |                     | microserviceA_data | List of UUIDs                     |               | UUIDs of required data sources for MicroserviceA |           |
|                     |                     | microserviceB_data | List of UUIDs                     |               | UUIDs of required data sources for MicroserviceB |           |
|                     |                     | microserviceC_data | List of UUIDs                     |               | UUIDs of required data sources for MicroserviceC |           |
