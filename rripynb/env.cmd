@ECHO OFF
CHCP 65001
SETLOCAL ENABLEEXTENSIONS
SET script_directory=%~dp0

WHERE /Q pipenv ^
        || ECHO The pipenv executable not found. ^
        && CALL :pause_if_double_click ^
        && EXIT /B 1

CD "%script_directory%" ^
        || ECHO Change directory to project directory failed. ^
        && CALL :pause_if_double_click ^
        && EXIT /B 2

pipenv update --dev ^
        || ECHO Updates dependencies failed. ^
        && CALL :pause_if_double_click ^
        && EXIT /B 3

pipenv run jupyter contrib nbextension install --sys-prefix 1>NUL 2>NUL ^
        || ECHO Install jupyter contrib nbextension failed. ^
        && CALL :pause_if_double_click ^
        && EXIT /B 4

CALL :pause_if_double_click
EXIT /B 0

:pause_if_double_click
        ECHO %CMDCMDLINE% | FINDSTR /L %COMSPEC% 1>NUL 2>NUL ^
                && PAUSE
        EXIT /B 0