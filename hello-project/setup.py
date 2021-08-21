import io
import os.path
from setuptools import setup, find_packages

VERSION_PATH = os.path.join(
    os.path.dirname(__file__), 'package/version.txt')

with io.open(VERSION_PATH, 'r', encoding='utf-8') as f:
    version = f.read().strip()

setup(
    name='hello-project',
    #version='1.0',
    version = version,
    description='Hello World Enterprise Edition',
    packages=['src/package'],
    #packages=find_packages(where='src'),
    #package_dir={'':'src'},
    package_data = {"src/package": ["version.txt"]},

    dependency_links = [],
    install_requires=[],
    extras_require={},

    
    author='vjmadrid',
    author_email='vjmadrid@atsistemas.com',
    license = "Apache 2.0",
    keywords=['hello','world'],
    scripts=['bin/make-hello'],

    entry_points = {
        "console_scripts": [      
            "helloworld_in_python = package.hello:hello",
        ],
        "gui_scripts": []
    }
)
