# Visão Arquitetural (`docs/architecture.md`)

> Mantida viva conforme o projeto evolui. Decisões irreversíveis ou estruturais devem gerar um ADR em `docs/adr/`.

## 1. Stack & Componentes
* **Aplicação:** *(detectado automaticamente nos manifestos do repositório)*
* **Persistência / APIs:** *(a definir)*

## 2. Topologia & Fluxo de Dados
```text
Cliente / UI -> API / Serviços -> Persistência
```

## 3. Portas & Serviços Locais de Desenvolvimento
* `3333`: Painel de Agentes (`painel-agents`)
* `3334`: Kanban Minimalista (`kanban-agents`, estado em `.kanban/board.json`)
