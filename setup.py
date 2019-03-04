import os

from setuptools import setup


LICENSE = 'MIT'
AUTHOR = "HerveMignot"
EMAIL = "HerveMignot@github.com"
URL = "http://github.com/HerveMignot/AzureBlobIO"
CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'Intended Audience :: Education',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Topic :: Scientific/Engineering',
]


# Get the long description from the README file
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='azureblobio',
      version='0.1.0',
      description='Azure ByteIO wrapper for reading files from Blob Storage',
      long_description=long_description,
      long_description_content_type='text/markdown',
      keywords='Azure Blob files Python',
      url=URL,
      author=AUTHOR,
      author_email=EMAIL,
      license=LICENSE,
      packages=['azureblobio'],
      classifiers=CLASSIFIERS,
      install_requires=[
          'io',
          'azure.storage',
          ],
      include_package_date=False,
      zip_safe=False
      )
