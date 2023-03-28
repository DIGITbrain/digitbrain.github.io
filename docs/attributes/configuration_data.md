<style>
  .md-content__button {
    display: none;
  }
</style>
# Configuration Data Fields




The specification for Configuration Data
has these fields:


`file_path`{ #file-path }

:   **Optional**-*string*<br>
    full path to file including file name


    === "Example"
        ``` yaml     
        data/rclone.conf
        ```


`file_content`{ #file-content }

:   **Optional**-*string*<br>
    file content (not binary)


    === "Example"
        ``` yaml     
        [s3-server]
        access_key: 123abc

        ```


`mount_propagation`{ #mount-propagation }

:   **Optional**-*enum[ "None", "HostToContainer", "Bidirectional" ]*<br>
    Enable mountPropagation https://kubernetes.io/docs/concepts/storage/volumes/#mount-propagation
    . Defaults to None



    === "Example"
        ``` yaml     
        Bidirectional
        ```

