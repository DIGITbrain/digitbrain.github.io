# Open Parameters

When some input to your application is sensitive, or if
there is some customisation that can be applied as the Process
is started, DIGITbrain supports *open parameters*. Define these
as a Microservice's [Parameters](/attributes/microservice/#parameters)
and the Digital Agora will generate a web form when a Process starts,
requesting that the user provides a value for each parameter of each
Microservice bound to it. Keep the `name` of your parameter in mind, to
refer to later.

Use the `open_parameter(PARAMETER_NAME)` syntax to refer to these parameters,
for example in a Microservice's [deploymentData](/attributes/microservice/#deployment-data). 

=== "Defining Parameters"

    ``` yaml     
    parameters:
    - name: MINIO_ROOT_USER
      type: String
      mandatory: true
      defaultValue: admin
      description: MinIO username
    - name: MINIO_ROOT_PASS
      type: String
      mandatory: true
      description: MinIO password
    ```

=== "Referencing Parameters"

    ``` yaml     
    version: '3.7'
    services:
    ristra:
        image: dbs-container-repo.emgora.eu/db-ristra-cli-cpu:1.0.0
        entrypoint: /bin/sh -c
        environment:
        MINIO_ROOT_USER: open_parameter(MINIO_ROOT_USER)
        MINIO_ROOT_PASS: open_parameter(MINIO_ROOT_PASS)
    ```

**This feature is in beta. Please contact your support**
**person if you require further support with it**