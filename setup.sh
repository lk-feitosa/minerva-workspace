#!/usr/bin/env bash
# =======================================================
#   🐍 MINERVA & AGENTS ECOSYSTEM - LINUX / MACOS SETUP
# =======================================================
set -e

PROFILE="core"
SKIP_SKILLS=0
SKIP_TOOLS=0

for arg in "$@"; do
  case "$arg" in
    --full) PROFILE="full" ;;
    --core) PROFILE="core" ;;
    --skip-skills) SKIP_SKILLS=1 ;;
    --skip-tools) SKIP_TOOLS=1 ;;
  esac
done

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PARENT_DIR="$(dirname "$SCRIPT_DIR")"
SKILLS_DIR="$SCRIPT_DIR/skills"
MANIFEST="$SCRIPT_DIR/skills-manifest.json"

echo "======================================================="
echo "  🐍 MINERVA & AGENTS ECOSYSTEM - SETUP ($PROFILE)"
echo "======================================================="
echo "[*] Repositório: $SCRIPT_DIR"
echo ""

ensure_link() {
  local link_path="$1"
  local target_path="$2"
  mkdir -p "$(dirname "$link_path")"
  if [ -L "$link_path" ] || [ -e "$link_path" ]; then
    echo "    [!] $link_path já existe. Pulando."
  else
    ln -s "$target_path" "$link_path"
    echo "    [+] Link criado: $link_path -> $target_path"
  fi
}

echo "[1/4] Configurando links globais dos agentes..."
ensure_link "$HOME/.agents" "$SCRIPT_DIR"
ensure_link "$HOME/.codex/skills" "$SKILLS_DIR"
ensure_link "$HOME/.claude/skills" "$SKILLS_DIR"
ensure_link "$HOME/.gemini/config/skills" "$SKILLS_DIR"

echo ""
echo "[2/4] Verificando dependências..."
command -v node >/dev/null 2>&1 && HAS_NODE=1 || HAS_NODE=0
command -v python3 >/dev/null 2>&1 && echo "    [+] Python3 detectado" || echo "    [-] Python3 não encontrado"
command -v git >/dev/null 2>&1 && HAS_GIT=1 || HAS_GIT=0
[ "$HAS_NODE" -eq 1 ] && echo "    [+] Node.js detectado" || echo "    [-] Node.js não encontrado"
[ "$HAS_GIT" -eq 1 ] && echo "    [+] Git detectado" || echo "    [-] Git não encontrado"

if [ "$SKIP_SKILLS" -eq 0 ] && [ "$HAS_NODE" -eq 1 ] && [ -f "$MANIFEST" ]; then
  echo ""
  echo "[3/4] Instalando skills oficiais do perfil '$PROFILE' via skills.sh..."
  node -e '
    const fs = require("fs");
    const { execFileSync } = require("child_process");
    const m = JSON.parse(fs.readFileSync(process.argv[1], "utf8"));
    const pkgs = m.profiles[process.argv[2]].packages;
    for (const p of pkgs) {
      console.log("    ->", p.repo, "(" + p.skills.join(", ") + ")");
      execFileSync("npx", ["-y", "skills", "add", p.repo, "-s", ...p.skills, "-g", "-y"], { stdio: "inherit" });
    }
  ' "$MANIFEST" "$PROFILE"
else
  echo ""
  echo "[3/4] Instalação de skills pulada (--skip-skills ou Node ausente)."
fi

if [ "$SKIP_TOOLS" -eq 0 ] && [ "$HAS_GIT" -eq 1 ] && [ -f "$MANIFEST" ]; then
  echo ""
  echo "[4/4] Verificando repositórios companheiros (painel-agents & kanban-agents)..."
  mkdir -p "$SCRIPT_DIR/tools"
  for name in painel-agents kanban-agents; do
    if [ -d "$PARENT_DIR/$name" ]; then
      echo "    [+] $name encontrado em $PARENT_DIR/$name"
    elif [ -d "$SCRIPT_DIR/tools/$name" ]; then
      echo "    [+] $name encontrado em $SCRIPT_DIR/tools/$name"
    else
      echo "    -> Clonando https://github.com/lk-feitosa/$name.git..."
      git clone "https://github.com/lk-feitosa/$name.git" "$SCRIPT_DIR/tools/$name"
    fi
  done
fi

echo ""
echo "======================================================="
echo "  🎉 SETUP CONCLUÍDO! Abra qualquer projeto e rode /minerva"
echo "  Cofre Obsidian: $SCRIPT_DIR/vault/Agentes"
echo "======================================================="
