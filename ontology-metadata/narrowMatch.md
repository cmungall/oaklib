# Slot: narrowMatch

URI: [skos:narrowMatch](http://www.w3.org/2004/02/skos/core#narrowMatch)




## Inheritance

* [match](match.md) [ [match_aspect](match_aspect.md)]
    * **narrowMatch**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[HasMappings](HasMappings.md) |  |  no  |
[Term](Term.md) | A NamedThing that includes classes, properties, but not ontologies |  no  |
[Class](Class.md) |  |  yes  |
[Property](Property.md) |  |  yes  |
[AnnotationProperty](AnnotationProperty.md) | A property used in non-logical axioms |  no  |
[ObjectProperty](ObjectProperty.md) | A property that connects two objects in logical axioms |  no  |
[TransitiveProperty](TransitiveProperty.md) | An ObjectProperty with the property of transitivity |  no  |
[NamedIndividual](NamedIndividual.md) | An instance that has a IRI |  no  |
[HomoSapiens](HomoSapiens.md) | An individual human being |  no  |
[Agent](Agent.md) |  |  no  |
[Image](Image.md) |  |  no  |
[Subset](Subset.md) | A collection of terms grouped for some purpose |  no  |







## Properties

* Range: [Thing](Thing.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: http://purl.obolibrary.org/obo/omo/schema




## LinkML Source

<details>
```yaml
name: narrowMatch
from_schema: http://purl.obolibrary.org/obo/omo/schema
rank: 1000
is_a: match
slot_uri: skos:narrowMatch
multivalued: true
alias: narrowMatch
domain_of:
- HasMappings
range: Thing

```
</details>