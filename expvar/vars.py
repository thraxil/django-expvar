import resource
import sys

from . import ExpVar


class CmdlineExpVar(ExpVar):
    name = "cmdline"

    def value(self):
        return dict(cmdline=[sys.executable] + sys.argv)


class MemoryExpVar(ExpVar):
    name = "memory"

    def value(self):
        memstats = resource.getrusage(resource.RUSAGE_SELF)
        return dict(
            utime=memstats.ru_utime,
            stime=memstats.ru_stime,
            maxrss=memstats.ru_maxrss,
            ixrss=memstats.ru_ixrss,
            idrss=memstats.ru_idrss,
            isrss=memstats.ru_isrss,
            minflt=memstats.ru_minflt,
            majflt=memstats.ru_majflt,
            nswap=memstats.ru_nswap,
            inblock=memstats.ru_inblock,
            oublock=memstats.ru_oublock,
            msgsnd=memstats.ru_msgsnd,
            msgrcv=memstats.ru_msgrcv,
            nsignals=memstats.ru_nsignals,
            nvcsw=memstats.ru_nvcsw,
            nivcsw=memstats.ru_nivcsw,
        )
