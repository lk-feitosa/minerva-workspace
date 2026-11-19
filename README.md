<div align="center">

<img src="assets/logo.png" alt="Minerva Logo" width="200" style="border-radius: 20px; box-shadow: 0 8px 24px rgba(0,0,0,0.4);" />

# Minerva & AI Agents Ecosystem

**Init Unificado para Múltiplos Agentes de IA (`/minerva-setup` & `/minerva`), Raiz Global Única (`~/.minerva`), Economia de Contexto por Projeto & Cofre PT-BR para Obsidian.**

**[Português](README.md)** | **[English](README.en.md)**

[![Platform: Windows | Linux | macOS](https://img.shields.io/badge/platform-Windows%20|%20Linux%20|%20macOS-informational.svg?style=flat-square)](#-instalação-no-pc-1x-por-máquina)
[![skills.sh](https://skills.sh/b/lk-feitosa/minerva-workspace)](https://skills.sh/lk-feitosa/minerva-workspace)
[![Obsidian Ready](https://img.shields.io/badge/obsidian-vault%20PT--BR-purple.svg?style=flat-square)](vault/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg?style=flat-square)](LICENSE)

</div>

---

## Por que este projeto existe?

O ecossistema de IA muda toda semana e cada CLI ou editor cria sua própria pasta isolada (`~/.claude`, `~/.codex`, `~/.gemini`, `~/.agents`). Para quem está começando agora — ou alterna entre vários modelos no dia a dia — isso obriga a baixar as mesmas skills repetidas vezes, reconfigurar MCPs e repetir regras em cada ferramenta e projeto.

O **`minerva-workspace`** foi criado para ser esse **`init` centralizado em `~/.minerva`**:

1. **Raiz global única (`~/.minerva` / `%USERPROFILE%\.minerva`):** você instala uma vez via **`/minerva-setup`** (ou `setup.ps1`/`setup.sh`) e o instalador vasculha **skills e MCPs antigos** já presentes no PC (migrando e mesclando sem duplicar), baixa todas as skills curadas via `skills.sh` e conecta **Claude Code**, **Codex**, **Antigravity / Gemini CLI** e **[Maestri](https://www.themaestri.app/pt-br)** para apontarem para o mesmo diretório.
2. **Ativação completa por projeto (`/minerva`):** fora de um repositório seu terminal segue limpo; ao abrir qualquer projeto, basta selecionar a **Persona Minerva** e digitar **`/minerva`** para rodar o bootstrap determinístico (`minerva_bootstrap.py`: `.gitignore`, `.agents/`, `docs/`, `.mcp.json`, `rtk`, `ponytail`, `ai-memory`, `.kanban/board.json`, Painel `:3333` + Kanban `:3334` e Portais no Maestri).
3. **Orquestração multi-modelo (Anti-Monocultura + Failover Automático de IA):** ao delegar demandas para o **Team CODES**, a Minerva consulta diretamente os CLIs instalados para escolher o melhor modelo por papel de acordo com suas **contas e cotas reais** (sem abrir um time inteiro na mesma IA) e, se um terminal falhar, **troca automaticamente para outra IA disponível** e repassa a demanda (sem dar erro e sem codar sozinha).

---

## Comandos da Skill (`skills.sh`)

Ao instalar pelo `skills.sh` (`npx skills add lk-feitosa/minerva-workspace -g -y`), você recebe **4 comandos (`/` commands)**:

| Comando | Onde Usar | Função |
| :--- | :--- | :--- |
| **`/minerva-setup`** | **1x no PC** (Qualquer terminal) | Clona/atualiza `~/.minerva`, migra skills e MCPs antigos sem duplicar, cria junctions nos CLIs e baixa todo o catálogo + `painel-agents` e `kanban-agents`. |
| **`/minerva`** | **No Workspace de cada Projeto** | *(Usar após selecionar a Persona Minerva)* Inicializa o projeto (`minerva_bootstrap.py`) e ativa orquestração com economia de tokens, Conselho/Grill-Me e Team CODES. |
| **`/painel-agents`** | Projeto / Global | Abre, consulta cotas ou faz auto-heal do **Painel de Agentes** (`http://127.0.0.1:3333`). |
| **`/kanban-agents`** | Projeto | Abre ou gerencia o **Kanban Minimalista** do projeto (`http://127.0.0.1:3334` / `.kanban/board.json`). |

---

## Estrutura Global (`~/.minerva`)

```text
~/.minerva/ (ou %USERPROFILE%\.minerva -> raiz única no PC)
│
├── skills/                            <-- Todas as skills centralizadas (4 autorais + 17 pacotes via skills.sh)
│   ├── minerva-setup/                 <-- /minerva-setup (Configuração global do PC)
│   ├── minerva/                       <-- /minerva (Bootstrap & orquestração de workspace de projeto)
│   ├── painel-agents/                 <-- /painel-agents (Painel :3333)
│   └── kanban-agents/                 <-- /kanban-agents (Kanban :3334)
├── templates/project/                 <-- Modelos do /minerva (.agents/, docs/, .kanban/, .mcp.json, rtk)
├── skills-manifest.json               <-- Lista única oficial de skills (sem divisão core/full)
├── mcp_config.json                    <-- Servidores MCP globais (ai-memory, rea, agent-desktop)
├── toolkits/                          <-- minerva_bootstrap.py, minerva_quotas.py, agent_sort.py & statusline
├── vault/                             <-- Cofre direto do Obsidian (100% PT-BR)
│   ├── _Hub de Skills & MCPs.md
│   ├── _Arquitetura e Documentação do Ecossistema.md
│   ├── _Guia de Replicação em Novo PC.md
│   ├── Workspace/                     <-- Orquestração Minerva, Conselho & Team CODES
│   ├── Skills/                        <-- Notas resumidas PT-BR + 7 Hubs de Categoria
│   ├── MCP/                           <-- Manuais (ai-memory, rea, agent-desktop, context-mode)
│   ├── MODS/                          <-- vibe-coding-toolkit & ai-statusline
│   └── Frameworks/                    <-- Bibliotecas de agentes (alethe, claude-cookbooks, etc.)
│
├── setup.bat                          <-- Instalador Windows (CMD)
├── setup.ps1                          <-- Instalador Windows (PowerShell)
└── setup.sh                           <-- Instalador Linux & macOS
```

---

## Instalação no PC (1x por Máquina)

### Opção A — Via `skills.sh` + `/minerva-setup`:
```bash
npx skills add lk-feitosa/minerva-workspace -g -y
```
Em seguida, abra seu agente no terminal e digite **`/minerva-setup`**.

### Opção B — Clone Direto + Script Nativo:

**Windows (PowerShell):**
```powershell
git clone https://github.com/lk-feitosa/minerva-workspace.git $HOME\.minerva
cd $HOME\.minerva
.\setup.ps1
```

**Linux / macOS:**
```bash
git clone https://github.com/lk-feitosa/minerva-workspace.git ~/.minerva
cd ~/.minerva
chmod +x setup.sh && ./setup.sh
```

**O que o `/minerva-setup` (`setup.ps1` / `setup.sh`) faz automaticamente:**
1. **Migra Skills sem duplicar:** vasculha `~/.claude/skills`, `~/.codex/skills`, `~/.gemini/config/skills` e `~/.agents/skills`, movendo para `~/.minerva/skills` e descartando cópias repetidas.
2. **Sincroniza MCPs Globais sem duplicar:** mescla os MCPs globais (`ai-memory`, `rea`, `agent-desktop`) em `~/.gemini/mcp_config.json` e `~/.claude.json` preservando qualquer MCP que você já tenha configurado (enquanto o `context-mode` fica isolado no `.mcp.json` de cada projeto).
3. **Instala todo o catálogo:** baixa os 17 pacotes do `skills-manifest.json` via `npx skills add` e verifica/clona `painel-agents` e `kanban-agents` em `~/.minerva/tools/`.

---

## Como Usar em um Novo Projeto (Passo a Passo)

Sempre que abrir um projeto novo ou existente:

1. **Passo 1 — Configure a Persona Minerva:** no terminal principal do projeto (especialmente no **[Maestri Canvas](https://www.themaestri.app/pt-br)**), selecione primeiro a responsabilidade/persona **"Minerva - Orquestrador Central"**.
2. **Passo 2 — Rode `/minerva`:** digite **`/minerva`** no terminal do projeto.

### O que `/minerva` executa no workspace:
1. **Bootstrap em 1 comando (`minerva_bootstrap.py`):** blinda `.gitignore`, cria `.agents/` (`AGENTS.md`, `MINERVA.md`, `roles/`), `docs/` (`spec.md`, `architecture.md`, `adr/`), `.kanban/board.json` e classifica as skills do projeto em `.agents/skills.json` (**DAILY vs. LIBRARY** via `agent_sort.py`).
2. **Economia de Tokens Ativa:** configura `.mcp.json` local (`context-mode` + `ai-memory`), ativa o hook local do `rtk` em `.claude/settings.local.json` (se instalado) e aplica a skill **`ponytail`** (diffs mínimos, sem código especulativo).
3. **Painel (`:3333`), Kanban (`:3334`) & Portais no Maestri:** sobe os dois servidores em background e abre automaticamente as duas janelas de Portal no Maestri.
4. **Todos os Modelos & Cotas Direto dos CLIs + Política Tier N-1 (`minerva_quotas.py` — Anti-Monocultura):** consulta diretamente os CLIs instalados no PC (`agy`, `codex`, `claude`) para listar **todos os modelos disponíveis** e escolhe por padrão o **Tier N-1 / modelo do dia a dia** de cada conta (ex.: `Hydrogen` abaixo do `Neon`/`Argon` no Gemini; `Sonnet` abaixo do `Fable`/`Opus` no Claude; esforço `medium` no Codex), reservando o modelo mais top apenas para quando você especificar (`--top-tier`), **sem abrir um time inteiro da mesma IA**.
5. **Gate Obrigatório de Backlog + Arquivamento de Sprint Anterior (`--archive-sprint`):** ao receber uma demanda, arquiva o sprint anterior em `.kanban/archive/`, cria **todo o Backlog de tasks em `.kanban/board.json`** e **aguarda sua aprovação do Backlog ("OK")** antes de o Team CODES iniciar qualquer task.
6. **Descoberta e Injeção de Skills por Demanda (`agent_sort.py --match` + `find-skills`):** além das skills do papel (`.agents/roles/`) e da stack (`.agents/skills.json`), procura skills locais instantaneamente com `agent_sort.py --match "<demanda>"` ou busca novas skills na comunidade via **`find-skills`** (`npx skills find <termo>`), injetando os caminhos no prompt do terminal.
7. **Escolha de Sessões Temporárias (`ephemeral`) vs. Salvas (`persistent`) + Failover Automático de IA:** pergunta se você quer **sessões temporárias isoladas em `.agents/cache/`** (para que o `/resume` do seu CLI global nunca fique poluído com sessões dos sub-agentes) ou **sessões normais salvas no histórico** (1 por papel com *Reuse Before Recruiting*). Se uma IA falhar no terminal do Maestri, **substitui automaticamente in-place (`--replace`) por outra IA com cota e repassa a demanda** (sem dar erro e sem codar sozinha).

### O que a Minerva responde ao concluir o `/minerva`:

1. O checklist e os caminhos exatos criados no workspace (`.gitignore`, `.agents/`, `docs/`, `.mcp.json`, `rtk`, `skills.json`, Painel `:3333` e Kanban `:3334`).
2. A **tabela ao vivo de Contas, Modelos e Cotas** puxada direto dos seus CLIs (`agy`, `codex`, `claude`) com a sugestão **Anti-Monocultura + Failover** para os 4 papéis do Team CODES.
3. **Duas perguntas para iniciar o trabalho:**
   * **Qual modo de sessão prefere para os sub-agentes deste projeto?**
     * `[1] Sessões Temporárias / Isoladas (ephemeral — Recomendado)`: ficam restritas a `.agents/cache/`, sem poluir o `/resume` do seu CLI global.
     * `[2] Sessões Normais / Persistentes (persistent)`: ficam salvas no histórico global para consulta futura via `/resume`.
   * **Qual é a primeira demanda ou funcionalidade que vamos construir?**

---

## Cofre do Obsidian & Mapa de Endereços

1. Abra o **Obsidian** e clique em **"Open folder as vault"** (*Abrir pasta como cofre*).
2. Selecione o caminho: **`~/.minerva/vault`** (no Windows: **`%USERPROFILE%\.minerva\vault`**, ex.: `C:\Users\SeuUsuario\.minerva\vault`).
3. Comece por **`_Hub de Skills & MCPs.md`** e **`Workspace/Orquestração de Projetos - Minerva & Conselho.md`**.

### Mapa Completo de Endereços, Pastas & Portas (Onde Tudo Fica Salvo)

| Item | Caminho / Endereço Local | Escopo |
| :--- | :--- | :--- |
| **Raiz Única da Minerva** | `~/.minerva` (`%USERPROFILE%\.minerva`) | Global (PC) |
| **Cofre do Obsidian (Vault PT-BR)** | **`~/.minerva/vault`** (`%USERPROFILE%\.minerva\vault`) | Global (PC) |
| **Skills Centralizadas** | `~/.minerva/skills` *(conectada via junction a `~/.claude/skills`, `~/.codex/skills`, `~/.gemini/config/skills` e `~/.agents/skills`)* | Global (PC) |
| **MCPs Globais** | `~/.minerva/mcp_config.json` *(mesclado em `~/.gemini/mcp_config.json` e `~/.claude.json`)* | Global (PC) |
| **Painel de Agentes (Web / Portal)** | `http://localhost:3333` *(código em `~/.minerva/tools/painel-agents`)* | Servidor Local |
| **Kanban Minimalista (Web / Portal)** | `http://localhost:3334` *(código em `~/.minerva/tools/kanban-agents`)* | Servidor Local |
| **Governança, Roles & Leis (`/minerva`)** | `<PROJETO>/.agents/MINERVA.md`, `.agents/AGENTS.md`, `.agents/roles/` | Por Projeto |
| **Skills Ativas & Modo de Sessão** | `<PROJETO>/.agents/skills.json` & `<PROJETO>/.agents/session-mode.json` (cache em `.agents/cache/`) | Por Projeto |
| **Especificação, Arquitetura & ADRs** | `<PROJETO>/docs/spec.md`, `<PROJETO>/docs/architecture.md`, `<PROJETO>/docs/adr/` | Por Projeto |
| **Dados do Quadro Kanban do Projeto** | `<PROJETO>/.kanban/board.json` | Por Projeto |
| **MCPs & Economia de Contexto do Projeto** | `<PROJETO>/.mcp.json` (`context-mode` + `ai-memory`) & `<PROJETO>/.claude/settings.local.json` (`rtk`) | Por Projeto |

---

## Adicionais Oficiais & Repositórios Parceiros

Documentação completa de instalação e recursos avançados vive nos repositórios oficiais:

| Projeto | Porta | Papel no Ecossistema | Repositório Oficial |
| :--- | :--- | :--- | :--- |
| **Painel de Agentes** | `127.0.0.1:3333` | Telemetria passiva, cotas 3D, logs e grafo de arquitetura ao vivo | [`lk-feitosa/painel-agents`](https://github.com/lk-feitosa/painel-agents) |
| **Kanban Agents** | `127.0.0.1:3334` | Quadro ágil minimalista offline salvo em `.kanban/board.json` por projeto | [`lk-feitosa/kanban-agents`](https://github.com/lk-feitosa/kanban-agents) |

---

## Créditos, Atribuições & Licenças

Todos os direitos de propriedade intelectual, marcas e códigos de terceiros pertencem integralmente aos seus respectivos autores originais. Lista completa com links oficiais em:  
**[CREDITS.pt-br.md](CREDITS.pt-br.md)** *(English: [CREDITS.md](CREDITS.md))*
