import sys


def deprecated(message=None, version=None):
    """This decorator marks methods as deprecated.
    A warning is displayed if the method is called."""

    def decorated_method_to_deprecate(func):
        if "--debug" not in sys.argv:
            return func

        import inspect
        import warnings
        from functools import wraps

        if inspect.isclass(func):
            # Handle a deprecated class differently from a deprecated method
            msg = "Class {}() is DEPRECATED!".format(func.__name__)
            if message:
                msg += " *** %s ***" % message
            if version:
                msg += " (Since version %s)" % str(version)
            warnings.simplefilter("always", DeprecationWarning)
            warnings.warn(msg, category=DeprecationWarning, stacklevel=2)
            warnings.simplefilter("default", DeprecationWarning)
            return func

        @wraps(func)
        def new_func(*args, **kwargs):
            msg = "Method {}() is DEPRECATED!".format(func.__name__)
            if message:
                msg += " *** %s ***" % message
            if version:
                msg += " (Since version %s)" % str(version)
            warnings.simplefilter("always", DeprecationWarning)
            warnings.warn(msg, category=DeprecationWarning, stacklevel=2)
            warnings.simplefilter("default", DeprecationWarning)
            return func(*args, **kwargs)

        return new_func

    return decorated_method_to_deprecate
