# Model & Data Parameters

This section primarily concerns publishers of [Microservices](/attributes/microservice) on the
platform, and provides further info on how to refer to Model and Data in a Microservice configuration.

You may be familiar with the Docker-Compose [approach to variable substitution](https://docs.docker.com/compose/environment-variables/set-environment-variables/#substitute-with-an-env-file)
from a `.env` file. We support the same `${   }` braced syntax as Docker-Compose, but instead
of the `.env` file, the available environment variables are defined by Model, Data, and
[Open Parameters](params.md).

This section focuses on variables related to Model and Data that a Microservice developer
can refer to in their Docker-Compose [deployment data](/attributes/microservice/#deployment-data).

## Model Parameters

Only a single instance of a Model can be bound in a Process. You can refer to the URI of a Model
in your Docker-Compose with `${MODEL.repository_uri}`. See below for further examples.

## Data Parameters

Since multiple instances of Data can be bound in a Process, the approach adds an additional step.

First, define one or more [Data Resources](/attributes/microservice/#data-resource). The `ID` of the Data
Resource is important, so keep it in mind. Later, a publisher of a Process that uses your Microservice
will match each Data Resource you define with a concrete Data asset, so be sure to provide sufficient detail
when defining your Data Resource.

You can refer to the URI of a Data Resource with `${DATA_ID.uri}`.

!!! example
    You refer to a given Data Resource in your Docker-Compose by using its `ID`.
    For example, refer to the URI of a Data Resource with `ID` **SINK_A** using `${SINK_A.uri}`.
    See below for further examples.

## Examples with URI Fields

The `repository_uri`, `uri`, `path`, and `filename` are some special fields available on
both Model and Data assets. This section describes how to use them as parameters, for
example in [deploymentData](/attributes/microservice/#deployment-data).

!!! tip
    You can refer to [user-defined fields on Data assets](/attributes/data/#aux-info)
    with the same `${ }` notation used below.

### URI

You can use the `repository_uri` and `uri` fields of Model and Data, respectively,
to define a complete URI.

=== "Model"

    ``` yaml     
    version: '3.7'
    services:
    ristra:
        image: dbs-container-repo.emgora.eu/db-ristra-cli-cpu:1.0.0
        entrypoint: /bin/sh -c
        command: wget ${MODEL.repository_uri}
    ```

=== "Data"

    ``` yaml     
    version: '3.7'
    services:
    ristra:
        image: dbs-container-repo.emgora.eu/db-ristra-cli-cpu:1.0.0
        entrypoint: /bin/sh -c
        command: wget ${SINK_A.uri}
    ```
### Path and Filename

Models support the `path` and `filename` fields for more granularity.

=== "Model"

    ``` yaml     
    version: '3.7'
    services:
    ristra:
        image: dbs-container-repo.emgora.eu/db-ristra-cli-cpu:1.0.0
        entrypoint: /bin/sh -c
        command: wget ${MODEL.path}/${MODEL.filename}
    ```


### Additional Fields

For even finer grain use cases with Model and Data, several automatic fields are
generated from the `uri_repository` and `uri` fields, respectively.

!!! example
    See the table below for fields generated for a `uri` or `repository_uri` of:<br>
    <big>**https://user:pass@example.com:1234/path/to/service?key=value#something**</big> 

    | Value             ||             Newly Generated Fields            || Value           |
    | ----------------- |:---------------------:| |:---------------------:| ---------------:|
    | https             | <big>`SCHEME`</big>   | | <big>`PORT`</big>     | 1234            |
    | user              | <big>`USERNAME`</big> | | <big>`PATH`</big>     | path/to/service |
    | pass              | <big>`PASSWORD`</big> | | <big>`QUERY`</big>    | key=value       |
    | example.com       | <big>`HOST`</big>     | | <big>`FRAGMENT`</big> | something       |

=== "Model"

    ``` yaml     
    version: '3.7'
    services:
    ristra:
        image: dbs-container-repo.emgora.eu/db-ristra-cli-cpu:1.0.0
        entrypoint: /bin/sh -c
        command: python3 start.py --path $URL --user ${MODEL.USERNAME} --pass ${MODEL.PASSWORD}
        environment:
            URL: ${MODEL.SCHEME}//${MODEL.HOST}:${MODEL.PORT}
    ```

=== "Data"

    ``` yaml     
    version: '3.7'
    services:
    ristra:
        image: dbs-container-repo.emgora.eu/db-ristra-cli-cpu:1.0.0
        entrypoint: /bin/sh -c
        command: python3 start.py --path $URL --user ${SINK.USERNAME} --pass ${SINK.PASSWORD}
        environment:
            URL: ${SINK_A.SCHEME}//${SINK_A.HOST}:${SINK_A.PORT}
    ```

!!! note
    If a same-named field is defined manually by a user, it will not be overwritten.<br>
    If a field cannot be determined from the `uri`, it will be blank.
