<style>
  .md-content__button {
    display: none;
  }
</style>
# Deployment Fields

**This information is also available in [table format](/tables/deployment/)**


## Available Fields 

The metadata specification for a DIGITbrain Deployment
has these sections:

- [Description](#description)
- [Deployments](#deployments)


### Description


`id`{ #id }
:   **Auto-generated**-*UUID*- DIGITbrain reference


`name `{ #name- }
:   **Required**-*String*- Short name for the node/device


`author `{ #author- }
:   **Required**-*String*- Created by


`date`{ #date }
:   **Auto-generated**-*Date*- Created on



### Deployments


`type`{ #type }
:   **Required**-*Enumeration {cloudbroker, edge}*- computing centre


`cloudbroker`{ #cloudbroker }
:   **Optional**-*Map of…*- Configuration data for a CloudBroker instance

    `deployment_id`{ #deployment_id }
:   **Optional**-*UUID*- ID of CloudBroker Deployment

    `instance_type_id`{ #instance_type_id }
:   **Optional**-*UUID*- ID of CloudBroker InstanceType

    `key_pair_id`{ #key_pair_id }
:   **Optional**-*UUID*- ID of CloudBroker Key Pair

    `opened_port`{ #opened_port }
:   **Optional**-*String (comma separated integers)*- Ports to open at cloud side

    `endpoint`{ #endpoint }
:   **Optional**-*URL*- Endpoint of the CB Platform

    `cloud_config`{ #cloud_config }
:   **Optional**-*String*- cloud-init configuration for contextualisation of the VM
        === "Example"
            ``` yaml     
            #cloud-config\nruncmd:\n- [ sh, -xc, \"echo 'hello world!'\" ]
            ```

`edge`{ #edge }
:   **Optional**-*Map of…*- Connection data for a bring-your-own edge

    `endpoint`{ #endpoint }
:   **Optional**-*URL*- accesible IP or FQDN of edge device
