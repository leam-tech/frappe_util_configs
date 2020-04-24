# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in frappe_util_configs/__init__.py
from frappe_util_configs import __version__ as version

setup(
	name='frappe_util_configs',
	version=version,
	description='Useful frappe features for your random purposes',
	author='Leam Technology Systems',
	author_email='info@leam.ae',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
