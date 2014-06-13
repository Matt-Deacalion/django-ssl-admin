================
django-ssl-admin
================
.. image:: https://travis-ci.org/Matt-Stevens/django-ssl-admin.png?branch=master
    :target: https://travis-ci.org/Matt-Stevens/django-ssl-admin
    :alt: Build Status
.. image:: https://coveralls.io/repos/Matt-Stevens/django-ssl-admin/badge.png?branch=master
    :target: https://coveralls.io/r/Matt-Stevens/Pomodoro-Calculator?branch=master
    :alt: Test Coverage
.. image:: https://pypip.in/version/django-ssl-admin/badge.png
    :target: https://pypi.python.org/pypi/django-ssl-admin/
    :alt: Latest Version
.. image:: https://pypip.in/wheel/django-ssl-admin/badge.png?new
    :target: https://pypi.python.org/pypi/django-ssl-admin/
    :alt: Wheel Status
.. image:: https://pypip.in/license/django-ssl-admin/badge.png
    :target: https://pypi.python.org/pypi/django-ssl-admin/
    :alt: License

Make the Django admin only available via https.
Only for the very latest versions of Django (>= 1.7).

Installation
------------
You can install `django-ssl-admin` using pip::

    $ pip install django-ssl-admin

Usage
-----
To enable `django-ssl-admin` you need to add it to MIDDLEWARE_CLASSES:

.. code-block:: python

    MIDDLEWARE_CLASSES = (
        ...
        'ssladmin.middleware.SSLAdmin',
        ....
    )

If your admin path is not `/admin/` you can change the `ADMIN_PATH` setting like so:

.. code-block:: python

    ADMIN_PATH = '^/staff/'

If you have a reverse proxy set up remember to let Django know how it can detect a secure connection, e.g.:

.. code-block:: python

    SECURE_PROXY_SSL_HEADER = ('HTTP_X_SCHEME', 'https')

Licence
-------
Copyright © 2014 `Matt Deacalion Stevens`_, released under The `MIT License`_.

.. _Matt Deacalion Stevens: http://dirtymonkey.co.uk
.. _MIT License: http://deacalion.mit-license.org
