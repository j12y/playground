#!/usr/bin/env python

try:
    import ez_setup
    ez_setup.use_setuptools()
except ImportError:
    pass

from setuptools import setup
setup(name='RegexPicker plugin',
      version='0.1',
      author='John Doe',
      author_email='john.doe@gmail.com',
      description='Pick test methods based on a regex',
      license='Apache Server License 2.0',
      pymodules=['recipe13_plugin'],
      entry_points = {'nose.plugins': 
                      ['recipe13_plugin = recipe13_plugin:RegexPicker']
                      }
      )
