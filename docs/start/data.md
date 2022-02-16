# Data in DIGITbrain

## Introduction

*Data sources* are individual entities or assets in DIGITbrain that serve data for computations made by Algorithms 
whose results are persisted in the same or another **Data resource** called a *Data sink*.

When composing **DMA Tuples**, the *DMA Composer* chooses one or more **Data** resources, specifying exactly where the **Algorithm** should consume the data from and
where to store its outputs. Such decoupling makes possible that the same Data resource can potentially be processed by different Algorithms (different analytics on  same IPI data) or the same Algorithm can be applied on a different Data resource (same analytics but on different IPI data).
Note that **Model** that is though another parameter of DMA tuples are not considered as "Data resource" in this context.

Data resources can either provide data (*source*), store data (*sink*) or enable both (*bidirectional*), each is of a **kind**:
**file** store, **database**, or a **stream** of data - regardless of the particular implementations: Amazonon S3, Oracle MySQL, Mosquitto MQTT Broker, Apache Kafka, etc., and the corresponding **type**: s3, mysql, mqtt, kafka, etc. 

From *location* point of view, Data resources can be:

- on premise (or hosted in some private/public cloud external to compute cloud of Algorithm)
- cloud-hosted (hosted in the same compute cloud but managed independently of the Algorithm)

To enable particular access to data for Algorithms each Data resource has an **URI** (Uniform Resource Identifier) associated of the form:

- ``protocol://host:port/path``

which specifies the protocol, host and port information, and additional details in the *path* part (database name, path of the file, topic name) for connection.
For example, URI ``s3://aws.amazon.com/mybucket/myfile.dat`` specifies a Data resource providing a single file 'myfile.dat' available over S3 protocol at host aws.amazon.com in bucket 'mybucket'.


## Pre-requisites

On-premises Data resources must be accessible for Algorithms running in a cloud, thus they must:

- be accessible over the public internet
- have public IP address or domain name
- corresponding ports open for the domain towards the compute cloud of the Algorithms


## Metadata describing Data

For a closer look at this metadata, use the following resources:

- [Attribute Listing](/attributes/data) for an itemised listing of fields
- [Metadata Table](/tables/data) for a table-formatted overview
- Feel free to extend this list as desired

## Further reading...

This space is for any other required documentation on this asset.
