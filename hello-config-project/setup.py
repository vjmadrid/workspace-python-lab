# from setuptools import setup
from setuptools import setup, find_packages
import os

current_directory = os.path.dirname(os.path.abspath(__file__))


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def read_adv(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname), encoding='utf-8').read()
    except Exception:
        return ''


# *** README ***
# Option 1
try:
    with open(os.path.join(current_directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except Exception:
    long_description = ''

# Option 2
# with open('README.rst') as f:
#    long_description = f.read()

# Option 3
# long_description = read('README.md')
# long_description = read_adv('README.md')

# *** LICENCE **

# with open('LICENSE') as f:
#    license = f.read()

# def get_long_description():
#    descr = []
#    for fname in 'README.rst', 'CHANGES.txt':
#        with open(fname) as f:
#            descr.append(f.read())
#    return '\n\n'.join(descr)

setup(
    # Project name
    name="hello-project",
    # Project version number
    version="0.1",
    # Short description of your library
    description="xxx",
    # Long description of your
    long_description="xxx",
    long_description_content_type='text/markdown',
    # long_description=read('README'),
    # List a license for the project
    license="xxx",
    # Your name
    author="xxx",
    # Your email address
    author_email="xxx",
    # Link to your github repository or website
    url="xxx",
    # Download Link from where the project can be downloaded from
    download_url='',
    # Packages to include in the distribution
    # packages=['src.hello','src.package'],
    # packages=['src','tests'],
    packages=find_packages(exclude=('tests', 'docs')),
    # List project dependencies
    # install_requires=["pytest"],
    # install_requires=["pytest==1.1.0"],
    # install_requires=[i.strip() for i in open("requirements.txt").readlines()],
    #
    # Download dependencies not found in PyPI, you will need to add URLs to a dependency_links section under setup()
    # in the setup.py file. Assuming that the dependencies are packaged correctly, they will be automatically installed
    #
    # dependency_links=['http://github.com/<username>/<reponame>/tarball/master#egg=<packagename>–<version#>']
    # test_suite="tests",

    scripts=[],
    # List project dependencies
    classifiers=[
        "Development Status :: X - Alpha",
        "Topic :: Utilities",
        "License :: XXX"
    ]
)
