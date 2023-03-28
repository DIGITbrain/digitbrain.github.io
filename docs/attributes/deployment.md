<style>
  .md-content__button {
    display: none;
  }
</style>
# Deployment Fields




The specification for Deployment
has these fields:


`type`{ #type }

:   **Required**-*Enumeration ["cloudbroker", "edge"]*<br>
    DIGITbrain supports cloud infrastructure deployed via the
    CloudBroker platform, or bring-your-own Linux-based Edge devices. This should
    be specified in this field. The other metadata in this section should be
    completed according to the type (e.g. CloudBroker-specific metadata is not required
    if `type: edge`)



    === "Example"
        ``` yaml     
        cloudbroker
        ```

### Cloudbroker

`deployment_id`{ #deployment-id }

:   **Required**-*string (UUID)*<br>
    A CloudBroker deployment ties together software,
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
        ``` yaml     
        # Find a deployment_id by inspecting the URL
        https://<cloudbroker-endpoint>/deployments/<deployment-id>

        ```



`instance_type_id`{ #instance-type-id }

:   **Required**-*string (UUID)*<br>
    The CloudBroker instance type defines the CPU and RAM
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
        ``` yaml     
        # Find an instance_type_id by inspecting the URL
        https://<cloudbroker-endpoint>/instance_types/<instance-type-id>

        ```



`key_pair_id`{ #key-pair-id }

:   **Optional**-*string (UUID)*<br>
    ID of CloudBroker Key Pair


    === "Example"
        ``` yaml     
        # Find a key_pair_id by inspecting the URL
        https://<cloudbroker-endpoint>/key_pairs/<key-pair-id>

        ```


`opened_port`{ #opened-port }

:   **Required**-*string (comma separated integers)*<br>
    A comma-separated string listing port numbers,
    which will be opened on the instance (both TCP and UDP protocols
    will be affected). 

    **Note 51820 must be included in this list
    to ensure containers can communicate**




    === "Minimal"
        ``` yaml     
        51820
        ```


    === "SSH, HTTP, HTTPS"
        ``` yaml     
        51820,22,80,443
        ```



`cloud_config`{ #cloud-config }

:   **Optional**-*string (JSON)*<br>
    [cloud-init](https://cloudinit.readthedocs.io/) config for
    contextualisation of the provisioned virtual machine.



    === "Example"
        ``` yaml     
        {"runcmd": ["echo 'task one'", "echo 'task two'"]}

        ```


`endpoint`{ #endpoint }

:   **Required**-*string (URL)*<br>
    The endpoint of the CloudBroker platform that will
    handle the deployment of the above infrastructure.




    === "Default"
        ``` yaml     
        https://cloudsme-cbp.scaletools.com.ua
        ```



`domain_name`{ #domain-name }

:   **Optional**-*string*<br>
    Subdomain (on cbp-routing.ch) to create and attach
    to this instance using dynamic DNS. For the given
    example, the domain `my-subdomain.cbp-routing.ch`
    will be assigned to the instance. **Only letters,
    numbers and hyphens are allowed**.



    === "Example"
        ``` yaml     
        my-subdomain
        ```

### Edge

`endpoint `{ #endpoint  }

:   **Required**-*string*<br>
    The endpoint of the bring-your-own Edge device that provides this Deployment.


    === "Example"
        ``` yaml     
        192.168.1.1
        ```


`ssh_private_key`{ #ssh-private-key }

:   **Optional**-*String*<br>
    private key for SSH connection.


    === "Example"
        ``` yaml     
        -----BEGIN RSA PRIVATE KEY-----
        MIIBOgIBAAJBAKj34GkxFhD90vcNLYLInFEX6Ppy1tPf9Cnzj4p4WGeKLs1Pt8Qu
        KUpRKfFLfRYC9AIKjbJTWit+CqvjWYzvQwECAwEAAQJAIJLixBy2qpFoS4DSmoEm
        ...

        ```


`ssh_username`{ #ssh-username }

:   **Optional**-*String*<br>
    username for SSH connection. Defaults to ubuntu


    === "Example"
        ``` yaml     
        ubuntu
        ```

