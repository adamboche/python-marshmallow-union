0.1.15 (2020-05-30)
-------------------

Changes
^^^^^^^

- Fix `#32 <https://github.com/adamboche/python-marshmallow-union/issues/32>`_ : Never ignore the value passed to `_serialize`. Notably, this fixes the serialization of lists of unions, such as :code:`List(Union([Int(), String()]))`

.. code:: python
    marshmallow.fields.List(
        marshmallow_union.Union([marshmallow.fields.Int(), marshmallow.fields.String()])
    )


0.1.12 (2019-10-24)
-------------------


Backward-incompatible Changes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- On serialization, :class:`marshmallow_union.ExceptionGroup` is raised if all candidate fields fail.
  `#24 <https://github.com/adamboche/python-marshmallow-union/issues/24>`_


----


0.1.11 (2019-06-19)
-------------------


Changes
^^^^^^^

- Override the underscore-prefixed methods instead of the plain ones
  `#22 <https://github.com/adamboche/python-marshmallow-union/issues/22>`_


----


Changelog
=========

0.1.10 (2019-06-08)
-------------------


Changes
^^^^^^^

- Use Towncrier for changelog.
  `#18 <https://github.com/adamboche/python-marshmallow-union/issues/18>`_


----


0.1.0 (2019-06-07)
------------------

* First release on PyPI.
