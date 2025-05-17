import os
import requests
import base64
import string
import random
import time
import subprocess

from hacknet.models import Victim, AuthorizedToken, Credits, db
from wonderwords import RandomWord


try:
    requests.get("http://localhost:5502")
except ConnectionError:
    print("Please start the NON DOCKER webserver first!")
    exit()


def setup():
    from lastnames import last_names, common_files
    last = last_names.split("\n")
    common = common_files.split("\n")
    # Ensure they exst
    db.create_tables([Victim, AuthorizedToken, Credits])
    # Primary Hacker Token, needs to be specific
    # This should already exist, but we need a way to set it up
    AuthorizedToken.get_or_create(
        name="SealedVessel", token="jo7aiXieShaephaevi4Ohvengiey0kah"
    )
    r = RandomWord()
    hacker_names = [
        r.word(include_parts_of_speech=["adjectives"]).title()
        + r.word(include_parts_of_speech=["nouns"]).title()
        for name in range(10)
    ]
    victim_names = [
        str(
            random.choice(string.ascii_lowercase)
            + random.choice(last).title()
            + str(random.randint(10, 99))
        )
        for a in range(30)
    ]
    victim_files = [
        f"/home/{random.choice(victim_names)}/{random.choice(common)}"
        for a in range(50)
    ]

    for name in hacker_names:
        AuthorizedToken.create(
            name=name, token=base64.b64encode(os.urandom(24)).decode("utf-8")
        )

    tokens = [entry.token for entry in AuthorizedToken.select()]
    print(tokens)

    for x in range(24):
        resp = requests.post(
            "http://localhost:5502/api/get_signing_key",
            headers={"X-Hacker-Token": random.choice(tokens)},
            data={"file": random.choice(victim_files)},
        )
        time.sleep(random.uniform(.1, 3))
        print(resp)

    proc = subprocess.Popen("./chrometokenmanager")
    proc.wait()

    for x in range(48):
        requests.post(
            "http://localhost:5502/api/get_signing_key",
            data={"file": random.choice(victim_files)},
            headers={"X-Hacker-Token": random.choice(tokens)},
        )
        time.sleep(random.uniform(.1, 3))


if __name__ == "__main__":
    setup()
