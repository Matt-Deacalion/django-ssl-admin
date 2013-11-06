import unittest

from django.http import HttpRequest, HttpResponseRedirect
from django.test import override_settings
from django.conf import settings

from ssladmin.middleware import SSLAdmin

settings.configure()


class TestSSLAdminMiddleware(unittest.TestCase):
    @override_settings(DEBUG=True)
    def test_redirects_http_request(self):
        """
        Test http requests get redirected to https.
        """
        ssladmin_middleware = SSLAdmin()

        request = HttpRequest()
        request.META = {'HTTP_HOST': 'dirtymonkey'}
        request.path = '/admin/'

        response = ssladmin_middleware.process_request(request)

        self.assertIsInstance(response, HttpResponseRedirect)
        self.assertEqual(response.url, 'https://dirtymonkey/admin/')
        self.assertEqual(response.status_code, 302)

    @override_settings(DEBUG=True, SECURE_PROXY_SSL_HEADER=('monkey', 'ha'))
    def test_https_is_not_redirected(self):
        """
        Test https requests do not get redirected.
        """
        ssladmin_middleware = SSLAdmin()

        request = HttpRequest()
        request.META = {'HTTP_HOST': 'dirtymonkey', 'monkey': 'ha'}
        request.path = '/admin/'

        response = ssladmin_middleware.process_request(request)

        self.assertIsNone(response)

if __name__ == '__main__':
    unittest.main()
