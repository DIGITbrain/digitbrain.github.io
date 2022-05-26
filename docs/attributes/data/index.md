<style>
  .md-content__button {
    display: none;
  }
</style>
# Data Fields

**This information is also available in [table format](/tables/data/)**


## Available Fields 

The metadata specification for a DIGITbrain Data
has these sections:

- [Administrative Data](#administrative-data)
- [Description](#description)
- [Search support](#search-support)
- [Datakind specification](#datakind-specification)
- [Data access specification](#data-access-specification)
- [Open parameters](#open-parameters)
- [Further access clauses (extensible)](#further-access-clauses-extensible)
- [Data content semantics](#data-content-semantics)


### Administrative Data


`ID`{ #id }
:   **Auto-generated**-*ID*- Unique identifier of the asset.

    === "Example"
        ``` yaml     
        "DATAID_MYDATA_A"
        ```

`AUTHOR`{ #author }
:   **Auto-generated**-*ID*- Unique identifier of the user who created this record

    === "Example"
        ``` yaml     
        UUID
        ```

`PROVIDER`{ #provider }
:   **Auto-generated**-*ID*- Legal entity who provides the asset (owner). It is the affiliation of the author by default.

    === "Example"
        ``` yaml     
        UUID
        ```

`BUILD`{ #build }
:   **Auto-generated**-*Integer*- Build number, incremented automatically to provide versioning for the asset

    === "Example"
        ``` yaml     
        21
        ```

`DATE`{ #date }
:   **Auto-generated**-*DATE (ISO 8601)*- Date of asset registration.

    === "Example"
        ``` yaml     
        2022-04-28T08:11:53+00:00
        ```


### Description


`NAME`{ #name }
:   **Required**-*string*- Name of the data resource.

    === "Example"
        ``` yaml     
        "CNSPiezoBolt#1 (in directory: factory 1 , machine1 , piezobolts)"
        ```

`VERSION`{ #version }
:   **Optional**-*string*- Version of the data resource (not of the metadata), defined by the provider in the format of his/her choice (typically: major.minor.patch)
    === "Example"
        ``` yaml     
        "2.3.4"
        ```

`DESC`{ #desc }
:   **Optional**-*string*- Human readable description of the data resource characteristics, contents.
    === "Example"
        ``` yaml     
        "This sensor measures temperature in Celsius, sends data via ConSenses edge device via an MQTT broker"
        ```

`DESC_URL`{ #desc_url }
:   **Optional**-*URL*- More detailed specification of data source characteristics (doc, pdf, …)
    === "Example"
        ``` yaml     
        "https://some-host/docs/data-source-specification-sheet.pdf"
        ```

`SIZE`{ #size }
:   **Optional**-*integer*- Estimated/exact size of data (e.g. file size, volume size, or message size); might be used to assess HW requirements (RAM, CPU). In bytes.
    === "Example"
        ``` yaml     
        112
        ```


### Search support


`TAGS`{ #tags }
:   **Optional**-*List[String]*- A list of tags freely added to help in searching/indexing (not limited to a basic set of tags, keywords)
    === "Example"
        ``` yaml     
        ["camera", "rgb", "w640", "h480", "jpg"]
        ```


### Datakind specification


`KIND`{ #kind }
:   **Required**-*Enumeration ["FILE", "DATABASE", "STREAM"]*- Main category of the data resource (e.g. file/object storage, database management system, streaming broker). FILE can mean a single file or a folder.

    === "Example"
        ``` yaml     
        "STREAM"
        ```

`DIRECTION`{ #direction }
:   **Required**-*Enumeration ["SOURCE", "SINK", "BIDIRECTIONAL"]*- Direction of data flow (source: data provider, sink: data consumer/storage)

    === "Example"
        ``` yaml     
        "SINK"
        ```

`FORMAT`{ #format }
:   **Optional**-*List[String]*- Format/encoding of the data produced or consumed by the data resource as a MIME type (IETF RFC 6838 https://www.sitepoint.com/mime-types-complete-list/). More than one can appear here (remote directory with several files).
    === "Example"
        ``` yaml     
        ["application/json", "text/plain", "application/octet-stream", "application/zip"] 
        ```

`TYPE`{ #type }
:   **Optional**-*string*- The exact type of the data resource. Typically (but not always) corresponds to the scheme part (scheme://) of URI. E.g.: mysql, mqtt.
    === "Example"
        ``` yaml     
        "S3"
        ```


### Data access specification


`URI`{ #uri }
:   **Optional**-*URI*- Accessibility of the data resource, including host, port information, protocol, and other fields (path is protocol dependent, can be a topic name). GUI may show host, port, path separately. Hidden at search. Format: scheme://host:port/path.  Pseudo vars: SCHEME, HOST, PORT, PATH, QUERY, FRAGMENT.
    === "Example"
        ``` yaml     
        "kafka://host/topic#1"
        ```

`AUTH_TYPE`{ #auth_type }
:   **Optional**-*List[Enumeration ["none", "userpass", "accesskey_secretkey", "ssl_certificate", "tls_mutual", "access_token", "rclone_config"]]*- One or more authentication types that can be accepted by the storage resource.
    === "Example"
        ``` yaml     
        ["ssl_certificate", "access_token"]
        ```


### Open parameters


`CREDENTIALS`{ #credentials }
:   **Optional**-*OPEN*- Credentials (e.g. string/json, zip, config file). Its content (structure) depends on authentication type (e.g. token, username and password). OPEN means must not be filled here, but asked from user on startup.


### Further access clauses (extensible)


`AUX_INFO`{ #aux_info }
:   **Optional**-*Map[String, String]*- List of key-value pais (JSON object/YAML dictionary) for additional specification of the data resource. New keys can be added on demand, a list of known keys is available.
    === "Example"
        ``` yaml     
        {"PROTOCOL": "http", "MYSQL_DIALECT": "mariadbdialect", "MQTT_PROTOCOL_VERSION": "3.1.1", "KAFKA_BROKER_VERSION": "2.7.0", "S3_REGION": "eu-central-1"}
        ```


### Data content semantics


`SCHEMA`{ #schema }
:   **Optional**-*string*- Describes message internal structure, semantics, ontology. It can be any file (doc, rdf, owl, etc.). Asset Administration Shell, IEC 61360 - Common Data Dictionary, ...
    === "Example"
        ``` yaml     
        Database schema description/contents. 
        ```

`SCHEMA_URL`{ #schema_url }
:   **Optional**-*URL*- URL to schema specification document (in some format, rdf, owl, xsd, …)
    === "Example"
        ``` yaml     
        "https://schemas.org/date.rdf"
        ```
