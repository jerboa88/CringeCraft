@echo off
setlocal
set "CONTAINER_NAME=cringecraft-mc-1"
set "RCON_PASSWORD_FILE=config\secrets\rcon_password.txt"

if not exist %RCON_PASSWORD_FILE% (
		echo ERROR: RCON password file not found: %RCON_PASSWORD_FILE%
		exit /b 1
)

set /p RCON_PASSWORD=<%RCON_PASSWORD_FILE%

if "%RCON_PASSWORD%"=="" (
		echo ERROR: RCON password file is empty: %RCON_PASSWORD_FILE%
		exit /b 1
)

docker exec -i %CONTAINER_NAME% rcon-cli --password %RCON_PASSWORD%
