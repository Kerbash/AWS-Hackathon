from .dialog_class import Dialog

dialog_3 = Dialog()

dialog_3.text_box_gui = """
    Can I please have the name of your city and state, so I can determine the best tips to keep you cool?
"""

dialog_3.option = [{"text": "Yes", "on_click": "dialog_4"}, {"text": "No", "on_click": "dialog_1"}]
