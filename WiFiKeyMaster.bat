@echo off

REM Get a list of all saved Wi-Fi profiles.
for /f "delims=" %%i in ('netsh wlan show profiles') do (
  REM Extract the password for each profile.
  set password=
  for /f "delims=" %%j in ('netsh wlan show profile name=%%i key=clear') do (
    set password=%%j
  )

  REM Print the profile name and password to the console.
  echo %%i:%password%
)
