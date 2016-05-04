""" run tests for django-expvar

$ virtualenv ve
$ ./ve/bin/pip install .
$ ./ve/bin/python runtests.py
"""


import django
from django.conf import settings
from django.core.management import call_command


def main():
    # Dynamically configure the Django settings with the minimum necessary to
    # get Django running tests
    settings.configure(
        INSTALLED_APPS=(
            'testapp.main',
            'testapp.noexpvars',
            'testapp.skipme',
            'expvar',
        ),
        EXPVAR_SKIP=['testapp.skipme'],
        TEST_RUNNER='django.test.runner.DiscoverRunner',

        COVERAGE_EXCLUDES_FOLDERS=['migrations'],
        ROOT_URLCONF='testapp.urls',

        # Django replaces this, but it still wants it. *shrugs*
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',
                'HOST': '',
                'PORT': '',
                'USER': '',
                'PASSWORD': '',
            }
        },
    )

    django.setup()

    # Fire off the tests
    call_command('test')

if __name__ == '__main__':
    main()
