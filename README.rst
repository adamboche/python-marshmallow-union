========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/python-marshmallow-union/badge/?style=flat
    :target: https://readthedocs.org/projects/python-marshmallow-union
    :alt: Documentation Status


.. |travis| image:: https://travis-ci.org/adamboche/python-marshmallow-union.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/adamboche/python-marshmallow-union

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/adamboche/python-marshmallow-union?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/adamboche/python-marshmallow-union

.. |codecov| image:: https://codecov.io/github/adamboche/python-marshmallow-union/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/adamboche/python-marshmallow-union

.. |version| image:: https://img.shields.io/pypi/v/marshmallow-union.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/pypi/marshmallow-union

.. |commits-since| image:: https://img.shields.io/github/commits-since/adamboche/python-marshmallow-union/v0.1.12.svg
    :alt: Commits since latest release
    :target: https://github.com/adamboche/python-marshmallow-union/compare/v0.1.12...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/marshmallow-union.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/pypi/marshmallow-union

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/marshmallow-union.svg
    :alt: Supported versions
    :target: https://pypi.org/pypi/marshmallow-union

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/marshmallow-union.svg
    :alt: Supported implementations
    :target: https://pypi.org/pypi/marshmallow-union


.. end-badges

Union fields for marshmallow.

* Free software: MIT license

Installation
============

::

    pip install marshmallow-union

Documentation
=============


https://python-marshmallow-union.readthedocs.io/


Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
