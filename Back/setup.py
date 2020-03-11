import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'pyramid',
    'pypyodbc',
    'pyramid_chameleon',
    'pyramid_debugtoolbar',
    'pyramid_tm',
    'sqlalchemy',
    'transaction',
    'zope.sqlalchemy==1.1',
    'waitress',
    'webtest',
    'pyodbc==4.0.27',
    'sqlalchemy',
    'pyramid_jwt',
    'pyramid_jwtauth',
    'zope.interface==4.6',
    'parse'
    ]

setup(name='ns_portal',
      version='0.0',
      description='ns_portal',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='ns_portal',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = ns_portal:main
      [console_scripts]
      initialize_ns_portal_db = ns_portal.scripts.initializedb:main
      """,
      )
