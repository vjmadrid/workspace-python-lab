

# Versión de Python

Hay que decidir que versión de Python utilizar

* Cada minor version tiene soporte de 18 meses de bugfix y 5 años de seguridad

Su instalacíon depende del sistema operativo utilizado 

```bash
$ brew list | grep python

$ brew info python
```





## Ejecutar python


```bash
# Buscar directorio de instalacion 
$ which python

# Ejecutar python
$ python
Python 3.7.4 (default, Aug 13 2019, 15:17:50)
[Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> sys.executable
'/Users/vjmadrid/Workspace/personal/python-lab/venv/bin/python'
```

cat .bash_profile | grep anaconda
cat .bash_profile | grep python
cat .bash_profile | grep PATH

cat .zshrc | grep anaconda
cat .zshrc | grep python
cat .zshrc | grep PATH

echo $PATH


Existen herramientas para gestionar entorno de Python

## pyenv

Gestor de instalaciones de versiones de Python que funciona con Linux

* Instalar versiones de Python
* Administración de versiones de Python
* Reduce los problemas de las dependencias conflictivas
* Util cuando se trabaja con diferentes versiones de Python

https://github.com/pyenv/pyenv

Instalación

```bash
# Instalación con brew
$ brew install pyenv 

# Verificar la versión instalada
$ pyenv --version

# IMPORTANTE : Añadir parametros en .bashrc (.bash_profile en Mac o .zshrc)

# Cargar variable de entorno PYENV_ROOT
$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc

# Cargar variable de entorno PYENV_ROOT en PATH
$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc

# Cargar inicializador
echo 'eval "$(pyenv init -)"' >> ~/.zshrc

# Resetear ~/.zshrc
source ~/.zshrc
```

Uso

```bash
# Verificar al versión de Python utilizada en el sistema
$ python --version

# Verificar versiones gestionadas
$ pyenv versions

# Listar versiones disponibles
$ pyenv install –list

# Instalar Python 3.9.0
$ pyenv install 3.9.0

# Instalar Python 3.9.0 de forma global
$ pyenv global 3.9.0

# Instalar Python 3.9.0 de forma global
$ pyenv local 3.9.0

# Verificar la versión instalada
$ pyenv --version

# Desinstalar una version
$ pyenv uninstall 3.7.7

# Verificar al versión de Python utilizada en el sistema tras la actualización
$ python --version
```

Cada versión de Python es instalada en su propio directorio : $(pyenv root)/version

Mirar el directorio de control generadoo
/Users/vjmadrid/.pyenv/version



# Entorno virtual : "virtualenv"

https://virtualenv.pypa.io/en/stable/

Crear un ambiente con el objetivo de aislar sus recursos : librerías y entornos de ejecución (entorno principal y entornos virutales)

* Facilita tener instaladas otras versiones de una misma librería
* Se puede instalar desde el gestor de paquetes de Linux o mediante el instalador de paquetes de Python

Instalación

```bash
# Instalar dependencia "virtualenv" usando paquete de Python
$ pip install virtualenv
```

Uso

```bash
# Ubicarse dentro del proyecto que se quiera trabajar
cd <PATH_PROJECT>

# Crear un entorno virutal con nombre "venv"
$ virtualenv venv --python=python3

# Verificar que existe el directorio "venv"

# Activar el entorno virtual
$ cd venv
$ source bin/activate

# Verificar la activación el en prompt
(venv)$

# Verificar paquetes disponibles (No debería de mostrar ninguno)
pip freeze

# Instalar paquetes en el entorno virtual
$ pip install <nombre>

# Desativar el entorno virtual
$ deactivate
```

## Integracion con virtualenv

*pyenv-virtualenv* : Plugin de integración que vincula pyenv con virtualenv

https://github.com/pyenv/pyenv-virtualenv

Instalación

```bash
# Instalación
$ git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv

or

$ git clone https://github.com/yyuu/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv

# Cargar inicializador
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc

# Resetear ~/.zshrc
$ source ~/.zshrc
```

Uso

```bash
# Verificar versiones gestionadas
$ pyenv versions

# Crea un entorno virtual para la versión 3.9.0 con nombre venv
$ pyenv virtualenv 3.9.0 venv

# Activar el entorno virtual
$ pyenv activate venv

# Verificar la version de python (Debería de mostrar una ruta como la siguiente : /home/staff/jmoreira/.pyenv/shims/python)
$ which python

# Desactivar
pyenv deactivate
```



# Gestión de Dependencias

```bash
# Verificar paquetes disponibles
$ pip freeze

# Instalar un paquete
$ pip install <name>

# Actualizar un paquete
$ pip install <name> --upgrade
$ pip install <name> -U

# Generar un fichero de dependencias (Conviene actualizarlo)
$ pip freeze > requirements.txt

# Cargar un fichero de dependencias
$ pip install -r requirements.txt
```

## Dependencias de utilidad (opcionales)

*pipreqs* : Generar un fichero requirements.txt basado en los imports de un proyecto

```bash
# Instalación
$ pip install pipreqs

# Uso de pipreqs
$ pipreqs /your_project/path
```

*pipdeptree* : Muestra las dependencias instaladas en forma de arbol

```bash
# Instalación 
pip install pipdeptree

# Uso de pipdeptree
$ pipdeptree
```


## Dependencias básicas del proyecto


# FLAKE8

https://pypi.org/project/flake8/

https://flake8.pycqa.org/en/latest/

Instalación

```bash
# Instalación 
$ pip install flake8
```

Uso

```bash
# ayuda
$ pycodestyle -h

# Uso 
$ pycodestyle xxx.py
```

Define sus condidciones en el fichero : setup.cfg





pip3 install Flask


# FLASK

```bash
# Establecer variable de entorno LINUX / MACOs
export FLASK_APP=helloworld.py

# Establecer variable de entorno Windows
set FLASK_APP=helloworld.py
```

```bash
# Establecer variable de entorno LINUX / MACOs
export FLASK_ENV=development

# Establecer variable de entorno Windows
set FLASK_ENV=development
```


flask run

python -m flask run

python3 helloworld.py


## Problemas con puertos

```bash
# Detectar proceso en Mac que tiene el puerto bloqueado
sudo lsof -i tcp:5000

# Matar lel proceso informado anteriormente
kill -9 <PID>
```

flask run --host=0.0.0.0 --port=80







# Coding Style and automated check

https://www.python.org/dev/peps/pep-0008/

pip install pep8

https://pep8.readthedocs.io

pep8 --ignore=E3 hello.py


tox 

flake 8

# Catch Style Errors -> Errores de codificación reales

* Pyflakes (https://launchpad.net/pyflakes/): Extensible a través de plugins.
*  Pylint (https://pypi.org/project/pylint/): Comprueba la conformidad con PEP 8 mientras
realizando comprobaciones de errores de código por defecto; puede ser ampliado mediante plugins.

Usar 

flake8 (https://pypi.org/ project/flake8/) que combina pyflakes y pep8 en un solo comando. También añade algunas nuevas características de lujo: por ejemplo, puede saltarse las comprobaciones de las líneas que contienen # noqa

pip install flake8-import-order


# Testing

pytest==6.1.1
pytest-cov==2.10.1


pip install virtualenv


set FLASK_APP=app.py


flask run


# Docker

https://www.fullstackpython.com/docker.html