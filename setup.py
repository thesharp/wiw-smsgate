#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="wiw-smsgate",
    version="1.0",
    scripts=["wiw-smsgate"],
    py_modules=["smsgate"],
    data_files=[("etc", ["wiw-smsgate.conf"])],
    # install_requires=[""],
    author="Ilya Otyutskiy",
    author_email="ilya.otyutskiy@icloud.com",
    maintainer="Ilya Otyutskiy",
    url="https://github.com/thesharp/wiw-smsgate",
    description="wiw-smsgate",
    license="MIT"
)
