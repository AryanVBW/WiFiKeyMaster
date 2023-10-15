import subprocess

def get_saved_wifi_passwords():
  """Returns a list of all saved Wi-Fi passwords on the current Windows system."""

  # Get a list of all saved Wi-Fi profiles.
  command = "netsh wlan show profiles"
  profiles = subprocess.check_output(command, shell=True).decode("utf-8")

  # Extract the password for each profile.
  passwords = []
  for profile in profiles.split("\n"):
    profile_name = profile.split(":")[1].strip()
    command = f"netsh wlan show profile name={profile_name} key=clear"
    password = subprocess.check_output(command, shell=True).decode("utf-8")

    # Split the password output on the colon to get the actual password.
    password = password.split(":")[1].strip()

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
