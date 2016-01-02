#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    'docopt >= 0.6',
    'netaddr >= 0.7',
    'prettytable >= 0.7',
    'requests >= 2.9',
]

test_requirements = [
    'coverage',
    'flake8',
    'nose',
]

setup(
    name='ilo-utils',
    version='0.1.1',
    description='ILO Utils',
    long_description=readme + '\n\n' + history,
    author='Jonathan Stacks',
    author_email='jonstacks13@gmail.com',
    url='https://github.com/jonstacks13/ilo-utils',
    entry_points={
        'console_scripts': [
            'ilo-sweep = ilo_utils.sweep:main',
        ]
    },
    packages=find_packages(),
    install_requires=requirements,
    tests_require=test_requirements,
    test_suite='nose.collector',
    license='BSD',
    zip_safe=False,
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',

    ],
    keywords=[
        'ilo',
        'utils', 
    ],
)