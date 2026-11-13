<div align="center">

<img src="assets/logo.png" alt="Minerva Logo" width="200" style="border-radius: 20px; box-shadow: 0 8px 24px rgba(0,0,0,0.4);" />

# Minerva & AI Agents Ecosystem

**Hub Unificado de Orquestração Multi-Agente (`/minerva`), Base Portátil (`skills.sh`), Economia de Contexto por Projeto, Servidores MCP & Cofre PT-BR para Obsidian.**

🌐 **[Português](README.md)** | **[English](README.en.md)**

[![Platform: Windows | Linux | macOS](https://img.shields.io/badge/platform-Windows%20|%20Linux%20|%20macOS-informational.svg?style=flat-square)](#-instalação-rápida-cross-platform)
[![skills.sh](https://img.shields.io/badge/skills.sh-minerva--workspace-blue.svg?style=flat-square)](skills/)
[![Obsidian Ready](https://img.shields.io/badge/obsidian-vault%20PT--BR-purple.svg?style=flat-square)](vault/Agentes/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg?style=flat-square)](LICENSE)

</div>

---

## Visão Geral

Este repositório centraliza toda a infraestrutura agêntica de desenvolvimento, integrando inteligências artificiais líderes de mercado (**Antigravity / Gemini CLI**, **Claude Code**, **Codex** e **Maestri Canvas**) sob uma arquitetura híbrida:

* **Base Global Única (`skills` + `setup`):** mantém suas skills leves e centralizadas via junctions/symlinks (sem duplicar por agente ou projeto) usando o **`skills.sh`** como fonte oficial.
* **Ativação por Workspace (`/minerva`):** dentro de qualquer projeto no terminal, `/minerva` ativa apenas ali a economia de contexto (**Context Mode**, **Ponytail**, **RTK** local, **Graphify** opcional) e inicia **Painel (`:3333`) + Kanban (`:3334`)**, mantendo o resto da máquina limpo.

```text
minerva-workspace/                     <-- Raiz Única do Repositório
│
├── 📁 skills/                         <-- Skills Autorais (minerva, painel-agents, kanban-agents)
├── 📁 templates/project/              <-- Modelos portáteis (.mcp.json, AGENTS.md, hook local rtk)
├── 📄 skills-manifest.json            <-- Catálogo curado skills.sh (perfis core e full)
├── 📄 mcp_config.json                 <-- Configuração base de servidores MCP
├── 📁 toolkits/                       <-- Vibe Coding Toolkit & scripts (statusline)
├── 📁 vault/Agentes/                  <-- Cofre enxuto 100% em PT-BR do Obsidian
│   ├── 📁 Workspace/                  <-- Arquitetura Minerva, Conselho & Team CODES
│   ├── 📁 Skills/                     <-- Notas resumidas PT-BR + 7 Hubs de Categoria
│   ├── 📁 MCP/                        <-- Manuais (ai-memory, rea, agent-desktop, magicpath)
│   ├── 📁 MODS/                       <-- Toolkits curados (vibe-coding-toolkit)
│   ├── 📁 Frameworks/                 <-- Bibliotecas de agentes (alethe, claude-cookbooks, etc.)
│   ├── 📁 Opcionais/                  <-- Ferramentas de apoio (painel-agents, kanban-agents, ai-statusline)
│   └── 📄 _Hub de Skills & MCPs.md    <-- Dashboard de navegação do cofre
│
├── 📄 setup.bat                       <-- Instalador 1-click para Windows (CMD)
├── 📄 setup.ps1                       <-- Instalador 1-click para Windows (PowerShell)
└── 📄 setup.sh                        <-- Instalador 1-click para Linux e macOS
```

---

## Instalação Rápida (Cross-Platform)

Você pode instalar direto pelo **`skills.sh`** ou clonar o repositório completo para montar a base global com um comando.

### Via `skills.sh` (Início Rápido):

```bash
npx skills add lk-feitosa/minerva-workspace
```
Em seguida, abra seu agente (**Claude Code**, **Codex**, **Gemini CLI** ou **Antigravity**) e digite **`/minerva`** — a própria skill ajuda a finalizar o setup global ou inicializar o workspace do projeto atual.

---

### No Windows:

Abra o PowerShell (ou Prompt de Comando) e execute:
```powershell
git clone https://github.com/lk-feitosa/minerva-workspace.git ~/DEV/minerva-workspace
cd ~/DEV/minerva-workspace
.\setup.ps1
```
*(Ou via CMD: `setup.bat`. Use `.\setup.ps1 -Profile full` para instalar também o catálogo estendido da comunidade).*

O script cria automaticamente os NTFS Junctions vinculando o repositório aos caminhos padrão dos agentes (`~/.agents`, `~/.codex/skills`, `~/.claude/skills` e `~/.gemini/config/skills`) e instala o perfil **`core`** curado do `skills.sh`.

---

### No Linux ou macOS:

Abra o terminal e execute:
```bash
git clone https://github.com/lk-feitosa/minerva-workspace.git ~/DEV/minerva-workspace
cd ~/DEV/minerva-workspace
chmod +x setup.sh
./setup.sh
```
*(Use `./setup.sh --full` para instalar o catálogo estendido).*

O script cria os links simbólicos necessários (`~/.agents`, `~/.codex/skills`, `~/.claude/skills` e `~/.gemini/config/skills`), baixa o pacote curado do `skills.sh` e verifica os repositórios companheiros.

---

## Como Abrir o Cofre no Obsidian

1. Abra o aplicativo **Obsidian**.
2. Clique em **"Open folder as vault"** (Abrir pasta como cofre).
3. Selecione o diretório:
   * **No Windows:** `<PASTA_DO_REPO>\vault\Agentes` (ou `%USERPROFILE%\.agents\vault\Agentes`)
   * **No Linux/Mac:** `<PASTA_DO_REPO>/vault/Agentes` (ou `~/.agents/vault/Agentes`)
4. Pronto! O cofre abrirá com:
   * **Excalidraw** pré-configurado em Dark Mode.
   * Plugins essenciais ativos.
   * Dashboard interativo em `_Hub de Skills & MCPs.md` e 7 Hubs de Categoria no Grafo.
   * Nota mestra em `Workspace/Orquestração de Projetos - Minerva & Conselho.md`.

### Gerenciando Skills via `skills.sh`
```bash
npx skills find <termo>        # Descobre novas skills no catálogo oficial skills.sh
npx skills update -g            # Atualiza as skills globais instaladas
```

---

## Arquitetura de Orquestração: Minerva, Economia & Team CODES

Consulte a documentação completa no Obsidian em:  
👉 **`Workspace/Orquestração de Projetos - Minerva & Conselho.md`**

* **Minerva (`/minerva`):** Orquestrador Central que prepara o workspace atual, ativa economia de tokens e coordena múltiplos agentes/terminais em branches semânticas (`feature/<slug>`, `fix/<slug>`).
* **Conselho dos 5 (`llm-council`) + `grill-me`:** Contrário, Primeiros Princípios, Expansionista, Forasteiro e Executor acionados sob demanda antes de codar decisões críticas.
* **Economia de Contexto no Projeto:** **Context Mode** (`npx -y context-mode` no `.mcp.json` local), **Ponytail** (edições mínimas), **RTK** (hook local opcional em `.claude/settings.local.json`) e **Graphify** (grafo AST opcional).
* **Team CODES:** Pipeline de engenharia de 12 papéis (`spec`, `plan`, `dev`, `front-end`, `back-end`, `test`, `qa`, `qualidade`, `webperf`, `code-simpl`, `review`, `ship`).

---

## 🧩 Adicionais Oficiais para o Ecossistema (Iniciam com `/minerva`)

1. **📊 [Painel de Agentes (`painel-agents`)](https://github.com/lk-feitosa/painel-agents):**
   * **Porta Local:** `http://127.0.0.1:3333/`
   * **O que oferece:**
     * **Monitoramento e Cotas 3D:** Leituras de capacidade de 5h e semanal (Antigravity / Gemini, Claude Code, Codex) com sincronização de missões.
     * **Feed de Logs de Atividades ao Vivo (`📜 Logs`):** Linha do tempo cronológica de demandas, atualizações do Kanban e delegações.
     * **Live Architecture Graph (`🗺️ Arquitetura`):** Grafo interativo em tempo real (SVG 60 FPS) com destaque de arquivos alterados recentemente (< 15 min) e despacho de missões.
   * **Como abrir no Maestri:** `maestri portal create http://localhost:3333 "Painel de Agentes"`

2. **📋 [Kanban para Agentes (`kanban-agents`)](https://github.com/lk-feitosa/kanban-agents):**
   * **Porta Local:** `http://127.0.0.1:3334/`
   * **O que oferece:**
     * **Quadro Ágil Minimalista:** Leve (< 20 MB RAM, zero Docker, zero login), sincronizado em `.kanban/board.json` na raiz de cada projeto.
     * **Ciclos & Sprints:** Alternância entre quadro ativo e sprints arquivadas com arquivamento em 1 clique.
     * **Preservação de Scroll & Anti-Colisão:** Troca automática de porta se `3334` estiver ocupada.
   * **Como abrir no Maestri:** `maestri portal create http://localhost:3334 "Kanban"`

---

## Configuração Automática via Agente de IA (Prompt de Setup)

Se você utiliza um assistente de IA no terminal ou editor (**Antigravity**, **Claude Code**, **Codex** ou **Cursor**) e prefere que o próprio agente configure o ambiente para esta arquitetura global, clone o repositório e cole o prompt abaixo:

```text
Você é o meu assistente de IA configurando este computador.
Acabei de clonar o ecossistema Minerva Workspace (minerva-workspace) nesta máquina.
Por favor, configure o meu ambiente para operar nesta arquitetura global unificada:

1. Identifique o meu Sistema Operacional (Windows / Linux / macOS) e a pasta onde este repositório foi clonado.
2. Execute o setup nativo (`.\setup.ps1` no Windows ou `./setup.sh` no Linux/macOS) — ou crie os links globais apontando para o repositório:
   - Windows (NTFS Junctions):
     * %USERPROFILE%\.agents -> [caminho_deste_repositorio]
     * %USERPROFILE%\.codex\skills -> [caminho_deste_repositorio]\skills
     * %USERPROFILE%\.claude\skills -> [caminho_deste_repositorio]\skills
     * %USERPROFILE%\.gemini\config\skills -> [caminho_deste_repositorio]\skills
   - Linux / macOS (ln -s):
     * ~/.agents -> [caminho_deste_repositorio]
     * ~/.codex/skills -> [caminho_deste_repositorio]/skills
     * ~/.claude/skills -> [caminho_deste_repositorio]/skills
     * ~/.gemini/config/skills -> [caminho_deste_repositorio]/skills
3. Valide se Node.js, Python 3 e Git estão presentes no PATH e se o perfil 'core' de skills foi instalado via `skills-manifest.json`.
4. Confirme que o cofre do Obsidian está localizado em 'vault/Agentes' e apresente um resumo claro com o status de cada item configurado.
```

---

## Créditos, Atribuições & Licenças

Este projeto é um ecossistema integrador. Todos os direitos de propriedade intelectual, marcas e códigos de terceiros pertencem aos seus respectivos criadores originais (Anthropic, Vercel Labs, Fabio Akita, DietrichGebert, mksglu, rtk-ai, Graphify Labs, Addy Osmani, Matt Pocock, Affaan M, Composio, etc.).

Consulte a lista completa com os links para os repositórios originais em:  
👉 **[CREDITS.pt-br.md](CREDITS.pt-br.md)** *(English version: [CREDITS.md](CREDITS.md))*
