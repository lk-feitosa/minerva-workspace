#!/usr/bin/env bash
# =======================================================
#   🐍 MINERVA ECOSYSTEM - LINUX / MACOS SETUP
# =======================================================
set -e

SKIP_SKILLS=0
SKIP_TOOLS=0

for arg in "$@"; do
  case "$arg" in
    --skip-skills) SKIP_SKILLS=1 ;;
    --skip-tools) SKIP_TOOLS=1 ;;
  esac
done

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PARENT_DIR="$(dirname "$SCRIPT_DIR")"
SKILLS_DIR="$SCRIPT_DIR/skills"
MANIFEST="$SCRIPT_DIR/skills-manifest.json"
MINERVA_HOME="$HOME/.minerva"

echo "======================================================="
echo "  🐍 MINERVA ECOSYSTEM - SETUP GLOBAL (~/.minerva)"
echo "======================================================="
echo "[*] Repositório: $SCRIPT_DIR"
echo ""

migrate_legacy_skills() {
  local legacy_dir="$1"
  [ -e "$legacy_dir" ] || [ -L "$legacy_dir" ] || return 0
  if [ -L "$legacy_dir" ]; then
    local resolved
    resolved="$(readlink -f "$legacy_dir" 2>/dev/null || true)"
    [ "$resolved" = "$SKILLS_DIR" ] && return 0
    rm -f "$legacy_dir"
    return 0
  fi
  [ "$legacy_dir" = "$SKILLS_DIR" ] && return 0

  echo "    [~] Vasculhando skills existentes em $legacy_dir..."
  mkdir -p "$SKILLS_DIR"
  for entry in "$legacy_dir"/*; do
    [ -e "$entry" ] || continue
    local name
    name="$(basename "$entry")"
    if [ ! -e "$SKILLS_DIR/$name" ]; then
      mv "$entry" "$SKILLS_DIR/$name"
      echo "        [+] Migrada para .minerva/skills/: $name"
    else
      rm -rf "$entry"
      echo "        [-] Duplicata ignorada/removida: $name"
    fi
  done

  if [ -z "$(ls -A "$legacy_dir" 2>/dev/null)" ]; then
    rmdir "$legacy_dir"
  else
    local backup="${legacy_dir}.backup.$(date +%Y%m%d%H%M%S)"
    mv "$legacy_dir" "$backup"
    echo "    [!] Arquivos extras preservados em: $backup"
  fi
}

ensure_link() {
  local link_path="$1"
  local target_path="$2"
  mkdir -p "$(dirname "$link_path")"
  if [ -L "$link_path" ]; then
    local resolved
    resolved="$(readlink -f "$link_path" 2>/dev/null || true)"
    if [ "$resolved" = "$target_path" ]; then
      echo "    [=] Link ativo: $link_path -> $target_path"
      return 0
    fi
    rm -f "$link_path"
  elif [ -e "$link_path" ]; then
    echo "    [!] $link_path existe como pasta real. Pulando."
    return 0
  fi
  ln -s "$target_path" "$link_path"
  echo "    [+] Link criado: $link_path -> $target_path"
}

echo "[1/5] Migrando layout antigo (.agents -> .minerva) e skills existentes..."
if [ -L "$HOME/.agents" ]; then
  rm -f "$HOME/.agents"
  echo "    [~] Removido link legado ~/.agents (substituído por ~/.minerva)"
elif [ -d "$HOME/.agents" ]; then
  migrate_legacy_skills "$HOME/.agents/skills"
fi

SKILL_TARGETS=(
  "$HOME/.codex/skills"
  "$HOME/.claude/skills"
  "$HOME/.gemini/config/skills"
  "$HOME/.agents/skills"
)
for st in "${SKILL_TARGETS[@]}"; do
  migrate_legacy_skills "$st"
done

echo ""
echo "[2/5] Criando raiz ~/.minerva e conectando CLIs sem duplicação..."
ensure_link "$MINERVA_HOME" "$SCRIPT_DIR"
for st in "${SKILL_TARGETS[@]}"; do
  ensure_link "$st" "$SKILLS_DIR"
done

echo ""
echo "[3/5] Verificando dependências no PATH..."
command -v node >/dev/null 2>&1 && HAS_NODE=1 || HAS_NODE=0
command -v python3 >/dev/null 2>&1 && echo "    [+] Python3 detectado" || echo "    [-] Python3 não encontrado"
command -v git >/dev/null 2>&1 && HAS_GIT=1 || HAS_GIT=0
[ "$HAS_NODE" -eq 1 ] && echo "    [+] Node.js detectado" || echo "    [-] Node.js não encontrado"
[ "$HAS_GIT" -eq 1 ] && echo "    [+] Git detectado" || echo "    [-] Git não encontrado"
command -v rtk >/dev/null 2>&1 && echo "    [+] rtk detectado" || echo "    [i] Opcional: cargo install rtk (github.com/rtk-ai/rtk)"
command -v graphify >/dev/null 2>&1 && echo "    [+] graphify detectado" || echo "    [i] Opcional: uv tool install graphifyy"

if [ "$SKIP_SKILLS" -eq 0 ] && [ "$HAS_NODE" -eq 1 ] && [ -f "$MANIFEST" ]; then
  echo ""
  echo "[4/5] Instalando todas as skills do projeto via skills.sh..."
  node -e '
    const fs = require("fs");
    const { execFileSync } = require("child_process");
    const m = JSON.parse(fs.readFileSync(process.argv[1], "utf8"));
    for (const p of m.packages) {
      console.log("    ->", p.repo, "(" + p.skills.join(", ") + ")");
      execFileSync("npx", ["-y", "skills", "add", p.repo, "-s", ...p.skills, "-g", "-y"], { stdio: "inherit" });
    }
  ' "$MANIFEST"
else
  echo ""
  echo "[4/5] Instalação de skills pulada (--skip-skills ou Node ausente)."
fi

if [ "$SKIP_TOOLS" -eq 0 ] && [ "$HAS_GIT" -eq 1 ] && [ -f "$MANIFEST" ]; then
  echo ""
  echo "[5/5] Verificando repositórios companheiros (painel-agents & kanban-agents)..."
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
echo "  🎉 SETUP CONCLUÍDO! Raiz global em: $MINERVA_HOME"
echo "  Cofre Obsidian: $SCRIPT_DIR/vault"
echo "  Em qualquer projeto, rode /minerva no seu agente!"
echo "======================================================="
