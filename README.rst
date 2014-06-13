================
django-ssl-admin
================
.. image:: https://travis-ci.org/Matt-Stevens/django-ssl-admin.png?branch=master
    :target: https://travis-ci.org/Matt-Stevens/django-ssl-admin

Make the Django admin only available via https.
Only for the very latest versions of Django (>= 1.7).

Installation
------------
You can install django-ssl-admin using pip::

    $ pip install django-ssl-admin

And to enable you need to add it to MIDDLEWARE_CLASSES:

.. code-block:: python

    MIDDLEWARE_CLASSES = (
        ...
        'ssladmin.middleware.SSLAdmin',
        ....
    )

If your admin path is not `/admin/` you can change the `ADMIN_PATH` setting like so:

.. code-block:: python

    ADMIN_PATH = '^/staff/'

If you have a reverse proxy set up remember to let Django know how it can detect a secure connection, e.g.::

.. code-block:: python

    SECURE_PROXY_SSL_HEADER = ('HTTP_X_SCHEME', 'https')
