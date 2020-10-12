# Seleccionar la Versión de Python

Hay que decidir que versión de Python utilizar

* Cada minor version tiene soporte de 18 meses de bugfix y 5 años de seguridad

Su instalacíon depende del sistema operativo utilizado 

```bash
$ brew list | grep python

$ brew info python
```

Existen herramientas para gestionar los entorno de Python





## Pruebas de ejecución de Python

```bash
# Verificar al versión de Python utilizada en el sistema
$ python --version

o

$ python --V


# Localizar directorio de instalacion 
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





## PYENV

https://github.com/pyenv/pyenv

Gestor de instalaciones de versiones de Python que funciona con Linux

* Instalar versiones de Python
* Administración de versiones de Python
* Reduce los problemas de las dependencias conflictivas
* Util cuando se trabaja con diferentes versiones de Python
* Dispone de plugins que añaden funcionalidad pyenv-virtualenv, pyenv-doctor, etc.
* ...

Existe pyenv en Windows
https://github.com/pyenv-win/pyenv-win


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

# Instalacion de dependencias asociadas
brew install openssl readline sqlite3 xz zlib
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

```bash
# Listar versiones instaladas para el usuario
$ ls ~/.pyenv/versions/

# Borrar versión 
pyenv uninstall X.Y.Z

rm -rf ~/.pyenv/versions/X.Y.Z
```





## Integracion con pyenv-doctor

*pyenv-doctor* : Plugin que permite ver la correccion de la instalacion de un entorno

https://github.com/pyenv/pyenv-virtualenv

Instalación

```bash
# Instalación
$ git clone git://github.com/pyenv/pyenv-doctor.git $(pyenv root)/plugins/pyenv-doctor

o

$ git clone https://github.com/yyuu/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-doctor

# Cargar inicializador
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc

# Resetear ~/.zshrc
$ source ~/.zshrc
```

Uso

```bash
# Ejecutar
$ pyenv doctor
```
