#!/bin/bash

find * -name challenge.yml -not -path 'kctf/*' | xargs dirname | xargs ctf challenge sync