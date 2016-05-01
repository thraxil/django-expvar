import expvar


class ExampleExpVar(expvar.ExpVar):
    name = "example1"

    def value(self):
        return 42
