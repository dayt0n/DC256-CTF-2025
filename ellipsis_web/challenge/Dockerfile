# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
FROM ubuntu:24.04 as chroot

# ubuntu24 includes the ubuntu user by default
RUN /usr/sbin/userdel -r ubuntu && /usr/sbin/useradd --no-create-home -u 1000 user

RUN apt-get update \
    && apt-get install -yq --no-install-recommends \
       curl ca-certificates socat gnupg lsb-release python3-pip vim

COPY web-apps /web-apps
COPY web-servers /web-servers

COPY flag.txt /flag.txt
RUN chmod 644 /flag.txt
RUN openssl ecparam -name secp384r1 -genkey > /jwt.key
RUN chmod 400 /jwt.key && chown user /jwt.key
RUN mkdir /home/user && chown -R 1000 /home/user 

USER 1000
RUN python3 -m pip install flask arrow tinydb jwcrypto bcrypt python_jwt==3.3.3 --break-system-packages
USER root

FROM gcr.io/kctf-docker/challenge@sha256:9f15314c26bd681a043557c9f136e7823414e9e662c08dde54d14a6bfd0b619f

RUN apt update && apt install nginx -y
COPY --from=chroot / /chroot

COPY nginx.conf /nginx.conf

CMD kctf_setup && (chroot /chroot /bin/bash -c '/bin/bash -c "su user - web-servers/python.sh"' &) && bash -c 'nginx -e stderr -c /nginx.conf'
