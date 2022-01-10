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


[Algorithm]: https://github.com/DIGITbrain/metadata/blob/main/assets/algorithm.csv
[Microservice]: https://github.com/DIGITbrain/metadata/blob/main/assets/microservice.csv
[Data]: https://github.com/DIGITbrain/metadata/blob/main/assets/data.csv
[Model]: https://github.com/DIGITbrain/metadata/blob/main/assets/model.csv
[MA Pair]: https://github.com/DIGITbrain/metadata/blob/main/assets/ma_pair.csv
[DMA Tuple]: https://github.com/DIGITbrain/metadata/blob/main/assets/dma_tuple.csv
[Supporting Metadata]: https://github.com/DIGITbrain/metadata/blob/main/assets/supporting_metadata.csv
