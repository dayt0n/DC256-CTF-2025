# DC256 2025 CTF Workshop

This repo uses [kCTF](https://github.com/google/kctf) for remote challenge infrastructure and [ctfcli](https://github.com/ctfd/ctfcli) for syncing challenges with CTFd. 

## ctfcli

### Installation
```bash
python3 -m venv .venv
source .venv/bin/activate
pip3 install ctfcli
```

Initialize it with an access key for your CTFd instance:
```bash
ctf init
```

### Creating a challenge
```bash
ctf challenge new
```

### Installing a new challenge to CTFd
```bash
ctf challenge install [path to challenge]
```

### Syncing challenge changes to CTFd from here
```bash
ctf challenge sync [path to challenge]
```

## kCTF
Activate the environment:
```bash
source kctf/activate
```

From there, follow this guide for local testing: [https://google.github.io/kctf/local-testing.html](https://google.github.io/kctf/local-testing.html).