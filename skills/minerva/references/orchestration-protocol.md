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

## 3. Alocação Anti-Monocultura Direto dos CLIs & Seleção de Skills (`agent_sort` + `find-skills`) (Lei 8)

1. **Leitura Direta dos CLIs no PC (`minerva_quotas.py`):** execute `python ~/.minerva/toolkits/minerva_quotas.py`, que consulta diretamente os CLIs instalados (`agy models` + `agy -p /usage`, `codex app-server --stdio` com `account/rateLimits/read` + `model/list`, e `claude --no-session-persistence`) trazendo **todos os modelos disponíveis no PC** e as cotas de cada família sem criar sessões no histórico.
2. **Proibição de Monocultura:** nunca abra todos os terminais do Team CODES na mesma IA se houver mais de um provedor autenticado com cota. Distribua cada papel (`Front-End`, `Back-End`, `Test/QA`, `Review`) para o **Preset + Modelo** que melhor combina **aptidão técnica da tarefa + folga de cota**.
3. **Como cada Terminal recebe as Skills Certas para a Demanda (`agent_sort.py` + `find-skills`):**
   * **Busca Local (`agent_sort.py --match`):** além das skills fixas de `.agents/roles/<papel>.md` e `.agents/skills.json` (stack DAILY), antes de enviar uma demanda rode `python ~/.minerva/toolkits/agent_sort.py --match "<descrição da demanda>"`.
   * **Busca Externa (`find-skills`):** se a demanda exigir tecnologia sem skill local, use a skill `find-skills` (`npx skills find <termo>` e `npx skills add <pacote> -g -y`).
   * **Injeção no Prompt:** no comando `maestri ask "<Terminal>"`, **liste explicitamente as skills recomendadas** (ex.: *"Antes de codar, leia `~/.minerva/skills/shadcn/SKILL.md`, `~/.minerva/skills/transitions-dev/SKILL.md` e aplique `ponytail`"*).
4. **Consulta Prévia Obrigatória:** apresente a tabela (`Papel | Preset/CLI | Modelo Sugerido | Cota & Justificativa`) e pergunte se o usuário aprova ou deseja trocar algum modelo antes de rodar `maestri recruit --preset "<Preset-Aprovado>"`.

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
