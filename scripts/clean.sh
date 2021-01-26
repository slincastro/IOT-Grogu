#!/bin/bash

ampy --port /dev/tty.SLAB_USBtoUART rmdir /domain
ampy --port /dev/tty.SLAB_USBtoUART rmdir /configuration
ampy --port /dev/tty.SLAB_USBtoUART rm config.json
ampy --port /dev/tty.SLAB_USBtoUART rm grogu.py
ampy --port /dev/tty.SLAB_USBtoUART rm log.txt
