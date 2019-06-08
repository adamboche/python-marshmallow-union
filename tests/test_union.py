"""Tests for marshmallow_union."""

import marshmallow
import pytest

import marshmallow_union


class PersonSchema(marshmallow.Schema):
    """Schema with reverse candidates."""

    name = marshmallow.fields.String()
    number_or_numbers = marshmallow_union.Union(
        [
            marshmallow.fields.List(marshmallow.fields.Integer()),
            marshmallow.fields.Integer(),
        ],
        reverse_serialize_candidates=True,
    )


class OtherSchema(marshmallow.Schema):
    """Schema with forward candidates."""

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
    """Input, dump, load are all equal."""
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
    """Invalid types raise exceptions in both directions."""
    with pytest.raises(marshmallow.exceptions.ValidationError):
        schema.dump(data)

    with pytest.raises(marshmallow.exceptions.ValidationError):
        schema.load(data)
