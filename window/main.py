#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

import ipaddress


class RealIPNotInRange(Exception):
    def __init__(self, text):
        self.text = text


def get_virt_ip(real_ip, r_real_ip_s, r_real_ip_e, r_virt_ip_s):
    real_ip = int(ipaddress.IPv4Address(real_ip))
    r_real_ip_s = int(ipaddress.IPv4Address(r_real_ip_s))
    r_real_ip_e = int(ipaddress.IPv4Address(r_real_ip_e))
    r_virt_ip_s = int(ipaddress.IPv4Address(r_virt_ip_s))

    d_result = r_real_ip_e - real_ip
    r_result = r_real_ip_e - r_real_ip_s

    if real_ip < r_real_ip_s or real_ip > r_real_ip_e:
        raise RealIPNotInRange('Real IP address not in range of Real IP addresses')

    r_virt_ip_e = ipaddress.IPv4Address(r_virt_ip_s + r_result)

    virt_ip = ipaddress.IPv4Address(int(r_virt_ip_e) - d_result)
    return str(virt_ip), str(r_virt_ip_e)
