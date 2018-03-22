from setuptools import *
__author__ = 'victor'

setup(
    name = 'spikesorting_cmdline',
    version = '0.1',
    author = 'Victor Benichoux',
    author_email = 'victor.benichoux@gmail',
    packages = ['spikesorting_cmdlinetools',
                "spikesorting_cmdlinetools.utils"],
    entry_points = {
        'console_scripts' : ['sorting-manager=spikesorting_cmdlinetools.sorting_manager:main',
                             'lsmat=spikesorting_cmdlinetools.utils.lsmat:main',
                             'sorting-manager-putback=spikesorting_cmdlinetools.put_back_in_matfiles:main',
                             'update_prmfiles=spikesorting_cmdlinetools.utils.update_prmfiles:main']
    },
    package_data={
        'spikesorting_cmdlinetools': ['probe files/*.prb']
    }

)