
from setuptools import setup, find_packages
from os import path
# Python 2.7 compat
from io import open

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='smola-test',
    version='0.1.0.dev0',
    description='A sample Python project',
    long_description=long_description, 
    long_description_content_type='text/markdown',
    url='https://github.com/smola/test',
    author='Santiago M. Mola',
    author_email='santi@mola.io',
    classifiers=[  # Optional
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='sample',
    packages=find_packages(exclude=['tests']),
    install_requires=[],
    extras_require={
        'dev': ['zest.releaser'],
    },
    package_data={},
    data_files=[],
    entry_points={},
    project_urls={
        'Bug Reports': 'https://github.com/smola/test/issues',
        'Source': 'https://github.com/smola/test',
    },
)