#-*- coding: utf-8 -*-

from phue import Bridge
from pit import Pit
import sys


def main():
    conf = Pit.get(
        'hue', {'require': {'ip_addr': 'IP Address of Hue'}}
    )

    b = Bridge(conf['ip_addr'])

    lights = b.lights
    for l in lights:
        print l.name

    print b.username
    print b.name
    print b.ip

if __name__ == '__main__':
    main()
