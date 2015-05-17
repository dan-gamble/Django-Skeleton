# My Django project skeleton layout
[![Requirements Status](https://requires.io/github/DanGamble89/Django-Skeleton/requirements.png?branch=master)](https://requires.io/github/DanGamble89/Django-Skeleton/requirements/?branch=master)

Project template for Django 1.8

Most of it is based on. [django-drf-template](https://github.com/Keats/django-drf-template) but i stripped out DRF and changed the folder structure a bit to suit what i tend to use.

## Install
You will need Postgres installed and the following ones (for ubuntu/debian, for others systems look in your package managers).

```bash
$ sudo apt-get install libpq-dev python-dev libffi-dev
```

Create your virtualenv (examples will use virtualenvwrapper), I will use the name myproject but use your own name.

```bash
$ mkdir myproject && cd myproject
$ mkvirtualenv myproject
$ pip install django
$ django-admin.py startproject myproject --template=https://github.com/DanGamble89/Django-Skeleton/archive/master.zip
$ cd myproject
$ pip install -r requirements/local.txt
$ vim project_name/settings/local.py // Edit database settings.
$ chmod +x manage.py
$ ./manage.py migrate
```

If you want, you can also add a pre-commit flake8 hook to ensure that commit respects it.

```bash
$ flake8 --install-hook
```

By default it will not stop commits because of warning, a quick look at .git/hooks/pre-commit shows that putting an environment variable of FLAKE8_STRICT will stop them.


And with all that, you should be almost good to go.
There are a few hardcoded temporary settings that you will want to replace, look for the string 'Ann Onymous' and you should find them.
