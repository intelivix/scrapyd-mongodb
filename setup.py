#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='scrapyd-mongodb',
    version='0.1.0',
    description='Scrapyd Queue Management with MongoDB',
    author='Intelivix',
    author_email='arthur@intelivix.com',
    license='MIT',
    url='https://github.com/intelivix/scrapyd-mongodb',
    download_url='https://github.com/intelivix/scrapyd-mongodb/tarball/0.1.0',
    keywords=['scrapy', 'scrapyd', 'mongodb', 'queue',
              'scrapyd-queue', 'scrapyd-backend', 'backend'],
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        'scrapy',
        'pymongo',
    ],
    classifiers=[],
)
