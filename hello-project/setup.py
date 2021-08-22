#from setuptools import setup
from setuptools import setup, find_packages

setup(
    name="hello-project",
    version="0.1",
    description="xxx",
    author="xxx",
    author_email="xxx",
    url="xxx",
    #packages=['src.hello','src.package'],
    packages=find_packages(),

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
