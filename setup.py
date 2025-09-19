"""
Create wheel for dom_locator

Use: python setup.py bdist_wheel
"""

from setuptools import setup

_ = setup(
    name="dom-locator",
    version="0.0.1",
    packages=["dom_locator"],
    url="https://github.com/VBenevides/dom-locator",
    license="MIT",
    author="Vinicius Benevides",
    author_email="viniciusm.benevides@gmail.com",
    description="Library for interacting with XML and HTML DOM ",
    install_requires=["lxml"],
)
