from flask import Flask, request
import os
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
TOKEN = os.getenv("TOKEN")
INSTANCE_ID = os.getenv("INSTANCE_ID")

def send_msg(to, msg):
    url = f"https://api.ultramsg.com/{INSTANCE_ID}/messages/chat"
    data = {
        "token": TOKEN,
        "to": to,
        "body": msg
    }
    return requests.post(url, data=data)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    if data and data.get("event") == "message":
        sender = data["data"]["from"]
        msg = data["data"]["body"].strip()

        if msg == "1":
            send_msg(sender, "🚗 Catálogo:\n- Fiat Cronos\n- VW Golf\n- Toyota Corolla")
        elif msg == "2":
            send_msg(sender, "💰 Precios:\n- Fiat Cronos: $15.000 USD\n- VW Golf: $18.000 USD")
        elif msg == "3":
            send_msg(sender, "📞 Contacto: 11-2345-6789 o email@tudominio.com")
        elif msg == "9":
            send_msg(sender, "🔁 Un representante te atenderá pronto.")
            notificar_humano(sender)
        else:
            menu = "👋 Bienvenido al bot de autos\n1. Ver catálogo\n2. Ver precios\n3. Contacto\n9. Hablar con un representante"
            send_msg(sender, menu)
    return "OK", 200

def notificar_humano(numero):
    # Simula notificación por email, Telegram o Firebase
    print(f"¡Atención! El número {numero} pidió hablar con un humano.")
    # Aquí podrías enviar un correo, mensaje a Telegram, o guardar en base de datos.
def notificar_humano(numero):
    print(f"¡Atención! El número {numero} pidió hablar con un humano.")

@app.route("/")
def home():
    return "¡El bot de autos está en línea!"

if __name__ == "__main__":
    app.run()


