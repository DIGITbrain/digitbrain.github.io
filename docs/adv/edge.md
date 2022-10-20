# Edges

DIGITbrain applications can run on your own *edge* devices, and
benefit from having compute power closer to the data.

## Requirements

For an edge device to be used as a hosting node for your application,
components of DIGITbrain will need to access your device and install
a small software component on it ([KubeEdge](https://kubeedge.io/)).
As such, the device must meet the following requirements:

- Have an endpoint accessible from the DIGITbrain cloud
- Have an SSH server open on port 22
- Have an SSH user with sudo privileges
- Have a *NIX operating system

For more specific information, such as the DIGITbrain cloud subnet,
please contact your support person.

## Metadata Description

The metadata specification for edges is [here](/attributes/deployment/#edge).