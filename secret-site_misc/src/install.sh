#!/bin/bash
sudo apt update && apt install nginx python3-pip
pip install certbot certbot-nginx
certbot --nginx
certbot install --cert-name we-l0ve-y0u-ietf-igaijedaejeequ0veishohwe.ropchain.party