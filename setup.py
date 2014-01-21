#!/usr/bin/env python

import re

from setuptools import setup

# load our version from our init file
init_data = open('menu/__init__.py').read()
matches = re.search(r"__version__ = '([^']+)'", init_data, re.M)
if matches:
    version = matches.group(1)
else:
    raise RuntimeError("Unable to load version")

requirements = [
    'setuptools',
    'Django'
]

setup(name='django-simple-menu',
      packages=['menu'],
      include_package_data=True,
      version=version,
      description='Simple, yet powerful, code-based menus for Django applications',
      long_description=open('README.rst').read(),
      author='Evan Borgstrom',
      author_email='evan@fatbox.ca',
      url='https://github.com/fatbox/django-simple-menu',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Natural Language :: English',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      install_requires=requirements)
