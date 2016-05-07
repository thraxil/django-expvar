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

You can easily expose variables through the expvar endpoint. In your
django app, just add a `vars.py` file with some classes that subclass
`expvar.ExpVar` like so:

```
import expvar


class Example(expvar.ExpVar):
    name = 'example'

    def value(self):
        return 42
```

In your django settings, you can optionally specify a `EXPVAR_SKIP`
variable with a list of apps to ignore (ie, any `vars.py` files in
those apps will be ignored).

If multiple variables declare the same `name`, two different things
can happen:

* if they return scalar values, it's a collision and only one of them
  will get reported. This is probably not what you intended, so try to
  stick to unique names
* if they return dicts as their value, variables with the same name
  will have their values merged.

## plugins:

By default, `expvar` will only expose the variables that you set up.

There are a few additional packages available though that act as
plugins to provide generic data on commandline arguments, process
data, etc. Generally, once you have `expvar` installed, you can pip
install them and add them to `INSTALLED_APPS` and that's enough to use
them.

* [django-expvar-cmdline](https://github.com/thraxil/django-expvar-cmdline) -
  reports the commandline data for the process (useful for
  compatability with expvarmon and similar, but may pose a security
  risk if you pass secrets on the commandline)
* [django-expvar-resource](https://github.com/thraxil/django-expvar-resource) -
  reports various info on resource usage (memory, interrupts, etc) via
  a library in the Python's standard lib.
