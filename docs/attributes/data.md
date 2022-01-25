<style>
  .md-content__button {
    display: none;
  }
</style>
# Data Metadata Fields

## Available Fields 

The metadata specification for a DIGITbrain Data
has these sections:

- [Administrative data](#administrative-data)
- [Description](#description)
- [Search support](#search-support)
- [Datakind specification](#datakind-specification)
- [Data access specification](#data-access-specification)
- [Open parameters](#open-parameters)
- [Further access clauses (extensible)](#further-access-clauses-extensible)
- [Data content semantics](#data-content-semantics)


### Administrative data


`ID`
:   **Auto-generated**-*id*- Unique identifier of the data resource.

    === "Example"
        ``` yaml     
        ID: UUID
        ```

`AUTHOR`
:   **Auto-generated**-*id*- Unique identifier of the user who created this record

    === "Example"
        ``` yaml     
        AUTHOR: UUID
        ```

`PROVIDER`
:   **Auto-generated**-*id*- Legal entity who provides the data resource (owner). It is the affiliation of the author by default.

    === "Example"
        ``` yaml     
        PROVIDER: UUID
        ```

`DATE`
:   **Auto-generated**-*timestamp*- Date of data resource registration.

    === "Example"
        ``` yaml     
        DATE: 10:45:13 CET 21/03/2021
        ```


### Description


`DATA_NAME`
:   **Required**-*string*- Name of the data resource. (The directory hierarchy in Nexus provides a fully qualified (FQ) name, which is unique.)

    === "Example"
        ``` yaml     
        DATA_NAME: CNSPiezoBolt#1 (in directory: factory 1 , machine1 , piezobolts)
        ```

`DATA_VERSION`
:   **Optional**-*string*- Version of this data resource entry (major.minor.patch). Defaults to 1.0.0
    === "Example"
        ``` yaml     
        DATA_VERSION: 2.3.4
        ```

`DATA_DESC`
:   **Optional**-*string*- Human readable description of the data resource.
    === "Example"
        ``` yaml     
        DATA_DESC: This sensor measures temperature in Celsius, sends data via ConSenses edge device via an MQTT broker
        ```

`DATA_DESC_URL`
:   **Optional**-*URL*- More detailed specification of data source characteristics (doc, pdf, …)
    === "Example"
        ``` yaml     
        DATA_DESC_URL: data-source-specification-sheet.pdf
        ```

`DATA_SIZE`
:   **Optional**-*integer*- Estimated/exact size of data (e.g. file size, volume size, or message size); might be used to assess HW requirements (RAM, CPU) . In bytes (k - kilo, m - mega, t - tera, p - peta)
    === "Example"
        ``` yaml     
        DATA_SIZE: 112m
        ```


### Search support


`DATA_TAGS`
:   **Optional**-*list of strings*- A list of tags freely added to help in searching/indexing (not limited to a basic set of tags, keywords)
    === "Example"
        ``` yaml     
        DATA_TAGS: [camera, rgb, w640, h480, jpg]
        ```


### Datakind specification


`DATA_KIND`
:   **Required**-*enum*- Type of the data resource (e.g. file/object storage, database management system, streaming broker). FILE can mean a single file or a folder.

    === "Example"
        ``` yaml     
        DATA_KIND: FILE , DATABASE , STREAM
        ```

`DATA_DIRECTION`
:   **Required**-*enum*- Direction of data flow (source: data provider, sink: data consumer/storage)

    === "Example"
        ``` yaml     
        DATA_DIRECTION: SOURCE , SINK , BIDIRECTIONAL
        ```

`DATA_FORMAT`
:   **Optional**-*list of strings*- Format/encoding of the data produced or consumed by the data resource as a MIME type (IETF RFC 6838 https://www.sitepoint.com/mime-types-complete-list/). More than one can appear here (remote directory with several files).
    === "Example"
        ``` yaml     
        DATA_FORMAT: [ { application/json , text/plain , application/octet-stream , application/zip } ] 
        ```


### Data access specification


`DATA_SOURCE_TYPE`
:   **Optional**-*string*- The exact type of the data resource. Typically corresponds to the scheme part (protocol://) of DATA_URI.
    === "Example"
        ``` yaml     
        DATA_SOURCE_TYPE: S3 , MYSQL , MQTT , ... (WP6: DATA_SOURCE_TYPE=LOCAL, PATH=...")
        ```

`DATA_URI`
:   **Optional**-*URI*- Accessibility of the data resource, including host, port information, protocol, and other fields (path is protocol dependent, can be a topic name). GUI may show host, port, path separately. Hidden at search. Format: protocol://host:port/path.  Pseudo vars: DATA_PROTOCOL, DATA_HOST, DATA_PORT, DATA_PATH, DATA_QUERY, DATA_FRAGMENT.
    === "Example"
        ``` yaml     
        DATA_URI: s3://amazonaws/bucket/object , kafka://host/topic#1 , ...
        ```

`DATA_AUTH`
:   **Optional**-*list of enums*- One or more authentication types that can be accepted by the storage resource.
    === "Example"
        ``` yaml     
        DATA_AUTH: [ { none , userpass , accesskey_secretkey , ssl_certificate , tls_mutual, access_token , rclone_config }+ ]
        ```


### Open parameters


`DATA_CREDENTIALS`
:   **Optional**-*OPEN*- Credentials (e.g. string/json, zip, config file)


### Further access clauses (extensible)


`DATA_PROTOCOL`
:   **Optional**-*string*- Protocol to use in communication with the data source, only if DATA_TYPE does not imply it (e.g. S3 over HTTP). Moved from to Data access specification.
    === "Example"
        ``` yaml     
        DATA_PROTOCOL: HTTP, HTTPS, TCP, UDP
        ```

`DATA_MYSQL_DIALECT`
:   **Optional**-*string*- Protocol dialect to be used in communication with the database
    === "Example"
        ``` yaml     
        DATA_MYSQL_DIALECT: mysqldialect , mariadbdialect
        ```

`DATA_MQTT_PROTOCOL_VERSION`
:   **Optional**-*string*- MQTT protocol version must be used
    === "Example"
        ``` yaml     
        DATA_MQTT_PROTOCOL_VERSION: 3.1.1, 5.0
        ```

`DATA_KAFKA_BROKER_VERSION`
:   **Optional**-*string*- Kafka broker version
    === "Example"
        ``` yaml     
        DATA_KAFKA_BROKER_VERSION: 2.7.0
        ```

`DATA_S3_REGION`
:   **Optional**-*string*- S3 region
    === "Example"
        ``` yaml     
        DATA_S3_REGION: eu-central-1
        ```


### Data content semantics


`DATA_SCHEMA`
:   **Optional**-*string*- Describes message internal structure, semantics, ontology. It can be any file (doc, rdf, owl, etc.). Asset Administration Shell, IEC 61360 - Common Data Dictionary, ...
    === "Example"
        ``` yaml     
        DATA_SCHEMA: database schema description/contents 
        ```

`DATA_SCHEMA_URL`
:   **Optional**-*URL*- No description available.
    === "Example"
        ``` yaml     
        DATA_SCHEMA_URL: database schema URL
        ```

`DATA_SCHEMA_ADDITIONAL_ATTRIBUTES`
:   **Optional**-*string*- Further restriction/specialization of DATA_SCHEMA, “general” schema.
