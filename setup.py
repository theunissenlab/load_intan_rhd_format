#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
import os

long_description = open("README.md").read()

setup(
    name = "intanutil",
    version = '0.1',
    packages = ['intanutil'],
    install_requires=[],
    extras_require={},
    author = "",
    author_email = "",
    description = "Load Intan RHD file",
    long_description = long_description,
    classifiers=[]
)
