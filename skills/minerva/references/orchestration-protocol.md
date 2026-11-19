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
2. **Gate Obrigatório de Aprovação do Backlog (Com Modelo Tier N-1 Explícito em Cada Linha):**
   * Ao receber uma demanda, atualize `docs/spec.md`, gere **todo o Backlog de tasks em `.kanban/board.json`** e rode `python ~/.minerva/toolkits/minerva_quotas.py`.
   * Na tabela de tasks do Backlog, a coluna `Responsável (CLI + Modelo Tier N-1)` **DEVE** conter o CLI + o modelo exato Tier N-1 (ex.: `Back-End (Codex — gpt-6-luna [medium])`, `Front-End (Antigravity — gemini-4-argon-medium)`, `Reviewer (Antigravity — claude-sonnet-5-5-medium)` — **proibido** escrever apenas `Back-End (Codex)` ou `Opus/Sonnet`).
   * Logo abaixo do Backlog, exiba sempre a **Tabela Resumo de Alocação de Modelos & Cotas do Sprint** (`Papel | Preset / CLI | Modelo Padrão (Tier N-1) | Cota Livre | Modelo Top-Tier (Só se você pedir) | Failover`) e peça a **Confirmação Dupla** (Backlog + Modelos). **O Team CODES só inicia a execução depois que o usuário aprovar ("OK")**.
3. **Leitura Direta dos CLIs & Regra de Economia Tier N-1 (`minerva_quotas.py`):**
   * Execute `python ~/.minerva/toolkits/minerva_quotas.py`, que consulta diretamente os CLIs instalados (`agy`, `codex`, `claude`) trazendo **todos os modelos disponíveis no PC** e as cotas de cada família.
   * **Política Tier N-1 (Modelo do Dia a Dia por Padrão):** nunca use o modelo #1 mais top da conta a menos que o usuário especifique (`--top-tier`):
     * **Gemini (`agy`):** se o mais inteligente da conta for `Neon`, usa o abaixo dele (`Argon`/`Hydrogen`); se o topo for `Argon` e `Hydrogen` for o modelo do dia a dia, usa `Hydrogen` (`gemini-4-hydrogen-medium`).
     * **Claude (`claude` / `agy`):** se o mais inteligente for `Fable` ou `Opus`, usa o tier anterior (`Sonnet`, ex.: `claude-sonnet-5-5-medium` / `claude-sonnet-4-6`).
     * **Codex (`codex`):** usa o modelo do dia a dia com esforço `medium` (`gpt-6-luna (medium)`).
4. **Proibição de Monocultura:** nunca abra todos os terminais do Team CODES na mesma IA se houver mais de um provedor autenticado com cota. Distribua cada papel (`Front-End`, `Back-End`, `Test/QA`, `Review`) para o **Preset + Modelo (Tier N-1)** que melhor combina **aptidão técnica da tarefa + folga de cota**.
5. **Como cada Terminal recebe as Skills Certas para a Demanda (`agent_sort.py` + `find-skills`):**
   * **Busca Local (`agent_sort.py --match`):** além das skills fixas de `.agents/roles/<papel>.md` e `.agents/skills.json` (stack DAILY), antes de enviar uma demanda rode `python ~/.minerva/toolkits/agent_sort.py --match "<descrição da demanda>"`.
   * **Busca Externa (`find-skills`):** se a demanda exigir tecnologia sem skill local, use a skill `find-skills` (`npx skills find <termo>` e `npx skills add <pacote> -g -y`).
   * **Injeção no Prompt:** no comando `maestri ask "<Terminal>"`, **liste explicitamente as skills recomendadas** (ex.: *"Antes de codar, leia `~/.minerva/skills/shadcn/SKILL.md`, `~/.minerva/skills/transitions-dev/SKILL.md` e aplique `ponytail`"*).

## 4. Escolha do Modo de Sessão (`ephemeral` vs. `persistent`), Handshake & Failover Automático de IA (Leis 9 & 10)

1. **Escolha do Modo de Sessão no Projeto (`.agents/session-mode.json`):**
   * Pergunte ao usuário no `/minerva` se prefere:
     * **`ephemeral` (Sessões Temporárias/Isoladas — Recomendado):** sub-agentes usam `.agents/cache/` (`--no-session-persistence` / `CODEX_SQLITE_HOME` local), para que o comando `/resume` do CLI global do usuário **nunca fique poluído com dezenas de sessões dos sub-agentes**.
     * **`persistent` (Sessões Salvas no Histórico):** sub-agentes salvam no histórico global para inspeção posterior via `/resume`.
   * **Regra "Reuse Before Recruiting":** antes de recrutar qualquer terminal, rode **`maestri list`**. Se já existir terminal ativo para aquele papel no Canvas, **reutilize-o via `maestri ask "<Nome>"`** em vez de criar um novo terminal — garantindo **apenas 1 sessão contínua por papel**.
2. **Proibição Absoluta de Auto-Codificação:** a Minerva jamais escreve o código de produção no lugar do Team CODES caso um terminal falhe.
3. **Handshake Imediato:** após `maestri recruit`, verifique com `maestri check "<Nome>"`. Se houver prompt interativo de confirmação (`Trust this folder?`, `Update available`, `Choose text style`), envie `maestri ask "<Nome>" --raw "\n"` e despache a tarefa completa em seguida.
4. **Failover Automático para Outra IA (`--replace`):** se o terminal recrutado apresentar erro de login (`Not logged in`), falta de cota, crash ou continuar travado após o Handshake:
   * **Não pare com erro e não codifique sozinha.**
   * Substitua imediatamente aquele terminal in-place por **outra IA autenticada e com cota disponível** (`maestri recruit --replace "<Nome>" --preset "<Outra-IA-Disponivel>"`).
   * Realize o Handshake no novo terminal e **passe a demanda integralmente (com as skills da tarefa) para a nova IA executar**.
