import typing as t

import marshmallow
import marshmallow.exceptions


class Union(marshmallow.fields.Field):
    """Field that accepts any one of multiple fields.

    Each argument will be tried until one succeeds.

    Args:
        fields: The list of candidate fields to try.
        reverse_serialize_candidates: Whether to try the candidates in reverse order when
           serializing.
    """

    def __init__(
        self,
        fields: t.List[marshmallow.fields.Field],
        *args,
        reverse_serialize_candidates: bool = False,
        **kwargs
    ):
        self._candidate_fields = fields
        self._reverse_serialize_candidates = reverse_serialize_candidates
        super().__init__(*args, **kwargs)

    def serialize(self, attr, obj, accessor=None, **kwargs):
        errors = []

        fields = self._candidate_fields
        if self._reverse_serialize_candidates:
            fields = reversed(fields)

        for candidate_field in fields:
            try:
                return candidate_field.serialize(attr, obj, **kwargs)
            except marshmallow.exceptions.ValidationError as exc:
                errors.append(exc.messages)

        raise marshmallow.exceptions.ValidationError(message=errors, field_name=attr)

    def deserialize(self, value, attr=None, data=None, **kwargs):
        errors = []
        for candidate_field in self._candidate_fields:
            try:
                return candidate_field.deserialize(value, attr, data, **kwargs)
            except marshmallow.exceptions.ValidationError as exc:
                errors.append(exc.messages)
        raise marshmallow.exceptions.ValidationError(message=errors, field_name=attr)


__version__ = "__version__ = 0.1.5"
