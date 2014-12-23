from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
	name='ckanext-fgp',
	version=version,
	description="CKAN Extension for the Canadian Federal Geospatial Project",
	long_description="""\
	""",
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='',
	author='Ross Thompson - Statistics Canada',
	author_email='ross.thompson@statcan.gc.ca',
	url='http://open.canada.ca',
	license='MIT',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	namespace_packages=['ckanext', 'ckanext.fgp'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		# -*- Extra requirements: -*-
	],
	entry_points=\
	"""
    [ckan.plugins]
	canada_fgp=ckanext.fgp.plugin:FgpPlugin
	""",
)
