import inspect
import re
import os
import base64
import datetime
import uuid

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from .models import AuthorizedToken, Victim, Credits
from .utils import get_secret

from flask import (
    Flask,
    session,
    render_template,
    redirect,
    url_for,
    flash,
    request,
    send_file,
    abort,
    jsonify,
)

app = Flask(__name__)


@app.route("/")
def index():
    if not session.get("authorized", None):
        session["authorized"] = False
        return render_template("index.html")

    flash(
        "Congratulations you are authorized here's a flag! uah{U23_S3CUR3_S35510N_T0K3NS}"
    )
    return render_template("flowernet.html", credits=Credits.select())


@app.route("/login", methods=["GET", "POST"])
def login():
    if not session.get("authorized", None):
        flash("You are not 'authorized'!")
        return redirect(url_for("index"))

    return render_template("login.html")


@app.route("/make_token", methods=["GET", "POST"])
def make_token():
    if not session.get("authorized", None):
        flash("You cannot make a token!")
        return redirect(url_for("index"))
    if request.method == "GET":
        return render_template("make_token.html")

    if request.method == "POST":
        name = request.form.get("name", None)
        if not name:
            flash("Name wasn't included in request!")
            return redirect(url_for("make_token"))

        token = base64.b64encode(os.urandom(24)).decode("UTF-8")
        AuthorizedToken.create(token=token, name=name)
        flash(f"X-Hacker-Token: {token}")
        return redirect(url_for("index"))


@app.route("/get_file")
def get_file():
    token = request.headers.get("X-Hacker-Token", None)
    if not token:
        return "X-Hacker-Token not specified!", 400

    if not AuthorizedToken.get_or_none(token=token):
        return "Token was not valid!", 400

    return send_file("static/chrometokenmanager", as_attachment=True, download_name="UAH{FR33B1E_F0R_Y0U_H@V3_FUN}")


@app.route("/source")
def source():
    method = request.args.get("method", None)
    if not method:
        return "Please specify a method!"

    try:
        source = inspect.getsource(globals().get(method))
    except TypeError:
        return "Method wasn't found!"
    source = re.sub(r"uah\{.*\}", "REDACTED", source)

    return "<pre>\n" + source + "</pre>"


# Hopefully this wont be guessed, but the key would be obfuscated anyway
@app.route("/api/get_signing_key", methods=["POST"])
def supersecretpleasedontleak_sadface_get_signing_key():
    if not (token := request.headers.get("X-Hacker-Token", None)):
        abort(400)

    if not (tok := AuthorizedToken.get_or_none(token=token)):
        print("bad token")
        abort(400)

    if not request.form:
        print("no form")
        abort(400)

    if not request.form.get("file", None):
        print("no file")
        abort(400)

    key = b"uah{k3y_3ncryp7_1ng_k3y}"
    key = base64.b64encode(key)
    key = key.ljust(32, b"=")
    cipher = AES.new(key, AES.MODE_CFB, iv=bytes(AES.block_size), segment_size=128)

    uuid_ = uuid.uuid1(clock_seq=69)
    timestamp = datetime.datetime(1582, 10, 15) + datetime.timedelta(
        microseconds=uuid_.time // 10
    )
    pt = bytes(str(uuid_), encoding="UTF-8")

    ct = base64.b64encode(
        cipher.iv + cipher.encrypt(pad(pt, AES.block_size, style="pkcs7"))
    ).decode("UTF-8")

    victim = Victim.create(
        date=timestamp, file_=request.form.get("file"), signing_key=ct
    )
    Credits.create(pwner=tok, pwn=victim)

    return jsonify(dict(token=ct)), 200


def main():
    app.config["SECRET_KEY"] = get_secret()
    app.run(host="0.0.0.0", port=5502)


if __name__ == "__main__":
    main()
