#!/bin/bash

# Get a list of all saved Wi-Fi profiles.
profiles=$(nmcli con show)

# Extract the password for each profile.
passwords=()
for profile in $profiles; do
  password=$(nmcli con show $profile | grep 'security.psk' | awk '{print $2}')
  passwords+=("$profile:$password")
done

# Print all saved Wi-Fi passwords to the console.
for password in "${passwords[@]}"; do
  echo "$password"
done
