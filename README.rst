ansible-testing
===============

Python module to help test or validate Ansible, specifically ansible
modules

Installation
------------

This module must be installed alongside the current development
release of Ansible to appropriately test the current development
state of modules.

Usage
~~~~~

::

    pip install git+https://github.com/ansible/ansible.git@devel#egg=ansible
    pip install git+https://github.com/sivel/ansible-testing.git#egg=ansible_testing
    ansible-validate-modules /path/to/ansible-modules-extras

Help
~~~~

::

    usage: ansible-validate-modules [-h] [-w] [--exclude EXCLUDE] modules

    positional arguments:
      modules            Path to module or module directory

    optional arguments:
      -h, --help         show this help message and exit
      -w, --warnings     Show warnings
      --exclude EXCLUDE  RegEx exclusion pattern

Current Validations
-------------------

Modules
~~~~~~~

Errors
^^^^^^

#. Interpreter line is not ``#!/usr/bin/python``
#. ``main()`` not at the bottom of the file
#. Module does not include ``from ansible.module_utils.basic import *``
#. ``module_utils`` imports at the top (excluding whitelisted
   ``module_utils``)
#. Invalid ``module_utils`` import
#. Missing ``DOCUMENTATION`` or invalid YAML
#. Missing ``EXAMPLES``
#. Invalid Python Syntax
#. Tabbed indentation
#. Use of ``sys.exit()`` instead of ``exit_json`` or ``fail_json``
#. Missing GPLv3 license header in module
#. Powershell module missing ``WANT_JSON``
#. Powershell module missing ``REPLACER_WINDOWS``
#. New modules have the correct ``version_added``
#. Modules should not import requests, instead use ``ansible.module_utils.urls``
#. Missing ``RETURN`` for new modules

Warnings
^^^^^^^^

#. Whitelisted ``module_utils`` imports at the top
#. Try/Except ``HAS_`` expression missing
#. Missing ``RETURN`` for existing modules
#. ``import json`` found
#. Module contains duplicate globals from basic.py

Notes
^^^^^

#. ``module_utils`` imports not at bottom may be error or warning
   depending on the import.

Module Directories (Python Packages)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Missing ``__init__.py``

