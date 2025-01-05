Development Guide
=================

This guide covers development practices for contributing to python-first-project.

Development Environment
-----------------------

1. Clone the repository:

   .. code-block:: bash

      git clone https://github.com/jcherranz/python-first-project.git
      cd python-first-project

2. Create and activate a virtual environment:

   .. code-block:: bash

      python -m venv .venv
      .\.venv\Scripts\activate  # On Windows
      source .venv/bin/activate # On Unix/MacOS

3. Install development dependencies:

   .. code-block:: bash

      pip install -e ".[dev]"

4. Install pre-commit hooks:

   .. code-block:: bash

      pre-commit install

Code Quality Tools
------------------

We use several tools to maintain code quality:

- **black**: Code formatting with 88-character line length
- **isort**: Import sorting configured to work with black
- **pylint**: Code analysis with customized rules
- **pre-commit**: Automated checks before commits
- **pytest**: Testing framework with coverage reports

Running Tests
-------------

Run the test suite with coverage:

.. code-block:: bash

   pytest --cov=src/python_first_project

Documentation
-------------

Build documentation locally:

.. code-block:: bash

   cd docs
   make html       # On Unix/MacOS
   .\make.bat html # On Windows

View the built documentation by opening ``docs/build/html/index.html`` in your browser.

Development Workflow
--------------------

1. Create a new branch for your feature:

   .. code-block:: bash

      git checkout -b feature/your-feature-name

2. Make your changes, following our coding standards

3. Run tests and checks:

   .. code-block:: bash

      pytest
      pre-commit run --all-files

4. Commit your changes using Conventional Commits:

   .. code-block:: bash

      git add .
      git commit -m "feat: your feature description"

Version Control
---------------

We follow the `Conventional Commits <https://www.conventionalcommits.org/>`_ specification:

- ``feat``: New feature
- ``fix``: Bug fix
- ``docs``: Documentation only
- ``style``: Code style changes
- ``refactor``: Code refactoring
- ``test``: Adding tests
- ``chore``: Maintenance tasks

Release Process
---------------

1. Update version in ``pyproject.toml``
2. Update CHANGELOG.md
3. Create a new release on GitHub
4. Publish to PyPI

Testing Standards
-----------------

1. Write tests for all new features
2. Maintain >95% code coverage
3. Test both success and error cases
4. Use meaningful test names
5. Group related tests in classes
