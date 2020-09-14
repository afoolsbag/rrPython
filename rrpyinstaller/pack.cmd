@ECHO OFF
CHCP 65001
SETLOCAL ENABLEEXTENSIONS
SET script_directory=%~dp0
FOR %%I IN (.) DO SET script_directory_name=%%~nxI%%~xI
IF EXIST "%script_directory%\%script_directory_name%" (
        SET source_directory_name=%script_directory_name%
) ELSE (
        SET source_directory_name=_%script_directory_name%
)

WHERE /Q pipenv ^
        || ECHO The pipenv executable not found. ^
        && CALL :pause_if_double_click ^
        && EXIT /B 1

CD "%script_directory%" ^
        || ECHO Change directory to project directory failed. ^
        && CALL :pause_if_double_click ^
        && EXIT /B 2

IF NOT EXIST "build" MKDIR "build" ^
        || ECHO Make directory "build" failed. ^
        && CALL :pause_if_double_click ^
        && EXIT /B 3

pipenv run create-version-file --outfile "build\version_file.txt" ^
                               "%source_directory_name%\metadata.yml" ^
        || ECHO Run create-version-file failed. ^
        && CALL :pause_if_double_click ^
        && EXIT /B 4

pipenv run pyinstaller --onefile --name "%source_directory_name%" ^
                       --add-data "%script_directory%\data";"data" ^
                       --console --icon "data\icon.ico" ^
                       --version-file "build/version_file.txt" ^
                       "%source_directory_name%\__main__.py" ^
        || ECHO Run pyinstaller failed. ^
        && CALL :pause_if_double_click ^
        && EXIT /B 5

CALL :pause_if_double_click
EXIT /B 0

:pause_if_double_click
        ECHO %CMDCMDLINE% | FINDSTR /L %COMSPEC% 1>NUL 2>NUL ^
                && PAUSE
        EXIT /B 0
