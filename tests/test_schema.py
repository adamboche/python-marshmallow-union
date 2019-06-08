import marshmallow
import pytest


class PersonSchema(marshmallow.Schema):
    name = marshmallow.fields.String()
    age = marshmallow.fields.String()


class OtherSchema(marshmallow.Schema):
    name = marshmallow.fields.String()
    numbers = marshmallow.fields.List(marshmallow.fields.Integer())


@pytest.mark.parametrize(
    "data, schema,",
    [
        ({"name": "Alice", "age": "twenty-five"}, PersonSchema()),
        ({"name": "Alice", "numbers": [25]}, OtherSchema()),
    ],
)
def test_round_trip_schema(data, schema):

    loaded = schema.load(data)
    dumped = schema.dump(loaded)
    assert dumped == loaded


@pytest.mark.parametrize(
    "data,schema", [({"name": "Alice", "numbers": 25}, OtherSchema())]
)
def test_raises(data, schema):
    with pytest.raises(marshmallow.exceptions.ValidationError):
        loaded = schema.load(data)
