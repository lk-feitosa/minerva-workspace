# =======================================================
#   🐍 MINERVA & AGENTS ECOSYSTEM - POWERSHELL SETUP
# =======================================================
param(
    [ValidateSet("core", "full")]
    [string]$Profile = "core",
    [switch]$SkipSkills,
    [switch]$SkipTools
)

$ErrorActionPreference = "Stop"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$ParentDir = Split-Path -Parent $ScriptDir
$SkillsDir = Join-Path $ScriptDir "skills"
$ManifestPath = Join-Path $ScriptDir "skills-manifest.json"

Write-Host "=======================================================" -ForegroundColor Cyan
Write-Host "  🐍 MINERVA & AGENTS ECOSYSTEM - POWERSHELL SETUP" -ForegroundColor Cyan
Write-Host "=======================================================" -ForegroundColor Cyan
Write-Host "[*] Repositorio: $ScriptDir | Perfil: $Profile" -ForegroundColor Gray
Write-Host ""

function Ensure-Junction {
    param([string]$LinkPath, [string]$TargetPath)
    $parent = Split-Path -Parent $LinkPath
    if (-not (Test-Path $parent)) { New-Item -ItemType Directory -Path $parent -Force | Out-Null }
    if (Test-Path $LinkPath) {
        Write-Host "    [!] $LinkPath ja existe. Pulando." -ForegroundColor Yellow
    } else {
        cmd /c mklink /J "$LinkPath" "$TargetPath" | Out-Null
        Write-Host "    [+] Junction criada: $LinkPath -> $TargetPath" -ForegroundColor Green
    }
}

Write-Host "[1/4] Configurando links globais dos agentes..." -ForegroundColor Cyan
Ensure-Junction (Join-Path $HOME ".agents") $ScriptDir
Ensure-Junction (Join-Path $HOME ".codex\skills") $SkillsDir
Ensure-Junction (Join-Path $HOME ".claude\skills") $SkillsDir
Ensure-Junction (Join-Path $HOME ".gemini\config\skills") $SkillsDir

Write-Host ""
Write-Host "[2/4] Verificando ferramentas base no PATH..." -ForegroundColor Cyan
$HasNode = [bool](Get-Command node -ErrorAction SilentlyContinue)
$HasGit = [bool](Get-Command git -ErrorAction SilentlyContinue)
$HasPython = [bool](Get-Command python -ErrorAction SilentlyContinue)
if ($HasNode) { Write-Host "    [+] Node.js detectado" -ForegroundColor Green } else { Write-Host "    [-] Node.js nao encontrado (necessario para npx skills / context-mode)" -ForegroundColor Yellow }
if ($HasPython) { Write-Host "    [+] Python detectado" -ForegroundColor Green } else { Write-Host "    [-] Python nao encontrado (necessario para painel-agents / kanban-agents)" -ForegroundColor Yellow }
if ($HasGit) { Write-Host "    [+] Git detectado" -ForegroundColor Green } else { Write-Host "    [-] Git nao encontrado" -ForegroundColor Yellow }

if (-not $SkipSkills -and $HasNode -and (Test-Path $ManifestPath)) {
    Write-Host ""
    Write-Host "[3/4] Instalando skills oficiais do perfil '$Profile' via skills.sh..." -ForegroundColor Cyan
    $manifest = Get-Content $ManifestPath -Raw | ConvertFrom-Json
    $packages = $manifest.profiles.$Profile.packages
    foreach ($pkg in $packages) {
        $skillArgs = @($pkg.skills)
        Write-Host "    -> $($pkg.repo) ($($skillArgs -join ', '))" -ForegroundColor Gray
        & npx -y skills add $pkg.repo -s @skillArgs -g -y
    }
} else {
    Write-Host ""
    Write-Host "[3/4] Instalacao de skills pulada (-SkipSkills ou Node ausente)." -ForegroundColor Yellow
}

if (-not $SkipTools -and $HasGit -and (Test-Path $ManifestPath)) {
    Write-Host ""
    Write-Host "[4/4] Verificando repositorios companheiros (painel-agents & kanban-agents)..." -ForegroundColor Cyan
    $manifest = Get-Content $ManifestPath -Raw | ConvertFrom-Json
    $toolsFallbackDir = Join-Path $ScriptDir "tools"
    foreach ($tool in $manifest.companion_repos) {
        $siblingPath = Join-Path $ParentDir $tool.name
        $localToolPath = Join-Path $toolsFallbackDir $tool.name
        if (Test-Path $siblingPath) {
            Write-Host "    [+] $($tool.name) encontrado em $siblingPath" -ForegroundColor Green
        } elseif (Test-Path $localToolPath) {
            Write-Host "    [+] $($tool.name) encontrado em $localToolPath" -ForegroundColor Green
        } else {
            if (-not (Test-Path $toolsFallbackDir)) { New-Item -ItemType Directory -Path $toolsFallbackDir -Force | Out-Null }
            Write-Host "    -> Clonando $($tool.url) em $localToolPath..." -ForegroundColor Gray
            git clone $tool.url $localToolPath
        }
    }
}

Write-Host ""
Write-Host "=======================================================" -ForegroundColor Cyan
Write-Host "  🎉 SETUP CONCLUIDO! Abra qualquer projeto e rode /minerva" -ForegroundColor Green
Write-Host "  Cofre Obsidian: $ScriptDir\vault\Agentes" -ForegroundColor Yellow
Write-Host "=======================================================" -ForegroundColor Cyan
