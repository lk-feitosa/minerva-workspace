<div align="center">

<img src="assets/logo.png" alt="Minerva Logo" width="180" style="border-radius: 20px; box-shadow: 0 8px 24px rgba(0,0,0,0.4);" />

# Minerva & AI Agents Ecosystem

**Hub Unificado de Orquestração Multi-Agente, Biblioteca de 381 Skills (`skills.sh`), Servidores MCP & Cofre Enxuto em PT-BR para Obsidian.**

🌐 **[Português](README.md)** | **[English](README.en.md)**

[![Platform: Windows | Linux | macOS](https://img.shields.io/badge/platform-Windows%20|%20Linux%20|%20macOS-informational.svg?style=flat-square)](#-instalação-rápida-cross-platform)
[![Skills: 381](https://img.shields.io/badge/skills-381%20via%20skills.sh-blue.svg?style=flat-square)](skills/)
[![Obsidian Ready](https://img.shields.io/badge/obsidian-vault%20PT--BR-purple.svg?style=flat-square)](vault/Agentes/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg?style=flat-square)](LICENSE)

</div>

---

## Visão Geral

Este repositório centraliza toda a infraestrutura agêntica de desenvolvimento, integrando inteligências artificiais líderes de mercado (**Antigravity / Gemini CLI**, **Claude Code**, **Codex** e **Maestri Canvas**) sob uma arquitetura unificada com `skills.sh` como fonte oficial de skills de terceiros.

```text
minerva-workspace/                     <-- Raiz Única do Repositório
│
├── 📁 skills/                         <-- 381 Skills de desenvolvimento (skills.sh + locais)
├── 📄 skills-manifest.json            <-- Manifesto curado dos pacotes skills.sh
├── 📄 .skill-lock.json                <-- Lockfile oficial da CLI `npx skills`
├── 📄 mcp_config.json                 <-- Configuração unificada de servidores MCP
├── 📁 toolkits/                       <-- Vibe Coding Toolkit & scripts (statusline, kanban)
├── 📁 vault/Agentes/                  <-- Cofre enxuto 100% em PT-BR do Obsidian
│   ├── 📁 Workspace/                  <-- Arquitetura Minerva, Conselho & Team CODES
│   ├── 📁 Skills/                     <-- 381 notas resumidas PT-BR + 8 Hubs de Categoria
│   ├── 📁 MCP/                        <-- Manuais PT-BR (ai-memory, rea, agent-desktop, magicpath, kan)
│   ├── 📁 Frameworks/                 <-- Bibliotecas de agentes (alethe, claude-cookbooks, etc.)
│   ├── 📁 Opcionais/                  <-- Ferramentas de apoio (painel-agents, ai-statusline, kanban)
│   └── 📄 _Hub de Skills & MCPs.md    <-- Dashboard de navegação do cofre
│
├── 📄 setup.bat                       <-- Instalador 1-click para Windows (CMD)
├── 📄 setup.ps1                       <-- Instalador 1-click para Windows (PowerShell)
└── 📄 setup.sh                        <-- Instalador 1-click para Linux e macOS
```

---

## Instalação Rápida (Cross-Platform)

Você pode clonar este repositório em qualquer computador (**Windows, Linux ou macOS**) e rodar um único comando para deixar seu ambiente 100% pronto.

### No Windows:

Abra o prompt de comando (ou PowerShell) e execute:
```cmd
git clone https://github.com/lk-feitosa/minerva-workspace.git S:\DEV\minerva-workspace
cd S:\DEV\minerva-workspace
setup.bat
```
*(Ou no PowerShell: `.\setup.ps1`)*

O script criará automaticamente os NTFS Junctions vinculando o repositório aos caminhos padrão dos agentes (`~/.agents`, `~/.codex/skills`, `~/.claude/skills` e `~/.gemini/config/skills`).

---

### No Linux ou macOS:

Abra o terminal e execute:
```bash
git clone https://github.com/lk-feitosa/minerva-workspace.git ~/DEV/minerva-workspace
cd ~/DEV/minerva-workspace
chmod +x setup.sh
./setup.sh
```

O script criará automaticamente os links simbólicos necessários (`~/.agents`, `~/.codex/skills`, `~/.claude/skills`).

---

## Como Abrir o Cofre no Obsidian

1. Abra o aplicativo **Obsidian**.
2. Clique em **"Open folder as vault"** (Abrir pasta como cofre).
3. Selecione o diretório:
   * **No Windows:** `S:\DEV\minerva-workspace\vault\Agentes` (ou `C:\Users\SEU_USUARIO\.agents\vault\Agentes`)
   * **No Linux/Mac:** `~/DEV/minerva-workspace/vault/Agentes` (ou `~/.agents/vault/Agentes`)
4. Pronto! O cofre abrirá com:
   * **Excalidraw** pré-configurado em Dark Mode.
   * Plugins essenciais ativos.
   * Dashboard interativo em `_Hub de Skills & MCPs.md` e 8 Hubs de Categoria no Grafo.
   * Nota mestra em `Workspace/Orquestração de Projetos - Minerva & Conselho.md`.

### Atualizando Skills com `skills.sh`
```bash
npx skills find <termo>        # Descobre novas skills no catálogo oficial skills.sh
npx skills update -g            # Atualiza todas as skills rastreadas no .skill-lock.json
```

---

## Arquitetura de Orquestração: Minerva & Team CODES

Consulte a documentação completa no Obsidian em:  
👉 **`Workspace/Orquestração de Projetos - Minerva & Conselho.md`**

* **Minerva:** Orquestrador Central com supervisão autônoma de múltiplos terminais no Maestri (Zero Human-in-the-Loop).
* **Conselho dos 5:** Contrário, Primeiros Princípios, Expansionista, Forasteiro e Executor.
* **Team CODES:** Pipeline de engenharia de 12 papéis (Spec, Plan, Dev, UI, Backend, Tests, Review, Ship, etc.).
* **Branches no Git:** Nomes semânticos baseados na demanda (`feature/<demanda>`, `fix/<bug>`), evitando proliferação de branches desnecessárias ou genéricas.

---

## 🧩 Adicionais Oficiais para o Maestri Canvas

Para enriquecer o fluxo de desenvolvimento no [Maestri Spatial Development Workspace](https://maestri.app), o ecossistema disponibiliza dois plugins/aplicações locais independentes com **navegação unificada por abas** (permitindo operar tudo em uma única janela integrada):

1. **📊 [Painel de Agentes (`painel-agents`)](https://github.com/lk-feitosa/painel-agents):**
   * **Porta Local:** `http://localhost:3333/`
   * **O que oferece:**
     * **Monitoramento e Cotas 3D:** Leituras de capacidade semanal e 5h (Gemini, Claude, OpenAI) com dedução inteligente de modelo por terminal (Back-End $\rightarrow$ Codex GPT-5.6, Front-End $\rightarrow$ Claude Sonnet 4.6).
     * **Feed de Logs de Atividades ao Vivo (`📜 Logs`):** Linha do tempo cronológica registrando recepção de demandas, atualizações no Kanban e delegações de tarefas.
     * **Live Architecture Graph (`🗺️ Arquitetura`):** Grafo interativo em tempo real em SVG 60 FPS com nós arrastáveis, pan/zoom, detecção luminosa de arquivos alterados recentemente (< 15 min) e drawer para despachar missões diretas (refatorar, testar, auditar) aos agentes conectados no Maestri.
     * **Navegação Integrada:** Aba dedicada `[ 🦉 Kanban (:3334) ]` para alternar para o quadro de tarefas sem precisar abrir outra janela.
   * **Como abrir no Maestri:** `maestri portal create http://localhost:3333 "Painel de Agentes"`

2. **📋 [Kanban para Maestri (`kanban-agents`)](https://github.com/lk-feitosa/kanban-agents):**
   * **Porta Local:** `http://localhost:3334/`
   * **O que oferece:**
     * **Quadro Ágil Minimalista:** Leve (< 20 MB RAM, zero Docker, zero login), sincronizado diretamente em `.kanban/board.json`.
     * **Navegação por Abas no Header:** Alternância instantânea entre `[ 📌 Quadro Ativo ]`, `[ 📦 Sprints Arquivadas ]` e `[ 📊 Painel de Agentes (:3333) ]` (com iframe embutido na porta 3333).
     * **Arquivamento de Sprints:** Botão rápido `[ 🏁 Finalizar Sprint ]` para transferir tarefas concluídas para o histórico permanente, limpando a coluna para a próxima demanda.
     * **Preservação de Scroll & Anti-Colisão:** Sem saltos de tela ao carregar e com auto-redirecionamento de portas caso 3334 esteja ocupada.
   * **Como abrir no Maestri:** `maestri portal create http://localhost:3334 "Kanban"`

---

## Configuração Automática via Agente de IA (Prompt de Setup)

Se você utiliza um assistente de IA no seu terminal ou editor (**Antigravity**, **Claude Code**, **Codex**, **Cursor** ou **Aider**) e prefere que o próprio agente configure o seu sistema operacional para adotar esta arquitetura global, basta clonar este repositório e colar o prompt abaixo diretamente no seu agente:

```text
Você é o meu assistente de IA configurando este computador.
Acabei de clonar o ecossistema Minerva & Agents (minerva-workspace) nesta máquina.
Por favor, configure o meu ambiente para operar nesta arquitetura global unificada:

1. Identifique o meu Sistema Operacional (Windows / Linux / macOS) e a pasta onde este repositório foi clonado.
2. Em vez de utilizar diretórios individuais e isolados, configure o apontamento global criando os links necessários:
   - No Windows: Crie os NTFS Junctions vinculando:
     * %USERPROFILE%\.agents -> [caminho_deste_repositorio]
     * %USERPROFILE%\.codex\skills -> [caminho_deste_repositorio]\skills
     * %LOCALAPPDATA%\hermes\skins -> [caminho_deste_repositorio]\hermes\skins
   - No Linux ou macOS: Crie os links simbólicos (ln -s):
     * ~/.agents -> [caminho_deste_repositorio]
     * ~/.codex/skills -> [caminho_deste_repositorio]/skills
     * ~/.hermes/skins -> [caminho_deste_repositorio]/hermes/skins
3. Valide se Node.js, Python 3 e Git estão presentes no PATH.
4. Confirme que o cofre do Obsidian está localizado na pasta 'vault/Agentes' deste repositório e indique como abri-lo.
5. Apresente um resumo claro com o status de cada item configurado.
```

---

## Créditos, Atribuições & Licenças

Este projeto é um ecossistema integrador. Todos os direitos de propriedade intelectual, marcas e códigos de terceiros pertencem aos seus respectivos criadores originais (Google, Anthropic, Vercel Labs, Kanbn, Fabio Akita, Addy Osmani, Matt Pocock, Affaan M, Composio, etc.).

Consulte a lista completa com os links para os repositórios originais em:  
👉 **[CREDITS.pt-br.md](CREDITS.pt-br.md)** *(English version: [CREDITS.md](CREDITS.md))*


