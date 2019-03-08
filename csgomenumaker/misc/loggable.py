import sys

class Loggable:
    """
    Convenience class to make an object automatically log errors. It only has
    to implement get_error_name() (and only if the developer wants), which 
    returns a string.
    """
    
    def err_name(self):
        """
        Wrapper around get_error_name() which only calls it when a class
        implements get_error_name() itself.
        """
        print(self)
        if hasattr(self, "get_error_name"):
            return self.get_error_name()
        else:
            return type(self).__name__

    def error(self, s, exit=True):
        """
        Print an error and exit.
        """
        print("%s:\n\t\x1b[31mError: %s\x1b[0m" % (self.err_name(), s))
        if exit:
            sys.exit(1)

    def warning(self, s):
        """
        Print a warning.
        """
        print("%s:\n\t\x1b[33mWarning: %s\x1b[0m" % (self.err_name(), s))