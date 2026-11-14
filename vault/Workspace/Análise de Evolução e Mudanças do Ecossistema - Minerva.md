---
tags:
  - ai/workspace
  - minerva/changelog
  - architecture/evolution
name: "Análise de Evolução e Mudanças do Ecossistema - Minerva"
updated_at: "2026-11-11T22:58:00.000Z"
---

# 🐍 Análise Completa de Evolução: Minerva, Kanban, Painel & Team CODES

Este documento sintetiza todas as transformações arquiteturais, de governança, infraestrutura e ferramental implementadas no ecossistema da **Minerva** e do **Team CODES** nas últimas versões.

---

## 🧭 1. Resumo Executivo: O Que Mudou (Antes vs. Depois)

| Dimensão | Estado Anterior | Estado Atual (Evoluído) |
| :--- | :--- | :--- |
| **Quadro Kanban** | Docker pesado / Kan.bn Nuvem com token | **Kanban Minimalista Nativo (`:3334`)**, offline, zero-Docker, sincronizado com `.kanban/board.json`. |
| **Painel de Telemetria** | Poluído com abas duplicadas e emojis | **Painel Sóbrio (`:3333`)**, estilo console de desenvolvedor, cards 3D compactos e sem aba duplicada. |
| **Leis da Minerva** | 8 Leis engessadas e monolíticas | **10 Leis Fundamentais**, com proibição de auto-codificação (Lei 10) e Fast-Track ágil (Lei 1). |
| **Alocação de Modelos** | Presets estáticos (tentava Claude sem login) | **Protocolo Alethe (Lei 8)**: roteamento consultivo inteligente, anti-monocultura e fallback para Google AI Pro / Codex. |
| **Gestão de Terminais** | Minerva codificava sozinha quando o boot travava | **Protocolo de Handshake**: desbloqueia menus interativos com `\n` e **obriga delegação ativa real** (sem travar em confirmação de papel). |
| **Higiene de Sessões CLI** | Dezenas de sessões temporárias poluíam o terminal pessoal | **"Reuse Before Recruiting"**: terminais fixos persistentes no Canvas + comandos nativos de purga (`claude purge`, `codex archive`). |
| **Catálogo de Skills** | 368 skills estáticas sem categoria visual | **Raiz única `~/.minerva` via `skills.sh`**: **3 autorais** + **17 pacotes curados** em catálogo único *(sem divisão `core`/`full`, pacote Google removido)* + Hubs no Obsidian + **`find-skills`**. |

---

## 🏛️ 2. Evolução da Governança: As 10 Leis Fundamentais

A Minerva deixou de ser um simples script de prompt e tornou-se um **Orquestrador de Alta Governança**:

### Lei 1: Refinamento sob Demanda & Fast-Track
* **Antes:** Todo e qualquer comando acionava um interrogatório exaustivo de *Grill-Me* e parecer do *LLM Council*, tornando ajustes simples burocráticos.
* **Agora:**  
  * **Modo Padrão:** Execução ágil, direta ao ponto.
  * **Modo Stress-Test (Opt-in):** Só ativa o conselho e perguntas caso o usuário use tags explícitas como `[GRILL-ME]` ou `[CONSELHO]`.
  * **Fast-Track:** Micro-ajustes cosméticos (mudar cor, ajustar padding, corrigir texto) são aplicados em 1 linha sem abrir novos terminais nem cartões no Kanban.

### Lei 4: Branches Semânticas Reais
* **PROIBIDO:** Branches genéricas (`sprint-1`, `sprint-2`, `teste`).
* **OBRIGATÓRIO:** Nome refletindo a intenção real (`feature/<slug>`, `fix/<slug>`). O Team CODES atua em sub-branches isoladas (`agent/ui`, `agent/backend`, `agent/qa`, `agent/review`).
* **Critério de Continuidade:** Continuações ou ajustes da mesma demanda permanecem na mesma branch ativa.

### Lei 7: Auto-Heal das Portas 3333 e 3334
* Portas dedicadas e separadas:
  * `3333`: Telemetria, cotas 3D e status.
  * `3334`: Kanban visual em tempo real.
* Se um serviço cair (ex: reinício do computador), o launcher silencioso (`iniciar-silencioso.vbs`) é acionado automaticamente em background sem travar o terminal.
* Anti-colisão inteligente: se a porta estiver ocupada, salta para 3335, 3336 e grava em `docs/ports.md`.

### Lei 8: Alocação Consultiva de Modelos (Padrão Alethe)
* **Anti-Monocultura:** Se o Claude Code estiver sem login (`Not logged in`) ou sem assinatura, a Minerva **não pode clonar o Codex em todos os terminais** nem tentar usar o Claude deslogado.
* **Roteamento Heterogêneo:** Redireciona papéis visuais (Front-End) e de auditoria (Reviewer) para o **Google AI Pro (Antigravity)**, mantendo Back-End e QA no **Codex**.
* **Auto-Discovery:** Se a demanda exigir uma tecnologia não dominada, usa o `find-skills` (`npx skills find`) no marketplace global do `skills.sh`.

### Lei 9: Verificação de Sandbox e Diretório Raiz
* Garante que os agentes executem na raiz absoluta do projeto (`<PROJECT_DIR>`) com permissões completas de escrita e compilação.

### Lei 10: Proibição Estrita de Auto-Codificação & Delegação Ativa Completa
* **PROIBIDO CODIFICAR:** A Minerva nunca implementa arquivos `.ts`, `.tsx`, `.vue` ou `.py` ela mesma. Seu papel é liderança e coordenação.
* **Handshake de Desbloqueio:** Ao recrutar novos terminais, ela roda `maestri check` e envia `maestri ask "<Nome>" --raw "\n"` para aceitar termos de primeiro boot (*Trust this folder* ou seleção de tema).
* **Delegação Ativa Real:** É proibido parar em "Confirme seu papel". A Minerva despacha imediatamente os cartões do Kanban com branches e metas técnicas claras.

---

## 🛠️ 3. Infraestrutura & Refatoração dos Serviços (Painel & Kanban)

### 3.1 Kanban Minimalista (`porta 3334`)
* **Adeus Docker / Kan.bn Nuvem:** Eliminadas dependências externas que falhavam por token ou consumo de memória.
* **Arquitetura Baseada em Arquivo:** O estado reside em `.kanban/board.json` na raiz de cada projeto.
* **Estética Polar/Linear:** Removidos ícones e ornamentos visuais desnecessários; foco absoluto em cards, colunas e fluidez.

### 3.2 Painel de Agentes (`porta 3333`)
* **Remoção da Aba Duplicada de Kanban:** Como o Kanban roda de forma independente no Portal `:3334`, a aba interna do painel foi descontinuada para evitar redundância.
* **Console de Logs para Desenvolvedor:** Logs do ecossistema redesenhados com fonte monospaçada e estilo sóbrio.
* **Cards de Cotas 3D Compactos:** Monitoramento de 5h e semanal em tempo real (Google AI Pro, Codex e Claude Code) com visual limpo.
* **Multi-Threading TCP:** Servidor Python agora atende conexões simultâneas do Maestri WebView sem travar.

---

## 🧹 4. Higiene de Sessões e Não-Poluição do CLI Pessoal

Para resolver o problema de conversas descartáveis que poluíam o histórico pessoal do usuário fora do Maestri:
1. **Regra "Reuse Before Recruiting":** O time CODES é permanente no Canvas. Novas demandas são enviadas aos terminais existentes (`maestri ask`), gerando **apenas 1 sessão contínua por papel**.
2. **Purga Específica por Projeto:**
   * `claude purge <PROJECT_DIR>`: apaga dados temporários do Claude naquele projeto.
   * `codex archive <id>`: arquiva sessões concluídas no Codex.
3. **Isolamento de Diretório:** `.maestri/` e subpastas de roles mantidos 100% fora do Git via `.gitignore`.

---

## 🎨 5. Expansão de Skills & Organização no Obsidian

O acervo migrou de um pacote estático gigante (incluindo 186 skills redundantes) para um **manifesto único oficial no `skills.sh`** (`skills-manifest.json`: **3 autorais + 17 pacotes curados** centralizados em `~/.minerva/skills/`) organizado diretamente no cofre `vault/`:

### 5.1 Novas Skills de Alto Desempenho Adicionadas
* **`taste-skill` (`design-taste-frontend`):** Gate anti-slop com acabamento no nível figma.com e x.ai.
* **`awesome-design-md`:** 84 design systems de ponta catalogados (Linear, Stripe, Apple, Vercel, Supabase).
* **Suíte Vercel Labs:** `react-best-practices` (70 regras de performance), `composition-patterns`, `react-view-transitions`, `web-design-guidelines`.
* **`playwright-cli` (Microsoft):** Automação nativa de navegador e WebMCP via terminal.
* **`find-skills` (skills.sh):** Meta-skill para pesquisa e instalação instantânea de novos pacotes de agentes.

### 5.2 Navegação em Grafo no Obsidian
* Criada a nota central **`[[Skills/🎨 Design, UI & Frontend Systems]]`**.
* Todas as skills de interface agora possuem a tag `#category/design` e links bidirecionais, permitindo visualizar a constelação completa de UI ao clicar no nó ou filtrar no Graph View.

---

## ⚡ 6. Atualização Nativa no Maestri (`preferences.json`)

O arquivo interno de configurações do Maestri (`~/.maestri/preferences.json`) foi atualizado diretamente:
* O preset nativo da responsabilidade **"Minerva - Orquestrador Central"** agora contém nativamente as **10 Leis Fundamentais**, o **Protocolo Alethe** e o **`find-skills`**.
* Qualquer novo terminal aberto no Canvas com essa role já nasce 100% blindado e atualizado.
