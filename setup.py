#!/usr/bin/env python
import codecs
import os
import re
import sys
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

def find_packages():
    """adapted from IPython's setupbase.find_packages()"""
    packages = []
    for dir, subdirs, files in os.walk('src'):
        package = dir.replace(os.path.sep, '.')
        if '__init__.py' not in files:
            # not a package
            continue
        if sys.version_info < (3, 3) and 'asyncio' in package and 'sdist' not in sys.argv:
            # Don't install asyncio packages on old Python
            # avoids issues with tools like compileall, pytest, etc.
            # that get confused by presence of Python 3-only sources,
            # even when they are never imported.
            continue
        packages.append(package)
    return packages

def read(*parts):
    with codecs.open(os.path.join(here, *parts), 'r') as fp:
        return fp.read()

def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


def install_requires():
    return ['requests', 'coincurve>=7.0.0', 'pycryptodome>=3.5.1,<4', 'aiohttp>=2.3.0', 'web3']


setup(
    name='@bradennapier/idex-sdk-python',
    version=find_version("src", "__init__.py"),
    packages=find_packages(),
    description='API Wrapper for the IDEX v2 API',
    long_description=read('README.rst'),
    url='https://github.com/bradennapier/idex-sdk-python',
    author='Braden Napier',
    license='MIT',
    author_email='',
    install_requires=install_requires(),
    keywords='ethereum api idex rest websocket cryptocurrency',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python'
    ],
)
