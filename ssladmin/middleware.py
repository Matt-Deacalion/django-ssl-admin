import re

from urllib.parse import urljoin

from django.http import HttpResponseRedirect
from django.conf import settings


class SSLAdmin:
    """
    Middleware that prevents the Django admin from being accessed via
    non-secure methods (e.g. http). Responds with a 302 redirect to a
    https version of URL if this is the case.
    """
    def __init__(self):
        self.ADMIN_PATH = getattr(settings, 'ADMIN_PATH', '^/admin/')
        self.ADMIN_PATH = re.compile(self.ADMIN_PATH, re.IGNORECASE)

    def secure_url(self, request):
        """
        Build a secure URL from the request object.
        """
        location = request.get_full_path()
        uri = 'https://{}{}'.format(
            request.get_host(),
            request.path,
        )

        return urljoin(uri, location)

    def process_request(self, request):
        """
        Redirect non-secure admin page requests to `https` alternative.
        """
        if self.ADMIN_PATH.match(request.path) and not request.is_secure():
            return HttpResponseRedirect(self.secure_url(request))
