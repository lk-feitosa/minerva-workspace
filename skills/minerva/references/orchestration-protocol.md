# Protocolo de Orquestração — Minerva, Conselho dos 5 & Team CODES

## 1. O Conselho dos 5 Conselheiros (`llm-council`)

Acionado **somente sob demanda** quando o usuário pedir `[CONSELHO]`, `[GRILL-ME]` ou stress-test antes do código:

| Conselheiro | Lente | Foco na Análise Consolidada |
| :--- | :--- | :--- |
| **1. O Contrário** | Red Team / Riscos | Falhas ocultas, riscos técnicos e cenários de quebra |
| **2. Primeiros Princípios** | Guardião / Essência | Segurança, invariantes e o problema real sendo resolvido |
| **3. O Expansionista** | Escala / Upside | Oportunidades de alto impacto com baixo custo marginal |
| **4. O Forasteiro** | Olhar Leigo / UX | Clareza para usuários novos e remoção de jargão interno |
| **5. O Executor** | Pragmático / MVP | Primeiro passo executável hoje sem over-engineering |

## 2. Pipeline Team CODES, Roles & Branches Semânticas

```text
main / develop
 └── feature/<slug-semantico>
      ├── agent/ui       (🎨 feat(ui): ...     -> .agents/roles/front-end.md)
      ├── agent/backend  (⚙️ feat(api): ...    -> .agents/roles/back-end.md)
      ├── agent/tests    (🧪 test: ...         -> .agents/roles/test-qa.md)
      └── agent/review   (🔍 review: ...       -> .agents/roles/review.md)
```

* **Branches:** sempre semânticas (`feature/<slug-semantico>`, `fix/<slug>`, `refactor/<slug>`). Proibido `sprint-1` / `sprint-2`.
* **Terminais sem Bloqueio (`cwd`):** confirme `cwd` na raiz `<PROJECT_DIR>` e permissões de leitura/escrita/compilação/testes antes de delegar.

## 3. Gate de Backlog, Arquivamento de Sprint, Alocação Tier N-1 & Seleção de Skills (Leis 1, 5 & 8)

1. **Arquivamento de Sprint Anterior (`--archive-sprint`):** ao iniciar um novo sprint/demanda independente, arquive os cartões do sprint anterior rodando `python ~/.minerva/toolkits/minerva_bootstrap.py . --archive-sprint "<nome-sprint-anterior>"` (salvo em `.kanban/archive/`).
2. **Gate Obrigatório de Aprovação do Backlog (Com Modelo Tier N-1 + Skills & MCPs Explícitos):**
   * Ao receber uma demanda, atualize `docs/spec.md`, gere **todo o Backlog de tasks em `.kanban/board.json`** e rode `python ~/.minerva/toolkits/minerva_quotas.py` + `python ~/.minerva/toolkits/agent_sort.py . --team-plan "<demanda>"`.
   * Na tabela de tasks do Backlog, a coluna `Responsável (CLI + Modelo Tier N-1)` **DEVE** conter o CLI + o modelo exato Tier N-1 (ex.: `Back-End (Codex — gpt-6-luna [medium])`, `Front-End (Antigravity — gemini-4-argon-medium)`, `Reviewer (Antigravity — claude-sonnet-5-5-medium)` — **proibido** escrever apenas `Back-End (Codex)` ou `Opus/Sonnet`).
   * Logo abaixo do Backlog, exiba sempre a **Tabela Resumo de Alocação do Time (`Modelos, Cotas, Skills & MCPs`)** (`Papel | Preset / CLI | Modelo Padrão (Tier N-1) | Cota Livre | Skills & MCPs Ativos | Modelo Top-Tier (Só se você pedir) | Failover`) e peça a **Confirmação Tripla** (1: Backlog; 2: Modelos Tier N-1 vs. Top-Tier; 3: Skills & MCPs por papel, podendo adicionar/trocar/remover). **O Team CODES só inicia a execução depois que o usuário aprovar ("OK")**.
3. **Leitura Direta dos CLIs & Regra de Economia Tier N-1 (`minerva_quotas.py`):**
   * Execute `python ~/.minerva/toolkits/minerva_quotas.py`, que consulta diretamente os CLIs instalados (`agy`, `codex`, `claude`) trazendo **todos os modelos disponíveis no PC** e as cotas de cada família.
   * **Política Tier N-1 (Modelo do Dia a Dia por Padrão):** nunca use o modelo #1 mais top da conta a menos que o usuário especifique (`--top-tier`):
     * **Gemini (`agy`):** se o mais inteligente da conta for `Neon`, usa o abaixo dele (`Argon`/`Hydrogen`); se o topo for `Argon` e `Hydrogen` for o modelo do dia a dia, usa `Hydrogen` (`gemini-4-hydrogen-medium`).
     * **Claude (`claude` / `agy`):** se o mais inteligente for `Fable` ou `Opus`, usa o tier anterior (`Sonnet`, ex.: `claude-sonnet-5-5-medium` / `claude-sonnet-4-6`).
     * **Codex (`codex`):** usa o modelo do dia a dia com esforço `medium` (`gpt-6-luna (medium)`).
4. **Proibição de Monocultura:** nunca abra todos os terminais do Team CODES na mesma IA se houver mais de um provedor autenticado com cota. Distribua cada papel (`Front-End`, `Back-End`, `Test/QA`, `Review`) para o **Preset + Modelo (Tier N-1)** que melhor combina **aptidão técnica da tarefa + folga de cota**.
5. **Como cada Terminal recebe as Skills & MCPs Certos (`agent_sort.py --team-plan` + `find-skills` Opt-In):**
   * **Plano Local Determinístico (`agent_sort.py --team-plan`):** cruza `~/.minerva/skills/`, `.agents/roles/<papel>.md` e os MCPs reais de `.mcp.json` / configs globais para montar a coluna `Skills & MCPs Ativos` da tabela antes da aprovação.
   * **Fallback de Lacuna (`find-skills` — exclusiva da Minerva):** se `--team-plan` detectar lacuna local (`suggest_find_skills: true`) ou o usuário solicitar no Gate, rode `npx skills find <termo>`, proponha a skill no Gate e só execute `npx skills add <pacote> -g -y` após aprovação do usuário. Sub-agentes nunca instalam skills sozinhos.
   * **Injeção no Prompt:** no comando `maestri ask "<Terminal>"`, **liste explicitamente as skills e MCPs aprovados** (ex.: *"Antes de codar, leia `~/.minerva/skills/unslop/SKILL.md`, `~/.minerva/skills/emil-design-eng/SKILL.md`, use os MCPs `context-mode` e `ai-memory`, e aplique `ponytail`"*).

## 4. Escolha do Modo de Sessão (`ephemeral` vs. `persistent`), Handshake & Failover Automático de IA (Leis 9 & 10)

1. **Escolha do Modo de Sessão no Projeto (`.agents/session-mode.json`):**
   * Pergunte ao usuário no `/minerva` se prefere:
     * **`ephemeral` (Sessões Temporárias/Isoladas — Recomendado):** aplica isolamento real via `--command` do `maestri recruit` em **Claude Code** (`claude --no-session-persistence`) e **Codex** (`CODEX_SQLITE_HOME` em `.agents/cache/codex-home`). **Nota transparente sobre Antigravity (`agy`):** o `agy` não possui flag nativa de sessão efêmera — para não multiplicar conversas no `/resume`, reutilize rigorosamente **1 terminal fixo por papel** (nunca `dismiss` + `recruit`), priorize Codex/Claude para tarefas descartáveis e oriente o uso de `Ctrl+F` (*Grouped View*) no `/resume`.
     * **`persistent` (Sessões Salvas no Histórico):** sub-agentes salvam no histórico global para inspeção posterior via `/resume`.
   * **Regra "Reuse Before Recruiting":** antes de recrutar qualquer terminal, rode **`maestri list`**. Se já existir terminal ativo para aquele papel no Canvas, **reutilize-o via `maestri ask "<Nome>"`** em vez de criar um novo terminal — garantindo **apenas 1 sessão contínua por papel**.
2. **Proibição Absoluta de Auto-Codificação & Protocolo Pós-Aprovação:**
   * A Minerva **jamais** escreve ou edita código de produção/testes no lugar do Team CODES (só edita `docs/`, `.kanban/board.json` e `.agents/`).
   * Assim que o usuário aprovar o Backlog, o **primeiro comando obrigatório** da Minerva é `maestri list` → `maestri recruit` (se faltar algum papel) → `maestri ask "<Papel>"` com a ordem de serviço (ID, branch, skills e MCPs aprovados) → `maestri check` para monitorar. Fast-Track **nunca** se aplica a tasks de Backlog/Sprint.
3. **Handshake Imediato:** após `maestri recruit`, verifique com `maestri check "<Nome>"`. Se houver prompt interativo de confirmação (`Trust this folder?`, `Update available`, `Choose text style`), envie `maestri ask "<Nome>" --raw "\n"` e despache a tarefa completa em seguida.
4. **Failover Automático para Outra IA (`--replace`):** se o terminal recrutado apresentar erro de login (`Not logged in`), falta de cota, crash ou continuar travado após o Handshake:
   * **Não pare com erro e não codifique sozinha.**
   * Substitua imediatamente aquele terminal in-place por **outra IA autenticada e com cota disponível** (`maestri recruit --replace "<Nome>" --preset "<Outra-IA-Disponivel>"`).
   * Realize o Handshake no novo terminal e **passe a demanda integralmente (com as skills da tarefa) para a nova IA executar**.
