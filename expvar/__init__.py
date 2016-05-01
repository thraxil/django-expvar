class ExpVar(object):
    """ subclass this to define an expvar

    set the `name` attribute or override `.get_name()`

    and define a `.value()` method.
    """
    def get_name(self):
        return self.name

    def value(self):
        return None
