---
tags:
  - ai/arquitetura
  - documentacao
  - infraestrutura
  - ecossistema
updated_at: "2026-11-06T15:47:00-03:00"
---

# Arquitetura, Conceito & Organização Global do Ecossistema de IA

> [!NOTE] **Objetivo Deste Documento**  
> Registrar a visão técnica, os fundamentos de engenharia, a topologia de armazenamento no disco `S:`, os mecanismos de links simbólicos (NTFS Junctions), o isolamento de projetos via MCP (`ai-memory`) e a organização das 350+ skills no Obsidian.

---

## 1. A Ideia & Motivação

Historicamente, cada ferramenta de IA instalada no Windows (Codex, Claude Code, Antigravity, Hermes Agent, Ollama, etc.) cria arquivos e modelos nos diretórios de perfil de usuário dentro da unidade do sistema:
* `C:\Users\lukas\.agents`
* `C:\Users\lukas\.codex`
* `C:\Users\lukas\AppData\Local\...`

Essa abordagem fragmentada causa três problemas graves:
1. **Sobrecarga do Drive `C:`**: Modelos, caches de pacotes, compilações e repositórios consomem espaço valioso do SSD do sistema operacional.
2. **Falta de Portabilidade e Backup**: Dificuldade para clonar, versionar ou sincronizar o ambiente caso o sistema seja formatado ou migrado.
3. **Contaminação de Contexto entre Projetos**: IAs interagindo com projetos diferentes (como `Snorlax`, `kota`, etc.) acabam misturando regras de negócio, históricos e memórias se configuradas de forma ingênua.

### A Solução Adotada
Consolidar **100% dos dados, ferramentas, repositórios, skills, frameworks e cofre do Obsidian** na unidade de desenvolvimento dedicada:
$$\mathbf{S:\backslash DEV}$$

---

## 2. Topologia do Disco `S:\DEV`

```mermaid
graph TD
    DEV["S:\DEV (Unidade Central de Desenvolvimento)"]
    
    AGENTS["📁 S:\DEV\agents\ (Centro de Inteligência Artificial)"]
    PROJS["📁 S:\DEV\projs\ (Seus Projetos de Código: Snorlax, kota...)"]
    FRAMEWORKS["📁 S:\DEV\frameworks\ (Templates & Orquestração Multi-Agente)"]
    APPS["📁 S:\DEV\apps\ (Aplicações de IA Locais com Aceleração de GPU/CPU)"]
    
    DEV --> AGENTS
    DEV --> PROJS
    DEV --> FRAMEWORKS
    DEV --> APPS
    
    AGENTS --> SKILLS["📁 skills/ (368 Habilidades de Agentes)"]
    AGENTS --> MCP_CFG["⚙️ mcp_config.json (Configuração Mestre MCP)"]
    AGENTS --> MEM["📁 ai-memory/ (Base de Dados Rust do Akita)"]
    AGENTS --> HERMES["📁 hermes/skins/ (16 Skins Personalizadas)"]
    AGENTS --> TOOLKITS["📁 toolkits/ (Vibe Coding Toolkit & Prompts)"]
    AGENTS --> VAULT["📁 vault/Agentes/ (Cofre Hierárquico do Obsidian)"]
```

### Detalhamento dos Diretórios Principais:
| Diretório | Função | Conteúdo |
| :--- | :--- | :--- |
| `S:\DEV\agents\` | Núcleo do ecossistema de IA | Repositório Git mestre contendo todas as skills, configurações MCP, skins e o cofre do Obsidian. |
| `S:\DEV\frameworks\` | Frameworks de orquestração | `alethe-agents`, `agent-teams-ai`, `claude-cookbooks`, `ottomator-agents`, `openwork`, `scrapling`. |
| `S:\DEV\apps\` | Aplicações locais com GPU/CPU | `stable-diffusion-webui` (geração de imagens), `open-notebook` (pesquisa e RAG), `unsloth` (fine-tuning). |
| `S:\DEV\projs\` | Projetos de desenvolvimento | Código-fonte dos sistemas reais (ex: `Snorlax`, `kota`, etc.), totalmente isolados. |

---

## 3. A Estratégia de NTFS Junctions & Symlinks (Ponte Transparente no SO)

As ferramentas de IA normalmente procuram configurações na pasta de usuário (`~` ou `%USERPROFILE%`).  
Para contornar isso **sem duplicar arquivos e mantendo uma única biblioteca centralizada**, o sistema cria **Junções de Diretório NTFS** no Windows (`mklink /J`) ou **Links Simbólicos** no Linux/Mac (`ln -s`):

```mermaid
flowchart LR
    subgraph Usuario [Diretório do Usuário (~ ou %USERPROFILE%)]
        C_AGENTS["~/.agents"]
        C_CODEX["~/.codex/skills"]
        C_HERMES["~/.hermes/skins (ou %LOCALAPPDATA%)"]
    end
    
    subgraph Central [Repositório Central Clonado]
        S_AGENTS["S:\DEV\agents"]
        S_SKILLS["S:\DEV\agents\skills"]
        S_HERMES["S:\DEV\agents\hermes\skins"]
    end
    
    C_AGENTS -. Junction / Symlink .-> S_AGENTS
    C_CODEX -. Junction / Symlink .-> S_SKILLS
    C_HERMES -. Junction / Symlink .-> S_HERMES
```

### O que o Usuário Baixa vs O que o Setup Faz:
1. **No Clone do Git:** O usuário baixa exclusivamente os arquivos de inteligência, as 368 skills, as skins, os prompts e o cofre do Obsidian. Arquivos de cache e bancos binários ficam de fora (`.gitignore`).
2. **No Setup:** O script cria as pontes transparentes do sistema operacional. Com isso, **Claude Code, Codex, Antigravity e Maestri** passam a consultar a mesma pasta unificada sem redundância. Se você atualizar ou criar uma nova skill, todas as IAs a reconhecem instantaneamente.
```

> [!TIP] **Por que Junctions e não atalhos comuns (.lnk)?**  
> Uma junção NTFS opera em nível de sistema de arquivos do kernel do Windows. Para qualquer processo (Node.js, Python, Git, Claude, Codex), o caminho `C:\Users\lukas\.agents` é lido como uma pasta física real, mas todo byte escrito vai instantaneamente para `S:\DEV\agents`.

---

## 4. Protocolo MCP & Isolamento de Memória (`ai-memory`)

### O Desafio do Isolamento
Quando você trabalha no projeto `Snorlax` e depois no `kota`, como garantir que o agente não misture regras de um repositório no outro?

### Como o `ai-memory` (Akita on Rails) Resolve:
1. **Binário Nativo em Rust**: Instalado em `C:\Users\lukas\AppData\Local\Programs\ai-memory\ai-memory.exe`.
2. **Execução via Stdio MCP**: Invocado automaticamente pelas IAs através do protocolo padrão MCP.
3. **Detecção Dinâmica do Projeto**:  
   O `ai-memory` inspeciona a raiz do repositório Git atual (`git rev-parse --show-toplevel`) ou o diretório de execução (`cwd`).
   - Ao executar dentro de `S:\DEV\projs\Snorlax`, todo conhecimento gerado e memorizado é indexado com o escopo `Snorlax`.
   - Ao trocar para `S:\DEV\projs\kota`, o escopo muda imediatamente para `kota`.
   - Um projeto **nunca tem acesso** às notas, memórias ou segredos técnicos do outro.
4. **Armazenamento Centralizado**: A base bruta e banco de dados SQLite/Markdown ficam salvos com segurança em `S:\DEV\agents\ai-memory`.

```mermaid
sequenceDiagram
    participant Agente as Agente de IA (Codex / Antigravity)
    participant MCP as MCP ai-memory (Rust Stdio)
    participant Storage as S:\DEV\agents\ai-memory
    
    Note over Agente: Agente operando em S:\DEV\projs\Snorlax
    Agente->>MCP: Salvar aprendizado técnico sobre Snorlax
    MCP->>MCP: Detecta Git Root = 'Snorlax'
    MCP->>Storage: Grava na partição isolada do projeto 'Snorlax'
    
    Note over Agente: Usuário troca de projeto para S:\DEV\projs\kota
    Agente->>MCP: Consultar histórico e padrões do projeto atual
    MCP->>MCP: Detecta Git Root = 'kota'
    MCP->>Storage: Busca estritamente a partição 'kota'
    Storage-->>Agente: Retorna apenas regras do projeto 'kota'
```

---

## 5. A Estrutura Hierárquica do Cofre no Obsidian

Para evitar uma lista plana de centenas de pastas na raiz do Obsidian, o cofre em `S:\DEV\agents\vault\Agentes` foi desenhado com organização por categorias:

```text
S:\DEV\agents\vault\Agentes\
│
├── 📄 _Hub de Skills & MCPs.md                   <-- Dashboard Geral
├── 📄 _Arquitetura e Documentação do Ecossistema.md <-- Esta Nota
│
├── 📁 Skills/                                     <-- Catálogo de 359 Habilidades
│   ├── agent-deep-links/
│   │   ├── Visão Geral.md
│   │   └── deep-link-matrix.md
│   ├── browser-testing-with-devtools/
│   │   ├── Visão Geral.md
│   │   └── ...
│   └── (todas as outras com manuais e playbooks)
│
├── 📁 MCP/                                        <-- Servidores do Protocolo MCP
│   ├── _Visão Geral MCP.md
│   ├── ai-memory.md                               (Akita on Rails)
│   ├── agent-desktop.md                           (Vercel Labs - Computer Use)
│   ├── rea.md                                     (Reverse Engineer Anything)
│   └── magicpath.md                               (Design Engine)
│
├── 📁 MODS/                                       <-- Modificações & Estilos
│   ├── Hermes Skins/                              (16 skins YAML completas)
│   └── Toolkits/                                  (Vibe Coding Toolkit)
│
├── 📁 Frameworks/                                 <-- Arquiteturas de Agentes
│   ├── _Visão Geral Frameworks.md
│   ├── alethe-agents.md
│   ├── agent-teams-ai.md
│   ├── claude-cookbooks.md
│   ├── openwork.md
│   └── ottomator-agents.md
│
└── 📁 Opcionais/                                  <-- Utilitários de Apoio & Produtividade
    ├── _Visão Geral Opcionais.md
    ├── painel-agents.md                           (Telemetria e monitor de cotas Maestri)
    ├── kan-kanban.md                              (Quadro Kanban contextual por projeto)
    └── ai-statusline.md                           (Barra de status leve para terminal)
```

---

## 6. Aceleração de Hardware Local (GPU / CPU)

Para as ferramentas da pasta `S:\DEV\apps`, a máquina dispõe de hardware de ponta:
* **GPU Suportada**: NVIDIA GeForce (CUDA), Apple Silicon (MPS), AMD (ROCm) ou CPU.
* **CPU / Memória**: 16GB+ de RAM recomendados (32GB para modelos maiores).

### Como as ferramentas utilizam a GPU:
1. **`stable-diffusion-webui`**: Geração de imagens local de altíssima velocidade utilizando CUDA e xformers / SDP Attention. Inicie via `webui-user.bat`.
2. **`unsloth`**: Fine-tuning e calibração de modelos locais (Llama 3, Qwen 2.5, Gemma) consumindo até 80% menos VRAM com otimização manual dos kernels de GPU.
3. **`open-notebook`**: Processamento e embeddings locais de documentos para busca semântica privada sem enviar dados confidenciais para servidores externos.

---

## 7. Gestão Inteligente de Contexto e Orçamento de Tokens nas IDEs

Ao inspecionar as configurações no **Antigravity IDE** ou ferramentas similares com centenas de habilidades (378 skills), é exibido o aviso:
`Customization token budget exceeded. Large customizations are excluded from context.`

### O que isso significa e por que é o comportamento correto?
1. **Proteção da Janela de Contexto:** Se uma IA injetasse as instruções completas de 378 skills simultaneamente no prompt inicial, gastaria mais de **57.000 tokens** antes mesmo do usuário fazer uma pergunta.
2. **Hierarquia de Prioridade:**
   * **Rules (Regras Globais):** Têm prioridade máxima (sempre carregadas 100% no contexto).
   * **MCP Tools:** São disponibilizadas como esquemas compactos de ferramentas (como visto no IDE: `rea`, `agent-desktop`, `kan`).
   * **Skills:** Ficam indexadas globalmente com a tag `Global`. O IDE mantém seus metadados e demite o corpo extenso de skills não usadas até que sejam invocadas pelo usuário ou ativadas sob demanda.

---

## 8. Manutenção, Atualizações & Automação

Sempre que novas skills forem adicionadas no diretório `S:\DEV\agents\skills` ou novos servidores forem configurados no `mcp_config.json`, basta rodar o script de sincronização no terminal:

```bash
node S:\DEV\agents\sync_obsidian.mjs
```

### O que o script faz automaticamente:
* Varre todas as 370+ pastas de skills em busca de arquivos `SKILL.md` e referências `.md`.
* Gera a estrutura de subpastas organizada em `Skills/`.
* Extrai metadados (frontmatter) de cada skill (autor, repositório de origem, tags, comandos).
* Atualiza a lista de servidores MCP e **propaga automaticamente** para o Gemini CLI (`~/.gemini/config/mcp_config.json`).
* Atualiza os frameworks, opcionais e aplicações com documentação pronta para consulta.
* Reconstrói o dashboard central `_Hub de Skills & MCPs.md`.

---

## Resumo dos Benefícios Conquistados

1. **Unificação Real**: Todas as IAs (Antigravity, Codex, Claude Code, Hermes, Maestri) bebem da mesma fonte de dados no disco `S:`.
2. **Drive C: Limpo & Rápido**: O SSD do sistema permanece livre de gigabytes de repositórios e modelos.
3. **Privacidade e Isolamento**: O `ai-memory` impede vazamento de contexto entre projetos distintos.
4. **Navegação Produtiva no Obsidian**: Documentação viva, com links bidirecionais (`[[...]]`), visualização em grafo e pesquisa instantânea.
