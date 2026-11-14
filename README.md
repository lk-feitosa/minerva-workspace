<div align="center">

<img src="assets/logo.png" alt="Minerva Logo" width="200" style="border-radius: 20px; box-shadow: 0 8px 24px rgba(0,0,0,0.4);" />

# Minerva & AI Agents Ecosystem

**Init Unificado para Múltiplos Agentes de IA (`/minerva`), Base Portátil via `skills.sh`, Economia de Contexto por Projeto & Cofre PT-BR para Obsidian.**

🌐 **[Português](README.md)** | **[English](README.en.md)**

[![Platform: Windows | Linux | macOS](https://img.shields.io/badge/platform-Windows%20|%20Linux%20|%20macOS-informational.svg?style=flat-square)](#-instalação-rápida-cross-platform)
[![skills.sh](https://img.shields.io/badge/skills.sh-minerva--workspace-blue.svg?style=flat-square)](skills/)
[![Obsidian Ready](https://img.shields.io/badge/obsidian-vault%20PT--BR-purple.svg?style=flat-square)](vault/Agentes/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg?style=flat-square)](LICENSE)

</div>

---

## 💡 Por que este projeto existe?

O ecossistema de IA muda toda semana e cada CLI ou editor cria sua própria pasta isolada (`~/.claude`, `~/.codex`, `~/.gemini`, `~/.agents`). Para quem está **começando agora** — ou alterna entre vários modelos no dia a dia — isso obriga a **baixar as mesmas skills repetidas vezes, reconfigurar MCPs e repetir regras em cada ferramenta e projeto**.

O **`minerva-workspace`** nasceu para ser esse **`init` centralizado**:

1. **Uma única base global:** você clona ou instala uma vez e conecta **Claude Code**, **Codex**, **Antigravity / Gemini CLI** e **Maestri** para enxergarem exatamente o mesmo diretório de skills e MCPs (via *junctions*/*symlinks*, sem cópias espalhadas).
2. **Ativação limpa por projeto (`/minerva`):** fora de um projeto seu terminal segue normal; dentro de qualquer pasta de código, digitar `/minerva` ativa economia de tokens, painéis locais e fluxo organizado só para aquele workspace.
3. **Zero reescrita de docs de terceiros:** as skills públicas vêm direto do catálogo oficial **`skills.sh`**, e cada ferramenta mantém sua documentação oficial no respectivo repositório.

---

## Visão Geral da Estrutura

```text
minerva-workspace/                     <-- Raiz Única do Repositório
│
├── 📁 skills/                         <-- Skills Autorais (minerva, painel-agents, kanban-agents)
├── 📁 templates/project/              <-- Templates por projeto (.mcp.json, AGENTS.md, hook local rtk)
├── 📄 skills-manifest.json            <-- Catálogo curado skills.sh (core: 35 | full: 188)
├── 📄 mcp_config.json                 <-- Configuração base de servidores MCP
├── 📁 toolkits/                       <-- Vibe Coding Toolkit & statusline
├── 📁 vault/Agentes/                  <-- Cofre enxuto PT-BR do Obsidian (7 Hubs + tags #category/*)
├── 📄 setup.bat                       <-- Instalador Windows (CMD)
├── 📄 setup.ps1                       <-- Instalador Windows (PowerShell)
└── 📄 setup.sh                        <-- Instalador Linux & macOS
```

---

## Instalação Rápida (Cross-Platform)

### Opção 1 — Entrada rápida via `skills.sh`:
```bash
npx skills add lk-feitosa/minerva-workspace
```
Abra seu agente (**Claude Code**, **Codex**, **Gemini CLI** ou **Antigravity**) em qualquer pasta e digite **`/minerva`** — a própria skill conclui o setup global (se faltar) e inicializa o projeto.

### Opção 2 — Clone + Base Global Completa (1 comando):

**Windows (PowerShell):**
```powershell
git clone https://github.com/lk-feitosa/minerva-workspace.git ~/DEV/minerva-workspace
cd ~/DEV/minerva-workspace
.\setup.ps1
```
*(Ou `setup.bat` no CMD. Use `.\setup.ps1 -Profile full` para instalar também o catálogo estendido da comunidade).*

**Linux / macOS:**
```bash
git clone https://github.com/lk-feitosa/minerva-workspace.git ~/DEV/minerva-workspace
cd ~/DEV/minerva-workspace
chmod +x setup.sh && ./setup.sh
```
*(Use `./setup.sh --full` para o catálogo estendido).*

O instalador cria os links globais (`~/.agents`, `~/.codex/skills`, `~/.claude/skills` e `~/.gemini/config/skills`), instala o perfil **`core`** (**35 skills curadas** do `skills.sh` + **3 autorais**) e verifica os repositórios companheiros.

---

## Arquitetura: `/minerva`, Economia & Orquestração

* **Minerva (`/minerva`):** Prepara apenas o projeto atual (`.mcp.json`, `AGENTS.md`, `.kanban/board.json`) e coordena múltiplos agentes em branches semânticas (`feature/<slug>`, `fix/<slug>`).
* **Conselho dos 5 (`llm-council`) + `grill-me`:** Refinamento crítico sob demanda antes de implementar decisões arquiteturais complexas.
* **Economia de Contexto no Workspace:**
  * [`context-mode`](https://github.com/mksglu/context-mode) *(MCP local no projeto)* — tira logs e leituras grandes da janela do modelo.
  * [`ponytail`](https://github.com/DietrichGebert/ponytail) *(skill no `core`)* — prioriza o menor diff limpo possível.
  * [`rtk`](https://github.com/rtk-ai/rtk) *(hook local opcional em `.claude/settings.local.json`)* — enxuga saídas verbosas do terminal no projeto.
  * [`graphify`](https://github.com/Graphify-Labs/graphify) *(CLI AST opcional)* — gera grafo local do código (`graphify-out/`) para evitar buscas repetitivas.
* **Stack UI/Design pronta (`#category/design`):** `design-taste-frontend`, `awesome-design-md` ([VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md)), `transitions-dev` + `transitions-polish` ([transitions.dev](https://github.com/Jakubantalik/transitions.dev)), `shadcn` + registry `@react-bits` ([react-bits](https://github.com/DavidHDev/react-bits)), `magicpath` e `vercel-react-best-practices`.
* **Guia completo no Obsidian:** abra `<PASTA_DO_REPO>/vault/Agentes` como cofre e comece por `_Hub de Skills & MCPs.md` e `Workspace/Orquestração de Projetos - Minerva & Conselho.md`.

### Gerenciando Skills via `skills.sh`
```bash
npx skills find <termo>        # Descobre novas skills no catálogo oficial
npx skills update -g            # Atualiza suas skills globais instaladas
```

---

## 🧩 Adicionais Oficiais & Repositórios Parceiros

Ferramentas complementares integradas automaticamente pelo `/minerva` *(documentação completa e detalhes técnicos ficam nos próprios repositórios oficiais)*:

| Projeto | Porta / Escopo | Papel no Ecossistema | Repositório Oficial |
| :--- | :--- | :--- | :--- |
| **Painel de Agentes** | `127.0.0.1:3333` | Telemetria em tempo real, cotas 3D, logs e grafo de arquitetura ao vivo | [`lk-feitosa/painel-agents`](https://github.com/lk-feitosa/painel-agents) |
| **Kanban Agents** | `127.0.0.1:3334` | Quadro ágil minimalista offline gravado em `.kanban/board.json` por projeto | [`lk-feitosa/kanban-agents`](https://github.com/lk-feitosa/kanban-agents) |

---

## Configuração Automática via Agente de IA (Opcional)

Se preferir que seu próprio agente (**Claude Code**, **Codex**, **Gemini CLI**, **Antigravity** ou **Cursor**) configure a máquina após o `git clone`, cole o prompt abaixo:

```text
Você acabou de receber o repositório minerva-workspace clonado nesta máquina.
Detecte meu sistema operacional e rode o instalador nativo (`.\setup.ps1` no Windows ou `./setup.sh` no Linux/macOS) para criar os links globais (~/.agents, ~/.codex/skills, ~/.claude/skills, ~/.gemini/config/skills), instalar o perfil 'core' de `skills-manifest.json` e validar os pré-requisitos (Git, Node.js, Python 3). Ao final, confirme onde está o cofre do Obsidian (`vault/Agentes`) e o status de cada etapa.
```

---

## Créditos, Atribuições & Licenças

Todos os direitos de propriedade intelectual, marcas e códigos de terceiros pertencem integralmente aos seus respectivos autores originais. Lista completa com links oficiais em:  
👉 **[CREDITS.pt-br.md](CREDITS.pt-br.md)** *(English: [CREDITS.md](CREDITS.md))*
