import expvar


class SkipThis(expvar.ExpVar):
    name = "skipthis"

    def value(self):
        return "shouldn't see this"
