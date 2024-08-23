#!/bin/bash

security find-generic-password -ga "Wi-Fi" | grep "password:" | cut -d '"' -f 2
