<style>
  .md-content__button {
    display: none;
  }
</style>
# ConfigurationData Fields

**This information is also available in [table format](/tables/configurationdata/)**


## Available Fields 

The metadata specification for a DIGITbrain ConfigurationData
has these sections:

- [ConfigurationData](#configurationdata)


### ConfigurationData


`filePath`{ #filepath }
:   **Required**-*String*- full path to file including file name

    === "Example"
        ``` yaml     
        /data/rclone.conf
        ```

`fileContent`{ #filecontent }
:   **Required**-*String*- file content (not binary)

    === "Example"
        ``` yaml     
        [s3-server]\n    access_key: 123abc
        ```

`mountPropagation`{ #mountpropagation }
:   **Optional**-*boolean*- Enable mountPropagation https://kubernetes.io/docs/concepts/storage/volumes/#mount-propagation . Default: False
    === "Example"
        ``` yaml     
        True
        ```
