=====
Usage
=====

To use marshmallow-union in a project::

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


	data = {"name": "Alice", "number_or_numbers": 25}
	schema = PersonSchema()
	
	loaded = schema.load(data)
	dumped = schema.dump(data)