import sys

from . import ExpVar


class CmdlineExpVar(ExpVar):
    name = "cmdline"

    def value(self):
        return dict(cmdline=[sys.executable] + sys.argv)
