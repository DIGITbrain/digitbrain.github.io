<style>
  .md-content__button {
    display: none;
  }
</style>
# Supporting Metadata Fields

**This information is also available in [table format](/tables/supporting_metadata/)**


## Available Fields 

The metadata specification for a DIGITbrain Supporting Metadata
has these sections:

- [Person](#person)
- [Legal Entity (Organization)](#legal-entity-organization)
- [IP Family](#ip-family)
- [IP Instance](#ip-instance)


### Person


`ID`{ #ID }
:   **Optional**-*ID / URI*- Unique identifier for the Person

`Created at`{ #Created at }
:   **Optional**-*ISO 8601*- Date of creation

`Version`{ #Version }
:   **Optional**-*Integer*- Version number of the Person

`First name`{ #First name }
:   **Optional**-*Text*- First name of the Person

`Last name`{ #Last name }
:   **Optional**-*Text*- Last name of the Person

`Email`{ #Email }
:   **Optional**-*Email*- Email address of the Person

`CV`{ #CV }
:   **Optional**-*Text*- Short description of the Person

`Image`{ #Image }
:   **Optional**-*Image*- Profile picture of the Person

`Affiliation`{ #Affiliation }
:   **Optional**-*ID / URI*- Legal Entity the Person is affiliated with


### Legal Entity (Organization)


`ID`{ #ID }
:   **Optional**-*ID / URI*- Unique identifier for the Legal Entity

`Created at`{ #Created at }
:   **Optional**-*ISO 8601*- Date of creation

`Version`{ #Version }
:   **Optional**-*Integer*- Version number of the Legal Entity

`Author`{ #Author }
:   **Optional**-*ID / URI*- Identifier of the Author of the Legal Entity

`Name`{ #Name }
:   **Optional**-*Text*- Name of the Legal Entity

`Description`{ #Description }
:   **Optional**-*Text*- Description of the Legal Entity

`Logo`{ #Logo }
:   **Optional**-*Image*- Logo of the Legal Entity

`URL`{ #URL }
:   **Optional**-*URL*- Website of the Legal Entity

`Location`{ #Location }
:   **Optional**-*ID / URI?*- Physical address of the Legal Entity

`Phone`{ #Phone }
:   **Optional**-*String*- Phone Number of the Legal Entity

`VAT ID No.`{ #VAT ID No. }
:   **Optional**-*String*- VAT ID Number of the Legal Entity


### IP Family


`ID`{ #ID }
:   **Optional**-*ID / URI*- Unique identifier for the IP Fam.

`Created at`{ #Created at }
:   **Optional**-*ISO 8601*- Date of creation

`Version`{ #Version }
:   **Optional**-*Integer*- Version number of the IP Family

`Author`{ #Author }
:   **Optional**-*ID / URI*- Identifier of the Author of the IP Family

`Manager`{ #Manager }
:   **Optional**-*ID / URI*- Identifier of the Legal Entity managing the IP Family

`Name`{ #Name }
:   **Optional**-*Text*- Technical Name of the IP Family

`Image`{ #Image }
:   **Optional**-*Image*- Picture of the IP Family

`Model No.`{ #Model No. }
:   **Optional**-*Text*- Number defined by the IP Man.

`Description`{ #Description }
:   **Optional**-*Text*- Description of the IP Family

`Capacity`{ #Capacity }
:   **Optional**-*Text*- Capacity of the IP Family

`IP Man.`{ #IP Man. }
:   **Optional**-*ID / URI*- Identifier of the IP Manufacturer (Legal Entity)


### IP Instance


`ID`{ #ID }
:   **Optional**-*ID / URI*- Unique identifier for the IP Inst.

`Created at`{ #Created at }
:   **Optional**-*ISO 8601*- Date of creation

`Version`{ #Version }
:   **Optional**-*Integer*- Version number of the IP Instance

`Author`{ #Author }
:   **Optional**-*ID / URI*- Identifier of the Author of the IP Instance

`Operator`{ #Operator }
:   **Optional**-*ID / URI*- Identifier of the Legal Entity operating the IP Instance

`IP Family`{ #IP Family }
:   **Optional**-*ID / URI*- Reference to the IP Family

`Name`{ #Name }
:   **Optional**-*Text*- Name of the IP Instance

`Image`{ #Image }
:   **Optional**-*Image*- Picture of the IP Instance

`Serial No.`{ #Serial No. }
:   **Optional**-*Text*- Number defined by the IP Man.

`Description`{ #Description }
:   **Optional**-*Text*- Description of the IP Instance

`Location`{ #Location }
:   **Optional**-*ID / URI?*- Physical location of the IP Instance
