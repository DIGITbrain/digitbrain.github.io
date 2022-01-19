# Data in DIGITbrain

## Introduction

*Data sources* are individual entities in DIGITbrain that serve data for computations done by Algorithms. 
Also, often the results need to be persisted, which might be the same or another **Data resource**, a *Data sink*.

When composing DMA Tuples, the developer chooses one or more **D**ata resources, specifying exactly from where the **A**lgorithm is to consume the data and
where to store the outputs. In such decoupling, the same Data asset can so potentially be processed by different Algorithms of preference (different analytics on the same IPI data) or the same Algorithm can be fed by different Data resources (same analytics but on different IPI data).
Note that **M**odels, which is though another parameter or "input" of DMA tuples are not considered as "Data" in this context.

Data resources can thus either provide data (SOURCE), store data (SINK) or enable both (BIDIRECTIONAL), and each is of a *kind*:
file store, database, or a streaming data resource, regardless of the particular implementations: Amazonon S3, FTP, MySQL, MongoDB, Mosquitto MQTT broker, Apache Kafka, etc. 

From *location* point of view, Data resources can be:

- on premise (or hosted in some private/public cloud external to compute cloud of Algorithm)
- cloud-hosted (hosted in the same compute cloud but managed independently of the Algorithm)


## Pre-requisites

Information on any requirements imposed on this asset.

## Metadata describing Data

For a closer look at this metadata, use the following resources:

- [Attribute Listing](attributes/data.md) for an itemised listing of fields
- [Metadata Table](tables/data.md) for a table-formatted overview
- Feel free to extend this list as desired

## Further reading...

This space is for any other required documentation on this asset.
