---
name: minerva-setup
description: Instala, migra e configura globalmente o ecossistema Minerva no PC (~/.minerva). Use quando o usuário rodar /minerva-setup ou pedir para configurar a máquina pela primeira vez após baixar do skills.sh, migrando skills e MCPs antigos sem duplicar e instalando todo o catálogo.
user-invocable: true
---

# Minerva Setup — Configuração Global do PC (`~/.minerva`)

Use este comando **uma única vez por máquina** (ou quando quiser atualizar/reparar a instalação global do PC).  
*(Para configurar o repositório de um projeto específico no dia a dia, use **`/minerva`**).*

---

## O que `/minerva-setup` executa automaticamente no PC

1. **Garante a Raiz Canônica Única (`~/.minerva` / `%USERPROFILE%\.minerva`):**
   * Verifica se `~/.minerva/setup.ps1` (Windows) ou `~/.minerva/setup.sh` (Linux/macOS) já existe como repositório Git.
   * **Se ainda não existir** (ex.: o usuário instalou apenas as skills via `npx skills add lk-feitosa/minerva-workspace -g -y`):
     * Preserva temporariamente quaisquer skills já presentes em `~/.agents/skills`, `~/.claude/skills`, `~/.codex/skills` e `~/.gemini/config/skills`.
     * Clona o repositório oficial diretamente em `~/.minerva`:
       ```bash
       git clone https://github.com/lk-feitosa/minerva-workspace.git ~/.minerva
       ```
   * **Se já existir:** executa `git -C ~/.minerva pull --ff-only` para sincronizar a versão mais recente.

2. **Executa o Instalador Nativo (`setup.ps1` no Windows / `setup.sh` no Linux & macOS):**
   * **No Windows (PowerShell):**
     ```powershell
     powershell -ExecutionPolicy Bypass -File "$HOME\.minerva\setup.ps1"
     ```
   * **No Linux / macOS:**
     ```bash
     chmod +x ~/.minerva/setup.sh && ~/.minerva/setup.sh
     ```

3. **Etapas que o instalador realiza sem duplicação:**
   * **`[1/6]` Migração de Skills Antigas:** vasculha `~/.claude/skills`, `~/.codex/skills`, `~/.gemini/config/skills` e `~/.agents/skills`, movendo skills exclusivas para `~/.minerva/skills/` e removendo cópias duplicadas.
   * **`[2/6]` Links Globais (Junctions / Symlinks):** aponta todos os CLIs para `~/.minerva/skills/`.
   * **`[3/6]` Migração e Sincronização de MCPs Globais sem duplicar:** mescla os servidores base (`ai-memory`, `rea`, `agent-desktop`) de `~/.minerva/mcp_config.json` com os arquivos globais existentes dos CLIs (`~/.gemini/mcp_config.json`, `~/.claude.json`), preservando qualquer MCP que o usuário já possua.
   * **`[4/6]` Verificação de Ferramentas no `PATH`:** checa `node`, `python`, `git`, `rtk` e `graphify`.
   * **`[5/6]` Instalação do Catálogo Completo (`skills-manifest.json`):** instala os 17 pacotes curados do `skills.sh` em `~/.minerva/skills/`.
   * **`[6/6]` Repositórios Companheiros:** verifica ou clona `painel-agents` (`:3333`) e `kanban-agents` (`:3334`) em `~/.minerva/tools/`.

---

## Fechamento do `/minerva-setup` — Resposta Obrigatória com Todos os Endereços

Ao concluir, apresente ao usuário a tabela exata de **onde cada item ficou salvo no PC**:

| Item Configurado | Endereço / Caminho Salvo no PC |
| :--- | :--- |
| **🏠 Raiz Global Única da Minerva** | `~/.minerva` (`%USERPROFILE%\.minerva`) |
| **📓 Cofre do Obsidian (Abrir como Vault)** | `~/.minerva/vault` (`%USERPROFILE%\.minerva\vault`) |
| **🧠 Skills Centralizadas (Junction para todos os CLIs)** | `~/.minerva/skills` (`%USERPROFILE%\.minerva\skills`) |
| **🔌 MCPs Globais Sincronizados** | `~/.minerva/mcp_config.json` → `~/.gemini/mcp_config.json` & `~/.claude.json` |
| **📊 Painel de Agentes (`:3333`)** | `~/.minerva/tools/painel-agents` → `http://localhost:3333` |
| **📋 Kanban Minimalista (`:3334`)** | `~/.minerva/tools/kanban-agents` → `http://localhost:3334` |

E finalize com a instrução para usar em projetos:
> *"Para iniciar um projeto: abra a pasta do projeto, selecione primeiro a **Persona Minerva (Orquestrador Central)** no terminal principal e digite **`/minerva`**."*
