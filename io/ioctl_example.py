#!/usr/bin/python3

import socket
import fcntl
import struct


def get_iphostname():
    def get_ip(if_name):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print(if_name)
        ipaddr = socket.inet_ntoa(fcntl.ioctl(
                            sock.fileno(),
                            0x8915,  # SIOCGIFADDR
                            struct.pack('256s', if_name[:15].encode())
                            )[20:24]
                            )
        sock.close()
        return ipaddr
    
    try:
        ip = get_ip('wlp5s0')
    except IOError:
        ip = get_ip('lo')
    hostname = socket.gethostname()
    return {'hostname': hostname, 'ip': ip}


def main():
    print(get_iphostname())

if __name__ == "__main__":
    main()

