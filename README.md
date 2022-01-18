# Metadata in DIGITbrain
Metadata is used to describe all assets in DIGITbrain.This repository stores the DIGITbrain
Metadata Specification ([metadata.xlsx](https://github.com/DIGITbrain/metadata/blob/main/metadata.xlsx)).
Whenever this metadata specification is updated in this repository, respective *.csv* files will be generated
for each of the assets, to provide some attempt at tracking version control over time.
These files are linked below.

## [Microservice]
A Microservice is the basic application unit in DIGITbrain.
Microservices can be composed to create an Algorithm.

## [Algorithm]
An algorithm is a collection of Microservices working together to realise some functionality.
It can be paired with a Model to create an MA Pair.

## [Model]
The model required by the Algorithm.

## [Data]
Data being collected (usually from the shop floor) to be used by the Algorithm.
Data will be added to an MA Pair to create a DMA Tuple.

## [MA Pair]
The pairing of Model with Algorithm.

## [DMA Tuple]
The pairing of an MA Pair with Data. The deployable unit in DIGITbrain

## [Supporting Metadata]
Additional metadata not related to any one asset.


[Algorithm]: https://github.com/DIGITbrain/metadata/blob/main/docs/tables/algorithm.md
[Microservice]: https://github.com/DIGITbrain/metadata/blob/main/docs/tables/microservice.md
[Data]: https://github.com/DIGITbrain/metadata/blob/main/docs/tables/data.md
[Model]: https://github.com/DIGITbrain/metadata/blob/main/docs/tables/model.md
[MA Pair]: https://github.com/DIGITbrain/metadata/blob/main/docs/tables/ma_pair.md
[DMA Tuple]: https://github.com/DIGITbrain/metadata/blob/main/docs/tables/dma_tuple.md
[Supporting Metadata]: https://github.com/DIGITbrain/metadata/blob/main/docs/tables/supporting_metadata.md
