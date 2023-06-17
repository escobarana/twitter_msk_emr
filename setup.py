#!/usr/bin/env python
from pathlib import Path

from setuptools import find_packages, setup

setup(
    name="Real-time Twitter Analytics for Eurovision 2023",
    version="1.0.0",
    description='This project is to analyse the tweets in real-time during the Eurovision 2023 contest.',
    long_description=(Path(__file__).parent / "README.md").read_text(),
    long_description_content_type="text/markdown",
    author="Ana Escobar",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords="Amazon MSK, Amazon EMR, Apache Kafka and spark structured streaming",
    packages=find_packages(include=["pyspark_scripts"]),
    python_requires=">=3.5, <4",
)
