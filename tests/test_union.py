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


class MappingSchema(marshmallow.Schema):
    """Schema with union inside mapping."""

    items = marshmallow.fields.Dict(
        marshmallow.fields.String(),
        marshmallow_union.Union(
            [
                marshmallow.fields.Integer(),
                marshmallow.fields.List(marshmallow.fields.Integer()),
            ]
        ),
    )


class StrIntSchema(marshmallow.Schema):
    """Schema with str and int candidates."""

    x = marshmallow_union.Union([marshmallow.fields.Int(), marshmallow.fields.String()])


@pytest.mark.parametrize(
    "data, schema",
    [
        ({"name": "Alice", "number_or_numbers": 25}, PersonSchema()),
        ({"name": "Alice", "number_or_numbers": [25, 50]}, PersonSchema()),
        ({"name": "Alice", "number_or_numbers": [25, 50]}, OtherSchema()),
        ({"x": 5}, StrIntSchema()),
        ({"x": "hello"}, StrIntSchema()),
        ({"items": {"a": 42, "b": [17]}}, MappingSchema()),
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
        ({"name": "Alice", "number_or_numbers": {"x": 14}}, PersonSchema()),
        ({"items": {"a": 42, "b": "spam"}}, MappingSchema()),
    ],
)
def test_raises(data, schema):
    """Invalid types raise exceptions in both directions."""
    with pytest.raises(marshmallow.exceptions.ValidationError):
        schema.load(data)

    with pytest.raises(marshmallow_union.ExceptionGroup):
        schema.dump(data)
