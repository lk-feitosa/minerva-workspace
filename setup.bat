@echo off
setlocal enabledelayedexpansion
chcp 65001 >nul

set "SCRIPT_DIR=%~dp0"
if "%SCRIPT_DIR:~-1%"=="\" set "SCRIPT_DIR=%SCRIPT_DIR:~0,-1%"

where powershell >nul 2>&1
if %ERRORLEVEL% equ 0 (
    powershell -ExecutionPolicy Bypass -File "%SCRIPT_DIR%\setup.ps1" %*
    goto :done
)

echo [!] PowerShell nao encontrado. Criando apenas junctions basicas...
if not exist "%USERPROFILE%\.agents" mklink /J "%USERPROFILE%\.agents" "%SCRIPT_DIR%"
if not exist "%USERPROFILE%\.codex" mkdir "%USERPROFILE%\.codex"
if not exist "%USERPROFILE%\.codex\skills" mklink /J "%USERPROFILE%\.codex\skills" "%SCRIPT_DIR%\skills"
if not exist "%USERPROFILE%\.claude" mkdir "%USERPROFILE%\.claude"
if not exist "%USERPROFILE%\.claude\skills" mklink /J "%USERPROFILE%\.claude\skills" "%SCRIPT_DIR%\skills"
if not exist "%USERPROFILE%\.gemini\config" mkdir "%USERPROFILE%\.gemini\config"
if not exist "%USERPROFILE%\.gemini\config\skills" mklink /J "%USERPROFILE%\.gemini\config\skills" "%SCRIPT_DIR%\skills"

:done
pause
