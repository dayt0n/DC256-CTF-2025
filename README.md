# DC256 2025 CTF Workshop

This repo uses [kCTF](https://github.com/google/kctf) for remote challenge infrastructure and [ctfcli](https://github.com/ctfd/ctfcli) for syncing challenges with CTFd. 

## Writeups
If you're looking for writeups, [click here](./WRITEUPS.md)!

## Slides from the CTF 101 talk
If you want the slides from my presentation at the DC256 group on CTF 101, [click here](./CTF%20101.pdf).

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

### Sync all challenges with the scoreboard
```bash
./sync-ctfd.sh
```

## Running the challenges locally
Make sure you have Docker installed: https://docs.docker.com/engine/install/.

### Non-web / kCTF-based challenges
For kCTF on Debian/Ubuntu, run:
```bash
umask a+rx
echo 'kernel.unprivileged_userns_clone=1' | sudo tee -a /etc/sysctl.d/00-local-userns.conf
sudo service procps restart
```

Activate the environment:
```bash
source kctf/activate
kctf cluster load local-cluster
```

Get a list of all kctf-compatible challenges by running this script:
```bash
./kctf-utils/list.sh
```

For each of those challenges, use kctf to spin it up locally, forward the port to yourself, and access it on your local system. 

For instance, if we want to start c-repl, we would:
```bash
cd c-repl
kctf chal start
kctf chal debug port-forward
# the port-forward command prints out a random local port 
#  you can then use to access the challenge
```

For more information on using kCTF in a local environment, see this: [https://google.github.io/kctf/local-testing.html](https://google.github.io/kctf/local-testing.html).

### Web challenges
For the web challenges, start the containers with:
```bash
docker compose up
```

This will start `ellipsis` at http://127.0.0.1:8080 and `hackernet` at https://127.0.0.1:8081. 
