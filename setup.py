from os import environ as env
from setuptools import find_packages, setup
from setuptools.command.install import install
import sys

VERSION = '0.2.2'

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()


class VerifyVersionCommand(install):
    """Custom command to verify that the git tag matches our version"""
    description = "verify that the git matches this version"

    def run(self):
        tag = env.get("ACTIVEJSON_TAG")
        if tag != VERSION:
            info = f"Git tag: {tag} doesn't match this version {VERSION}"
            sys.exit(info)


setup(
    name='activejson',
    version=VERSION,
    description='A convenient library to deal with large json data',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Daniel Omar Vergara Pérez',
    author_email='daniel.omar.vergara@gmail.com',
    url='https://github.com/dany2691/activejson',
    packages=find_packages(exclude=('tests',)),
    install_requires=[],
    license='MIT',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    cmdclass={"verify": VerifyVersionCommand}
)
