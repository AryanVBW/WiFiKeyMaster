import subprocess

def get_saved_wifi_passwords():
  """Returns a list of all saved Wi-Fi passwords on the current Linux system."""

  # Get a list of all saved Wi-Fi profiles.
  command = "nmcli con show"
  profiles = subprocess.check_output(command, shell=True).decode("utf-8")

  # Extract the password for each profile.
  passwords = []
  for profile in profiles.split("\n"):
    profile_name = profile.split()[0]
    command = f"nmcli con show {profile_name} | grep 'security.psk'"
    password = subprocess.check_output(command, shell=True).decode("utf-8")

    # Strip the leading and trailing whitespace from the password.
    password = password.strip()

    passwords.append((profile_name, password))

  return passwords


def print_saved_wifi_passwords(passwords):
  """Prints a list of saved Wi-Fi passwords to the console."""

  print("Saved Wi-Fi passwords:")
  for profile_name, password in passwords:
    print(f"{profile_name}: {password}")


# Get and print all saved Wi-Fi passwords.
passwords = get_saved_wifi_passwords()
print_saved_wifi_passwords(passwords)
