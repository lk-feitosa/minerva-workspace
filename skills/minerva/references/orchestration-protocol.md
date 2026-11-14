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
* **Terminais sem Bloqueio:** confirme `cwd` na raiz `<PROJECT_DIR>` e permissões de leitura/escrita/compilação/testes antes de delegar.
* **Alocação Consultiva (`alethe` + `maestri`):** leia contas/cotas reais (`painel-agents`, `Codex`, `Claude Code`, `Gemini/Antigravity`), apresente tabela sugerida por papel (`Back-End`, `Front-End`, `QA`, `Review`) e peça confirmação antes de disparar `maestri recruit`.
* **Estado Vivo:** mantenha `.kanban/board.json` sincronizado e registre decisões arquiteturais em `docs/adr/` + `ai-memory`.
