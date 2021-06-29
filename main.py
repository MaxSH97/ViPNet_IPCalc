#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

import ipaddress

real_ip = input('Real IP address: ')
real_ip = int(ipaddress.IPv4Address(real_ip))

r_real_ip_s = input('Start range of Real IP addresses: ')
r_real_ip_s = int(ipaddress.IPv4Address(r_real_ip_s))

r_real_ip_e = input('End range of Real IP addresses: ')
r_real_ip_e = int(ipaddress.IPv4Address(r_real_ip_e))

d_result = r_real_ip_e - real_ip
r_result = r_real_ip_e - r_real_ip_s

r_virt_ip_s = input('Start range of Virtual IP addresses: ')
r_virt_ip_s = int(ipaddress.IPv4Address(r_virt_ip_s))

r_virt_ip_e = int(ipaddress.IPv4Address(r_virt_ip_s + r_result))

virt_ip = ipaddress.IPv4Address(r_virt_ip_e - d_result)

result = '\nReal IP address: ' + str(ipaddress.IPv4Address(real_ip)) + '\nRange of Real IP addresses: ' \
         + str(ipaddress.IPv4Address(r_real_ip_s)) + ' - ' + str(ipaddress.IPv4Address(r_real_ip_e)) \
         + '\nRange of Virtual IP addresses: ' + str(ipaddress.IPv4Address(r_virt_ip_s)) + ' - ' \
         + str(ipaddress.IPv4Address(r_virt_ip_e)) + '\nVirtual IP address: ' + str(virt_ip)
print(result)
