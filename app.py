import settings
import requests
from flask import Flask, request, make_response, redirect
from telebot import TeleBot
from telebot.types import Update


app = Flask(__name__)
client = TeleBot(settings.BOT_TOKEN)


@app.route("/", methods=["GET"])
def index():
    return f"<p>{client.get_webhook_info()}</p>"


@app.route("/activate", methods=["GET"])
def activate():
    client.set_webhook(url=settings.WEBHOOK_URL)
    return redirect("/")


@app.route("/deactivate", methods=["GET"])
def deactivate():
    client.remove_webhook()
    return redirect("/")

def start_command(message):
    client.send_message(message["from"]["id"], "mo ngapain anda?")


def make_request(message):
    url = 'https://api.simsimi.vn/v1/simtalk'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {'text': f'{message}', 'lc': 'id', 'key': ''}

    response = requests.post(url, headers=headers, data=data)
    return response.json()

@app.route(f"/{settings.BOT_TOKEN}", methods=['POST'])
def bot_response():
    update = Update.de_json(request.get_json(force=True))
    message = update.message.json

    if "entities" in message and message["entities"][0]["type"] == "bot_command":
        command = message["text"]
        if command == "/start":
            start_command(message)
        return make_response("")
                
    try:
        if message["text"]:
            response = make_request(message["text"])
            client.send_message(message["from"]["id"], response.get("message"))
            
    except:
        client.send_message(message["from"]["id"], "Mohon maaf, ga support pesannya dong 🤦‍♂️\nText only")
    
    return make_response("")
    