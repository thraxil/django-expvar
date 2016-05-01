import os
from setuptools import setup

ROOT = os.path.abspath(os.path.dirname(__file__))

setup(
    name="django-expvar",
    version="0.1.0",
    author="Anders Pearson",
    author_email="anders@columbia.edu",
    url="https://github.com/thraxil/django-expvar",
    description="Django expvar endpoint",
    long_description=open(os.path.join(ROOT, 'README.md')).read(),
    install_requires=['Django>=1.8', 'nose', 'six'],
    scripts=[],
    license="BSD",
    platforms=["any"],
    zip_safe=False,
    package_data = {'': ['*.*']},
    packages=['expvar'],
    test_suite='nose.collector',
)
