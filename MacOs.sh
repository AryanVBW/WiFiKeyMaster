#!/bin/bash

security find-generic-password -ga "Wi-Fi" | grep "password:" | cut -d '"' -f 2






#!/bin/bash

security find-generic-password -ga "Wi-Fi" | while read line; do
    ssid=$(echo $line | grep "label:" | cut -d '"' -f 2)
    password=$(echo $line | grep "password:" | cut -d '"' -f 2)
    if [ -n "$ssid" ] && [ -n "$password" ]; then
        echo "Network Name (SSID): $ssid"
        echo "Password: $password"
        echo "-------------------------"
    fi
done
