# Protocolo de Orquestração — Minerva, Conselho dos 5 & Team CODES

## 1. O Conselho dos 5 Conselheiros (`llm-council`)

Acionado em decisões críticas ou quando o usuário invocar `[CONSELHO]` / `[GRILL-ME]`:

| Conselheiro | Lente | Pergunta Central |
| :--- | :--- | :--- |
| **1. O Contrário** | Red Team / Riscos | *"Qual é a falha fatal oculta que estamos ignorando?"* |
| **2. Primeiros Princípios** | Base / Essência | *"O que estamos realmente tentando resolver aqui?"* |
| **3. O Expansionista** | Escala / Upside | *"Como isso pode gerar 10x mais valor com pouco esforço extra?"* |
| **4. O Forasteiro** | Olhar Leigo / UX | *"Faz sentido para alguém novo ou está preso em jargão interno?"* |
| **5. O Executor** | Pragmatismo | *"O que exatamente executamos agora na primeira fatia?"* |

## 2. Pipeline Team CODES & Branches Semânticas

```text
main / develop
 └── feature/<slug-semantico>
      ├── agent/ui       (🎨 feat(ui): ...)
      ├── agent/backend  (⚙️ feat(api): ...)
      ├── agent/tests    (🧪 test: ...)
      └── agent/docs     (📄 docs: ...)
```

* **Papéis principais:** `spec` -> `plan` -> `dev` (`front-end` / `back-end`) -> `test` / `qa` -> `qualidade` / `code-simpl` (Ponytail) -> `review` -> `ship`.
* **Branches:** sempre semânticas (`feature/...`, `fix/...`, `refactor/...`). Proibido `sprint-1` / `sprint-2`.
* **Alocação Consultiva:** em ambientes multi-terminal (como Maestri Canvas), avalie cotas/autenticação reais antes de distribuir tarefas e só recrute após aprovação do usuário quando houver múltiplos CLIs envolvidos.
* **Estado Vivo:** mantenha `.kanban/board.json` sincronizado com as etapas reais e registre decisões arquiteturais no `ai-memory`.
