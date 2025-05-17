#!/bin/bash

find * -name challenge.yaml -not -path 'kctf/*' | xargs dirname 