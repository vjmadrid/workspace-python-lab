#from setuptools import setup
from setuptools import setup, find_packages


#with open('README.rst') as f:
#    readme = f.read()

#with open('LICENSE') as f:
#    license = f.read()

#def get_long_description():
#    descr = []
#    for fname in 'README.rst', 'CHANGES.txt':
#        with open(fname) as f:
#            descr.append(f.read())
#    return '\n\n'.join(descr)

setup(
    name="hello-project",
    version="0.1",
    description="xxx",
    long_description="xxx",
    author="xxx",
    author_email="xxx",
    license="xxx",
    url="xxx",
    #packages=['src.hello','src.package'],
    packages=find_packages(exclude=('tests', 'docs')),

    #install_requires=["pytest"],
    # install_requires=["pytest==1.1.0"],
    #install_requires=[i.strip() for i in open("requirements.txt").readlines()],

    #test_suite="tests",

    scripts=[],

    classifiers=[
        "Development Status :: X - Alpha",
        "Topic :: Utilities",
        "License :: XXX"
    ]
)
