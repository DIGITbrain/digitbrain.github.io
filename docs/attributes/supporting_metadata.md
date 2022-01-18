# Supporting Metadata Metadata Specification

## Available Fields 

The metadata specification for a DIGITbrain Supporting Metadata
has these sections:

- [Person](#person)
- [Legal Entity (Organization)](#legal-entity-(organization))
- [IP Instance](#ip-instance)


### Person


`ID`

:   **Optional**-*ID / URI*- Unique identifier for the IP Inst.

`Created at`

:   **Optional**-*ISO 8601*- Date of creation

`Version`

:   **Optional**-*Integer*- Version number of the IP Instance

`First name`

:   **Optional**-*Text*- First name of the Person

`Last name`

:   **Optional**-*Text*- Last name of the Person

`Email`

:   **Optional**-*Email*- Email address of the Person

`CV`

:   **Optional**-*Text*- Short description of the Person

`Image`

:   **Optional**-*Image*- Picture of the IP Instance

`Affiliation`

:   **Optional**-*ID / URI*- Legal Entity the Person is affiliated with


### Legal Entity (Organization)


`Author`

:   **Optional**-*ID / URI*- Identifier of the Author of the IP Instance

`Name`

:   **Optional**-*Text*- Name of the IP Instance

`Description`

:   **Optional**-*Text*- Description of the IP Instance

`Logo`

:   **Optional**-*Image*- Logo of the Legal Entity

`URL`

:   **Optional**-*URL*- Website of the Legal Entity

`Location`

:   **Optional**-*ID / URI?*- Physical location of the IP Instance

`Phone`

:   **Optional**-*String*- Phone Number of the Legal Entity

`VAT ID No.`

:   **Optional**-*String*- VAT ID Number of the Legal Entity

`IP Family`

:   **Optional**-*ID / URI*- Reference to the IP Family

`Manager`

:   **Optional**-*ID / URI*- Identifier of the Legal Entity managing the IP Family

`Model No.`

:   **Optional**-*Text*- Number defined by the IP Man.

`Capacity`

:   **Optional**-*Text*- Capacity of the IP Family

`IP Man.`

:   **Optional**-*ID / URI*- Identifier of the IP Manufacturer (Legal Entity)


### IP Instance


`Operator`

:   **Optional**-*ID / URI*- Identifier of the Legal Entity operating the IP Instance

`Serial No.`

:   **Optional**-*Text*- Number defined by the IP Man.
