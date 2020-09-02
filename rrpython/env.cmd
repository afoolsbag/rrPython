:: Copy Pipfile to parent, and run pipenv update on current and parent directory.

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

DEL "%script_directory%\..\Pipfile" ^
        || ECHO Delete parent directory's Pipfile failed. ^
        && CALL :pause_if_double_click ^
        && EXIT /B 4

MKLINK /H "%script_directory%\..\Pipfile" "%script_directory%\Pipfile" ^
        || ECHO Make parent directory's Pipfile link failed. ^
        && CALL :pause_if_double_click ^
        && EXIT /B 5

CD "%script_directory%\.." ^
        || ECHO Change directory to parent directory failed. ^
        && CALL :pause_if_double_click ^
        && EXIT /B 6

pipenv update --dev ^
        || ECHO Updates dependencies failed. ^
        && CALL :pause_if_double_click ^
        && EXIT /B 7

CALL :pause_if_double_click
EXIT /B 0

:pause_if_double_click
        ECHO %CMDCMDLINE% | FINDSTR /L %COMSPEC% 1>NUL 2>NUL ^
                && PAUSE
        EXIT /B 0
