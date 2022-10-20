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

    === "Example"
        ``` yaml     
        "HOSTID_MYHOST_A"
        ```

`name`{ #name }
:   **Required**-*String*- Short name for the node/device

    === "Example"
        ``` yaml     
        "Ubuntu small"
        ```

`author`{ #author }
:   **Required**-*String*- Created by

    === "Example"
        ``` yaml     
        "Jay"
        ```

`date`{ #date }
:   **Auto-generated**-*Date*- Created on

    === "Example"
        ``` yaml     
        18.08.2022
        ```


### Deployments


`type`{ #type }
:   **Required**-*Enumeration ["cloudbroker", "edge"]*- computing centre

    === "Example"
        ``` yaml     
        "cloudbroker"
        ```

`cloudbroker`{ #cloudbroker }
:   **Optional**-*Map[String, String]*- Configuration data for a CloudBroker instance

    `deployment_id`{ #deployment_id }
:   **Optional**-*UUID*- ID of CloudBroker Deployment
        === "Example"
            ``` yaml     
            "16b1e2d4-3a2c-406e-8c45-5637099021f0"
            ```

    `instance_type_id`{ #instance_type_id }
:   **Optional**-*UUID*- ID of CloudBroker InstanceType
        === "Example"
            ``` yaml     
            "ca727925-a5ca-4697-b2c3-8788d82457d5"
            ```

    `key_pair_id`{ #key_pair_id }
:   **Optional**-*UUID*- ID of CloudBroker Key Pair
        === "Example"
            ``` yaml     
            "ap207925-a5ca-4697-b2c3-5637099021f0"
            ```

    `opened_port`{ #opened_port }
:   **Optional**-*String (comma separated integers)*- Ports to open at cloud side
        === "Example"
            ``` yaml     
            "80,443,8080,30010"
            ```

    `endpoint`{ #endpoint }
:   **Optional**-*URL*- Endpoint of the CB Platform
        === "Example"
            ``` yaml     
            "https://cloudsme-cbp.scaletools.com.ua"
            ```

    `domain_name`{ #domain_name }
:   **Optional**-*String*- Subdomain (on cbp-routing.ch) to create and attach to this instance using dynamic DNS. For the given example, the following domain will be assigned to the instance: mysubdomain.cbp-routing.ch
        === "Example"
            ``` yaml     
            "mysubdomain"
            ```

    `domain_names`{ #domain_names }
:   **Optional**-*List of UUIDs*- ID of a CloudBroker Domain Name for this instance
        === "Example"
            ``` yaml     
            ["om207925-b52a-4697-b2c3-563702208h9"]
            ```

    `cloud_config`{ #cloud_config }
:   **Optional**-*Map*- cloud-init - https://cloudinit.readthedocs.io/ - configuration for contextualisation of the VM
        === "Example"
            ``` yaml     
            {
              "runcmd": ["echo one", "echo two"]
            }
            ```

`edge`{ #edge }
:   **Optional**-*Map[String, String]*- Connection data for a bring-your-own edge

    `endpoint`{ #endpoint }
:   **Optional**-*URL*- accesible IP or FQDN of edge device

    `ssh_username`{ #ssh_username }
:   **Optional**-*String*- username for SSH connection. Defaults to ubuntu
        === "Example"
            ``` yaml     
            "ubuntu"
            ```

    `ssh_private_key`{ #ssh_private_key }
:   **Optional**-*String*- private key for SSH connection.
        === "Example"
            ``` yaml     
            "-----BEGIN RSA PRIVATE KEY----- MIIEowIBAAKCAQEApwn..."
            ```
