# Crear un Entorno Virtual

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

# Brew
$ brew install pyenv-virtualenv

# Cargar inicializador
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc

if which pyenv-virtualenv-init > /dev/null; then 
 eval “$(pyenv virtualenv-init -)”;
fi

# Resetear ~/.zshrc
$ source ~/.zshrc
```

Uso

```bash
# Verificar versiones gestionadas
$ pyenv versions

# Crea un entorno virtual para la versión 3.9.0 con nombre venv
$ pyenv virtualenv 3.9.0 venv

# Crea un entorno virtual para la versión 3.9.0 con nombre venv
$ pyenv virtualenv 3.9.0 venv3.9.0

# Activar el entorno virtual
$ pyenv activate venv

$ pyenv activate venv3.9.0

# Verificar virtualenvs
$ pyenv virtualenvs

# Verificar la version de python (Debería de mostrar una ruta como la siguiente : /home/staff/xxxx/.pyenv/shims/python)
$ which python

# Desactivar
pyenv deactivate
```
