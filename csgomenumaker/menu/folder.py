import copy

from .. import command
from .. import component
from .. import param

from .menu import Menu


@component.Component("folder")
class Folder(Menu, command.navstate.VertFolder):
    """
    A folder to organize Menu objects in.
    """

    params = param.ParamObj(
        param.Name("Folder"),
        param.Desc("A folder to organize components in."),
        param.Flex(
            "tree",
            param.String(
                "type",
                description=(
                    "The type (or function) of the child component."
                ),
                default="..."
            ),
            description=(
                "The child components of this folder or hierarchy."
            )
        )
    )

    def __init__(self, parent, options):
        Menu.__init__(self, parent, options)
        command.navstate.VertFolder.__init__(self, parent)
        self.ui_name = self.params["name"]
        self.desc = self.params["desc"]
        self.cls = "menu-folder"

        # Take everything in the "tree" param and make it into a menu!
        for ch in self.params["tree"]:
            self.instantiate(ch)
        self.make_dialog()

    def instantiate(self, obj):
        # Instantiate a specific object, based off of its "type" parameter.
        otype = None
        if obj["type"] not in self.root.class_mapping:
            if obj["type"] != "...":
                # There isn't a class of that name. ERROR!
                self.error(
                    "Unknown type '%s' in object '%s'" %
                    (
                        obj["type"],
                        obj
                    )
                )
            else:
                return
        else:
            otype = self.root.class_mapping[obj["type"]]
            if isinstance(otype, str):
                otype = self.root.class_mapping[otype]
        self.selections.append(otype(self, obj))

    def make_dialog(self):
        """
        Generate the UI text for this object.
        """
        if len(self.selections) == 0:
            text0 = ""
            text1 = ""
            text2 = ""
            text3 = ""
        elif len(self.selections) == 1:
            text0 = ""
            text1 = self.selections[0].ui_name
            text2 = ""
            text3 = ""
        elif len(self.selections) == 2:
            text0 = ""
            text1 = self.selections[0].ui_name
            text2 = self.selections[1].ui_name
            text3 = ""
        elif len(self.selections) == 3:
            text0 = ""
            text1 = self.selections[0].ui_name
            text2 = self.selections[1].ui_name
            text3 = self.selections[2].ui_name
        elif len(self.selections) == 4:
            text0 = self.selections[0].ui_name
            text1 = self.selections[1].ui_name
            text2 = self.selections[2].ui_name
            text3 = self.selections[3].ui_name
        elif len(self.selections) > 4:
            text0 = self.selections[0].ui_name
            text1 = self.selections[1].ui_name
            text2 = self.selections[2].ui_name
            text3 = "..."
        # pre_none, pre_contents, and pre_children are prefixes added to the
        # child name based off of the amount of children in the folder total.
        # pre_none is blank space, pre_contents is the "Contents: " indicator,
        # and pre_children shows how many children are in the folder if there
        # are more than 4.
        pre_none = " "*15
        pre_contents = "     Contents: "
        pre_children = ("(%i children) " % len(self.selections)).rjust(15)
        self.dummy.text_contents[0] = pre_none+text0
        self.dummy.text_contents[1] = pre_contents+text1
        self.dummy.text_contents[2] = pre_none+text2
        if len(self.selections) > 4:
            self.dummy.text_contents[2] = pre_children+text2
        self.dummy.text_contents[3] = pre_none+text3

    def join_children(self):
        command.navstate.VertFolder.join_children(self)

    def make_realiases(self):
        command.navstate.VertFolder.make_realiases(self)
