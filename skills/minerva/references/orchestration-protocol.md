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

## 3. Alocação Anti-Monocultura por Cota & Seleção de Skills por Demanda (Lei 8 — Protocolo Alethe)

1. **Leitura Direta do Maestri e do PC (`minerva_quotas.py`):** execute `python ~/.minerva/toolkits/minerva_quotas.py`, que lê diretamente `~/.maestri/usage/providers/.status.json`, `~/.maestri/preferences.json` e os arquivos nativos dos CLIs no PC (`~/.gemini/antigravity-cli/live_quota.json`, `~/.codex/auth.json`, `~/.claude.json`) **sem depender do Painel (`:3333`) estar aberto** e **sem abrir sessões nos CLIs**.
2. **Proibição de Monocultura:** nunca abra todos os terminais do Team CODES na mesma IA se houver mais de um provedor autenticado com cota. Distribua cada papel (`Front-End`, `Back-End`, `Test/QA`, `Review`) para a IA que melhor combina **aptidão técnica da tarefa + folga de cota**.
3. **Como cada Terminal recebe as Skills Certas para a Demanda:**
   * Além das skills fixas de `.agents/roles/<papel>.md` e `.agents/skills.json` (stack DAILY), antes de enviar uma demanda rode `python ~/.minerva/toolkits/agent_sort.py --match "<descrição da demanda>"`.
   * No comando `maestri ask "<Terminal>"`, **liste explicitamente as skills recomendadas** (ex.: *"Antes de codar, leia `~/.minerva/skills/shadcn/SKILL.md`, `~/.minerva/skills/transitions-dev/SKILL.md` e aplique `ponytail`"*).
4. **Consulta Prévia Obrigatória:** apresente a tabela (`Papel | Preset/CLI | Modelo Sugerido | Cota & Justificativa`) e pergunte se o usuário aprova ou deseja trocar algum modelo antes de rodar `maestri recruit --preset "<Preset-Aprovado>"`.

## 4. Higiene de Sessões (Zero Poluição no PC), Handshake & Failover Automático de IA (Lei 10)

1. **Regra "Reuse Before Recruiting" (Anti-Poluição de Sessões no PC):**
   * Antes de recrutar qualquer terminal, rode **`maestri list`**. Se já existir terminal ativo para aquele papel no Canvas, **reutilize-o via `maestri ask "<Nome>"`** em vez de criar um novo terminal — garantindo **apenas 1 sessão contínua por papel** no histórico do PC.
   * Quando encerrar um ciclo grande, podem ser usados `claude purge` / `codex archive` para limpar sessões antigas.
2. **Proibição Absoluta de Auto-Codificação:** a Minerva jamais escreve o código de produção no lugar do Team CODES caso um terminal falhe.
3. **Handshake Imediato:** após `maestri recruit`, verifique com `maestri check "<Nome>"`. Se houver prompt interativo de confirmação (`Trust this folder?`, `Update available`, `Choose text style`), envie `maestri ask "<Nome>" --raw "\n"` e despache a tarefa completa em seguida.
4. **Failover Automático para Outra IA (`--replace`):** se o terminal recrutado apresentar erro de login (`Not logged in`), falta de cota, crash ou continuar travado após o Handshake:
   * **Não pare com erro e não codifique sozinha.**
   * Substitua imediatamente aquele terminal in-place por **outra IA autenticada e com cota disponível** (`maestri recruit --replace "<Nome>" --preset "<Outra-IA-Disponivel>"`).
   * Realize o Handshake no novo terminal e **passe a demanda integralmente (com as skills da tarefa) para a nova IA executar**.
