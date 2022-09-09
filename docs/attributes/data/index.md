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
        "1.0.0"
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
        ["sensor", "celsius", "press machine"]
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
        "SOURCE"
        ```

`FORMAT`{ #format }
:   **Optional**-*List[String]*- Format/encoding of the data produced or consumed by the data resource as a MIME type (IETF RFC 6838 https://www.sitepoint.com/mime-types-complete-list/). More than one can appear here (remote directory with several files).
    === "Example"
        ``` yaml     
        ["application/json"] 
        ```

`TYPE`{ #type }
:   **Optional**-*string*- The exact type of the data resource. Typically (but not always) corresponds to the scheme part (scheme://) of URI. E.g.: mysql, mqtt.
    === "Example"
        ``` yaml     
        "MQTT"
        ```


### Data access specification


`URI`{ #uri }
:   **Optional**-*List[URI]*- Accessibility of the data resource in form of: scheme://host:port/path (passed as pseudo environment variables: SCHEME, HOST, PORT, PATH, QUERY, FRAGMENT). A list of URIs can be passed to support multiple data sources (e.g. more than one message topics, databases).
    === "Example"
        ``` yaml     
        ["kafka://host/topic#1"]
        ```

`AUTH_TYPE`{ #auth_type }
:   **Optional**-*List[Enumeration ["none", "username_password", "accesskey_secretkey", "tls_client_certificate", "access_token", "rclone_config"]]*- One or more authentication types that can be accepted by the storage resource.
    === "Example"
        ``` yaml     
        ["tls_client_certificate"]
        ```


### Open parameters


`CREDENTIALS`{ #credentials }
:   **Optional**-*OPEN*- DO NOT ENTER ANY CREDENTIALS HERE! This is just a placeholder, an OPEN parameter for credentials (e.g. username-password, token, config file, certificate). 
    === "Example"
        ``` yaml     
        -
        ```


### Further access clauses (extensible)


`AUX_INFO`{ #aux_info }
:   **Optional**-*Map[String, String]*- List of key-value pais (JSON object/YAML dictionary) for additional specification of the data resource. New keys can be added on demand, a list of known keys is available.
    === "Example"
        ``` yaml     
        {"PROTOCOL": "tcp", "MQTT_PROTOCOL_VERSION": "3.1.1", "KAFKA_BROKER_VERSION": "2.7.0"}
        ```


### Data content semantics


`SCHEMA_DESC`{ #schema_desc }
:   **Optional**-*string*- Describes message internal structures, content semantics, ontology in a human readable way. 
    === "Example"
        ``` yaml     
        "Messages constain raw sensor values as floats in Celsius, each is a JSON object with key name 'temperature'."
        ```

`SCHEMA_URL`{ #schema_url }
:   **Optional**-*URL*- URL to schema specification (e.g. rdf, owl, xsd, json-ld)
    === "Example"
        ``` yaml     
        "https://schemas.org/data.rdf"
        ```
