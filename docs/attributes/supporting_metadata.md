<style>
  .md-content__button {
    display: none;
  }
</style>
# Supporting Metadata Metadata Fields

## Available Fields 

The metadata specification for a DIGITbrain Supporting Metadata
has these sections:

- [Person](#person)
- [Legal Entity (Organization)](#legal-entity-organization)
- [IP Family](#ip-family)
- [IP Instance](#ip-instance)


### Person


`ID`
:   **Optional**-*ID / URI*- Unique identifier for the Person

`Created at`
:   **Optional**-*ISO 8601*- Date of creation

`Version`
:   **Optional**-*Integer*- Version number of the Person

`First name`
:   **Optional**-*Text*- First name of the Person

`Last name`
:   **Optional**-*Text*- Last name of the Person

`Email`
:   **Optional**-*Email*- Email address of the Person

`CV`
:   **Optional**-*Text*- Short description of the Person

`Image`
:   **Optional**-*Image*- Profile picture of the Person

`Affiliation`
:   **Optional**-*ID / URI*- Legal Entity the Person is affiliated with


### Legal Entity (Organization)


`ID`
:   **Optional**-*ID / URI*- Unique identifier for the Legal Entity

`Created at`
:   **Optional**-*ISO 8601*- Date of creation

`Version`
:   **Optional**-*Integer*- Version number of the Legal Entity

`Author`
:   **Optional**-*ID / URI*- Identifier of the Author of the Legal Entity

`Name`
:   **Optional**-*Text*- Name of the Legal Entity

`Description`
:   **Optional**-*Text*- Description of the Legal Entity

`Logo`
:   **Optional**-*Image*- Logo of the Legal Entity

`URL`
:   **Optional**-*URL*- Website of the Legal Entity

`Location`
:   **Optional**-*ID / URI?*- Physical address of the Legal Entity

`Phone`
:   **Optional**-*String*- Phone Number of the Legal Entity

`VAT ID No.`
:   **Optional**-*String*- VAT ID Number of the Legal Entity


### IP Family


`ID`
:   **Optional**-*ID / URI*- Unique identifier for the IP Fam.

`Created at`
:   **Optional**-*ISO 8601*- Date of creation

`Version`
:   **Optional**-*Integer*- Version number of the IP Family

`Author`
:   **Optional**-*ID / URI*- Identifier of the Author of the IP Family

`Manager`
:   **Optional**-*ID / URI*- Identifier of the Legal Entity managing the IP Family

`Name`
:   **Optional**-*Text*- Technical Name of the IP Family

`Image`
:   **Optional**-*Image*- Picture of the IP Family

`Model No.`
:   **Optional**-*Text*- Number defined by the IP Man.

`Description`
:   **Optional**-*Text*- Description of the IP Family

`Capacity`
:   **Optional**-*Text*- Capacity of the IP Family

`IP Man.`
:   **Optional**-*ID / URI*- Identifier of the IP Manufacturer (Legal Entity)


### IP Instance


`ID`
:   **Optional**-*ID / URI*- Unique identifier for the IP Inst.

`Created at`
:   **Optional**-*ISO 8601*- Date of creation

`Version`
:   **Optional**-*Integer*- Version number of the IP Instance

`Author`
:   **Optional**-*ID / URI*- Identifier of the Author of the IP Instance

`Operator`
:   **Optional**-*ID / URI*- Identifier of the Legal Entity operating the IP Instance

`IP Family`
:   **Optional**-*ID / URI*- Reference to the IP Family

`Name`
:   **Optional**-*Text*- Name of the IP Instance

`Image`
:   **Optional**-*Image*- Picture of the IP Instance

`Serial No.`
:   **Optional**-*Text*- Number defined by the IP Man.

`Description`
:   **Optional**-*Text*- Description of the IP Instance

`Location`
:   **Optional**-*ID / URI?*- Physical location of the IP Instance
