Welcome to python-first-project's documentation!
================================================

``python-first-project`` is a professional Python project template that demonstrates best practices
in Python development, testing, and project organization.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   usage
   api/modules
   development

Getting Started
---------------

To get started with ``python-first-project``, first install it using pip:

.. code-block:: bash

   pip install python-first-project

Quick Example
-------------

Here's a quick example of using the financial calculations module:

.. code-block:: python

   from python_first_project.financial import calculate_total

   numbers = [100, 200, 300]
   total = calculate_total(numbers, multiplier=1.1)
   print(f"Total with 10% markup: {total}")

Features
--------

- Professional project structure following Python best practices
- Comprehensive test suite with high coverage
- Automated code quality checks
- Clear documentation
- CI/CD pipeline integration

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
