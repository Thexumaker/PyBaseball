from setuptools import setup

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="pybaseball",
    version="0.0.1",
    author="David Xu",
    author_email="thexumaker@berkeley.edu",
    description="Python baseball",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Thexumaker/PyBaseball/tree/master/pybaseball",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
