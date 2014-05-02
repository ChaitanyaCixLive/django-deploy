django-deploy
=============

Management command to automate deployment of django project using
distutils/setuptools.

Usage
=====

1. Install `django-deploy` and add it into your requirements.

2. Add `django_deploy` to your INSTALLED_APPS.

3. Next step depends whether your project uses `setup.py` or not:

With ``setup.py``
-----------------

Add custom install command to `cmdclass` argument in your setup.py:

```python
from django_deploy.setup import DjangoInstall as install

setup(
    ...
    cmdclass={'install': install},
)
```

`DjangoInstall` will call `deploy` management command after regular install.

### Problem with `install_requires`

**Please note** this approach has one major flaw. In case you specify your
project requirements using `install_requires` keyword, you won't be able to
import `django_deploy` module during initial install.

One possible solution is add following import statement and install
application twice. Updates will work just fine:

```python
try:
    from django_deploy.setup import DjangoInstall as install
except ImportError:
    from distutils.command.install import install
```


Without ``setup.py``
--------------------

Simply call `manage.py deploy` after updating codebase and
installing requirements.


Licence
=======

MIT