#!/usr/bin/env python

from distutils.core import setup, find_packages

setup(name='django-simple-menu',
      packages=find_packages(),
      version='1.0.1',
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
      ])
