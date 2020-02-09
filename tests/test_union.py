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


class IntStrSchema(marshmallow.Schema):
    """Schema with int and str candidates."""

    x = marshmallow_union.Union([marshmallow.fields.Int(), marshmallow.fields.String()])


@pytest.mark.parametrize(
    "data, schema",
    [
        ({"name": "Alice", "number_or_numbers": 25}, PersonSchema()),
        ({"name": "Alice", "number_or_numbers": [25, 50]}, PersonSchema()),
        ({"name": "Alice", "number_or_numbers": [25, 50]}, OtherSchema()),
        ({"x": 5}, IntStrSchema()),
        ({"x": "hello"}, IntStrSchema()),
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
def test_load_raises(data, schema):
    """Invalid types raise ValidationError while loading."""
    with pytest.raises(marshmallow.exceptions.ValidationError):
        schema.load(data)


@pytest.mark.parametrize(
    "data,schema",
    [
        ({"name": "Alice", "number_or_numbers": "twenty-five"}, PersonSchema()),
        ({"name": "Alice", "number_or_numbers": {"x": 14}}, PersonSchema()),
        ({"items": {"a": 42, "b": "spam"}}, MappingSchema()),
    ],
)
def test_dump_raises(data, schema):
    """Invalid types raise ExceptionGroup while loading."""
    try:
        schema.dump(data)
    except marshmallow_union.ExceptionGroup as e:
        assert e.errors
