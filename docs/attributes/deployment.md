<style>
  .md-content__button {
    display: none;
  }
</style>
# Deployment Fields


The specification for a Delpoyment
has these fields:

`type`

:   **Required**– DIGITbrain supports cloud infrastructure deployed via the
CloudBroker platform, or bring-your-own Linux-based Edge devices. This should
be specified in this field. The other metadata in this section should be
completed according to the type (e.g. CloudBroker-specific metadata is not required
if `type: edge`)

    === "cloudbroker"

        ``` yaml
        type: cloudbroker
        cloudbroker:
          deployment_id:
          instance_type_id:
          key_pair_id:
          opened_port:
          domain_name:
          cloud_config:
          endpoint:
        ```

    === "edge"

        ``` yaml
        type: edge
        edge:
          endpoint:
          ssh_username:
          ssh_private_key:
        ```

### CloudBroker

`deployment_id`

:   **Required**– A CloudBroker deployment ties together software,
resource and region. Indicative IDs are given below, but any LTS
Debian-based Linux distribution should be supported. It is recommended
to use the MiCADO-Optimised deployment.


    === "MiCADO-Optimised"

        ``` yaml
        1860cb3f-4f23-417f-a1f1-3705158cd3b3
        ```

    === "Ubuntu 20.04"

        ``` yaml
        16b1e2d4-3a2c-406e-8c45-5637099021f0
        ```

    === "Ubuntu 18.04"

        ``` yaml
        5a081b54-8992-4ff7-8a21-74e425062507
        ```

    === "Custom"
        ``` html
        <!-- Find your deployment_id at this URL  -->
        https://<cloudbroker-endpoint>/deployments/<deployment-id>
        ```

`instance_type_id`

:   **Required**– The CloudBroker instance type defines the CPU and RAM
that will be available on the infrastructure. Indicative IDs are given
below. The minimum requirements are a 2 vCPU/2GB RAM

    === "2 vCPU | 4GB RAM"

        ``` yaml
        ca727925-a5ca-4697-b2c3-8788d82457d5
        ```

    === "4 vCPU | 8GB RAM"

        ``` yaml
        ffb42759-fb52-4401-9c75-889ea0ed9602
        ```

    === "8 vCPU | 16GB RAM"

        ``` yaml
        664330f3-42b1-4f52-a675-fd182a21ef51
        ```

    === "Custom"
        ``` html
        <!-- Find your instance_type_id at this URL  -->
        https://<cloudbroker-endpoint>/instance_types/<instance-type-id>
        ```

`key_pair_id`

:   **Optional**– The CloudBroker ID for an SSH key pair, for remote
access to the infrastructure. A key pair must be created on the platform.

    === "Custom"
        ``` html
        <!-- Find your key_pair_id at this URL  -->
        https://<cloudbroker-endpoint>/key_pairs/<key-pair-id>
        ```

`opened_port`

:   **Optional**– A comma-separated string listing port numbers,
which will be opened on the instance (both TCP and UDP protocols
will be affected). **Note 51820 must be included in this list
to ensure containers can communicate across nodes**

    === "Custom"
        ``` yaml     
        51820,22,80,443
        ```

`endpoint`

:   **Required**– The endpoint of the CloudBroker platform that will
handle the deployment of the above infrastructure.

    === "DIGITbrain"
        ``` yaml     
        https://cloudsme-cbp.scaletools.com.ua
        ```

`domain_name`{ #domain_name }

:   **Optional**- Subdomain (on cbp-routing.ch) to create and attach to this instance using dynamic DNS. For the given example, the domain `my-subdomain.cbp-routing.ch` will be assigned to the instance. **Only letters, numbers and hyphens are allowed**.
   
    === "DIGITbrain"
        ``` yaml     
        my-subdomain
        ```

`cloud_config`

:   **Required**– [cloud-init](https://cloudinit.readthedocs.io/) config
for contextualisation of the provisioned virtual machine. This fields expects JSON.

    === "DIGITbrain"
        ``` json     
        {"runcmd": ["echo 'task one'", "echo 'task two'"]}
        ```

## Edge

`endpoint`

:   **Required**– The endpoint of the bring-your-own Edge device that
provides this Deployment.

    === "Your Edge Device"
        ``` yaml     
        https://192.168.1.1
        ```
        
`ssh_username`{ #ssh_username }
:   **Optional**- username for SSH connection. Defaults to ubuntu

    === "DIGITbrain"
        ``` yaml     
        ubuntu
        ```

`ssh_private_key`{ #ssh_private_key }
:   **Optional**- private key for SSH connection.

    === "Example"
        ``` yaml     
        "-----BEGIN RSA PRIVATE KEY----- MIIEowIBAAKCAQEApwn..."
        ```
