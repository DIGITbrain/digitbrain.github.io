<style>
  .md-content__button {
    display: none;
  }
</style>
# Data Resources Fields

**This information is also available in [table format](/tables/data_resources/)**


## Available Fields 

The metadata specification for a DIGITbrain Data Resources
has these sections:

- [Data Resources](#data-resources)


### Data Resources


`DATA_RESOURCE_ID`{ #data_resource_id }
:   **Required**-*String*- human-readable identifier, unique within a Microservice

    === "Example"
        ``` yaml     
        file1
        ```

`DATA_KIND`{ #data_kind }
:   **Required**-*List( DATA_KIND)*- supported types of the data resource (e.g. file/object storage, database management system, streaming broker). FILE can mean a single file or a folder.

    === "Example"
        ``` yaml     
        {FILE, STREAM}
        ```

`DATA_DIRECTION`{ #data_direction }
:   **Required**-*List( DATA_DIRECTION)*- supported direction of data flow (source: data provider, sink: data consumer/storage)

    === "Example"
        ``` yaml     
        {SOURCE, SINK, BIDIRECTIONAL}
        ```

`DATA_FORMAT`{ #data_format }
:   **Optional**-*List( DATA_FORMAT)*- supported format/encoding of the data produced or consumed by the data resource as a MIME type (IETF RFC 6838 https://www.sitepoint.com/mime-types-complete-list/). More than one can appear here (remote directory with several files).
    === "Example"
        ``` yaml     
        {application/zip, image/jpg}
        ```

`DATA_SOURCE_TYPE`{ #data_source_type }
:   **Optional**-*List( DATA_SOURCE_TYPE)*- supported exact type of the data resource. Typically corresponds to the scheme part (protocol://) of DATA_URI
    === "Example"
        ``` yaml     
        {MYSQL, KAFKA}
        ```

`DATA_PROTOCOL`{ #data_protocol }
:   **Optional**-*List( DATA_PROTOCOL)*- supported protocols
    === "Example"
        ``` yaml     
        {HTTP}
        ```

`DATA_AUTH_TYPE`{ #data_auth_type }
:   **Optional**-*List( DATA_AUTH_TYPE)*- supported authentication type
    === "Example"
        ``` yaml     
        {tls_mutual, userpass}
        ```

`DATA_MYSQL_DIALECT`{ #data_mysql_dialect }
:   **Optional**-*List( DATA_MYSQL_DIALECT)*- supported MYSQL dialect
    === "Example"
        ``` yaml     
        {mariadbdialect}
        ```

`DATA_MQTT_PROTOCOL_VERSION`{ #data_mqtt_protocol_version }
:   **Optional**-*List( DATA_MQTT_PROTOCOL_VERSION)*- supported MQTT protocol version
    === "Example"
        ``` yaml     
        {2.3.1}
        ```

`DATA_KAFKA_BROKER_VERSION`{ #data_kafka_broker_version }
:   **Optional**-*List( DATA_KAFKA_BROKER_VERSION)*- supported Kafka broker version
    === "Example"
        ``` yaml     
        {2.7.1, 2.5}
        ```

`DATA_S3_REGION`{ #data_s3_region }
:   **Optional**-*List( DATA_S3_REGION)*- supported S3 region
    === "Example"
        ``` yaml     
        {eu-central-1}
        ```

`DATA_SCHEMA`{ #data_schema }
:   **Optional**-*List( DATA_SCHEMA)*- supported internal message structure, semantics, ontology. It can be any file (doc, rdf, owl, etc.). Asset Administration Shell, IEC 61360 - Common Data Dictionary, …
    === "Example"
        ``` yaml     
        {jpg}
        ```
