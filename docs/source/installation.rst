Installation Guide
==================

Requirements
------------

- Python 3.12 or higher
- pip (Python package installer)

Basic Installation
------------------

You can install ``python-first-project`` using pip:

.. code-block:: bash

   pip install python-first-project

Development Installation
------------------------

For development, you should clone the repository and install in editable mode with development dependencies:

.. code-block:: bash

   git clone https://github.com/jcherranz/python-first-project.git
   cd python-first-project
   python -m venv .venv
   .\.venv\Scripts\activate  # On Windows
   pip install -e ".[dev]"

This will install all development dependencies including:

- pytest and pytest-cov for testing
- black for code formatting
- isort for import sorting
- pylint for code analysis
- pre-commit for automated checks
- Sphinx for documentation

Setting up Pre-commit Hooks
---------------------------

After installation, set up pre-commit hooks:

.. code-block:: bash

   pre-commit install

This will ensure code quality checks run automatically before each commit.
