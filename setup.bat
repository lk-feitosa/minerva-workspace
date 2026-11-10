@echo off
setlocal enabledelayedexpansion
chcp 65001 >nul

echo =======================================================
echo   🐍 MINERVA & AGENTS ECOSYSTEM - WINDOWS SETUP
echo =======================================================
echo.

set "SCRIPT_DIR=%~dp0"
:: Remove trailing backslash if present
if "%SCRIPT_DIR:~-1%"=="\" set "SCRIPT_DIR=%SCRIPT_DIR:~0,-1%"

echo [*] Diretorio do repositorio: %SCRIPT_DIR%
echo.

:: 1. Criar Junction para %USERPROFILE%\.agents
echo [*] Configurando %%USERPROFILE%%\.agents...
if exist "%USERPROFILE%\.agents" (
    echo     [!] %%USERPROFILE%%\.agents ja existe. Pulando criacao.
) else (
    mklink /J "%USERPROFILE%\.agents" "%SCRIPT_DIR%"
    if !errorlevel! equ 0 (
        echo     [+] Junction criada com sucesso: %%USERPROFILE%%\.agents -^> %SCRIPT_DIR%
    ) else (
        echo     [-] Falha ao criar junction. Execute como Administrador se necessario.
    )
)

:: 2. Configurar %USERPROFILE%\.codex\skills
echo [*] Configurando %%USERPROFILE%%\.codex\skills...
if not exist "%USERPROFILE%\.codex" mkdir "%USERPROFILE%\.codex"
if exist "%USERPROFILE%\.codex\skills" (
    echo     [!] %%USERPROFILE%%\.codex\skills ja existe.
) else (
    mklink /J "%USERPROFILE%\.codex\skills" "%SCRIPT_DIR%\skills"
    if !errorlevel! equ 0 (
        echo     [+] Junction criada: %%USERPROFILE%%\.codex\skills -^> %SCRIPT_DIR%\skills
    )
)

:: 3. Configurar %USERPROFILE%\.claude\skills
echo [*] Configurando %%USERPROFILE%%\.claude\skills...
if not exist "%USERPROFILE%\.claude" mkdir "%USERPROFILE%\.claude"
if exist "%USERPROFILE%\.claude\skills" (
    echo     [!] %%USERPROFILE%%\.claude\skills ja existe.
) else (
    mklink /J "%USERPROFILE%\.claude\skills" "%SCRIPT_DIR%\skills"
    if !errorlevel! equ 0 (
        echo     [+] Junction criada: %%USERPROFILE%%\.claude\skills -^> %SCRIPT_DIR%\skills
    )
)

echo.
echo [*] Verificando dependencias locais...
where node >nul 2>&1 && (echo     [+] Node.js detectado) || (echo     [-] Node.js nao encontrado)
where python >nul 2>&1 && (echo     [+] Python detectado) || (echo     [-] Python nao encontrado)
where git >nul 2>&1 && (echo     [+] Git detectado) || (echo     [-] Git nao encontrado)

echo.
echo =======================================================
echo   🎉 SETUP CONCLUIDO COM SUCESSO!
echo   Para abrir o cofre no Obsidian:
echo   Abra o Obsidian e selecione a pasta:
echo   %SCRIPT_DIR%\vault\Agentes
echo =======================================================
pause
