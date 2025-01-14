

# Slot: type



URI: [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type)




## Inheritance

* [logical_predicate](logical_predicate.md)
    * **type**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Class](Class.md) |  |  no  |
| [HomoSapiens](HomoSapiens.md) | An individual human being |  no  |
| [Agent](Agent.md) |  |  no  |
| [NamedObject](NamedObject.md) | Anything with an IRI |  no  |
| [Property](Property.md) |  |  no  |
| [AnnotationProperty](AnnotationProperty.md) | A property used in non-logical axioms |  no  |
| [NamedIndividual](NamedIndividual.md) | An instance that has a IRI |  no  |
| [Thing](Thing.md) |  |  no  |
| [Image](Image.md) |  |  no  |
| [Term](Term.md) | A NamedThing that includes classes, properties, but not ontologies |  no  |
| [Subset](Subset.md) | A collection of terms grouped for some purpose |  no  |
| [ObjectProperty](ObjectProperty.md) | A property that connects two objects in logical axioms |  no  |
| [Ontology](Ontology.md) | An OWL ontology |  no  |
| [TransitiveProperty](TransitiveProperty.md) | An ObjectProperty with the property of transitivity |  no  |







## Properties

* Range: [Uriorcurie](Uriorcurie.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/oak/ontology-metadata




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rdf:type |
| native | omoschema:type |




## LinkML Source

<details>
```yaml
name: type
from_schema: https://w3id.org/oak/ontology-metadata
rank: 1000
is_a: logical_predicate
slot_uri: rdf:type
designates_type: true
alias: type
domain_of:
- Thing
range: uriorcurie
multivalued: true

```
</details>