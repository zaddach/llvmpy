from __future__ import print_function, absolute_import, division
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions


from llvmpy import extra

version = extra.get_llvm_version()
del extra

class Wrapper(object):
    __slots__ = '__ptr'

    def __init__(self, ptr):
        assert ptr
        self.__ptr = ptr

    @property
    def _ptr(self):
        try:
            return self.__ptr
        except AttributeError:
            raise AttributeError("_ptr resource has been removed")

    @_ptr.deleter
    def _ptr(self):
        del self.__ptr


def _extract_ptrs(objs):
    return [(x._ptr if x is not None else None)
            for x in objs]

class LLVMException(Exception):
    pass

def test(verbosity=3, run_isolated=True):
    """test(verbosity=1) -> TextTestResult

        Run self-test, and return the number of failures + errors
        """
    from llvm.tests import run

    result = run(verbosity=verbosity, run_isolated=run_isolated)
    errct = len(result.failures) + len(result.errors)

    print()
    if errct:
        print("FAILED")
        print("%d tests failed" % errct)
    else:
        print("PASSED")
    return errct
