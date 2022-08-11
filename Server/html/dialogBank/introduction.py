from .dialog_class import Dialog

introduction = Dialog()

introduction.text_box_gui = """
    Welcome! Would you like to learn some specific tips on how to stay cool in your location?
"""

introduction.option = [{"text": "Yes", "on_click": "dialog_2"}, {"text": "No", "on_click": "dialog_1"}]
