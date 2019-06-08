import typing as t

import marshmallow
import marshmallow.exceptions


class Union(marshmallow.fields.Field):
    """Field that accepts any one of multiple fields.
    
    Each argument will be tried until one succeeds. 
    """

    def __init__(
        self,
        fields: t.List[marshmallow.fields.Field],
        reverse_serialize_candidates: bool = False,
        *args,
        **kwargs
    ):
        """
        Args:
            fields: The list of candidate fields to try.
            reverse_serialize_candidates: Whether to try the candidates in reverse order when serializing.
        """
        self._candidate_fields = fields
        self._reverse_serialize_candidates = reverse_serialize_candidates
        super().__init__(*args, **kwargs)

    def _serialize(self, value, attr, obj, **kwargs):
        errors = []

        fields = self._candidate_fields
        if self._reverse_serialize_candidates:
            fields = reversed(fields)

        for candidate_field in fields:
            try:
                return candidate_field._serialize(value, attr, obj, **kwargs)
            except marshmallow.exceptions.ValidationError as e:
                errors.append(e.messages)
        raise marshmallow.exceptions.ValidationError(message=errors, field_name=attr)

    def _deserialize(self, value, attr, obj, **kwargs):
        errors = []
        for candidate_field in self._candidate_fields:
            try:
                return candidate_field._deserialize(value, attr, obj, **kwargs)
            except marshmallow.exceptions.ValidationError as e:
                errors.append(e.messages)
        raise marshmallow.exceptions.ValidationError(message=errors, field_name=attr)
