---
hide:
  - toc
---

# Open Parameters

This section primarily concerns publishers of [Microservices](/attributes/microservice) on the
platform, and provides further info on how to refer to open parameters in a Microservice configuration.

When some input to your Microservice is sensitive, or if
there is some customisation that can be applied as the Process
is started, DIGITbrain supports *open parameters*.

Define these
as a Microservice's [Parameters](/attributes/microservice/#parameters)
and the Digital Agora will generate a web form when a Process starts,
requesting that the user provide a value for each parameter of each
Microservice bound to the Process. 

!!! tip
    When defining open parameters, keep the `name` of the parameter in mind, to refer to it later

You may be familiar with the Docker-Compose [approach to variable substitution](https://docs.docker.com/compose/environment-variables/set-environment-variables/#substitute-with-an-env-file)
from a `.env` file. We support the same `${   }` braced syntax as Docker-Compose, but instead
of the `.env` file, the available environment variables are defined by [Model & Data](model_data.md), and
Open Parameters.

For open parameters, use the `${PARAMETER_NAME}` syntax to refer to them,
for example in a Microservice's Docker-Compose.

=== "Defining Parameters"

    ``` yaml     
    parameters:
    - name: MINIO_URL
      type: String
      mandatory: true
      defaultValue: https://minio.example.com
      description: MinIO url
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
        entrypoint: python -m connect ${MINIO_URL} --user $MINIOUSER --pass $MINIOPASS
        environment:
          MINIOUSER: ${MINIO_ROOT_USER}
          MINIOPASS: ${MINIO_ROOT_PASS}
    ```
