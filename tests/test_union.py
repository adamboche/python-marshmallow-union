import pytest
import marshmallow

import marshmallow_union


class PersonSchema(marshmallow.Schema):
    name = marshmallow.fields.String()
    age = marshmallow_union.Union(
        [marshmallow.fields.String(), marshmallow.fields.Integer()]
    )


class OtherSchema(marshmallow.Schema):
    name = marshmallow.fields.String()
    number_or_numbers = marshmallow_union.Union(
        [
            marshmallow.fields.List(marshmallow.fields.Integer()),
            marshmallow.fields.Integer(),
        ]
    )


@pytest.mark.parametrize(
    "data, schema",
    [
        ({"name": "Alice", "age": "twenty-five"}, PersonSchema()),
        ({"name": "Alice", "age": 25}, PersonSchema()),
        ({"name": "Alice", "number_or_numbers": 25}, OtherSchema()),
        ({"name": "Alice", "number_or_numbers": [25, 50]}, OtherSchema()),
    ],
)
def test_round_trip(data, schema):

    loaded = schema.load(data)
    dumped = schema.dump(loaded)

    assert dumped == loaded
