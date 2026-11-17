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

## 3. Alocação Anti-Monocultura por Cota & Aptidão (Lei 8 — Protocolo Alethe)

1. **Inspeção Real de Contas e Cotas:** consulte os dados ao vivo do Painel (`:3333` / `publico/dados.json` ou `live_quota.json`) e verifique quais CLIs estão autenticados e com saldo.
2. **Proibição de Monocultura:** nunca abra todos os terminais do Team CODES na mesma IA se houver mais de um provedor autenticado com cota. Distribua cada papel (`Front-End`, `Back-End`, `Test/QA`, `Review`) para a IA que melhor combina **aptidão técnica da tarefa + folga de cota**.
3. **Consulta Prévia Obrigatória:** apresente a tabela (`Papel | Preset/CLI | Modelo Sugerido | Cota & Justificativa`) e pergunte se o usuário aprova ou deseja trocar algum modelo antes de rodar `maestri recruit --preset "<Preset-Aprovado>"`.

## 4. Handshake & Failover Automático de IA no Terminal (Lei 10)

1. **Proibição Absoluta de Auto-Codificação:** a Minerva jamais escreve o código de produção no lugar do Team CODES caso um terminal falhe.
2. **Handshake Imediato:** após `maestri recruit`, verifique com `maestri check "<Nome>"`. Se houver prompt interativo de confirmação (`Trust this folder?`, `Update available`, `Choose text style`), envie `maestri ask "<Nome>" --raw "\n"` e despache a tarefa completa em seguida.
3. **Failover Automático para Outra IA:** se o terminal recrutado apresentar erro de login (`Not logged in`), falta de cota, crash ou continuar travado após o Handshake:
   * **Não pare com erro e não codifique sozinha.**
   * Troque imediatamente aquele terminal para **outra IA autenticada e com cota disponível** (`maestri recruit --replace "<Nome>" --preset "<Outra-IA-Disponivel>"`).
   * Realize o Handshake no novo terminal e **passe a demanda integralmente para a nova IA executar**.
