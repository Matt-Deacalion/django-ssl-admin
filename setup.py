from setuptools import setup
import ssladmin

setup(
    name='django-ssl-admin',
    version=ssladmin.__version__.strip(),
    url='http://dirtymonkey.co.uk/django-ssl-admin',
    license='MIT',
    author=ssladmin.__author__.strip(),
    author_email='matt@dirtymonkey.co.uk',
    description=ssladmin.__doc__.strip(),
    long_description=open('README.rst').read(),
    keywords='django https secure admin ssl',
    packages=['ssladmin'],
    include_package_data=True,
    test_suite='tests',
    tests_require=[
        'Django>=1.6.2',
    ],
    install_requires=[
        'Django>=1.6.2',
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware',
    ],
)
