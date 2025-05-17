#  Copyright 2020-2022 Google LLC
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
FROM python:latest
LABEL maintainer="uahcybersec@uah.edu"
LABEL version="0.1"
LABEL description="web challenge 'hackernet' for the UAH Cybersecurity Club's 2022 Week of Welcome CTF."
RUN /usr/sbin/useradd --no-create-home -u 1000 user
WORKDIR /home/user
ADD src/hacknet /home/user/hacknet
COPY start.sh /home/user/start.sh
COPY src/victims.db /home/user/victims.db
RUN chmod -R 555 /home/user
RUN pip install -e /home/user/hacknet/
CMD bash -c "/home/user/start.sh"