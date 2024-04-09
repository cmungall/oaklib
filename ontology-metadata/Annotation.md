# Class: Annotation


_A reified property-object pair_





URI: [omoschema:Annotation](http://purl.obolibrary.org/obo/omo/schema/Annotation)




```{mermaid}
 classDiagram
    class Annotation
      Annotation : object
        
      Annotation : predicate
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [predicate](predicate.md) | 0..1 <br/> [String](String.md) |  | direct |
| [object](object.md) | 0..1 <br/> [String](String.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Axiom](Axiom.md) | [annotations](annotations.md) | range | [Annotation](Annotation.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: http://purl.obolibrary.org/obo/omo/schema





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | omoschema:Annotation |
| native | omoschema:Annotation |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Annotation
description: A reified property-object pair
from_schema: http://purl.obolibrary.org/obo/omo/schema
attributes:
  predicate:
    name: predicate
    from_schema: http://purl.obolibrary.org/obo/omo/schema
    domain_of:
    - Annotation
    relational_role: PREDICATE
  object:
    name: object
    from_schema: http://purl.obolibrary.org/obo/omo/schema
    domain_of:
    - Annotation
    relational_role: OBJECT
represents_relationship: true

```
</details>

### Induced

<details>
```yaml
name: Annotation
description: A reified property-object pair
from_schema: http://purl.obolibrary.org/obo/omo/schema
attributes:
  predicate:
    name: predicate
    from_schema: http://purl.obolibrary.org/obo/omo/schema
    alias: predicate
    owner: Annotation
    domain_of:
    - Annotation
    relational_role: PREDICATE
    range: string
  object:
    name: object
    from_schema: http://purl.obolibrary.org/obo/omo/schema
    alias: object
    owner: Annotation
    domain_of:
    - Annotation
    relational_role: OBJECT
    range: string
represents_relationship: true

```
</details>