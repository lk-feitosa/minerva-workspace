---
tags:
  - ai/skill
  - agent-tooling
  - category/discovery
  - category/meta-skill
name: "find-skills"
github: "https://github.com/vercel-labs/skills"
updated_at: "2026-11-11T21:48:00.000Z"
---

# Skill: find-skills (Vercel Labs / skills.sh)

> [!INFO] **Visão Geral**
> **Repositório Oficial:** [https://github.com/vercel-labs/skills](https://github.com/vercel-labs/skills)  
> **Diretório Global de Skills:** [https://skills.sh](https://skills.sh)  
> **Caminho Local no Sistema:** `C:\Users\lukas\.agents\skills\find-skills`  
> **CLI Oficial:** `npx skills find` / `npx skills add`

### Descrição & Finalidade (PT-BR)
A **`find-skills`** é uma **meta-skill** desenvolvida pela Vercel Labs que capacita os agentes de IA (Minerva, Claude Code, Codex, Antigravity) a descobrirem, pesquisarem e instalarem dinamicamente novas habilidades sob demanda a partir do ecossistema aberto da **[skills.sh](https://skills.sh/)**.

Use quando:
- O usuário pergunta *"Como eu faço X?"* e X pode ser resolvido por uma skill open-source existente.
- O usuário diz *"Procure uma skill para X"* ou *"Existe alguma skill para..."*.
- Uma demanda do projeto exige uma ferramenta especializada ainda não presente no repositório (ex: testes de carga com k6, animações avançadas Framer Motion, migração Drizzle/Prisma, geração de diagramas OpenAPI, etc.).

---

## 🛠️ Comandos Principais do CLI (`npx skills`)

```bash
# 1. Pesquisar skills interativamente ou por termo
npx skills find [termo]
npx skills find react performance
npx skills find playwright --owner microsoft

# 2. Instalar uma skill diretamente para os agentes do projeto
npx skills add <owner/repo@skill> -g -y

# 3. Listar skills instaladas
npx skills list -g
```

---

## 🐍 Como a Minerva Utiliza o `find-skills` (Governança Ativa)

1. **Auto-Extensão sob Demanda (Auto-Discovery):**  
   Ao analisar a especificação (`docs/spec.md`) de uma nova demanda, se a Minerva detectar que o time necessita de uma capacidade técnica inédita (ex.: Stripe Webhooks, Three.js 3D, automação Docker), ela pode pesquisar com `npx skills find [tecnologia]`.
2. **Proposta Consultiva:**  
   Em vez de alucinar ou escrever instruções do zero, ela apresenta ao usuário:  
   *"Encontrei a skill oficial `owner/repo@skill` com 50k+ instalações no skills.sh. Autoriza a instalação para o Team CODES?"*
3. **Instalação e Injeção Instantânea:**  
   Com a autorização (ou automaticamente em modo Zero-HITL), ela executa `npx skills add ...` e a nova skill fica imediatamente acessível para o terminal especialista do Canvas.
