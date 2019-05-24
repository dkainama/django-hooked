#!/usr/bin/env python

import os

from setuptools import setup


def get_packages(package):
    return [
        dirpath
        for dirpath, dirnames, filenames in os.walk(package)
        if os.path.exists(os.path.join(dirpath, '__init__.py'))
    ]


setup(
    name='django-hooked',
    version='0.2.1',
    packages=get_packages('hooked'),
    license='MIT',
    author='Donald Kainama',
    description='WebHooks for Django and Django Rest Framework.',
    author_email='dkainama@jouwomgeving.nl',
    long_description='Receive signed and secure webhooks in Django',
    install_requires=[],
    include_package_data=True,
    url='https://github.com/dkainama/django-hooked',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
