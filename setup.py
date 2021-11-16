#!/usr/bin/env python3

from os.path import join, abspath, dirname
from setuptools import setup

with open(join(dirname(abspath(__file__)), 'requirements.txt')) as f:
    requirements = f.readlines()

PLUGIN_ENTRY_POINT = 'nlp_stt_plugin = mycroft_nlp_stt_plugins:nlpSTTPlugin'
setup(
    name='mycroft-nlp-stt-plugins',
    version='0.1',
    description='NLU stt plugin for mycroft',
    url='https://github.com/Songtorn/mycroft_stt_plugins_nlp.git',
    author='Songtorn',
    author_email='punn.sk137@gmail.com',
    license='Apache-2.0',
    packages=['mycroft_nlp_stt_plugins'],
    install_requires=requirements,
    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Linguistic',
        'License :: OSI Approved :: Apache Software License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='mycroft plugin stt',
    entry_points={'mycroft.plugin.stt': PLUGIN_ENTRY_POINT}
)