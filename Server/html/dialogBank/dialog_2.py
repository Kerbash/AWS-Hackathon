from .dialog_class import Dialog

dialog_2 = Dialog()

dialog_2.text_box_gui = """
    Can we use the user’s location data?
"""

dialog_2.option = [{"text": "Yes", "on_click": "dialog_4"}, {"text": "No", "on_click": "dialog_3"}]
