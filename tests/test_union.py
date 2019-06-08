import marshmallow
import pytest

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


class OtherSchema(marshmallow.Schema):
    name = marshmallow.fields.String()
    number_or_numbers = marshmallow_union.Union(
        [
            marshmallow.fields.List(marshmallow.fields.Integer()),
            marshmallow.fields.Integer(),
        ],
        reverse_serialize_candidates=False,
    )


@pytest.mark.parametrize(
    "data, schema",
    [
        ({"name": "Alice", "number_or_numbers": 25}, PersonSchema()),
        ({"name": "Alice", "number_or_numbers": [25, 50]}, PersonSchema()),
        ({"name": "Alice", "number_or_numbers": [25, 50]}, OtherSchema()),
    ],
)
def test_round_trip(data, schema):
    dumped = schema.dump(data)
    loaded = schema.load(dumped)
    assert dumped == loaded == data


@pytest.mark.parametrize(
    "data,schema",
    [
        ({"name": "Alice", "number_or_numbers": "twenty-five"}, PersonSchema()),
        ({"name": "Alice", "number_or_numbers": True}, PersonSchema()),
        ({"name": "Alice", "number_or_numbers": {}}, PersonSchema()),
    ],
)
def test_raises(data, schema):
    with pytest.raises(marshmallow.exceptions.ValidationError):
        dumped = schema.dump(data)

    with pytest.raises(marshmallow.exceptions.ValidationError):
        loaded = schema.load(data)