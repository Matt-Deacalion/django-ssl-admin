================
django-ssl-admin
================

Make the Django admin only available via https.

Installation
------------
You can install django-ssl-admin using pip.

    $ pip install django-ssl-admin

And to enable you need to add it to MIDDLEWARE_CLASSES::

    MIDDLEWARE_CLASSES = (
        ...
        'ssladmin.middleware.SSLAdmin',
        ....
    )

If your admin path is not `/admin/` you can change the `ADMIN_PATH` setting like so::

    ADMIN_PATH = '^/staff/'

If you have a reverse proxy set up remember to let Django know how it can detect a secure connection, e.g.::

    SECURE_PROXY_SSL_HEADER = ('HTTP_X_SCHEME', 'https')
