---
name: painel-agents
description: Abre e gerencia o Painel de Agentes (telemetria, cotas, Kanban sync e aprovações) em tempo real na porta 3333. Use quando o usuário pedir para abrir o painel, verificar status/cotas ou como parte da inicialização do /minerva.
user-invocable: true
---

# Painel de Agentes

Monitor web local e zero-dependência (`https://github.com/lk-feitosa/painel-agents`, Python Standard Library) para acompanhar múltiplos agentes (`Claude Code`, `Codex`, `Antigravity`), cotas por conta, cartões do `.kanban/board.json` e aprovações pendentes na porta `3333`.

## Localização Portátil

Resolva o diretório da ferramenta nesta ordem (sem depender de caminho fixo):
1. Comando global `painel` no `PATH` (criado por `instalar.bat` / `instalar.sh` do repositório)
2. Variável de ambiente `$MINERVA_PAINEL_DIR` (ou `$MINERVA_TOOLS_DIR/painel-agents`)
3. Diretório irmão ao workspace global: `~/.agents/../painel-agents` ou `~/.agents/tools/painel-agents`

Se ainda não estiver instalado localmente:
```bash
git clone https://github.com/lk-feitosa/painel-agents.git ~/.agents/tools/painel-agents
```

## Comandos

* **Iniciar no projeto atual (com portal no Maestri, se presente):**
  ```bash
  painel --projeto .
  ```
* **Auto-Heal silencioso / background (porta `3333` sem duplicar janela):**
  ```bash
  python "<PAINEL_DIR>/painel.py" --projeto "<PROJECT_DIR>" --sem-portal --ensure
  ```
  *(No Windows, também existe `wscript.exe "<PAINEL_DIR>/iniciar-silencioso.vbs"` para subir em background sem console).*
* **Abrir direto no navegador padrão:**
  ```bash
  python "<PAINEL_DIR>/painel.py" --projeto "<PROJECT_DIR>" --navegador
  ```
* **Coleta única sem manter servidor:**
  ```bash
  python "<PAINEL_DIR>/painel.py" --projeto "<PROJECT_DIR>" --uma-vez
  ```

## O que o Painel exibe (`http://127.0.0.1:3333`)

1. **Tabela de Agentes:** estado, modelo carregado, uso de contexto (`%`), PR/CI e missão sincronizada com `.kanban/board.json`.
2. **Cotas por Conta (`cotas.js`):** janelas de 5h e semanal para Antigravity, Codex CLI e Claude Code com mascaramento automático de credenciais/e-mail.
3. **Precisa de Você:** pendências de aprovação (ex.: specs e alocação de modelos).
4. **Ecossistema & Mapa de Arquitetura:** visão dos módulos do repositório atual e skills/MCPs conectados.
