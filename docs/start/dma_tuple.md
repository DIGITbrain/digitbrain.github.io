# Data-Model-Algorithm Tuples in DIGITbrain

## Introduction

A DMA Tuple (i.e. Data-Model-Algorithm Tuple) is built by connecting one behaviour of an IP Instance represented by an MA Pair of the corresponding IP Family with Data resources (zero or more) associated to the same IP Instance as illustrated in the following figure. Multiple active DMA Tuples associated to a given IP Instance represent a valid Digital Twin for a specific point in time. DMA Tuples associated to a Digital Twin can be activated or deactivated according to the needs of the IP Instance, facilitating the flexible reconfiguration of Digital Twins without the needs for creating dedicated Digital Twins. Such a flexible reconfiguration allows for the on-demand customisation of Digital Twins and IP Instances to adapt to changing conditions within the production site.

![DMA_Tuple_Composition](https://user-images.githubusercontent.com/24694029/152173510-67dc3a86-645e-4da9-85a0-3148f2bf74eb.png)

## Pre-requisites

The IP Instance (i.e. Industrial-Product Instance), the MA Pair (i.e. Model-Algorithm Pair), and the Data Asset to be referenced by the DMA Tuple would need to be published beforehand, in order to facilitate the creation and publishing of the DMA Tuple.

## Metadata describing DMA Tuples

For a closer look at this metadata, use the following resources:

- [Attribute Listing](/attributes/dma_tuple) for an itemised listing of fields
- [Metadata Table](/tables/dma_tuple) for a table-formatted overview
- Feel free to extend this list as desired

## Further reading...

The following figure shows how the elements that constitute a DMA Tuple (i.e. Microservices, Algorithms, Models, MA Pairs, Data) of a Digital Twin in the DIGITbrain Solution are hierarchically structured; a higher hierarchy indicates more specialisation and more relation to the manufacturing process where the Digital Twin is used. The following figure also illustrates how the collective intelligence within the DIGITbrain Solution is exploited. On the one side, a software developer might have no notion of a given manufacturing process where the developed Microservice could be used; nevertheless, by leveraging the know-how of additional experts, DMA Tuples can be configured for Digital Twins with the developed Microservice, unlocking its full benefits. On the other side, a production manager might have no deep understanding of a given microservice; however, the involvement of other experts facilitates its utilisation within the context of a DMA Tuple without the need for a dedicated training or detailed know-how about the Microservice itself.

![DIGITbrain_Hierarchy](https://user-images.githubusercontent.com/24694029/152174486-97fbccc9-e578-46cb-820a-afe7c3d41478.png)

This hierarchical abstraction largely contributes to one of the main technical objectives of the DIGITbrain Solution and the Digital Product Brain: to democratise the adoption of Digital Twins in the manufacturing industry (especially for SMEs). To this end, the Digital Product Brain is built upon core principles such as:
- reusability: lower Db Assets are individually reused in higher Db Assets and the DMA Tuple as many times as appropriate;
-	versatility: Db Assets are published with customised metadata, covering more use cases and scenarios;
-	sovereignty: Db Assets only store references to the actual assets (governed by the owners) and DMA Tuples are stored in dedicated storage (governed by the IPI owner);
-	modularity: DMA Tuples are composed by interchangeable Db Assets, which are selected depending on the targeted properties (e.g. price, performance, accuracy);
-	simplicity: every Db Asset Provider uses a dedicated web form (of the Db Publishing Interface) for publishing the Db Asset, only focusing on the essential metadata; and
-	homogeneity: Db Assets and DMA Tuples are interfaced in the same manner regardless of their nature but without limiting their individual capabilities.

The following figure generally illustrates the process flow involved in the development and publishing of a Db Asset, as well as the composition, the deployment, and the evaluation of a DMA Tuple. The following figure also highlights that a DMA Tuple is composed, deployed, and evaluated by a manufacturing end user with the proper access to the IP Instance to be associated with the DMA Tuple.

![DMATuple_process_flow](https://user-images.githubusercontent.com/24694029/152173453-f23d4791-94fc-41ba-a8c4-6d5564640783.png)
