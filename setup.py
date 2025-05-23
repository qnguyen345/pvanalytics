#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
except ImportError:
    raise RuntimeError('setuptools is required')

DESCRIPTION = ('PVAnalytics is a python library for the analysis of ' +
               'photovoltaic system-level data.')

LONG_DESCRIPTION = """
PVAnalytics is a collection of functions for working with data
from photovoltaic power systems. The library includes functions for
general data quality tests such as outlier detection, validation that
data is physically plausible, filtering data for specific conditions,
and labeling specific features in the data.

Documentation: https://pvanalytics.readthedocs.io

Source code: https://github.com/pvlib/pvanalytics
"""

DISTNAME = 'pvanalytics'
AUTHOR = 'pvanalytics Contributors'
MAINTAINER_EMAIL = 'pvlib-admin@googlegroups.com'
LICENSE = 'MIT'
URL = 'https://github.com/pvlib/pvanalytics'

TESTS_REQUIRE = [
    'pytest',
    'pytest-cov',
    'packaging',
]

INSTALL_REQUIRES = [
    'numpy >= 1.20.0',
    'pandas >= 1.3.0',
    'pvlib >= 0.9.4',
    'scipy >= 1.6.0',
    'statsmodels >= 0.13.0',
    'scikit-image >= 0.18.0',
    'importlib-metadata; python_version < "3.8"',
]

DOCS_REQUIRE = [
    'sphinx == 4.5.0',
    'pydata-sphinx-theme == 0.8.1',
    'sphinx-gallery',
    'matplotlib',
    'pyarrow'
]

EXTRAS_REQUIRE = {
    'optional': ['ruptures'],
    'test': TESTS_REQUIRE,
    'doc': DOCS_REQUIRE
}

EXTRAS_REQUIRE['all'] = sorted(set(sum(EXTRAS_REQUIRE.values(), [])))

SETUP_REQUIRES = ['setuptools_scm']

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Operating System :: OS Independent',
    'Intended Audience :: Science/Research',
    'Programming Language :: Python :: 3',
    'Topic :: Scientific/Engineering'
]

PACKAGES = find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"])

setup(
    name=DISTNAME,
    use_scm_version=True,
    packages=PACKAGES,
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    tests_require=TESTS_REQUIRE,
    setup_requires=SETUP_REQUIRES,
    ext_modules=[],
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author=AUTHOR,
    maintainer_email=MAINTAINER_EMAIL,
    license=LICENSE,
    classifiers=CLASSIFIERS,
    url=URL,
    include_package_data=True,
)
