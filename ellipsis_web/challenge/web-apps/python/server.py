import sys
from arrow import utcnow
import arrow
from flask import (
    Flask,
    abort,
    make_response,
    redirect,
    request,
    url_for,
    render_template,
)
from tinydb import TinyDB, Query
import bcrypt

from jwcrypto import jwt, jws
from jwcrypto.common import json_encode
import python_jwt as pyjwt

KEY = jwt.JWK()
KEY.import_from_pem(open("/jwt.key", "rb").read())

FLAG = open("/flag.txt", "r").read().strip()

db = TinyDB("/tmp/db.json")

app = Flask(__name__)


def validate(data):
    if not data:
        abort(400)
    if not all(k in data for k in ("username", "password")):
        abort(400)
    return data.get("username"), data.get("password")


@app.route("/register", methods=["POST"])
def register():
    if request.method == "POST":
        data = request.get_json(silent=True)
        username, password = validate(data)
        if username == "" or password == "":
            return '<div class="text-danger">Username/Password cannot be blank!</div>'
        User = Query()
        if db.search(User.username == username):
            # user already exists
            abort(400)
        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        db.insert(
            {"username": username, "password": hashed.decode(), "isAdmin": "false"}
        )
        return "Registered"


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        data = request.get_json(silent=True)
        username, password = validate(data)
        User = Query()
        if not (u := db.search(User.username == username)):
            abort(401)
        if len(u) != 1:
            abort(500)
        if not bcrypt.checkpw(password.encode(), u[0]["password"].encode()):
            abort(401)

        payload = {
            "expires": int(utcnow().shift(hours=+1).timestamp()),
            "isAdmin": u[0]["isAdmin"],
            "username": username,
        }
        token = jws.JWS(json_encode(payload))
        token.add_signature(
            KEY,
            None,
            json_encode({"alg": "ES384"}),
            json_encode({"kid": KEY.thumbprint()}),
        )
        resp = make_response()
        resp.set_cookie("session", token.serialize(compact=True))
        return resp
    else:
        return render_template("login.html")


@app.route("/")
def home():
    sess = request.cookies.get("session")
    if not sess:
        return redirect(url_for("login"))
    _, data = pyjwt.process_jwt(sess)
    if arrow.get(data["expires"]) < arrow.utcnow():
        # JWT has expired
        resp = make_response()
        resp.set_cookie("session", "", expires=0)
        return resp
    flags = []

    token = jws.JWS()
    try:
        token.deserialize(sess, KEY)
    except Exception:
        abort(401)  # bad key

    if "isAdmin" in data and data["isAdmin"] == "true":
        flags.append(FLAG)
    return render_template("home.html", flags=flags)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)