import expvar


class ExampleExpVar(expvar.ExpVar):
    name = "example1"

    def value(self):
        return 42


class PlainExpVar(expvar.ExpVar):
    name = "plain"
