#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  cisco_vpn_users.py
#
#  Copyright 2020 David Dekanozishvili
#

from netmiko import ConnectHandler


def vpn(IP, USER, PASS):
    main_router = {
        'device_type': 'cisco_ios',
        'host': IP,
        'username': USER,
        'password': PASS,
        'port': 22
    }

    net_connect = ConnectHandler(**main_router)
    webvpn_users = net_connect.send_command('show webvpn session context all')
    net_connect.disconnect()

    print(75*'=')
    print(webvpn_users)
    print(75*'=')


def main(args):
    if len(args) == 4:
        IP = args[1]
        USER = args[2]
        PASS = args[3]
        vpn(IP, USER, PASS)
    else:
        print(35*'=')
        print('Pass the arguments following order:\n   IP     USERNAME      PASSWORD')
        print(35*'=')

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
