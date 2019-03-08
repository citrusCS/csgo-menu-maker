from .. import misc

from .command import Command
from .compound import Compound
from .echo import Echo
from .indirect import Indirect


class Dialog(Compound):
    """
    Renders the contents of a UI dialog to the screen.
    
    This is accomplished through six echo commands, because that is the 
    maximum number of lines able to be shown in `developer 1` on the Source
    engine.
    
    A dialog is 80 characters wide. The first line of a dialog is the path of
    the current option that the dialog references. The second, third, fourth
    and fifth lines are divided into two sectors. The first sector has a 25
    character wide space for the currently selected folder object. The second
    has a 40 character wide space for the action that the dialog's parent
    employs. This can vary, and is discovered by the dialog upon generation.
    """
    def __init__(self, parent):
        Compound.__init__(self, parent)
        self.cls = "dialog"
        
        # Dialogs are nested two-fold. To find the command.navstate.Horz object
        # that serves as the controller for what this displays, we must find
        # the second-degree parent.
        self.horz_parent = self.parent.parent

    def get_neighbors(self):
        """
        Find the neighbors that will be displayed in the first sector, which
        is the folder contents display.
        
        self.neighbor0, neighbor1, neighbor2, and neighbor3 will be populated.
        Additionally, their texts will be computed or left blank depending on
        their sequence in the folder.
        """
        # Find neighbors.
        self.neighbor0 = self.horz_parent.neighbors["up"]
        self.neighbor1 = self.horz_parent.parent
        self.neighbor2 = self.horz_parent.neighbors["down"]
        self.neighbor3 = self.horz_parent.neighbors["down"].neighbors["down"]
        
        # Determine if the neighbors' text should be left blank.
        if self.neighbor0.sequence >= self.neighbor1.sequence:
            self.neighbor0_text = ""
        else:
            self.neighbor0_text = self.neighbor0.ui_name
        self.neighbor1_text = self.neighbor1.ui_name
        if self.neighbor2.sequence <= self.neighbor1.sequence:
            self.neighbor2_text = ""
        else:
            self.neighbor2_text = self.neighbor2.ui_name
        if self.neighbor3.sequence <= self.neighbor1.sequence:
            self.neighbor3_text = ""
        else:
            self.neighbor3_text = self.neighbor3.ui_name

    def format_header(self):
        """
        Return a string representation of the header (path).
        """
        # backn is the up-directory of the dialog's parent.
        backn = self.horz_parent.neighbors["back"]
        text = backn.parent.get_path()
        
        # Concatenate the header. join() for speed.
        header = "".join([
            self.root.box_drawing[0b0011],
            self.root.box_drawing[0b0101]*2,
            self.root.box_drawing[0b1110],
            " ",
            misc.text_extend(text, 70, self.root.pad_char),
            " ",
            self.root.box_drawing[0b1011],
            self.root.box_drawing[0b0101]*2,
            self.root.box_drawing[0b0110]
        ])
        return header

    def format_contents_0(self):
        horz_text = self.horz_parent.text_contents[0]
        return self.format_contents_other(self.neighbor0_text, horz_text)

    def format_contents_1(self):
        vert_text = self.neighbor1_text
        vert_text = misc.text_restrict(vert_text, 25)
        vert_text = misc.text_center("> " + vert_text + " < ", 30)
        horz_text = self.horz_parent.text_contents[1]
        horz_text = misc.text_extend(horz_text, 40)
        out_text = vert_text + self.root.box_drawing[0b1010] + " " + horz_text
        return self.format_contents_generic(out_text)

    def format_contents_2(self):
        horz_text = self.horz_parent.text_contents[2]
        return self.format_contents_other(self.neighbor2_text, horz_text)

    def format_contents_3(self):
        horz_text = self.horz_parent.text_contents[3]
        return self.format_contents_other(self.neighbor3_text, horz_text)

    def format_contents_other(self, vert_text, horz_text):
        """
        Format a line that is not the currently selected line.
        """
        vert_text = misc.text_restrict(vert_text, 25)
        vert_text = misc.text_center("  " + vert_text + "   ", 30)
        horz_text = misc.text_extend(horz_text, 40)
        out_text = vert_text + self.root.box_drawing[0b1010] + " " + horz_text
        return self.format_contents_generic(out_text)

    def format_contents_generic(self, text):
        """
        Format a line that is the currently selected line (add '> <').
        """
        out_text = "".join([
            self.root.box_drawing[0b1010],
            "  ",
            text,
            "    ",
            self.root.box_drawing[0b1010]
        ])
        return out_text

    def format_footer(self):
        """
        Return a string representation of the footer (the description).
        """
        text = self.horz_parent.parent.desc
        footer = "".join([
            self.root.box_drawing[0b1001],
            self.root.box_drawing[0b0101]*2,
            self.root.box_drawing[0b1110],
            " ",
            misc.text_extend(text, 70, " "),
            " ",
            self.root.box_drawing[0b1011],
            self.root.box_drawing[0b0101]*2,
            self.root.box_drawing[0b1100]
        ])
        return footer

    def format_key(self, keybind):
        """
        Return a nicely-formatted representation of a key name, e.g. [ENTER]
        """
        return "[%s]" % self.root.config.keybinds[keybind].upper()

    def generate_dialog(self):
        """
        Make the `echo` commands needed to be run in order to show this dialog
        on-screen.
        """
        self.get_neighbors()
        
        # Generate help texts, which show which keys do which action.
        help0 = self.format_key("up") + " / " + self.format_key("down") \
            + " - Previous/Next"
        help1 = self.format_key("left") + " / " + self.format_key("right") \
            + " - Change Setting"
        help2 = self.format_key("fire") + " - Enter Folder / Run Command"
        help3 = self.format_key("back") + " - Exit Folder"
        
        # Generate the individual lines which are shown on-screen.
        line0 = self.format_header()
        line1 = self.format_contents_0() + " " + help0
        line2 = self.format_contents_1() + " " + help1
        line3 = self.format_contents_2() + " " + help2
        line4 = self.format_contents_3() + " " + help3
        line5 = self.format_footer()
        
        # The commands are nested in an Indirect, because of a fucking stupid
        # parsing bug in the Source engine. Valve, please fix. Actually do,
        # though, because this bug goes all the way back to FUCKING QUAKE with
        # the concmd system. SERIOUSLY!!!
        # A description of the bug is as follows.
        
        # The Source engine is derived from the GoldSrc engine. The GoldSrc
        # engine is derived from Quake (1996), albeit with heavy modification.
        # Thus, there is some residual code from Quake in the Source engine.
        # No problem, Quake was a great game, id software is amazing (shoutout
        # to JC), the code was state-of-the-art for back then. However, now, it
        # is not state-of-the-art. Namely, the lack of special character
        # support is at fault here. It is my impression that Quake was an ASCII
        # only game (totally fine for '96), and thus unicode or wchar_t most
        # likely were not compatible with the codebase. To put that whole thing
        # in perspective, Quake (22 years old, as of 2019) is six years older
        # than I am.
        # Let's walk through the code leading up to this. Follow along at:
        # https://github.com/ValveSoftware/source-sdk-2013/blob/master/sp/src/tier1/commandbuffer.cpp
        # Ignore the spelling error on line 423 (literally unreadable)
        # Valve has deliberately #if'd out the section of this file that was
        # derived from Quake, but it's still used in CS:GO, for sure; the
        # error messages and alias command syntax is EXACTLY the same.
        # Aliases are stored in `cmdalias_t`, which is a simple linked-list
        # node (meaning aliases are searched O(n)). The contents of the alias
        # are stored as char*, which is perplexing because char* should be able
        # to handle Unicode strings JUST FINE. It was my impression that there
        # is some kind of mangling going on by CCommandBuffer or the command
        # system as a whole that's converting Unicode to some kind of invalid
        # character placeholder. The manifestation of this bug is that if you
        # place special characters (Unicode or otherwise) in a cmd statement
        # in an alias command it will display ?s for each character making up
        # the Unicode codepoint (sorry if I used the wrong terminology).
        # For example:
        # ```
        # alias test_echo_unicode="echo ℽ"
        #
        # ] test_echo_unicode
        # ? ? ?
        # ```
        # But when running this:
        # ```
        # ] echo ℽ
        # ℽ
        # ```
        # It works fine???
        # Mysteriously, this bug does not show up when you are executing
        # commands normally, i.e. from the console or from a .cfg. What gives??
        # I would trace it further, but I decided it wasn't worth it after 3+
        # hours of searching, especially as I would have no way of fixing it.
        
        # Anyway, the outcome of this is that each set of echo commands must be
        # put inside a separate .cfg file. Pretty gnarly. However, it was fun
        # to poke around the Source codebase. Regardless of how weird its
        # organization is, the engine is remarkable and is one of the easiest
        # engines to understand, as well as the company being relatively
        # developer friendly. Thanks Valve!
        
        indir = Indirect(self)
        Echo(indir, line0)
        Echo(indir, line1)
        Echo(indir, line2)
        Echo(indir, line3)
        Echo(indir, line4)
        Echo(indir, line5)
