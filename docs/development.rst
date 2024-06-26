.. highlight:: shell
.. index:: Development
.. _Development:

===========
Development
===========


For local development you need to install Node v18.x, Python3, and Git.

It is strongly recommended to use a Python virtual environment.

The build process derives the version from repository data, so it's necessary
to clone the repository and not just download a single snapshot.

Mac or Linux
============

You should have ``make`` installed. 

If the first command below produces an error, you can follow the steps below in the Windows section.

Start with running the ``make`` command in the terminal. 
This will show all the tasks that are available using that ``make`` command.

.. code-block:: shell

   # show all available tasks
   make

Follow the steps highlighted in your terminal.
These steps will ensure that you have installed the requirements and fulfilled Python and Node demands.

.. code-block:: text

   make setup

When doing frontend development compile your changes at any time

.. code-block:: text

   make frontend

Build and install the package

.. code-block:: text

   make install

Build and install the package for development

.. code-block:: text

   make install-for-development

Don't forget to update the docs. Render the documentation

.. code-block:: text

   make docs

Serve build docs locally

.. code-block:: text

   make serve

Check the Python code. The CI workflow requires ``lint-minimal`` to succeed

.. code-block:: shell

   # for local use
   make lint

   # used in the workflow
   make lint-minimal

Run Python unit tests

.. code-block:: text

   make test

Rebuild and install from Python wheel package

.. code-block:: shell

   make install

   # then verify the module can be imported and used
   make test-import


To find out whether the created wheel package passes the `twine check` test and
can be uploaded to PyPi run

.. code-block:: text

   make build test


.. _venv: https://docs.python.org/3/library/venv.html


Windows, or systems without ``make`` installed
==============================================

Windows does not have ``make`` therefore we must run the commands directly
rather than using the shortcuts in the Makefile. Assume the commands below are
all run in PowerShell. These instructions will also work on Mac or Linux without
make installed as well.

First, be sure to install Python 3, and Node 18.
`fnm <https://github.com/Schniz/fnm>`_ is really useful for
managing multiple versions of Node on Windows.

Make a Python virtual environment. Let's make it in a folder called ``.venv``
which will be ignored by git.

.. code-block:: shell

   # Create the venv
   python -m venv ./.venv/

   # Activate it (PowerShell)
   ./.venv/Scripts/Activate.ps1

   # Install dependencies
   pip install -r requirements-dev.txt

Install the the NPM dependencies:

.. code-block:: text

   npm install

Now, build the frontend (this compiles the CSS and JavaScript). Re-run this
whenever you edit ``.scss`` or ``.js`` files.

.. code-block:: text

   npm run frontend

To test out the sphinx theme, build the project's own documentation using the
theme! The command below tells Sphinx to build the ``./docs/`` folder as HTML,
and put the output HTML files in ``./docs/_build/``.

.. code-block:: text

   sphinx-build -M html ./docs/ ./docs/_build/

If you see any red errors in the console, that would most likely be related to
a syntax error in a ``.rst`` or ``.md`` file in the ``./docs/`` folder.

To browse the docs you just built, fire up a simple web server using Python:

.. code-block:: text

   python -m http.server -d ./docs/_build/html/

Now go to http://localhost:8000/ in your browser.

If you make any changes to the Python code, you'll want to run the linters to
check for errors:

.. code-block:: text

   flake8 .


Example Pages
=============

When working on the theme it is often going to be helpful to know the impact of your changes.
The :doc:`examples section <examples/index>` should be helpful for this.

When you are adding new elements or styles that are not part of the examples, please make sure to add them.


Javascript package management
=============================

Use ``npm`` for package management.
