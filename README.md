[![Build Status](https://travis-ci.org/thraxil/django-expvar.svg?branch=master)](https://travis-ci.org/thraxil/django-expvar)
[![Coverage Status](https://coveralls.io/repos/github/thraxil/django-expvar/badge.svg?branch=master)](https://coveralls.io/github/thraxil/django-expvar?branch=master)

django-expvar
==============

[expvar](https://golang.org/pkg/expvar/) compatible endpoint for django

`pip install django-expvar`, add `expvar` to `INSTALLED_APPS` and add
to your `urls.py`:

```
from expvar.views import ExpVarView

...

    url('^debug/vars$', ExpVarView.as_view(), name='expvar'),
...
```

Then, accessing `/debug/vars` on your app will return a JSON dict with
the exposed variables, which you can use for monitoring, debugging,
etc.

By default, `expvar` reports commandline arguments and some basic
memory stats, just like the Go package. (currently, the particular
memory stats don't match up with what Go reports. That's being worked
on so tools like [expvarmon](https://github.com/divan/expvarmon) can
be used out of the box, but the Python and Go runtimes are not exactly
identical...)

You can also easily expose other variables through the expvar
endpoint. In your django app, just add a `vars.py` file with some
classes that subclass `expvar.ExpVar` like so:

```
import expvar


class Example(expvar.ExpVar):
    name = 'example'

    def value(self):
        return 42
```

