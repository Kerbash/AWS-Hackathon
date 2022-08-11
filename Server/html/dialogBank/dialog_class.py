class Dialog:
    """
        Dialog class

        a Dialog class should be created for each dialog box and
        named in the document accordingly

    """
    # text_box_gui
    # things that should be in the textbox like
    # the actual dialog, any graph etc
    text_box_gui = ""

    # option
    # what options are there for the user
    # should be done in a list format
    # template [{"text": "Yes", "on_click": 3}]
    # will create a button with the text being yes and navigate
    # to dialog option number 3 when pressed
    option = []