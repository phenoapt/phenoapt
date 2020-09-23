#!/usr/bin/env python

"""The setup script."""

#  Copyright (c) 2018-2020 Beijing Ekitech Co., Ltd.
#  All rights reserved.

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', 'requests', 'tabulate']

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest>=3', ]

setup(
    author="PhenoApt Team",
    author_email='phenoapt@ekitech.cn',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="PhenoApt python client API library",
    entry_points={
        'console_scripts': [
            'phenoapt=phenoapt.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='phenoapt',
    name='phenoapt',
    packages=find_packages(include=['phenoapt', 'phenoapt.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/phenoapt/phenoapt',
    version='0.1.4',
    zip_safe=False,
)
