# =======================================================
#   🐍 MINERVA ECOSYSTEM - POWERSHELL SETUP
# =======================================================
param(
    [switch]$SkipSkills,
    [switch]$SkipTools
)

$ErrorActionPreference = "Stop"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$ParentDir = Split-Path -Parent $ScriptDir
$SkillsDir = Join-Path $ScriptDir "skills"
$ManifestPath = Join-Path $ScriptDir "skills-manifest.json"
$MinervaHome = Join-Path $HOME ".minerva"

Write-Host "=======================================================" -ForegroundColor Cyan
Write-Host "  🐍 MINERVA ECOSYSTEM - SETUP GLOBAL (~/.minerva)" -ForegroundColor Cyan
Write-Host "=======================================================" -ForegroundColor Cyan
Write-Host "[*] Repositorio: $ScriptDir" -ForegroundColor Gray
Write-Host ""

function Normalize-PathString([string]$p) {
    if ([string]::IsNullOrWhiteSpace($p)) { return "" }
    return $p.TrimEnd('\', '/').ToLowerInvariant()
}

function Migrate-LegacySkills {
    param([string]$LegacySkillsDir)

    if (-not (Test-Path $LegacySkillsDir)) { return }
    $item = Get-Item $LegacySkillsDir -Force
    $isReparse = [bool]($item.Attributes -band [IO.FileAttributes]::ReparsePoint)
    if ($isReparse) {
        $target = Normalize-PathString ($item.Target | Select-Object -First 1)
        if ($target -eq (Normalize-PathString $SkillsDir)) { return }
    }

    if ((Normalize-PathString $LegacySkillsDir) -eq (Normalize-PathString $SkillsDir)) { return }

    if ($isReparse) {
        [System.IO.Directory]::Delete($LegacySkillsDir)
        return
    }

    Write-Host "    [~] Vasculhando skills existentes em $LegacySkillsDir..." -ForegroundColor Yellow
    if (-not (Test-Path $SkillsDir)) { New-Item -ItemType Directory -Path $SkillsDir -Force | Out-Null }

    foreach ($entry in (Get-ChildItem -Path $LegacySkillsDir -Directory -Force)) {
        $dest = Join-Path $SkillsDir $entry.Name
        if (-not (Test-Path $dest)) {
            Move-Item -Path $entry.FullName -Destination $dest -Force
            Write-Host "        [+] Migrada para .minerva/skills/: $($entry.Name)" -ForegroundColor Green
        } else {
            Remove-Item -Path $entry.FullName -Recurse -Force
            Write-Host "        [-] Duplicata ignorada/removida: $($entry.Name)" -ForegroundColor DarkGray
        }
    }

    $remaining = Get-ChildItem -Path $LegacySkillsDir -Force
    if ($remaining.Count -eq 0) {
        Remove-Item -Path $LegacySkillsDir -Force
    } else {
        $stamp = Get-Date -Format "yyyyMMddHHmmss"
        $backup = "$LegacySkillsDir.backup.$stamp"
        Move-Item -Path $LegacySkillsDir -Destination $backup -Force
        Write-Host "    [!] Arquivos extras preservados em: $backup" -ForegroundColor Yellow
    }
}

function Ensure-Junction {
    param([string]$LinkPath, [string]$TargetPath)
    if ((Normalize-PathString $LinkPath) -eq (Normalize-PathString $TargetPath)) {
        Write-Host "    [=] Raiz canonica ja configurada: $LinkPath" -ForegroundColor DarkGreen
        return
    }
    $parent = Split-Path -Parent $LinkPath
    if (-not (Test-Path $parent)) { New-Item -ItemType Directory -Path $parent -Force | Out-Null }

    if (Test-Path $LinkPath) {
        $item = Get-Item $LinkPath -Force
        $isReparse = [bool]($item.Attributes -band [IO.FileAttributes]::ReparsePoint)
        $currentTarget = Normalize-PathString ($item.Target | Select-Object -First 1)
        if ($isReparse -and $currentTarget -eq (Normalize-PathString $TargetPath)) {
            Write-Host "    [=] Junction ativa: $LinkPath -> $TargetPath" -ForegroundColor DarkGreen
            return
        }
        if ($isReparse) {
            [System.IO.Directory]::Delete($LinkPath)
        } else {
            Write-Host "    [!] $LinkPath existe como pasta real. Pulando substituicao." -ForegroundColor Yellow
            return
        }
    }

    cmd /c mklink /J "$LinkPath" "$TargetPath" | Out-Null
    Write-Host "    [+] Junction criada: $LinkPath -> $TargetPath" -ForegroundColor Green
}

Write-Host "[1/5] Migrando layout antigo (.agents -> .minerva) e skills existentes..." -ForegroundColor Cyan
$LegacyAgentsRoot = Join-Path $HOME ".agents"
if (Test-Path $LegacyAgentsRoot) {
    $legacyItem = Get-Item $LegacyAgentsRoot -Force
    $legacyIsReparse = [bool]($legacyItem.Attributes -band [IO.FileAttributes]::ReparsePoint)
    if ($legacyIsReparse) {
        [System.IO.Directory]::Delete($LegacyAgentsRoot)
        Write-Host "    [~] Removido link legado ~/.agents (substituido por ~/.minerva)" -ForegroundColor Yellow
    } else {
        Migrate-LegacySkills (Join-Path $LegacyAgentsRoot "skills")
    }
}

$SkillTargets = @(
    (Join-Path $HOME ".codex\skills"),
    (Join-Path $HOME ".claude\skills"),
    (Join-Path $HOME ".gemini\config\skills"),
    (Join-Path $HOME ".agents\skills")
)
foreach ($st in $SkillTargets) { Migrate-LegacySkills $st }

Write-Host ""
Write-Host "[2/5] Criando raiz ~/.minerva e conectando CLIs sem duplicacao..." -ForegroundColor Cyan
Ensure-Junction $MinervaHome $ScriptDir
foreach ($st in $SkillTargets) { Ensure-Junction $st $SkillsDir }

Write-Host ""
Write-Host "[3/5] Verificando ferramentas no PATH..." -ForegroundColor Cyan
$HasNode = [bool](Get-Command node -ErrorAction SilentlyContinue)
$HasGit = [bool](Get-Command git -ErrorAction SilentlyContinue)
$HasPython = [bool](Get-Command python -ErrorAction SilentlyContinue)
$HasRtk = [bool](Get-Command rtk -ErrorAction SilentlyContinue)
$HasGraphify = [bool](Get-Command graphify -ErrorAction SilentlyContinue)
if ($HasNode) { Write-Host "    [+] Node.js detectado" -ForegroundColor Green } else { Write-Host "    [-] Node.js nao encontrado (necessario para npx skills / context-mode)" -ForegroundColor Yellow }
if ($HasPython) { Write-Host "    [+] Python detectado" -ForegroundColor Green } else { Write-Host "    [-] Python nao encontrado (necessario para painel-agents / kanban-agents)" -ForegroundColor Yellow }
if ($HasGit) { Write-Host "    [+] Git detectado" -ForegroundColor Green } else { Write-Host "    [-] Git nao encontrado" -ForegroundColor Yellow }
if ($HasRtk) { Write-Host "    [+] rtk detectado (hook local por projeto habilitado)" -ForegroundColor Green } else { Write-Host "    [i] Opcional: instale rtk (github.com/rtk-ai/rtk/releases)" -ForegroundColor DarkGray }
if ($HasGraphify) { Write-Host "    [+] graphify detectado (grafo AST por projeto habilitado)" -ForegroundColor Green } else { Write-Host "    [i] Opcional: uv tool install graphifyy" -ForegroundColor DarkGray }

if (-not $SkipSkills -and $HasNode -and (Test-Path $ManifestPath)) {
    Write-Host ""
    Write-Host "[4/5] Instalando todas as skills do projeto via skills.sh..." -ForegroundColor Cyan
    $manifest = Get-Content $ManifestPath -Raw | ConvertFrom-Json
    foreach ($pkg in $manifest.packages) {
        $skillArgs = @($pkg.skills)
        Write-Host "    -> $($pkg.repo) ($($skillArgs -join ', '))" -ForegroundColor Gray
        try {
            & npx -y skills add $pkg.repo -s @skillArgs -g -y
        } catch {
            Write-Host "    [!] Aviso: falha ao instalar $($pkg.repo) ($($_.Exception.Message))" -ForegroundColor Yellow
        }
    }
} else {
    Write-Host ""
    Write-Host "[4/5] Instalacao de skills pulada (-SkipSkills ou Node ausente)." -ForegroundColor Yellow
}

if (-not $SkipTools -and $HasGit -and (Test-Path $ManifestPath)) {
    Write-Host ""
    Write-Host "[5/5] Verificando repositorios companheiros (painel-agents & kanban-agents)..." -ForegroundColor Cyan
    $manifest = Get-Content $ManifestPath -Raw | ConvertFrom-Json
    $toolsFallbackDir = Join-Path $ScriptDir "tools"
    foreach ($tool in $manifest.companion_repos) {
        $siblingPath = Join-Path $ParentDir $tool.name
        $localToolPath = Join-Path $toolsFallbackDir $tool.name
        $envOverride = if ($tool.name -eq "painel-agents") { $env:MINERVA_PAINEL_DIR } elseif ($tool.name -eq "kanban-agents") { $env:MINERVA_KANBAN_DIR } else { $null }
        if ($envOverride -and (Test-Path $envOverride)) {
            Write-Host "    [+] $($tool.name) encontrado via env em $envOverride" -ForegroundColor Green
        } elseif ($env:MINERVA_TOOLS_DIR -and (Test-Path (Join-Path $env:MINERVA_TOOLS_DIR $tool.name))) {
            Write-Host "    [+] $($tool.name) encontrado via MINERVA_TOOLS_DIR" -ForegroundColor Green
        } elseif (Test-Path $siblingPath) {
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
Write-Host "  🎉 SETUP CONCLUIDO! Raiz global em: $MinervaHome" -ForegroundColor Green
Write-Host "  Cofre Obsidian: $ScriptDir\vault" -ForegroundColor Yellow
Write-Host "  Em qualquer projeto, rode /minerva no seu agente!" -ForegroundColor Cyan
Write-Host "=======================================================" -ForegroundColor Cyan
