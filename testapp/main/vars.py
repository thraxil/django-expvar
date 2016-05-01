import expvar


class ExampleExpVar(expvar.ExpVar):
    name = "example1"

    def value(self):
        return 42


class PlainExpVar(expvar.ExpVar):
    name = "plain"


class Other(object):
    """ this one exists to make sure it doesn't barf on a
    non-ExpVar object """
    pass
