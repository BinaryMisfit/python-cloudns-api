#!/usr/bin/env python3
from setuptools import setup

def readme():
      with open('README.rst') as f:
            return f.read()

setup(name='libcloudns',
      version='0.0.1',
      description='ClouDNS HTTP API Library',
      long_description=readme(),
      classifiers=[
          'Development Status:: 2 - Pre-Alpha',
          'License :: OSI Approved :: GPLv3 ',
          'Programming Language :: Python :: 3.8',
          'Topic :: Software Development :: Libraries :: Python Modules'
      ],
      keywords='cloudns http api library',
      url='https://github.com/binarymisfit/python-cloudns-api',
      author='BinaryMisfit',
      author_email="binarymisfit@digitalmisfit.net",
      license='GPLv3',
      packages=['libcloudns'],
      include_package_data=True,
      zip_safe=False)