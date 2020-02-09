OdooChain Install
----

anaconda

```
conda create -n py37 python=3.7.2

source activate py37

pip install -r requirements.txt

pip install cython (to install python-imap)

pip install phonenumbers
(if python3.7) pip install psycopg2-binary

-r odoochain -w *** --addons-path=addons,odoo/addons

PYTHONUNBUFFERED=1;PYDEVD_USE_FRAME_EVAL=NO;TZ=UTC

```

Odoo is a suite of web based open source business apps.

The main Odoo Apps include an <a href="https://www.odoo.com/page/crm">Open Source CRM</a>,


Odoo Apps can be used as stand-alone applications, but they also integrate seamlessly so you get
a full-featured <a href="https://www.odoo.com">Open Source ERP</a> when you install several Apps.


Getting started with install Odoo in python3.7 and windows
-------------------------

follow <a href="http://initd.org/psycopg/docs/install.html#prerequisites">how to install psycopg2 in windows and python3.7</a>

Problems

1. pip install Pillow  not conda install Pillow

Please see <a href="https://www.jianshu.com/p/e0743c35480e"> how to solve "Using the database user 'postgres' is a security risk, aborting"

## how to install pytorch

```
conda install pytorch-cpu -c pytorch

conda install --use-local mkl-2019.1-144.tar.bz2

```


