#!/usr/bin/env python
from setuptools import setup

setup(
    name="django-simple-menu",
    packages=["menu"],
    include_package_data=True,
    use_scm_version={"version_scheme": "post-release"},
    setup_requires=["setuptools_scm"],
    description="Simple, yet powerful, code-based menus for Django applications",
    long_description=open("README.rst").read(),
    author="Evan Borgstrom",
    author_email="evan@borgstrom.ca",
    url="https://github.com/jazzband/django-simple-menu",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Django",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 3.1",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    install_requires=["Django>=2.2"],
    python_requires=">=3.6",
)
