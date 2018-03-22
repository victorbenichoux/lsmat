from setuptools import *
__author__ = 'victorbenichoux'

setup(
    name = 'lsmat',
    version = '0.1',
    author = 'Victor Benichoux',
    author_email = 'victor.benichoux@gmail',
    packages = ['lsmat'],
    entry_points = dict(console_scripts = ['lsmat=lsmat.lsmat:main']),
    package_data=dict()
)
