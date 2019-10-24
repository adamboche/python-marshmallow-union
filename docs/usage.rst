=====
Usage
=====

To use marshmallow-union in a project import ``marshmallow_union.Union`` and pass it a
list of ``marshmallow.fields.Field`` instances.

When deserializing, each field will be tried in sequence until one succeeds, not raising
``marshmallow.exceptions.ValidationError``. If none of them is successful,
``marshmallow.exceptions.ValidationError`` is raised.

When serializing, each field will be tried in sequence until one succeeds, not raising
*any* exception. If none of them is successful, :class:`marshmallow_union.ExceptionGroup`
is raised, containing the values of the raised exceptions.

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
