# hello-project

./sample/ : code module
LICENSE : Lawyering up
Setup.py : Package and distribution management
requirements.txt : Development dependencies.
./docs/ : Package reference documentation
./test/ : Package reference documentation
./Makefile : Generic management tasks



python setup.py sdist

pip install hello-project-0.1.tar.gz

pip uninstall paquete

python setup.py test

python setup.py develop

Una vez tenemos toda la información configurada, podemos probar nuestro paquete fácilmente realizando una instalación en modo desarrollo. Para ello utilizaríamos el siguiente comando:

python setup.py develop

Este modo es muy práctico, ya que nos permite utilizar nuestro módulo en cualquier lugar y hacer modificacione sin necesidad de reinstalarlo constamente. Eso es posible porque se utiliza desde el propio directorio.

Una vez hayamos hecho las probaturas y estemos satisfechos, podemos desinstalar el paquete de desarrollo:

python setup.py develop --uninstall

Para instalar el paquete definitivo utilizaríamos: 

python setup.py develop --uninstall

Para instalar el paquete definitivo utilizaríamos: 

python setup.py install

## Distribuir un package localmente

Generando un fichero comprimido que podemos compartir con nuestros conocidos.

## Distribuir un package Públicamente 

En el repositorio PyPI para que todo el mundo pueda utilizarlo.