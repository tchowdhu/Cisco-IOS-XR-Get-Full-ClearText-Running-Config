#!/usr/bin/env python

# -*- coding: utf-8 -*-

"""
Copyright (c) 2021 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at
               https://developer.cisco.com/docs/licenses
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""

__author__ = "Tahsin Chowdhury"
__email__ = "tchowdhu@cisco.com"
__version__ = "0.1.0"
__copyright__ = "Copyright (c) 2021 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"


import socket
host=socket.gethostname()

import sys
sys.path.append("/pkg/bin")

from ztp_helper import ZtpHelpers
ztp_obj=ZtpHelpers()

cmd={"exec_cmd" : "show running-config"}
config = ztp_obj.xrcmd(cmd)

config_list = config['output']

cli_config = ''

for line in config_list:
    cli_config = cli_config+line+'\n'

#cli_config = cli_config.strip()

print(cli_config)

with open("%s.txt" % host, 'w') as f:
    f.write(cli_config)
