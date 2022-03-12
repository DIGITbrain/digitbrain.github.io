
<style>
  .md-content__button {
    display: none;
  }
</style>

**This information is also available in** **[list format](/attributes/configurationdata/)**

| Concept           | Key              | Subkey   | Type    | Example Value                         | Comment                                                                                                         | Condition   |
|:------------------|:-----------------|:---------|:--------|:--------------------------------------|:----------------------------------------------------------------------------------------------------------------|:------------|
| ConfigurationData |                  |          |         |                                       |                                                                                                                 |             |
|                   | filePath         |          | String  | "/data/rclone.conf"                   | full path to file including file name                                                                           | mandatory   |
|                   | fileContent      |          | String  | "[s3-server]\n    access_key: 123abc" | file content (not binary)                                                                                       | mandatory   |
|                   | mountPropagation |          | boolean | True                                  | Enable mountPropagation https://kubernetes.io/docs/concepts/storage/volumes/#mount-propagation . Default: False | optional    |