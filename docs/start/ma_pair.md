# Behaviours in DIGITbrain

## Introduction

Behaviours (Model-Algorithm Pairs) are each composed of one Model and one Algorithms to describe a certain behaviour of an IP Family. An Behaviour corresponds to one behaviour of the respective IP Family – it can serve more than one purpose.

This asset includes the references to already published Model (“M Asset”) and Algorithm (“A Asset”) within the Db Asset Metadata Registry. The configurable information related to the “Rules” (to determine when to trigger an action), “Frequency” (to determine how often an evaluation should be triggered), and “Payload” (to include any additional information that has not been homogenised nor standardised).

The processes of publishing a Behaviour relies on previously published and reused Db Assets (e.g. Microservices, Algorithms, Models, IP Families) as illustrated in the following figure.

![MA_Pair_Composition](https://user-images.githubusercontent.com/24694029/152166908-bbda6a71-b3c5-42d3-91f1-29045b88f352.png)

## Pre-requisites

The IP Family (i.e. Industrial-Product Family), the Model Asset, and the Algorithm Asset to be referenced by the MA Pair would need to be published beforehand, in order to facilitate the creation and publishing of the Behaviour.

## Describing Behaviours

For a closer look at the fields available for Behaviours, use the following resources:

- [Behaviours in Detail](/attributes/ma_pair) for an itemised listing of fields
- [Behaviours Overview](/tables/ma_pair) for a table-formatted overview

## Further reading...

The following figure shows how the elements that constitute a DMA Tuple (i.e. Microservices, Algorithms, Models, Behaviours, Data) of a Digital Twin in the DIGITbrain Solution are hierarchically structured; a higher hierarchy indicates more specialisation and more relation to the manufacturing process where the Digital Twin is used. The following figure also illustrates how the collective intelligence within the DIGITbrain Solution is exploited. On the one side, a software developer might have no notion of a given manufacturing process where the developed Microservice could be used; nevertheless, by leveraging the know-how of additional experts, DMA Tuples can be configured for Digital Twins with the developed Microservice, unlocking its full benefits. On the other side, a production manager might have no deep understanding of a given microservice; however, the involvement of other experts facilitates its utilisation within the context of a DMA Tuple without the need for a dedicated training or detailed know-how about the Microservice itself.

![DIGITbrain_Hierarchy](https://user-images.githubusercontent.com/24694029/152166232-716d7175-9011-4485-8708-fe1153dd4f70.png)

This hierarchical abstraction largely contributes to one of the main technical objectives of the DIGITbrain Solution and the Digital Product Brain: to democratise the adoption of Digital Twins in the manufacturing industry (especially for SMEs). To this end, the Digital Product Brain is built upon core principles such as:
- reusability: lower Db Assets are individually reused in higher Db Assets and the DMA Tuple as many times as appropriate;
-	versatility: Db Assets are published with customised metadata, covering more use cases and scenarios;
-	sovereignty: Db Assets only store references to the actual assets (governed by the owners) and DMA Tuples are stored in dedicated storage (governed by the IPI owner);
-	modularity: DMA Tuples are composed by interchangeable Db Assets, which are selected depending on the targeted properties (e.g. price, performance, accuracy);
-	simplicity: every Db Asset Provider uses a dedicated web form (of the Db Publishing Interface) for publishing the Db Asset, only focusing on the essential metadata; and
-	homogeneity: Db Assets and DMA Tuples are interfaced in the same manner regardless of their nature but without limiting their individual capabilities.

The following figure generally illustrates the process flow involved in the development and publishing of a Db Asset, as well as the composition, the deployment, and the evaluation of a DMA Tuple. The following figure also highlights that a Behaviour is developed and published by a domain expert with the propser knowledge to describe the behavior presented by the Behaviour.

![MAPair_process_flow](https://user-images.githubusercontent.com/24694029/152169262-79c90119-0baf-4637-9767-ab8823a409d3.png)
