# =======================================================
#   🐍 MINERVA & AGENTS ECOSYSTEM - POWERSHELL SETUP
# =======================================================

$ErrorActionPreference = "Stop"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

Write-Host "=======================================================" -ForegroundColor Cyan
Write-Host "  🐍 MINERVA & AGENTS ECOSYSTEM - POWERSHELL SETUP" -ForegroundColor Cyan
Write-Host "=======================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "[*] Diretorio do repositorio: $ScriptDir" -ForegroundColor Gray

# 1. Configurar ~/.agents
$AgentsTarget = Join-Path $HOME ".agents"
if (Test-Path $AgentsTarget) {
    Write-Host "    [!] $AgentsTarget ja existe. Pulando." -ForegroundColor Yellow
} else {
    cmd /c mklink /J "$AgentsTarget" "$ScriptDir" | Out-Null
    Write-Host "    [+] Junction criada: $AgentsTarget -> $ScriptDir" -ForegroundColor Green
}

# 2. Configurar ~/.codex/skills
$CodexDir = Join-Path $HOME ".codex"
if (-not (Test-Path $CodexDir)) { New-Item -ItemType Directory -Path $CodexDir -Force | Out-Null }
$CodexSkills = Join-Path $CodexDir "skills"
if (Test-Path $CodexSkills) {
    Write-Host "    [!] $CodexSkills ja existe. Pulando." -ForegroundColor Yellow
} else {
    $SkillsDir = Join-Path $ScriptDir "skills"
    cmd /c mklink /J "$CodexSkills" "$SkillsDir" | Out-Null
    Write-Host "    [+] Junction criada: $CodexSkills -> $SkillsDir" -ForegroundColor Green
}

# 3. Configurar ~/.claude/skills
$ClaudeDir = Join-Path $HOME ".claude"
if (-not (Test-Path $ClaudeDir)) { New-Item -ItemType Directory -Path $ClaudeDir -Force | Out-Null }
$ClaudeSkills = Join-Path $ClaudeDir "skills"
if (Test-Path $ClaudeSkills) {
    Write-Host "    [!] $ClaudeSkills ja existe. Pulando." -ForegroundColor Yellow
} else {
    $SkillsDir = Join-Path $ScriptDir "skills"
    cmd /c mklink /J "$ClaudeSkills" "$SkillsDir" | Out-Null
    Write-Host "    [+] Junction criada: $ClaudeSkills -> $SkillsDir" -ForegroundColor Green
}

# 4. Configurar ~/.gemini/config/skills
$GeminiCfgDir = Join-Path $HOME ".gemini\config"
if (-not (Test-Path $GeminiCfgDir)) { New-Item -ItemType Directory -Path $GeminiCfgDir -Force | Out-Null }
$GeminiSkills = Join-Path $GeminiCfgDir "skills"
if (Test-Path $GeminiSkills) {
    Write-Host "    [!] $GeminiSkills ja existe. Pulando." -ForegroundColor Yellow
} else {
    $SkillsDir = Join-Path $ScriptDir "skills"
    cmd /c mklink /J "$GeminiSkills" "$SkillsDir" | Out-Null
    Write-Host "    [+] Junction criada: $GeminiSkills -> $SkillsDir" -ForegroundColor Green
}

Write-Host ""
Write-Host "[*] Verificando ferramentas no PATH..." -ForegroundColor Gray
if (Get-Command node -ErrorAction SilentlyContinue) { Write-Host "    [+] Node.js detectado" -ForegroundColor Green } else { Write-Host "    [-] Node.js nao encontrado" -ForegroundColor Yellow }
if (Get-Command python -ErrorAction SilentlyContinue) { Write-Host "    [+] Python detectado" -ForegroundColor Green } else { Write-Host "    [-] Python nao encontrado" -ForegroundColor Yellow }
if (Get-Command git -ErrorAction SilentlyContinue) { Write-Host "    [+] Git detectado" -ForegroundColor Green } else { Write-Host "    [-] Git nao encontrado" -ForegroundColor Yellow }

Write-Host ""
Write-Host "=======================================================" -ForegroundColor Cyan
Write-Host "  🎉 SETUP CONCLUIDO COM SUCESSO!" -ForegroundColor Green
Write-Host "  Para abrir o cofre no Obsidian:" -ForegroundColor White
Write-Host "  Abra o Obsidian e selecione a pasta:" -ForegroundColor Gray
Write-Host "  $ScriptDir\vault\Agentes" -ForegroundColor Yellow
Write-Host "=======================================================" -ForegroundColor Cyan
