
<style>
  .md-content__button {
    display: none;
  }
</style>

**This information is also available in** **[list format](/attributes/deployment/)**

| Concept     | Key         | Subkey           | Type                              | Example Value                                                  | Comment                                                  | Condition   |
|:------------|:------------|:-----------------|:----------------------------------|:---------------------------------------------------------------|:---------------------------------------------------------|:------------|
| Description |             |                  |                                   |                                                                |                                                          |             |
|             | id          |                  | UUID                              |                                                                | DIGITbrain reference                                     | auto        |
|             | name        |                  | String                            |                                                                | Short name for the node/device                           | mandatory   |
|             | author      |                  | String                            |                                                                | Created by                                               | mandatory   |
|             | date        |                  | Date                              |                                                                | Created on                                               | auto        |
| Deployments |             |                  |                                   |                                                                |                                                          |             |
|             | type        |                  | Enumeration {cloudbroker, edge}   |                                                                | computing centre                                         | mandatory   |
|             | cloudbroker |                  | Map of…                           |                                                                | Configuration data for a CloudBroker instance            |             |
|             |             | deployment_id    | UUID                              |                                                                | ID of CloudBroker Deployment                             | optional    |
|             |             | instance_type_id | UUID                              |                                                                | ID of CloudBroker InstanceType                           | optional    |
|             |             | key_pair_id      | UUID                              |                                                                | ID of CloudBroker Key Pair                               | optional    |
|             |             | opened_port      | String (comma separated integers) |                                                                | Ports to open at cloud side                              | optional    |
|             |             | endpoint         | URL                               |                                                                | Endpoint of the CB Platform                              | optional    |
|             |             | cloud_config     | String                            | #cloud-config\nruncmd:\n- [ sh, -xc, \"echo 'hello world!'\" ] | cloud-init configuration for contextualisation of the VM | optional    |
|             | edge        |                  | Map of…                           |                                                                | Connection data for a bring-your-own edge                |             |
|             |             | endpoint         | URL                               |                                                                | accesible IP or FQDN of edge device                      | optional    |