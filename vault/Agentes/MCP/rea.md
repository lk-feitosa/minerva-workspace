---
tags:
  - ai/mcp
  - mcp-server
  - reverse-engineering
  - security
  - binary-analysis
name: "rea"
github: "https://github.com/morluto/rea"
updated_at: "2026-11-12T18:50:00.000Z"
---

# 🕵️ Servidor MCP: REA (Reverse Engineer Anything)

> [!INFO] **Visão Geral Oficial**
> **Repositório Oficial:** [https://github.com/morluto/rea](https://github.com/morluto/rea)  
> **Website Oficial:** [https://rea.tools](https://rea.tools)  
> **Comunidade & Documentação:** [https://rea.tools/guides/](https://rea.tools/guides/)  
> **Pacote npm:** `rea-agents`  
> **Licença:** MIT  
> **Identificador MCP:** `rea`

---

## 💡 O que é o REA? (Resumo Oficial)

O **REA (Reverse Engineer Anything)** é um servidor MCP abrangente projetado para capacitar agentes de IA a realizarem **engenharia reversa completa** em binários compilados, aplicativos desktop (Electron, .NET, nativos), pacotes móveis (APKs Android) e sites/scripts web.

### Proposta de Valor Central:
> *"Viu uma funcionalidade que gostou em outro software? Entenda exatamente como ela funciona, até o nível binário, e construa uma versão limpa para o seu projeto."*

### O que o REA Permite Analisar:
* **Binários Nativos:** Descompilação para pseudocódigo C e assembly integrando-se nativamente a engines locais como Hopper, Ghidra, IDA Pro ou Rizin.
* **Aplicações JavaScript & Electron:** Extração e recuperação de módulos originais, reconciliação de runtime e mapeamento de dependências.
* **Pacotes Android (APK):** Mapeamento de classes, inspeção de bytecode, decodificação de recursos via Apktool/JEB e rastreamento de chamadas JNI.
* **Tráfego de Rede & Protocolos:** Análise profunda de pacotes PCAP e contratos de API.

---

## 🛠️ Como Funciona e Como Usar no Projeto

### 1. Configuração Rápida via CLI
```bash
npx rea-agents@latest setup
```
O utilitário detecta os engines de engenharia reversa instalados na máquina (Hopper, Ghidra, Rizin) e registra o servidor MCP no seu ambiente de agentes.

### 2. Exemplos de Comandos para Agentes
* *"Analise o executável `app.exe` e me diga quais endpoints de telemetria ele chama."*
* *"Inspecione o bundle JavaScript da pasta `dist/` e recupere as assinaturas das funções de autenticação."*
* *"Extraia o APK `client.apk` e mapeie as permissões e serviços em segundo plano."*

---

## 🔌 Configuração Oficial no MCP (Model Context Protocol)

Adicione ao seu arquivo de configuração MCP (`~/.claude.json`, Codex, etc.):

```json
{
  "mcpServers": {
    "rea": {
      "command": "cmd.exe",
      "args": [
        "/d",
        "/c",
        "npx",
        "-y",
        "rea-agents@latest",
        "mcp"
      ]
    }
  }
}
```

---

## 📖 README Oficial do Repositório (REA Upstream)

<details>
<summary><strong>📄 Clique aqui para expandir o README oficial original (em inglês)</strong></summary>

```markdown
# REA: Reverse Engineer Anything

One MCP for reverse engineering across binaries, applications, and runtime behavior.
See a feature you like. Understand how it works, down to the binary level.

Website: https://rea.tools

## Quick Start
```bash
npx rea-agents setup
```

## Capabilities
- Native binaries (pseudocode & assembly via Hopper, Ghidra, IDA, Rizin)
- JavaScript & Electron bundles (module recovery and runtime reconciliation)
- Android APKs (classes, JNI bindings, bytecode inspection)
- Network pcaps & API contract reverse engineering

## License
MIT. Copyright (c) Morluto.
```

</details>
