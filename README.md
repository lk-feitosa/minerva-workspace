<div align="center">

<img src="assets/logo.png" alt="Minerva Logo" width="200" style="border-radius: 20px; box-shadow: 0 8px 24px rgba(0,0,0,0.4);" />

# Minerva & AI Agents Ecosystem

**Init Unificado para Múltiplos Agentes de IA (`/minerva`), Raiz Global Única (`~/.minerva`), Economia de Contexto por Projeto & Cofre PT-BR para Obsidian.**

🌐 **[Português](README.md)** | **[English](README.en.md)**

[![Platform: Windows | Linux | macOS](https://img.shields.io/badge/platform-Windows%20|%20Linux%20|%20macOS-informational.svg?style=flat-square)](#-instalação-rápida-cross-platform)
[![skills.sh](https://img.shields.io/badge/skills.sh-minerva--workspace-blue.svg?style=flat-square)](skills/)
[![Obsidian Ready](https://img.shields.io/badge/obsidian-vault%20PT--BR-purple.svg?style=flat-square)](vault/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg?style=flat-square)](LICENSE)

</div>

---

## 💡 Por que este projeto existe?

O ecossistema de IA muda toda semana e cada CLI ou editor cria sua própria pasta isolada (`~/.claude`, `~/.codex`, `~/.gemini`, `~/.agents`). Para quem está **começando agora** — ou alterna entre vários modelos no dia a dia — isso obriga a **baixar as mesmas skills repetidas vezes, reconfigurar MCPs e repetir regras em cada ferramenta e projeto**.

O **`minerva-workspace`** nasceu para ser esse **`init` centralizado em `~/.minerva`**:

1. **Uma única raiz global (`~/.minerva` / `%USERPROFILE%\.minerva`):** você instala uma vez e o instalador vasculha skills antigas já presentes no PC (movendo sem duplicar), baixa todas as skills curadas do projeto via `skills.sh` e conecta **Claude Code**, **Codex**, **Antigravity / Gemini CLI** e **Maestri** para apontarem para o mesmo lugar.
2. **Ativação completa por projeto (`/minerva`):** fora de um repositório seu terminal segue limpo; dentro de qualquer projeto, digitar **`/minerva`** executa todo o bootstrap de governança (`.gitignore`, `.agents/`, `docs/`, `ai-memory`, `.kanban/board.json`, Painel `:3333` + Kanban `:3334`, Portais no Maestri e economia de contexto local).
3. **Zero reescrita de docs de terceiros:** as skills públicas vêm direto do catálogo oficial **`skills.sh`**, e os apps companheiros mantêm sua documentação completa nos respectivos repositórios oficiais.

---

## Estrutura Global (`~/.minerva`)

```text
~/.minerva/ (ou %USERPROFILE%\.minerva -> raiz do repositório)
│
├── 📁 skills/                         <-- Todas as skills centralizadas (3 autorais + 188 via skills.sh)
├── 📁 templates/project/              <-- Modelos do /minerva (.agents/, docs/, .kanban/, .mcp.json, rtk)
├── 📄 skills-manifest.json            <-- Lista única oficial de skills (sem divisão core/full)
├── 📄 mcp_config.json                 <-- Configuração base de servidores MCP
├── 📁 toolkits/                       <-- Vibe Coding Toolkit, agent_sort.py & statusline
├── 📁 vault/                          <-- Cofre direto do Obsidian (100% PT-BR)
│   ├── 📄 _Hub de Skills & MCPs.md
│   ├── 📄 _Arquitetura e Documentação do Ecossistema.md
│   ├── 📄 _Guia de Replicação em Novo PC.md
│   ├── 📁 Workspace/                  <-- Orquestração Minerva, Conselho & Team CODES
│   ├── 📁 Skills/                     <-- Notas resumidas PT-BR (inclui painel-agents & kanban-agents) + 7 Hubs
│   ├── 📁 MCP/                        <-- Manuais (ai-memory, rea, agent-desktop, magicpath, context-mode)
│   ├── 📁 MODS/                       <-- vibe-coding-toolkit & ai-statusline
│   └── 📁 Frameworks/                 <-- Bibliotecas de agentes (alethe, claude-cookbooks, etc.)
│
├── 📄 setup.bat                       <-- Instalador Windows (CMD)
├── 📄 setup.ps1                       <-- Instalador Windows (PowerShell)
└── 📄 setup.sh                        <-- Instalador Linux & macOS
```

---

## Instalação Rápida (Cross-Platform)

### Passo 1 — Clonar & rodar o Setup Global (1 comando):

**Windows (PowerShell):**
```powershell
git clone https://github.com/lk-feitosa/minerva-workspace.git $HOME\.minerva
cd $HOME\.minerva
.\setup.ps1
```
*(Ou `setup.bat` no CMD).*

**Linux / macOS:**
```bash
git clone https://github.com/lk-feitosa/minerva-workspace.git ~/.minerva
cd ~/.minerva
chmod +x setup.sh && ./setup.sh
```

**O que o instalador faz automaticamente:**
1. Vasculha skills antigas em `~/.claude/skills`, `~/.codex/skills`, `~/.gemini/config/skills` e `~/.agents/skills`, movendo para `~/.minerva/skills` sem duplicar.
2. Usa `~/.minerva` como raiz canônica única e conecta todos os CLIs para `~/.minerva/skills` via junction/symlink.
3. Instala todas as skills curadas do `skills-manifest.json` via `npx skills add` e verifica/clona `painel-agents` e `kanban-agents`.

*(Entrada alternativa via CLI oficial: `npx skills add lk-feitosa/minerva-workspace` — e depois rode `/minerva` no terminal para completar a base global).*

---

## O que `/minerva` faz ao rodar em um Projeto

Ao abrir qualquer projeto no terminal (**Claude Code**, **Codex**, **Gemini CLI**, **Antigravity** ou **Maestri**) e digitar **`/minerva`**, ele substitui prompts longos manuais executando automaticamente:

1. **Blindagem do Git (`.gitignore`):** garante que `.maestri/`, `.kanban/`, `.agents/cache/`, `.ai-memory/cache/`, `graphify-out/`, `*.session`, `*.tmp` e builds/env nunca sejam commitados.
2. **Governança `.agents/` + Economia Local:** cria `.agents/AGENTS.md`, `.agents/MINERVA.md` (10 Leis Fundamentais) e `.agents/roles/` (`front-end`, `back-end`, `test-qa`, `review`), configura `.mcp.json` (`context-mode` + `ai-memory`) e ativa hook local do `rtk` em `.claude/settings.local.json` (se instalado).
3. **Documentação Viva (`docs/`):** cria `docs/spec.md`, `docs/architecture.md` e `docs/adr/`.
4. **Memória, Kanban & Portais no Maestri:** inicializa `ai-memory`, cria `.kanban/board.json` (5 colunas), sobe **Painel (`:3333`)** + **Kanban (`:3334`)** em background e abre ambos os Portais automaticamente no Maestri (`maestri portal create`).
5. **Fluxo Padrão vs. Stress-Test vs. Fast-Track:** execução ágil direta por padrão; `[GRILL-ME]` / `[CONSELHO]` acionam Grill-Me + Conselho dos 5 sob demanda; micro-ajustes vão direto em 1 linha.
6. **Branches Semânticas & Terminais sem Bloqueio:** proíbe `sprint-1`/`sprint-2`, usa `feature/<slug>` / `fix/<slug>` no `cwd` real do projeto.
7. **Delegação Consultiva Multi-Modelo (`alethe` + `maestri`):** consulta contas/cotas reais antes de abrir terminais do Team CODES e pede sua confirmação antes de recrutar.

---

## Como Abrir o Cofre no Obsidian

1. Abra o **Obsidian** e clique em **"Open folder as vault"**.
2. Selecione **`~/.minerva/vault`** (ou `<PASTA_DO_REPO>/vault`).
3. Comece por **`_Hub de Skills & MCPs.md`** e **`Workspace/Orquestração de Projetos - Minerva & Conselho.md`**.

---

## 🧩 Adicionais Oficiais & Repositórios Parceiros

Documentação completa de instalação e recursos avançados vive nos repositórios oficiais:

| Projeto | Porta | Papel no Ecossistema | Repositório Oficial |
| :--- | :--- | :--- | :--- |
| **Painel de Agentes** | `127.0.0.1:3333` | Telemetria passiva, cotas 3D, logs e grafo de arquitetura ao vivo | [`lk-feitosa/painel-agents`](https://github.com/lk-feitosa/painel-agents) |
| **Kanban Agents** | `127.0.0.1:3334` | Quadro ágil minimalista offline salvo em `.kanban/board.json` por projeto | [`lk-feitosa/kanban-agents`](https://github.com/lk-feitosa/kanban-agents) |

---

## Créditos, Atribuições & Licenças

Todos os direitos de propriedade intelectual, marcas e códigos de terceiros pertencem integralmente aos seus respectivos autores originais. Lista completa com links oficiais em:  
👉 **[CREDITS.pt-br.md](CREDITS.pt-br.md)** *(English: [CREDITS.md](CREDITS.md))*
