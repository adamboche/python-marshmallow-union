=====
Usage
=====

To use marshmallow-union in a project import ``marshmallow_union.Union`` and
pass it a list of ``marshmallow.fields.Field`` instances. When serializing and
deserializing, each one will be tried in sequence until one succeeds, not
raising ``marshmallow.exceptions.ValidationError``. If none of them is
successful, ``marshmallow.exceptions.ValidationError`` is raised.

See the API reference for more details.

.. testcode::

    import marshmallow
    import marshmallow_union


    class PersonSchema(marshmallow.Schema):
        name = marshmallow.fields.String()
        number_or_numbers = marshmallow_union.Union(
            [
                marshmallow.fields.List(marshmallow.fields.Integer()),
                marshmallow.fields.Integer(),
            ],
        	reverse_serialize_candidates=True,
        )



    input_data = {"name": "Alice", "number_or_numbers": 25}
    schema = PersonSchema()

    loaded = schema.load(input_data)
    dumped = schema.dump(loaded)

    assert dumped == input_data




.. testoutput::
   :hide:
