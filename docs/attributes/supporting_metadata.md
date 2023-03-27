<style>
  .md-content__button {
    display: none;
  }
</style>
# Supporting Metadata Fields


## Available Fields 

The metadata specification for a DIGITbrain Supporting Metadata
has these sections:

- [Person](#person)
- [Legal Entity (Organization)](#legal-entity-organization)
- [IP Family](#ip-family)
- [IP Instance](#ip-instance)


### Person


`ID`{ #id }
:   **Auto-generated**-*ID / URI*- Unique identifier for the Person


`Created at`{ #created-at }
:   **Auto-generated**-*ISO 8601*- Date of creation


`Version`{ #version }
:   **Auto-generated**-*Integer*- Version number of the Person


`First name`{ #first-name }
:   **Required**-*Text*- First name of the Person


`Last name`{ #last-name }
:   **Required**-*Text*- Last name of the Person


`Email`{ #email }
:   **Required**-*Email*- Email address of the Person


`CV`{ #cv }
:   **Optional**-*Text*- Short description of the Person

`Image`{ #image }
:   **Optional**-*Image*- Profile picture of the Person

`Affiliation`{ #affiliation }
:   **Optional**-*ID / URI*- Legal Entity the Person is affiliated with


### Legal Entity (Organization)


`ID`{ #id }
:   **Auto-generated**-*ID / URI*- Unique identifier for the Legal Entity


`Created at`{ #created-at }
:   **Auto-generated**-*ISO 8601*- Date of creation


`Version`{ #version }
:   **Auto-generated**-*Integer*- Version number of the Legal Entity


`Author`{ #author }
:   **Required**-*ID / URI*- Identifier of the Author of the Legal Entity


`Name`{ #name }
:   **Required**-*Text*- Name of the Legal Entity


`Description`{ #description }
:   **Required**-*Text*- Description of the Legal Entity


`Logo`{ #logo }
:   **Optional**-*Image*- Logo of the Legal Entity

`URL`{ #url }
:   **Optional**-*URL*- Website of the Legal Entity

`Location`{ #location }
:   **Optional**-*ID / URI?*- Physical address of the Legal Entity

`Phone`{ #phone }
:   **Optional**-*String*- Phone Number of the Legal Entity

`VAT ID No.`{ #vat-id-no. }
:   **Optional**-*String*- VAT ID Number of the Legal Entity


### IP Family


`ID`{ #id }
:   **Auto-generated**-*ID / URI*- Unique identifier for the IP Fam.


`Created at`{ #created-at }
:   **Auto-generated**-*ISO 8601*- Date of creation


`Version`{ #version }
:   **Auto-generated**-*Integer*- Version number of the IP Family


`Author`{ #author }
:   **Required**-*ID / URI*- Identifier of the Author of the IP Family


`Manager`{ #manager }
:   **Required**-*ID / URI*- Identifier of the Legal Entity managing the IP Family


`Name`{ #name }
:   **Required**-*Text*- Technical Name of the IP Family


`Image`{ #image }
:   **Optional**-*Image*- Picture of the IP Family

`Model No.`{ #model-no. }
:   **Optional**-*Text*- Number defined by the IP Man.

`Description`{ #description }
:   **Optional**-*Text*- Description of the IP Family

`Capacity`{ #capacity }
:   **Optional**-*Text*- Capacity of the IP Family

`IP Man.`{ #ip-man. }
:   **Optional**-*ID / URI*- Identifier of the IP Manufacturer (Legal Entity)


### IP Instance


`ID`{ #id }
:   **Auto-generated**-*ID / URI*- Unique identifier for the IP Inst.


`Created at`{ #created-at }
:   **Auto-generated**-*ISO 8601*- Date of creation


`Version`{ #version }
:   **Auto-generated**-*Integer*- Version number of the IP Instance


`Author`{ #author }
:   **Required**-*ID / URI*- Identifier of the Author of the IP Instance


`Operator`{ #operator }
:   **Required**-*ID / URI*- Identifier of the Legal Entity operating the IP Instance


`IP Family`{ #ip-family }
:   **Required**-*ID / URI*- Reference to the IP Family


`Name`{ #name }
:   **Required**-*Text*- Name of the IP Instance


`Image`{ #image }
:   **Optional**-*Image*- Picture of the IP Instance

`Serial No.`{ #serial-no. }
:   **Optional**-*Text*- Number defined by the IP Man.

`Description`{ #description }
:   **Optional**-*Text*- Description of the IP Instance

`Location`{ #location }
:   **Optional**-*ID / URI?*- Physical location of the IP Instance
