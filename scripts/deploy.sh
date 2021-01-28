#!/bin/bash
echo "----------------------------------------------"
echo "-------- Preparing to deploy gamora ----------"
echo "----------------------------------------------"
echo "Cleaning older artifacts"
echo "----------------------------------------------"
#sh ./clean.sh
echo "----------------------------------------------"
echo "Deploying Artifacts"
echo "----------------------------------------------"
ampy --port /dev/tty.SLAB_USBtoUART put ./src/domain/
ampy --port /dev/tty.SLAB_USBtoUART put ./src/configuration/
ampy --port /dev/tty.SLAB_USBtoUART put ./src/util/
ampy --port /dev/tty.SLAB_USBtoUART put ./srcg/rogu.py ./src/main.py
ampy --port /dev/tty.SLAB_USBtoUART put ./src/config.json
echo "---------------Folder------------------"
ampy --port /dev/tty.SLAB_USBtoUART ls 
echo "---------------Domain Folder------------------"
ampy --port /dev/tty.SLAB_USBtoUART ls domain
echo "---------------Util Folder------------------"
ampy --port /dev/tty.SLAB_USBtoUART ls util
echo "---------------Configuration Folder------------------"
ampy --port /dev/tty.SLAB_USBtoUART ls configuration
echo "Run Application ......"
#ampy --port /dev/tty.SLAB_USBtoUART run grogu.py