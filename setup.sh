#!/usr/bin/env bash
# =======================================================
#   🐍 MINERVA & AGENTS ECOSYSTEM - LINUX / MACOS SETUP
# =======================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "======================================================="
echo "  🐍 MINERVA & AGENTS ECOSYSTEM - SETUP"
echo "======================================================="
echo ""
echo "[*] Diretório do repositório: $SCRIPT_DIR"
echo ""

# 1. Symlink ~/.agents
echo "[*] Configurando ~/.agents..."
if [ -L "$HOME/.agents" ]; then
    echo "    [!] ~/.agents já é um link simbólico."
elif [ -d "$HOME/.agents" ]; then
    echo "    [!] ~/.agents já existe como pasta física. Faça backup ou remova para criar o link."
else
    ln -s "$SCRIPT_DIR" "$HOME/.agents"
    echo "    [+] Link simbólico criado: ~/.agents -> $SCRIPT_DIR"
fi

# 2. Symlink ~/.codex/skills
echo "[*] Configurando ~/.codex/skills..."
mkdir -p "$HOME/.codex"
if [ -L "$HOME/.codex/skills" ]; then
    echo "    [!] ~/.codex/skills já é um link simbólico."
elif [ -d "$HOME/.codex/skills" ]; then
    echo "    [!] ~/.codex/skills já existe como pasta física."
else
    ln -s "$SCRIPT_DIR/skills" "$HOME/.codex/skills"
    echo "    [+] Link simbólico criado: ~/.codex/skills -> $SCRIPT_DIR/skills"
fi

# 3. Symlink ~/.claude/skills
echo "[*] Configurando ~/.claude/skills..."
mkdir -p "$HOME/.claude"
if [ -L "$HOME/.claude/skills" ]; then
    echo "    [!] ~/.claude/skills já é um link simbólico."
elif [ -d "$HOME/.claude/skills" ]; then
    echo "    [!] ~/.claude/skills já existe como pasta física."
else
    ln -s "$SCRIPT_DIR/skills" "$HOME/.claude/skills"
    echo "    [+] Link simbólico criado: ~/.claude/skills -> $SCRIPT_DIR/skills"
fi

echo ""
echo "[*] Verificando dependências locais..."
command -v node >/dev/null 2>&1 && echo "    [+] Node.js detectado" || echo "    [-] Node.js não encontrado"
command -v python3 >/dev/null 2>&1 && echo "    [+] Python3 detectado" || echo "    [-] Python3 não encontrado"
command -v git >/dev/null 2>&1 && echo "    [+] Git detectado" || echo "    [-] Git não encontrado"

echo ""
echo "======================================================="
echo "  🎉 SETUP CONCLUÍDO COM SUCESSO!"
echo "  Para abrir o cofre no Obsidian:"
echo "  Abra o Obsidian e selecione a pasta:"
echo "  $SCRIPT_DIR/vault/Agentes"
echo "======================================================="
