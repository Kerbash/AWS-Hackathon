function response(option) {
    let xmlHttpReq = new XMLHttpRequest();
    xmlHttpReq.open("GET", window.location.href + "/chat_response", true);
    xmlHttpReq.setRequestHeader("new_dialog", option)
    // send request
    xmlHttpReq.send(null);

    // once ready
    xmlHttpReq.onreadystatechange = function () {
        response = xmlHttpReq.responseText
        console.log(response)
        dialog = JSON.parse(response)

        document.getElementById("chatbot_dialog").innerHTML = dialog["dialog_text"]
        document.getElementById("response_panel").innerHTML = dialog["option"]
    }
}