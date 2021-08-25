# hello-project

This project represents a basic Hello World (Greeting) in python

This project stands out for:

* Diferentes examples : modules, class
* Use Modules -> import





## Technological Stack

* [Python](https://www.python.org/)

Dependencies with architecture projects

* N/A

Third Party Dependencies


* **pycodestyle** [2.7.2] : Framework for checking Python style guide -> [Pypi](https://pypi.org/project/pycodestyle/) [Documentation](https://www.python.org/dev/peps/pep-0008/)
* **autopep8** [1.5.7] : Framework for formats Python code to conform to the PEP 8 style guide -> [Pypi](https://pypi.org/project/autopep8/)
* **yapf** [0.31.0] : Framework for formats Python code with ‘clang-format’, -> [Pypi](https://pypi.org/project/yapf/)
* **black** [21.7b0] : Framework for formats Python code with ‘clang-format’, -> [Pypi](https://pypi.org/project/yapf/)

* **pre-commit** [2.14.0] : Framework for managing and maintaining multi-language pre-commit hooks -> [Pypi](https://pypi.org/project/pre-commit/) [Documentation](https://pre-commit.com/)

* **XXX** [X.Y] : XXX -> [Pypi](XXX) [Documentation](XXX)


pycodestyle file.py
autopep8 --in-place optparse.py


## Prerequisites

Define what elements are needed to install the software

* Python installed (3.9.x+ version required)
* Pip installed  (20.0.x+ version required

This was made on `python 3.9.6` and `pip3 20.0.2`





## Configuration instructions




## Installation instructions

### UNIX (MacOS or Linux)

1. Choose `Use this as template` on [the repo website](xxx).
2. Run `source setup.sh` to set the repo up to be done.

### Windows

N/A





## Operating instructions

### Generic 

There are different folders and files

- **sample/:** Package reference to the code module
- **src/:** Package reference to the other code modules
- **tests/:** Package reference to the tests
- **docs/:** Package reference testing
- **dist/:** (Optional) Package reference to the distribution
- **res/:** (Optional) Package reference to the resources such as images, data files etc.


- **README.md :** Project documentation file
- **MANIFEST.in :** Project documentation file
- **LICENSE :** Lawyering up file
- **Makefile :** Generic management tasks file
- **requirements.txt :** Development dependencies file
- **Setup.py :** Package and distribution management1




## Use


### Use virtualenv when developing

The service will accept HTTP GET requests at :

```bash
http://localhost:8091/greeting
```


**virtualenv** is a tool to create isolated python environments

Steps to follow

* Start a terminal
* Install virutalenv

```bash
pip install virtualenv
```

* To be located in the PATH of installation (the place where the project is located)
* Create virtual environment

```bash
virtualenv venv-hello-project
```

* Activate virtual environment

```bash
source venv-hello-project/bin/activate
```

Note that ``venv*/`` is ignored via ``.gitignore``.

* Install requirements

```bash
pip install -r dev-requirements.txt
```






## A file manifest (list of files included)

```
# Put code
```

Generated using `tree` (install it using `brew install tree`). To generate your own for you own project, use

``tree -a -I '*.pyc|__pycache__|.git|.pytest_cache' YOUR-REPO-NAME/``



## Copyright and licensing information

```
MIT License

Copyright (c) [year] [fullname]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```



## Contact information for the distributor or programmer

Víctor Madrid



## Known bugs[3]





## Troubleshooting[3]





## Credits and acknowledgments

- MIT license is fetched from [this site](https://choosealicense.com/licenses/mit/). Information retrieved 21/8/2021





## A changelog (usually for programmers)





## A news section (usually for users)






### Coming soon

- Idea1
- Idea2

