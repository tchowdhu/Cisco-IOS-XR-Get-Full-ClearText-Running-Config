# Cisco-IOS-XR-Get-Full-ClearText-Running-Config-using-Netconf

This is a work around to retrieve clear text running config using ncclient get_config API for Cisco IOS-XR router. 
The example scripts remove the xml tags and keep the clear text running config. 

## Problem Statement:

In ncclient get_config API, there is a filter option. The following filter is used to retrieve CLI running-config for IOS-XR instead of a full XML coded running config. 

    <filter type="subtree">
      <cli xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-cli-cfg"/>
    </filter>

Even though this provides CLI running config, this still contains some xml tags as root nodes before the CLI config starts as shown below:

        <?xml version="1.0" encoding="UTF-8"?>
        <rpc-reply message-id="101" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
          <data>
                  <cli xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-cli-cfg">
                                        ...
                                        ...
                  </cli>
          </data>
        </rpc-reply>
  
## Objective:

The objective is to remove those tags from top and bottom and only keep the cleat text running config.

## Solutions:

There are two scripts shared here to achieve this.

1. In first script, we need to import "ncclient" and “xml.etree.ElementTree”  library. The "xml.etree.ElementTree" is a standard library in python >=3.3 versions so NO need to install this library separately like ncclient but required to import in the script. This was used to remove the xml content by simply break the xml tags into root/parent node and store the value of the node that has CLI config as its value.
 
2. Second file is a work around without the “xml.etree.ElementTree”  library. Say user does not want to use any library other than ncclient, then we can do some work around with simple string processing (simply checking the tags and remove, a bit hardcoded steps). The additional code will be more than one line (unlike the first method) but, no additional library has to be imported in the script.

## Enviroment Requirement:

This script has been tested with python 3.6.X version. So, recommending python 3.3 or greater.

The only required libraries are "ncclient" and/or "xml.etree.ElementTree". However, the requirements.txt file includes the environment setup on which the scripts were tested.

## Alternate:

We could easily utilize the python ztp_helper (by default available in the python enviroment of IOS-XR) to get clear text cli.
The third file "ztp_python_xr_get_cli_cfg.py" includes the code for this purpose. User requires copy this file inside the IOS-XR device.
Simply log into the XR box.

1.  bash (to get into the linux enviroment)
2.  python ztp_python_xr_get_cli_cfg.py (run this command).

## License

This project is licensed to you under the terms of the [Cisco Sample
Code License](./LICENSE).
