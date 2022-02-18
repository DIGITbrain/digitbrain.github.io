
<style>
  .md-content__button {
    display: none;
  }
</style>

**This information is also available in** **[list format](/attributes/supporting_metadata/)**

| Concept                     | Key         | Subkey   | Type      | Example Value   | Comment                                                  | Condition   |
|:----------------------------|:------------|:---------|:----------|:----------------|:---------------------------------------------------------|:------------|
| Person                      |             |          |           |                 |                                                          |             |
|                             | ID          |          | ID / URI  |                 | Unique identifier for the Person                         | auto        |
|                             | Created at  |          | ISO 8601  |                 | Date of creation                                         | auto        |
|                             | Version     |          | Integer   |                 | Version number of the Person                             | auto        |
|                             | First name  |          | Text      |                 | First name of the Person                                 | mandatory   |
|                             | Last name   |          | Text      |                 | Last name of the Person                                  | mandatory   |
|                             | Email       |          | Email     |                 | Email address of the Person                              | mandatory   |
|                             | CV          |          | Text      |                 | Short description of the Person                          | optional    |
|                             | Image       |          | Image     |                 | Profile picture of the Person                            | optional    |
|                             | Affiliation |          | ID / URI  |                 | Legal Entity the Person is affiliated with               | optional    |
| Legal Entity (Organization) |             |          |           |                 |                                                          |             |
|                             | ID          |          | ID / URI  |                 | Unique identifier for the Legal Entity                   | auto        |
|                             | Created at  |          | ISO 8601  |                 | Date of creation                                         | auto        |
|                             | Version     |          | Integer   |                 | Version number of the Legal Entity                       | auto        |
|                             | Author      |          | ID / URI  |                 | Identifier of the Author of the Legal Entity             | mandatory   |
|                             | Name        |          | Text      |                 | Name of the Legal Entity                                 | mandatory   |
|                             | Description |          | Text      |                 | Description of the Legal Entity                          | mandatory   |
|                             | Logo        |          | Image     |                 | Logo of the Legal Entity                                 | optional    |
|                             | URL         |          | URL       |                 | Website of the Legal Entity                              | optional    |
|                             | Location    |          | ID / URI? |                 | Physical address of the Legal Entity                     | optional    |
|                             | Phone       |          | String    |                 | Phone Number of the Legal Entity                         | optional    |
|                             | VAT ID No.  |          | String    |                 | VAT ID Number of the Legal Entity                        | optional    |
| IP Family                   |             |          |           |                 |                                                          |             |
|                             | ID          |          | ID / URI  |                 | Unique identifier for the IP Fam.                        | auto        |
|                             | Created at  |          | ISO 8601  |                 | Date of creation                                         | auto        |
|                             | Version     |          | Integer   |                 | Version number of the IP Family                          | auto        |
|                             | Author      |          | ID / URI  |                 | Identifier of the Author of the IP Family                | mandatory   |
|                             | Manager     |          | ID / URI  |                 | Identifier of the Legal Entity managing the IP Family    | mandatory   |
|                             | Name        |          | Text      |                 | Technical Name of the IP Family                          | mandatory   |
|                             | Image       |          | Image     |                 | Picture of the IP Family                                 | optional    |
|                             | Model No.   |          | Text      |                 | Number defined by the IP Man.                            | optional    |
|                             | Description |          | Text      |                 | Description of the IP Family                             | optional    |
|                             | Capacity    |          | Text      |                 | Capacity of the IP Family                                | optional    |
|                             | IP Man.     |          | ID / URI  |                 | Identifier of the IP Manufacturer (Legal Entity)         | optional    |
| IP Instance                 |             |          |           |                 |                                                          |             |
|                             | ID          |          | ID / URI  |                 | Unique identifier for the IP Inst.                       | auto        |
|                             | Created at  |          | ISO 8601  |                 | Date of creation                                         | auto        |
|                             | Version     |          | Integer   |                 | Version number of the IP Instance                        | auto        |
|                             | Author      |          | ID / URI  |                 | Identifier of the Author of the IP Instance              | mandatory   |
|                             | Operator    |          | ID / URI  |                 | Identifier of the Legal Entity operating the IP Instance | mandatory   |
|                             | IP Family   |          | ID / URI  |                 | Reference to the IP Family                               | mandatory   |
|                             | Name        |          | Text      |                 | Name of the IP Instance                                  | mandatory   |
|                             | Image       |          | Image     |                 | Picture of the IP Instance                               | optional    |
|                             | Serial No.  |          | Text      |                 | Number defined by the IP Man.                            | optional    |
|                             | Description |          | Text      |                 | Description of the IP Instance                           | optional    |
|                             | Location    |          | ID / URI? |                 | Physical location of the IP Instance                     | optional    |