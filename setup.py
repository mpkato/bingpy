# -*- coding:utf-8 -*-
from setuptools import setup

setup(
    name = "bingpy",
    packages = ["bingpy"],
    version = "0.0.1",
    description = "Bing Search APIs (V5)",
    author = "Makoto P. Kato",
    author_email = "kato@dl.kuis.kyoto-u.ac.jp",
    license     = "MIT License",
    url = "https://github.com/mpkato/bingpy",
    install_requires = [
        "requests",
    ],
    tests_require=['pytest'],
)
