<style>
  .md-content__button {
    display: none;
  }
</style>
# Data Fields


**For a more condensed summary this information is available in [table view](/tables/data/)**



The specification for Data
has these fields:

`name`{ #name }

:   **Required**-*string*<br>
    Name of the data resource.



    === "Example"
        ``` yaml     
        "CNSPiezoBolt#1 (in directory: factory 1 , machine1 , piezobolts)"
        ```

`version`{ #version }

:   **Optional**-*string*<br>
    Version of the data resource (not of the metadata), defined by the provider in the format of his/her choice (typically: major.minor.patch)



    === "Example"
        ``` yaml     
        "1.0.0"
        ```

`description`{ #description }

:   **Optional**-*string*<br>
    Human readable description of the data resource characteristics, contents.


`description_url`{ #description-url }

:   **Optional**-*string*<br>
    More detailed specification of data source characteristics (doc, pdf, …)


`size`{ #size }

:   **Optional**-*integer*<br>
    Estimated/exact size of data (e.g. file size, volume size, or message size); might be used to assess HW requirements (RAM, CPU). In bytes.



    === "Example"
        ``` yaml     
        112
        ```

`tags`{ #tags }

:   **Optional**-*string[]*<br>
    A list of tags freely added to help in searching/indexing (not limited to a basic set of tags, keywords)



    === "Example"
        ``` yaml     
        ["sensor", "celsius", "press machine"]
        ```

`kind`{ #kind }

:   **Required**-*enum [FILE, DATABASE, STREAM]*<br>
    Main category of the data resource (e.g. file/object storage, database management system, streaming broker). FILE can mean a single file or a folder.



    === "Example"
        ``` yaml     
        "STREAM"
        ```

`direction`{ #direction }

:   **Required**-*enum [SOURCE, SINK, BIDIRECTIONAL]*<br>
    Direction of data flow (source: data provider, sink: data consumer/storage)



    === "Example"
        ``` yaml     
        "SOURCE"
        ```

`format`{ #format }

:   **Optional**-*string[]*<br>
    Format/encoding of the data produced or consumed by the data resource as a MIME type (IETF RFC 6838 https://www.sitepoint.com/mime-types-complete-list/). More than one can appear here (remote directory with several files).



    === "Example"
        ``` yaml     
        ["application/json"] 
        ```

`type`{ #type }

:   **Required**-*string*<br>
    The exact type of the data resource. Typically (but not always) corresponds to the scheme part (scheme://) of URI. E.g.: mysql, mqtt.



    === "Example"
        ``` yaml     
        "MQTT"
        ```

`uri`{ #uri }

:   **Required**-*string*<br>
    Accessibility of the data resource, including host, port information, protocol, and other fields (path is protocol dependent, can be a topic name). GUI may show host, port, path separately. Hidden at search. Format: scheme://host:port/path.  Pseudo vars: SCHEME, HOST, PORT, PATH, QUERY, FRAGMENT.



    === "Example"
        ``` yaml     
        ["kafka://host/topic#1"]
        ```

`auth_type`{ #auth-type }

:   **Required**-*string[]*<br>
    One or more authentication types that can be accepted by the storage resource.



    === "Example"
        ``` yaml     
        ["tls_client_certificate"]
        ```

`credentials`{ #credentials }

:   **Optional**-*string*<br>
    Credentials (e.g. string/json, zip, config file). Its content (structure) depends on authentication type (e.g. token, username and password). OPEN means must not be filled here, but asked from user on startup.



    === "Example"
        ``` yaml     
        -
        ```

`aux_info`{ #aux-info }

:   **Optional**-*string*<br>
    List of key-value pais (JSON object/YAML dictionary) for additional specification of the data resource. New keys can be added on demand, a list of known keys is available.



    === "Example"
        ``` yaml     
        {"PROTOCOL": "tcp", "MQTT_PROTOCOL_VERSION": "3.1.1", "KAFKA_BROKER_VERSION": "2.7.0"}
        ```

`schema`{ #schema }

:   **Optional**-*string*<br>
    Describes message internal structure, semantics, ontology. It can be any file (doc, rdf, owl, etc.). Asset Administration Shell, IEC 61360 - Common Data Dictionary, ...


`schema_url`{ #schema-url }

:   **Optional**-*string*<br>
    URL to schema specification document (in some format, rdf, owl, xsd, …)



    === "Example"
        ``` yaml     
        "https://schemas.org/data.rdf"
        ```

