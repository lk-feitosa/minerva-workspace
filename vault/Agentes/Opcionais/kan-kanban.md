---
tags:
  - ai/opcionais
  - kanban
  - mcp
  - maestri
  - orquestracao
  - produtividade
categoria: Opcionais
nome: kan-kanban
autor: lk-feitosa
local: "S:\\DEV\\frameworks\\kan"
updated_at: "2026-11-08T02:45:00-03:00"
---

# Kan Kanban & MCP — Orquestracao Visual no Maestri Canvas

> [!NOTE] **Kanban Aberto com Suporte Nativo a Model Context Protocol (MCP)**  
> O [Kan](https://github.com/kanbn/kan) é uma plataforma Kanban moderna, open-source e auto-hospedável com suporte completo ao protocolo MCP (`@kan.bn/mcp`). Ele permite que o agente orquestrador (**Minerva**) e subagentes criem, listem, organizem e movam tarefas programaticamente, enquanto você acompanha tudo visualmente no canvas do **Maestri** através de um nó de portal web.

```mermaid
flowchart TD
    subgraph MaestriCanvas ["Maestri Canvas"]
        Portal["Portal Node (Webview)<br>http://localhost:3000"]
        TerminalMinerva["Terminal: Minerva (Orquestrador)"]
    end

    subgraph StackKan ["Stack Local do Kan (Docker)"]
        Web["Kan Web & API (Port 3000)<br>Next.js + Better-Auth"]
        DB[("PostgreSQL 15<br>kan_db")]
    end

    subgraph MCPIntegration ["Camada de Protocolo MCP"]
        KanMCP["@kan.bn/mcp<br>(Stdio Server)"]
    end

    TerminalMinerva -->|Chamadas de Ferramenta MCP| KanMCP
    KanMCP -->|REST API /api/v1| Web
    Web <--> DB
    Portal <-->|Renderizacao Reativa em Tempo Real| Web
```

---

## Por que integrar o Kan ao Maestri?

1. **Acompanhamento Visual Passivo:**
   * Em vez de ler saídas textuais complexas no terminal, os cartões de progresso aparecem e se movem em colunas (*Backlog*, *Em Progresso*, *Revisão*, *Concluído*) no próprio quadro Kanban ao lado do terminal.
2. **Controle Total via IA (MCP First-Class):**
   * O pacote `@kan.bn/mcp` expõe ferramentas granulares para manipular workspaces, boards, listas, cards, checklists, membros e etiquetas.
3. **Persistência Local e Privada:**
   * Todos os dados residem no banco de dados PostgreSQL local gerenciado pelo Docker, sem dependência de SaaS de terceiros ou planos pagos.

---

## Isolamento Contextual por Projeto (Por que nao e Global?)

Um erro comum em fluxos de IA é misturar tarefas de diferentes clientes e sistemas em um único quadro global. No ecossistema Minerva:

* **Servidor Centralizado:** A stack do Docker roda uma única vez no sistema na porta `3000` (economia de CPU/RAM).
* **Quadros (Boards) Isolados:** Cada repositório Git ou pasta de trabalho mapeia para o seu **próprio quadro dedicado** no Kan.
* **Automação via CLI:** O comando `kanban` no terminal descobre a raiz do projeto e direciona a visualização e os cartões automaticamente para aquele projeto.
* **Orquestração Contextual com Minerva:** Ao ser acionada em uma pasta, Minerva identifica o projeto atual e restringe todas as chamadas de ferramentas MCP (`create_card`, `move_card`, etc.) ao quadro daquele projeto.

---

## Comando CLI Integrado: `kanban`

Um utilitário CLI rápido está disponível no PATH (`~/.local/bin/kanban` e `kanban.cmd`):

| Comando | Descrição |
| :--- | :--- |
| `kanban` | Detecta a pasta/projeto atual e abre o quadro Kanban no navegador. |
| `kanban portal` (ou `kanban -p`) | Cria diretamente um nó de Portal Web no **Maestri Canvas** apontando para o Kanban. |
| `kanban status` | Verifica se o servidor Kan (`http://localhost:3000`) está online ou offline. |
| `kanban start` | Inicializa os contêineres do Kan em background via Docker Compose. |
| `kanban stop` | Pausa os contêineres do Kan para liberar recursos. |

---

## Estrutura do Pacote e Arquivos

* **Repositório Local:** [`S:\DEV\frameworks\kan`](file:///S:/DEV/frameworks/kan)
* **Configuração Docker:** [`docker-compose.yml`](file:///S:/DEV/frameworks/kan/docker-compose.yml)
* **Ambiente Local:** [`.env`](file:///S:/DEV/frameworks/kan/.env)
* **Servidor MCP:** `@kan.bn/mcp` (instalável via `npx -y @kan.bn/mcp`)
* **Configuração Global MCP:** [`S:\DEV\agents\mcp_config.json`](file:///S:/DEV/agents/mcp_config.json)

---

## Ferramentas Disponíveis no Servidor MCP

O `@kan.bn/mcp` fornece as seguintes ferramentas para Minerva e seus agentes:

* **Workspaces:**
  * `list_workspaces` — lista os workspaces aos quais o usuário tem acesso.
  * `get_workspace` — detalhes de um workspace específico.
* **Boards:**
  * `list_boards` — lista todos os quadros de um workspace.
  * `get_board` — obtém detalhes e listas de um quadro.
  * `create_board` — cria um novo quadro de projeto.
  * `update_board` / `delete_board` — atualiza ou remove quadros.
* **Lists (Colunas):**
  * `list_lists` — recupera as listas/colunas existentes.
  * `create_list` — cria uma coluna (ex.: "To Do", "In Progress", "Done").
  * `update_list` / `move_list` / `delete_list` — reorganiza as colunas.
* **Cards (Cartões / Tarefas):**
  * `list_cards` — recupera os cartões de uma lista ou quadro.
  * `get_card` — lê detalhes, descrição e histórico de uma tarefa.
  * `create_card` — adiciona uma tarefa detalhada à lista indicada.
  * `update_card` — modifica título, descrição ou data de entrega.
  * `move_card` — move um cartão entre colunas (ex.: de "In Progress" para "Done").
  * `delete_card` — arquiva ou apaga cartões.
* **Checklists & Labels:**
  * `create_checklist`, `update_checklist_item`, `delete_checklist`.
  * `create_label`, `attach_label_to_card`, `detach_label_from_card`.

---

## Guia de Instalação e Teste Visual

### 1. Iniciar o Docker Desktop
Certifique-se de que o **Docker Desktop** esteja aberto e o daemon ativo.

### 2. Subir os Contêineres do Kan
No terminal (PowerShell ou Git Bash), navegue até a pasta do Kan e inicialize a stack:
```powershell
cd S:\DEV\frameworks\kan
docker compose up -d
```
> O Docker baixará as imagens oficiais (`kan:latest`, `kan-migrate:latest`, `postgres:15`) e executará automaticamente as migrações do banco de dados.

### 3. Criar a Conta e Gerar o API Token
1. Abra o navegador em `http://localhost:3000`.
2. Conclua o registro inicial de administrador local.
3. Crie um workspace ou quadro de teste.
4. Acesse as configurações da sua conta (**User Settings** > **API Tokens**) e gere um novo token de acesso pessoal.

### 4. Configurar o Token no MCP
Abra o arquivo [`mcp_config.json`](file:///S:/DEV/agents/mcp_config.json) (e no diretório [`~/.gemini/config/mcp_config.json`](file:///C:/Users/lukas/.gemini/config/mcp_config.json)) e substitua o valor de `KAN_API_TOKEN`:
```json
"kan": {
  "command": "npx",
  "args": [
    "-y",
    "@kan.bn/mcp"
  ],
  "env": {
    "KAN_BASE_URL": "http://localhost:3000",
    "KAN_API_TOKEN": "seu_token_aqui"
  }
}
```

### 5. Abrir o Quadro Visualmente no Maestri Canvas
Com o seu canvas aberto no Maestri, execute no terminal do canvas:
```bash
maestri portal create http://localhost:3000
```
Um nó de navegador dedicado será posicionado diretamente na sua área de trabalho do Maestri.

### 6. Testar a Orquestração com Minerva
Você pode agora solicitar a Minerva comandos naturais como:
* *"Minerva, liste os quadros no Kan e crie uma tarefa 'Refatorar autenticação' na coluna 'Em Progresso'."*
* *"Minerva, marque a tarefa 'Implementar statusline' como concluída no nosso quadro Kanban."*
* Ao disparar tarefas paralelas para outros agentes, Minerva criará e moverá os cartões visualmente no quadro em tempo real.
