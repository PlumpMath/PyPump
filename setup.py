##
#   Copyright (C) 2013 Jessica T. (Tsyesika) <xray7224@googlemail.com>
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program. If not, see <http://www.gnu.org/licenses/>.
##

from sys import version_info

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

install_requires = [
    "requests-oauthlib>=0.3.0",
    "requests>=2.3.0",
    "python-dateutil>=2.1",
]

tests_require = None

if version_info[0] == 2:
    tests_require = [
        "mock",
    ]

setup(
    name="PyPump",
    version="0.7",
    description="Python Pump.io library",
    long_description=open("README.rst").read(),
    author="Jessica Tallon",
    author_email="tfmyz@inboxen.org",
    scripts=['pypump-shell'],
    url="https://github.com/xray7224/PyPump",
    packages=["pypump", "pypump.models"],
    license="GPLv3+",
    install_requires=install_requires,
    tests_require=tests_require,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Operating System :: OS Independent",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X",
        "Intended Audience :: Developers",
        "License :: OSI Approved",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
    ],
    test_suite="tests",
)
