---
tags:
  - ai/mcp
  - mcp-server
  - design-systems
  - ui
  - prototyping
name: "magicpath"
website: "https://magicpath.ai"
updated_at: "2026-11-12T18:50:00.000Z"
---

# ✨ Servidor MCP: MagicPath (Design Systems & Geração de Componentes UI)

> [!INFO] **Visão Geral Oficial**
> **Website Oficial:** [https://magicpath.ai](https://magicpath.ai)  
> **Identificador MCP:** `magicpath`  
> **Tipo de Conexão:** SSE / Endpoint Remoto Seguro (`https://api.magicpath.ai/mcp`)  
> **CLI Local Auxiliar:** `npx -y magicpath-ai` (com a flag `-o json`)  
> **Papel Principal:** Front-End Specialist & Minerva

---

## 💡 O que é o MagicPath? (Resumo Oficial)

O **MagicPath** é uma plataforma e servidor MCP remoto dedicado à **geração automatizada de componentes visuais, telas de design system e protótipos de interface** diretamente para agentes de desenvolvimento de IA.

Conectado ao ambiente de trabalho, ele permite que a Minerva e o Front-End Specialist solicitem tokens de design, especificações de componentes e estruturas de tela prontos para React/Next.js e Tailwind CSS, acelerando dramaticamente a entrega da camada visual.

---

## 🛠️ Como Funciona e Como Usar no Projeto

### 1. Chamada via CLI do Terminal
```bash
# Consultar componentes ou tokens no MagicPath (sempre usar -o json para retorno estruturado):
npx -y magicpath-ai search "cards de faturamento" -o json
```

### 2. Uso Direto pelo Agente de IA
O agente invoca as ferramentas remotas do MagicPath via protocolo MCP:
* *"Gere uma estrutura de dashboard com cards de métricas usando o tema dark do MagicPath."*
* *"Consulte os tokens de espaçamento e tipografia recomendados para tabelas de alta densidade."*

---

## 🔌 Configuração Oficial no MCP (Model Context Protocol)

Adicione ao seu arquivo de configuração MCP (`~/.claude.json`, Codex, etc.):

```json
{
  "mcpServers": {
    "magicpath": {
      "url": "https://api.magicpath.ai/mcp"
    }
  }
}
```

---

## 🤝 Integração com o Team CODES
* **Minerva:** Utiliza o MagicPath para esboçar a arquitetura visual inicial e incluir referências de componentes na `docs/spec.md`.
* **Front-End Specialist:** Consome os componentes e tokens de design do MagicPath em conjunto com a `taste-skill` e os design systems do `awesome-design-md` para gerar código limpo e anti-slop na branch `agent/ui`.
