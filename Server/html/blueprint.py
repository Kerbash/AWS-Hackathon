from flask import render_template, redirect, request, Blueprint, current_app, make_response
from .dialogBank import DialogBank
import json

main_blueprint = Blueprint('main_blueprint', __name__, template_folder="template")


@main_blueprint.route("/")
def home():
    # direct the user to the chatbot url
    return redirect("/chat_bot", code=302)


@main_blueprint.route("/chat_bot")
def chat_bot():
    """
    Chat bot handler

    :return: the main chatbot page
    """
    # check if there is a chat in progress
    dialog_option = request.cookies.get("current_dialog")
    if dialog_option is None:
        dialog_option = "introduction"

    # get the current dialog to send back
    cur_dialog = DialogBank[dialog_option]
    # create the button response
    btn_html = ""
    # create the button html
    for button in cur_dialog.option:
        btn_html += object_to_html_btn(button["text"], button["on_click"])

    # form the response
    response = make_response(render_template("ChatBot.html", DIALOG=cur_dialog.text_box_gui, OPTION_BAR=btn_html))
    response.set_cookie("current_dialog", "introduction")
    return response


@main_blueprint.route("/chat_bot/chat_response")
def chat_response():
    """
    Return a json with text and option as html

    :return:
    """

    # get the response
    new_dialog = request.headers.get("new_dialog")

    # get the current dialog to send back
    cur_dialog = DialogBank[new_dialog]
    # create the button response
    btn_html = ""
    # create the button html
    for button in cur_dialog.option:
        btn_html += object_to_html_btn(button["text"], button["on_click"])

    # create a json to return this way the whole page don't have to load just the dialog and dialog option
    j = {"dialog_text": cur_dialog.text_box_gui, "option": btn_html}

    # form the response
    response = make_response(json.dumps(j))
    response.mimetype = "application/json"
    response.set_cookie("current_dialog", new_dialog)
    return response


def object_to_html_btn(text: str, on_click: str):
    button_html = f'<button class="btn btn-primary" type="button" onClick="response(\'{on_click}\')">{text}</button>'

    return button_html
