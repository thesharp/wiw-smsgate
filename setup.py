#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="wiw-smsgate",
    version="0.2",
    scripts=["wiw-smsgate"],
    data_files=[("etc", ["wiw-smsgate.conf"])],
    # install_requires=[""],
    author="Ilya A. Otyutskiy",
    author_email="sharp@thesharp.ru",
    maintainer="Ilya A. Otyutskiy",
    url="https://github.com/thesharp/wiw-smsgate",
    description="wiw-smsgate",
    license="MIT"
)
