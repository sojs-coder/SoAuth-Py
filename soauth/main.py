import requests
from flask import request, session

def soauth():
    if "so_auth" not in session:
        session["so_auth"] = {}

    if "so-auth" in request.cookies:
        response = requests.post("https://soauth.sojs.repl.co/checkValid", json={"token": request.cookies["so-auth"]})
        data = response.json()
        if "message" in data:
            print(data["message"])
            session["so_auth"]["user"] = False
        else:
            session["so_auth"]["user"] = data["data"]