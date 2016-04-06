#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 Matt Martz <matt@sivel.net>
# Copyright (C) 2015 Rackspace US, Inc.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import re
import codecs

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))


# Read the version number from a source file.
# Why read it, and not import?
# see https://groups.google.com/d/topic/pypa-dev/0PkjVpcxTzQ/discussion
def find_version(*file_paths):
    # Open in Latin-1 so that we avoid encoding errors.
    # Use codecs.open for Python 2 compatibility
    try:
        f = codecs.open(os.path.join(here, *file_paths), 'r', 'latin1')
        version_file = f.read()
        f.close()
    except:
        raise RuntimeError("Unable to find version string.")

    # The version line must have the form
    # __version__ = 'ver'
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


# Get the long description from the relevant file
try:
    f = codecs.open('README.rst', encoding='utf-8')
    long_description = f.read()
    f.close()
except:
    long_description = ''


setup(
    name='ansible-testing',
    version=find_version('ansible_testing/__init__.py'),
    description=('Python module to help test or validate Ansible, '
                 'specifically ansible modules'),
    long_description=long_description,
    keywords='ansible',
    author='Matt Martz',
    author_email='matt@sivel.net',
    url='https://github.com/sivel/ansible-testing',
    license='GPLv3',
    packages=find_packages(exclude=['tests', 'tests.*']),
    install_requires=[
        'ansible',
        'voluptuous==0.8.8',
    ],
    entry_points={
        'console_scripts': [
            'ansible-validate-modules=ansible_testing.modules:main',
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Environment :: Console',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Topic :: Utilities',
        'Topic :: Software Development :: Testing',
        ('License :: OSI Approved :: GNU General Public License v3 or '
         'later (GPLv3+)'),
    ]
)
