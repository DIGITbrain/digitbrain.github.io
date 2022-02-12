
<style>
  .md-content__button {
    display: none;
  }
</style>

**This information is also available in** **[list format](/attributes/deployment/)**

| Concept                                                  | Key         | Subkey           | Type                              | Example Value                                                  | Comment                                                  | Condition   |
|:---------------------------------------------------------|:------------|:-----------------|:----------------------------------|:---------------------------------------------------------------|:---------------------------------------------------------|:------------|
| *This substructure is part of [DMA Tuple](dma_tuple.md)* |             |                  |                                   |                                                                |                                                          |             |
| Description                                              |             |                  |                                   |                                                                |                                                          |             |
|                                                          | id          |                  | UUID                              |                                                                | DIGITbrain reference                                     | auto        |
|                                                          | name        |                  | String                            |                                                                | Short name for the node/device                           | mandatory   |
|                                                          | author      |                  | String                            |                                                                | Created by                                               | mandatory   |
|                                                          | date        |                  | Date                              |                                                                | Created on                                               | auto        |
| Deployments                                              |             |                  |                                   |                                                                |                                                          |             |
|                                                          | type        |                  | Enumeration {cloudbroker, edge}   |                                                                | computing centre                                         | mandatory   |
|                                                          | cloudbroker |                  | Map of…                           |                                                                | Configuration data for a CloudBroker instance            |             |
|                                                          |             | deployment_id    | UUID                              |                                                                | ID of CloudBroker Deployment                             |             |
|                                                          |             | instance_type_id | UUID                              |                                                                | ID of CloudBroker InstanceType                           |             |
|                                                          |             | key_pair_id      | UUID                              |                                                                | ID of CloudBroker Key Pair                               |             |
|                                                          |             | opened_port      | String (comma separated integers) |                                                                | Ports to open at cloud side                              |             |
|                                                          |             | endpoint         | URL                               |                                                                | Endpoint of the CB Platform                              |             |
|                                                          |             | cloud_config     | String                            | #cloud-config\nruncmd:\n- [ sh, -xc, \"echo 'hello world!'\" ] | cloud-init configuration for contextualisation of the VM |             |
|                                                          | edge        |                  | Map of…                           |                                                                | Connection data for a bring-your-own edge                |             |
|                                                          |             | endpoint         | URL                               |                                                                | accesible IP or FQDN of edge device                      |             |