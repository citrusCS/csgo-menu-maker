from .command import Command
from .primitive import Primitive


class Echo(Primitive):
    """
    A wrapper around Primitive which serves to output a single line of text.
    """
    def __init__(self, parent, text, out=False):
        Primitive.__init__(self, parent, "echo", [])
        self.cls = "primitive-echo"
        # If this should be filtered out of the console (con_filter) or not:
        if not out:
            self.text = self.root.filter_char+self.root.filter_after+text
        else:
            self.text = self.root.filter_char_out+self.root.filter_after+text

        # Pass the argument to Primitive.
        self.args.append('"'+self.text+'"')
