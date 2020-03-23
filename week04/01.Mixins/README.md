# Serializing & Deserializing from/to JSON and XML

## JSON & XML

[JSON](https://en.wikipedia.org/wiki/JSON) and [XML](https://en.wikipedia.org/wiki/XML) are file formats. They serve for communication between systems and interfaces.

## Serialization & Deserialization

Serialization is the process of translating an object into a primitive type. Deserialization is the opposite operation.

## Your task

All the classes from today should now how to serailize & deserialize themselves into JSON and XML.
You need to create two mixins called `Jsonable` and `Xmlable`.
They should have the following methods:

- `Jsonable`:
  - `to_json(indent)`. Default value `indent=4`. Returns JSON string representing the current object.
  - `from_json(json_string)`. Returns object instance of the current class with attributes from the passed argument.
- `Xmlable` with methods:
  - `to_xml()`. Returns XML string representing the current object.
  - `from_xml(xml_string)`. Returns object instance of the current class with attributes from the passed argument.

> NOTE: What should `from_json` and `from_xml` methods be?

### Example

#### Serialization

```python
p = Panda(name='Marto')
p.to_json()
'''
{
    "dict": {
        "name": "Marto"
    },
    "type": "Panda"
}
'''
p.to_xml()
'<Panda><name>Ivo</name></Panda>'
```

#### Deserialization

```python
p = Panda(name='marto')
json_string = p.to_json()
xml_string = p.to_xml()

p1 = Panda.from_json(json_string)
p2 = Panda.from_xml(xml_string)

assert p == p1
assert p == p2
```

#### Validation

Make sure you are `from_json` and `from_xml` return objects from the correct class. Raise `ValueError` instead.

```python
person = Person('Pesho')
Panda.from_json(person.to_json())  # ValueError
```

### Hints

- Use TDD!
- For XML, use the standard library - <https://docs.python.org/3/library/xml.etree.elementtree.html>
- For JSON, use the standard library - <https://docs.python.org/3/library/json.html>

### Bonus

Make your program work with nested structures.

```python
person = Person('Pesho', panda=Panda('Marto'))
person.to_json()
'''
{
    "dict": {
        "name": "Pesho",
        "panda": {
            "dict": {
                "name": "Marto"
            },
            "type": "Panda"
        }
    },
    "type": "Person"
}
'''
```
