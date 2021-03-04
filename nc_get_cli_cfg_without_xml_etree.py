#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Cisco-IOS-XR-Get-Full-ClearText-Running-Config-using-Netconf Console Script.

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

#importing libraries
from ncclient import manager

#Device credential for netconf
host='A.B.C.D'
username='username'
password='password'

#filter to retrieve config
cli_cfg_filter= """
    <filter type="subtree">
      <cli xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-cli-cfg"/>
    </filter>
"""

#Retrieving config from node using netconf
with manager.connect(host=host,
                     port=830,
                     username=username,
                     password=password,
                     hostkey_verify=False,
                     look_for_keys = False) as netconf_connection:

    config = netconf_connection.get_config("running", filter=cli_cfg_filter)

#Parsing CLI config in text format i.e. removing xml tags,
#This portion of code will be added to the existing code
config_data_string = config.data_xml
parsed_config=''
for item in config_data_string.split("\n"):
    if ('<data' not in item) and \
            ('</data>' not in item) and \
            ('<cli' not in item) and \
            ('</cli>' not in item):
        parsed_config += item + '\n'
parsed_config = parsed_config.strip()
print(parsed_config)

#Storing device configruation in a text file
with open("%s.txt" % host, 'w') as f:
    f.write(parsed_config)

