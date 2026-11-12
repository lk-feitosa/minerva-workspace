import fs from 'fs';
import path from 'path';
import os from 'os';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT_AGENTS_DIR = __dirname;
const SKILLS_DIR = path.join(ROOT_AGENTS_DIR, 'skills');
const MCP_CONFIG_PATH = path.join(ROOT_AGENTS_DIR, 'mcp_config.json');
const TOOLKITS_DIR = path.join(ROOT_AGENTS_DIR, 'toolkits');
const HERMES_SKINS_DIR = path.join(ROOT_AGENTS_DIR, 'hermes', 'skins');
const VAULT_DIR = path.join(ROOT_AGENTS_DIR, 'vault', 'Agentes');

const FRAMEWORKS_SRC_DIR = 'S:\\DEV\\frameworks';
const PTBR_CACHE_PATH = path.join(ROOT_AGENTS_DIR, 'skills_ptbr_cache.json');

const SKILLS_OUTPUT_DIR = path.join(VAULT_DIR, 'Skills');
const MCP_OUTPUT_DIR = path.join(VAULT_DIR, 'MCP');
const MODS_OUTPUT_DIR = path.join(VAULT_DIR, 'MODS');
const FRAMEWORKS_OUTPUT_DIR = path.join(VAULT_DIR, 'Frameworks');

const ADDY_SKILLS = new Set(['api-and-interface-design', 'browser-testing-with-devtools', 'ci-cd-and-automation', 'code-review-and-quality', 'code-simplification', 'constraint-driven-development', 'context-engineering', 'debugging-and-error-recovery', 'deprecation-and-migration', 'documentation-and-adrs', 'doubt-driven-development', 'frontend-ui-engineering', 'git-workflow-and-versioning', 'idea-refine', 'incremental-implementation', 'interview-me', 'observability-and-instrumentation', 'performance-optimization', 'planning-and-task-breakdown', 'security-and-hardening', 'shipping-and-launch', 'source-driven-development', 'spec-driven-development', 'test-driven-development', 'using-agent-skills']);

const MATT_SKILLS = new Set(['ask-matt', 'code-review', 'codebase-design', 'diagnosing-bugs', 'domain-modeling', 'grill-with-docs', 'implement', 'implement-spec', 'improve-codebase-architecture', 'pr', 'prototype', 'research', 'retro', 'setup-matt-pocock-skills', 'tdd', 'to-spec', 'to-tickets', 'triage', 'wayfinder', 'wizard', 'chief-of-staff', 'claude-handoff', 'loop-me', 'setup-ts-deep-modules', 'software-factory', 'writing-beats', 'writing-fragments', 'writing-shape', 'git-guardrails-claude-code', 'migrate-to-shoehorn', 'scaffold-exercises', 'setup-pre-commit', 'grill-me', 'grilling', 'handoff', 'teach', 'to-questionnaire', 'wait-what', 'writing-for-agents']);

const ECC_SKILLS = new Set(['agent-introspection-debugging', 'agent-sort', 'api-design', 'article-writing', 'backend-patterns', 'benchmark-methodology', 'brand-discovery', 'brand-voice', 'bun-runtime', 'change-impact', 'coding-standards', 'competitive-platform-analysis', 'competitive-report-structure', 'content-engine', 'context-and-decisions', 'crosspost', 'deep-research', 'dmux-workflows', 'docs-governance', 'documentation-lookup', 'e2e-testing', 'ecc-conventions', 'eval-harness', 'exa-search', 'fal-ai-media', 'frontend-patterns', 'frontend-slides', 'investor-materials', 'investor-outreach', 'market-research', 'mcp-dependency-review', 'mcp-server-patterns', 'mle-workflow', 'module-governance', 'module-regression', 'nextjs-turbopack', 'plan-canvas', 'product-capability', 'security-review', 'skill-host-compat', 'strategic-compact', 'tdd-workflow', 'test-collaboration', 'unified-memory', 'verification-loop', 'video-editing', 'x-api']);

const AWESOME_CODEX = new Set(['agent-deep-links', 'brand-guidelines', 'canvas-design', 'changelog-generator', 'codebase-migrate', 'competitive-ads-extractor', 'connect', 'connect-apps', 'content-research-writer', 'create-plan', 'datadog-logs', 'deploy-pipeline', 'developer-growth-analysis', 'domain-name-brainstormer', 'email-draft-polish', 'file-organizer', 'gh-address-comments', 'gh-fix-ci', 'helium-mcp', 'image-enhancer', 'internal-comms', 'invoice-organizer', 'issue-triage', 'langsmith-fetch', 'lead-research-assistant', 'linear', 'mcp-builder', 'meeting-insights-analyzer', 'meeting-notes-and-actions', 'notion-knowledge-capture', 'notion-meeting-intelligence', 'notion-research-documentation', 'notion-spec-to-implementation', 'paperjsx', 'pr-review-ci-fix', 'raffle-winner-picker', 'sentry-triage', 'skill-creator', 'skill-installer', 'skill-share', 'slack-gif-creator', 'spreadsheet-formula-helper', 'support-ticket-triage', 'tailored-resume-generator', 'template-skill', 'theme-factory', 'video-downloader', 'webapp-testing']);

function resolveRepo(name) {
  if (name.startsWith('google-')) return 'https://github.com/google/skills';
  if (ADDY_SKILLS.has(name)) return 'https://github.com/addyosmani/agent-skills';
  if (MATT_SKILLS.has(name)) return 'https://github.com/mattpocock/skills';
  if (ECC_SKILLS.has(name)) return 'https://github.com/affaan-m/ECC';
  if (AWESOME_CODEX.has(name)) return 'https://github.com/composio-community/awesome-codex-skills';
  if (name === 'alethe') return 'https://github.com/Kc1t/alethe-orchestrate-skill';
  if (name === 'llm-council') return 'https://github.com/aiwithremy/claude-skills-llm-council';
  if (name === 'reverse-engineer-anything') return 'https://github.com/morluto/rea';
  if (name.startsWith('agent-desktop')) return 'https://github.com/vercel-labs/agent-desktop';
  if (name.startsWith('maestri')) return 'https://maestri.ai';
  if (name === 'magicpath') return 'https://magicpath.ai';
  return 'Local / Ecossistema Pessoal';
}

function ensureDir(dir) {
  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir, { recursive: true });
  }
}

function parseFrontmatter(content) {
  const match = content.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n([\s\S]*)$/);
  if (!match) return { meta: {}, body: content };
  
  const rawMeta = match[1];
  const body = match[2];
  const meta = {};
  
  for (const line of rawMeta.split(/\r?\n/)) {
    const idx = line.indexOf(':');
    if (idx !== -1) {
      const key = line.slice(0, idx).trim();
      let val = line.slice(idx + 1).trim();
      if ((val.startsWith('"') && val.endsWith('"')) || (val.startsWith("'") && val.endsWith("'"))) {
        val = val.slice(1, -1).trim();
      }
      val = val.replace(/\\"/g, '"');
      meta[key] = val;
    }
  }
  return { meta, body };
}

function getAllFiles(dirPath, arrayOfFiles = []) {
  if (!fs.existsSync(dirPath)) return arrayOfFiles;
  const files = fs.readdirSync(dirPath, { withFileTypes: true });
  for (const file of files) {
    const fullPath = path.join(dirPath, file.name);
    if (file.isDirectory()) {
      if (file.name === '.git' || file.name === 'node_modules') continue;
      getAllFiles(fullPath, arrayOfFiles);
    } else {
      arrayOfFiles.push(fullPath);
    }
  }
  return arrayOfFiles;
}

function sync() {
  console.log('🔄 Sincronizando Ecossistema de IA em Estrutura Hierárquica no Obsidian...');

  ensureDir(SKILLS_OUTPUT_DIR);
  ensureDir(MCP_OUTPUT_DIR);
  ensureDir(MODS_OUTPUT_DIR);
  ensureDir(FRAMEWORKS_OUTPUT_DIR);
  ensureDir(APPS_OUTPUT_DIR);

  // ==========================================
  // 1. SINCRONIZAR SKILLS (Pasta por Skill)
  // ==========================================
  const skillDirs = fs.readdirSync(SKILLS_DIR, { withFileTypes: true })
    .filter(d => d.isDirectory() && d.name !== '.system')
    .map(d => d.name);

  const skillsData = [];

  // Carregar cache de tradução PT-BR
  let ptbrCache = {};
  if (fs.existsSync(PTBR_CACHE_PATH)) {
    try {
      ptbrCache = JSON.parse(fs.readFileSync(PTBR_CACHE_PATH, 'utf8'));
    } catch (e) {
      console.warn('⚠️ Erro ao carregar cache de tradução:', e.message);
    }
  }

  for (const skillName of skillDirs) {
    const skillSourcePath = path.join(SKILLS_DIR, skillName);
    const mainSkillFile = path.join(skillSourcePath, 'SKILL.md');
    
    if (!fs.existsSync(mainSkillFile)) continue;

    const safeSkillDirName = skillName.replace(/[<>:"/\\|?*]/g, '_');
    const skillVaultFolder = path.join(SKILLS_OUTPUT_DIR, safeSkillDirName);
    ensureDir(skillVaultFolder);

    const rawContent = fs.readFileSync(mainSkillFile, 'utf8');
    const { meta, body } = parseFrontmatter(rawContent);
    const repoUrl = resolveRepo(skillName);
    const rawDesc = meta.description || '';
    const descPT = ptbrCache[rawDesc] || rawDesc || 'Habilidade customizada para agentes de IA.';

    // Procurar notas extras / referências da skill
    const allSkillFiles = getAllFiles(skillSourcePath);
    const extraMdFiles = allSkillFiles.filter(f => f.endsWith('.md') && path.basename(f) !== 'SKILL.md');
    const extraNotesList = [];

    for (const extraFile of extraMdFiles) {
      const relPath = path.relative(skillSourcePath, extraFile);
      const noteTitle = path.basename(extraFile, '.md');
      const safeNoteFileName = `${noteTitle.replace(/[<>:"/\\|?*]/g, '_')}.md`;
      const extraContent = fs.readFileSync(extraFile, 'utf8');

      const extraNoteFormatted = `---
tags:
  - ai/skill/doc
  - skill/${safeSkillDirName}
skill: "${skillName}"
source: "${relPath}"
updated_at: "${new Date().toISOString()}"
---

# Documento: ${noteTitle} (Skill: ${skillName})

> [!NOTE] Documentação de suporte da skill **[[Visão Geral|${skillName}]]**.  
> **Caminho de origem:** \`${relPath}\`

---

${extraContent}
`;
      fs.writeFileSync(path.join(skillVaultFolder, safeNoteFileName), extraNoteFormatted, 'utf8');
      extraNotesList.push({ title: noteTitle, file: safeNoteFileName });
    }

    // Gerar nota principal "Visão Geral.md" dentro da pasta da skill
    const overviewContent = `---
tags:
  - ai/skill
  - agent-tooling
name: "${skillName}"
github: "${repoUrl}"
updated_at: "${new Date().toISOString()}"
---

# Skill: ${skillName}

> [!INFO] **Visão Geral**
> **Repositório / Origem:** [${repoUrl}](${repoUrl})  
> **Caminho Local no Sistema:** \`S:\\DEV\\agents\\skills\\${skillName}\`  
> **IAs Conectadas:** Codex, Antigravity, Claude, Maestri.

### Descrição & Finalidade (PT-BR)
${descPT}

${rawDesc && descPT !== rawDesc ? `
> [!NOTE]- 🇺🇸 Descrição Original em Inglês
> ${rawDesc}
` : ''}

${extraNotesList.length > 0 ? `
---

### Documentos & Manuais Inclusos
${extraNotesList.map(n => `* 📄 [[${n.title}]]`).join('\n')}
` : ''}

---

## Instruções Principais & Comandos Técnicos

${body}
`;

    fs.writeFileSync(path.join(skillVaultFolder, 'Visão Geral.md'), overviewContent, 'utf8');

    skillsData.push({
      name: skillName,
      folder: safeSkillDirName,
      title: meta.name || skillName,
      description: descPT,
      repoUrl,
      docsCount: extraNotesList.length + 1
    });
  }

  console.log(`  ✅ ${skillsData.length} pastas de Skills criadas em Skills/`);

  // ==========================================
  // 2. SINCRONIZAR MCP (Pasta MCP/)
  // ==========================================
  let mcpData = {};
  if (fs.existsSync(MCP_CONFIG_PATH)) {
    try {
      mcpData = JSON.parse(fs.readFileSync(MCP_CONFIG_PATH, 'utf8')).mcpServers || {};
    } catch (e) {
      console.warn('⚠️ Erro ao ler mcp_config.json:', e.message);
    }
  }

  const mcpOverview = `---
tags:
  - ai/mcp
  - configuration
updated_at: "${new Date().toISOString()}"
---

# Servidores MCP Globais

Arquivo Mestre no S: \`S:\\DEV\\agents\\mcp_config.json\`  
Espelhado no C: \`C:\\Users\\lukas\\.agents\\mcp_config.json\`

---

## Servidores Configurados
${Object.keys(mcpData).map(name => `* [[${name}|🔌 ${name}]]`).join('\n')}

---

### Configuração Completa (JSON):
\`\`\`json
${JSON.stringify({ mcpServers: mcpData }, null, 2)}
\`\`\`
`;
  fs.writeFileSync(path.join(MCP_OUTPUT_DIR, '_Visão Geral MCP.md'), mcpOverview, 'utf8');

  // Sincronizar automaticamente com o arquivo do Gemini no Windows se existir
  const geminiMcpConfig = path.join(os.homedir(), '.gemini', 'config', 'mcp_config.json');
  if (fs.existsSync(path.dirname(geminiMcpConfig))) {
    const geminiMcpServers = {};
    for (const [k, v] of Object.entries(mcpData)) {
      if (v.command === 'npx') {
        geminiMcpServers[k] = {
          command: 'cmd.exe',
          args: ['/d', '/c', 'npx', ...v.args],
          ...(v.env ? { env: v.env } : {})
        };
      } else if (k === 'ai-memory') {
        geminiMcpServers[k] = {
          command: path.join(os.homedir(), 'AppData', 'Local', 'Programs', 'ai-memory', 'ai-memory.exe'),
          args: ['serve', '--transport', 'stdio', '--data-dir', 'S:\\DEV\\agents\\ai-memory']
        };
      } else {
        geminiMcpServers[k] = v;
      }
    }
    fs.writeFileSync(geminiMcpConfig, JSON.stringify({ mcpServers: geminiMcpServers }, null, 2), 'utf8');
    console.log('  ✅ Configuração MCP sincronizada automaticamente para o Gemini (~/.gemini/config/mcp_config.json)');
  }

  // Gerar nota individual para cada MCP
  const MCP_DESCRIPTIONS = {
    'ai-memory': {
      title: 'AI Memory (Akita on Rails)',
      desc: 'Memória persistente de longo prazo em Rust com isolamento total por projeto/repositório Git. Sintetiza regras, padrões aprendidos e decisões de engenharia automaticamente.',
      repo: 'https://github.com/akitaonrails/ai-memory',
      usage: 'Ativo via Stdio. Mantém o contexto de cada projeto (ex: `Snorlax`, `kota`) estritamente separado através da pasta local de execução e do git root.'
    },
    'rea': {
      title: 'Reverse Engineer Anything (REA)',
      desc: 'Ferramenta de engenharia reversa para descompilar APKs, binários nativos (PE, ELF, Mach-O), web bundles e tráfego de rede.',
      repo: 'https://github.com/morluto/rea',
      usage: 'Peça no chat: "use o REA para inspecionar este binário/apk"'
    },
    'agent-desktop': {
      title: 'Agent Desktop (Computer Use)',
      desc: 'Automação visual e de janelas do sistema operacional Windows (cliques, digitação, captura de tela, leitura de UI).',
      repo: 'https://github.com/vercel-labs/agent-desktop',
      usage: 'Peça no chat: "abra a janela X e clique no botão Y usando o agent-desktop"'
    },
    'magicpath': {
      title: 'MagicPath AI Design Engine',
      desc: 'Integração remota de design system e componentes visuais com geração de código pronta para produção.',
      repo: 'https://magicpath.ai',
      usage: 'Conectado via SSE/HTTP remoto para criação e exportação de componentes de UI.'
    },
    'kan': {
      title: 'Kan Kanban (@kan.bn/mcp)',
      desc: 'Servidor MCP oficial do Kan para manipulação autônoma de workspaces, quadros, listas, cartões e checklists.',
      repo: 'https://github.com/kanbn/kan',
      usage: 'Permite que Minerva e subagentes criem e movam tarefas no Kanban em tempo real enquanto o usuário visualiza no Maestri Canvas.'
    }
  };

  for (const [mcpName, conf] of Object.entries(mcpData)) {
    const info = MCP_DESCRIPTIONS[mcpName] || {
      title: mcpName,
      desc: 'Servidor MCP configurado para extensão de ferramentas.',
      repo: 'Configuração Local',
      usage: 'Invocado automaticamente pelos agentes quando necessário.'
    };

    const isUrl = !!conf.url;
    const mcpNote = `---
tags:
  - ai/mcp
  - mcp-server
name: "${mcpName}"
updated_at: "${new Date().toISOString()}"
---

# Servidor MCP: ${info.title}

> [!INFO] **Visão Geral**
> **Identificador:** \`${mcpName}\`  
> **Origem / Repositório:** [${info.repo}](${info.repo})  
> **Tipo de Conexão:** ${isUrl ? 'HTTP / SSE Remoto' : 'CLI Local (Stdio via binário/npx)'}

### Descrição
${info.desc}

---

### Como Usar
${info.usage}

---

### Configuração
\`\`\`json
${JSON.stringify({ [mcpName]: conf }, null, 2)}
\`\`\`
`;
    fs.writeFileSync(path.join(MCP_OUTPUT_DIR, `${mcpName}.md`), mcpNote, 'utf8');
  }
  console.log('  ✅ Notas criadas na pasta MCP/');

  // ==========================================
  // 3. SINCRONIZAR MODS (Pasta MODS/)
  // ==========================================
  const HERMES_OUTPUT_DIR = path.join(MODS_OUTPUT_DIR, 'Hermes Skins');
  const TOOLKITS_OUTPUT_DIR = path.join(MODS_OUTPUT_DIR, 'Toolkits');
  ensureDir(HERMES_OUTPUT_DIR);
  ensureDir(TOOLKITS_OUTPUT_DIR);

  // 3.1 Hermes Skins
  const skins = [];
  if (fs.existsSync(HERMES_SKINS_DIR)) {
    const skinFiles = fs.readdirSync(HERMES_SKINS_DIR).filter(f => f.endsWith('.yaml'));
    for (const file of skinFiles) {
      const skinName = path.basename(file, '.yaml');
      skins.push({ name: skinName, file });

      const skinNote = `---
tags:
  - ai/skins
  - hermes
name: "${skinName}"
updated_at: "${new Date().toISOString()}"
---

# Skin Hermes: ${skinName}

> [!TIP] **Como Ativar**
> * No terminal: \`hermes skin use ${skinName}\`
> * Dentro do chat: \`/skin ${skinName}\`

**Arquivo YAML:** \`S:\\DEV\\agents\\hermes\\skins\\${file}\`
`;
      fs.writeFileSync(path.join(HERMES_OUTPUT_DIR, `${skinName}.md`), skinNote, 'utf8');
    }
  }

  const skinsOverview = `---
tags:
  - ai/skins
  - hermes
updated_at: "${new Date().toISOString()}"
---

# Hermes Agent - Skins & Visual Mods

Repositório Oficial: [joeynyc/hermes-skins](https://github.com/joeynyc/hermes-skins)  
Caminho Local: \`S:\\DEV\\agents\\hermes\\skins\`

### Como Usar no Terminal:
* **Listar todas as skins:** \`hermes skin list\`
* **Ativar uma skin:** \`hermes skin use <nome>\`

---

### Skins Disponíveis (${skins.length}):
${skins.map(s => `* [[${s.name}|🎭 ${s.name}]]`).join('\n')}
`;
  fs.writeFileSync(path.join(HERMES_OUTPUT_DIR, '_Visão Geral das Skins.md'), skinsOverview, 'utf8');

  // 3.2 Vibe Coding Toolkit
  const vibeSourceDir = path.join(TOOLKITS_DIR, 'vibe-coding-toolkit');
  const vibeVaultDir = path.join(TOOLKITS_OUTPUT_DIR, 'Vibe Coding Toolkit');
  ensureDir(vibeVaultDir);

  if (fs.existsSync(vibeSourceDir)) {
    const promptsDir = path.join(vibeSourceDir, 'docs', 'prompts');
    const promptNotes = [];
    if (fs.existsSync(promptsDir)) {
      const pFiles = fs.readdirSync(promptsDir).filter(f => f.endsWith('.md'));
      for (const pf of pFiles) {
        const pTitle = path.basename(pf, '.md');
        const pContent = fs.readFileSync(path.join(promptsDir, pf), 'utf8');
        fs.writeFileSync(path.join(vibeVaultDir, pf), pContent, 'utf8');
        promptNotes.push(pTitle);
      }
    }

    const vibeOverview = `---
tags:
  - ai/toolkit
  - vibe-coding
updated_at: "${new Date().toISOString()}"
---

# Vibe Coding Toolkit

Repositório Oficial: [soumatheusgomes/vibe-coding-toolkit](https://github.com/soumatheusgomes/vibe-coding-toolkit)  
Caminho Local: \`S:\\DEV\\agents\\toolkits\\vibe-coding-toolkit\`

### Prompts e Playbooks Inclusos:
${promptNotes.map(pn => `* [[${pn}]]`).join('\n')}
`;
    fs.writeFileSync(path.join(vibeVaultDir, '_Visão Geral.md'), vibeOverview, 'utf8');
  }
  console.log('  ✅ Notas criadas na pasta MODS/');

  // ==========================================
  // 4. SINCRONIZAR FRAMEWORKS (Pasta Frameworks/)
  // ==========================================
  const FRAMEWORKS_INFO = {
    'kan': {
      title: 'Kan (Open-Source Kanban & MCP)',
      repo: 'https://github.com/kanbn/kan',
      desc: 'Quadro Kanban moderno e auto-hospedável com suporte nativo ao protocolo MCP (@kan.bn/mcp) para orquestração visual e autônoma de tarefas no Maestri Canvas.',
      usage: 'Suba via Docker (`docker compose up -d` em `S:\\DEV\\frameworks\\kan`) e visualize via nó de Portal no Maestri Canvas (`maestri portal create http://localhost:3000`).'
    },
    'alethe-agents': {
      title: 'Alethe Agents & Orchestration',
      repo: 'https://github.com/Kc1t/alethe-agents',
      desc: 'Orquestração avançada de agentes autônomos em times, com papéis especializados (planejamento, execução, verificação e refatoração).',
      usage: 'Usado como repositório de referência para padrões de orquestração multi-agente e handoffs estruturados.'
    },
    'agent-teams-ai': {
      title: 'Agent Teams AI',
      repo: 'https://github.com/777genius/agent-teams-ai',
      desc: 'Framework de agentes colaborativos que trabalham em equipe com objetivos compartilhados, quadros de tarefas e resolução paralela.',
      usage: 'Abra projetos complexos usando os templates de time em `S:\\DEV\\frameworks\\agent-teams-ai`.'
    },
    'claude-cookbooks': {
      title: 'Anthropic Claude Cookbooks',
      repo: 'https://github.com/anthropics/claude-cookbooks',
      desc: 'Guias e receitas oficiais da Anthropic para engenharia de prompts, structured outputs, loops agênticos, RAG e avaliações de modelos Claude.',
      usage: 'Exemplos em Python e Jupyter notebooks prontos para consulta e adaptação em seus projetos de IA.'
    },
    'ottomator-agents': {
      title: 'Ottomator Agents (Cole Medin)',
      repo: 'https://github.com/coleam00/ottomator-agents',
      desc: 'Arquiteturas de agentes corporativos e ferramentas de automação com LangGraph, CrewAI, AutoGen e Claude.',
      usage: 'Consulte os templates prontos em `S:\\DEV\\frameworks\\ottomator-agents` para acelerar soluções de IA agêntica.'
    },
    'openwork': {
      title: 'OpenWork Workspace & Runtime',
      repo: 'https://github.com/different-ai/openwork',
      desc: 'Ambiente e runtime unificado para execução e cooperação entre humanos e agentes inteligentes em tarefas de desenvolvimento.',
      usage: 'Framework modular para orquestrar agentes e workflows interativos no desktop.'
    },
    'scrapling': {
      title: 'Scrapling (Undetectable Web Scraper)',
      repo: 'https://github.com/D4Vinci/Scrapling',
      desc: 'Motor ultrarrápido e indetectável de raspagem web em Python, com bypass nativo de Cloudflare Turnstile, Akamai e fingerprints TLS via Camoufox.',
      usage: 'Utilize via Python com Fetcher ou StealthFetcher para coleta de dados sem bloqueios.'
    }
  };

  const frameworksList = [];
  if (fs.existsSync(FRAMEWORKS_SRC_DIR)) {
    const fwDirs = fs.readdirSync(FRAMEWORKS_SRC_DIR, { withFileTypes: true })
      .filter(d => d.isDirectory())
      .map(d => d.name);

    for (const fwName of fwDirs) {
      const info = FRAMEWORKS_INFO[fwName] || {
        title: fwName,
        repo: `https://github.com/${fwName}`,
        desc: 'Framework e biblioteca de orquestração de IA.',
        usage: `Disponível em \`S:\\DEV\\frameworks\\${fwName}\``
      };

      const fwNote = `---
tags:
  - ai/framework
  - orchestration
name: "${fwName}"
updated_at: "${new Date().toISOString()}"
---

# Framework: ${info.title}

> [!INFO] **Visão Geral**
> **Repositório Oficial:** [${info.repo}](${info.repo})  
> **Caminho Local no Disco:** \`S:\\DEV\\frameworks\\${fwName}\`

### Descrição
${info.desc}

---

### Como Utilizar em Projetos
${info.usage}

---

### Estrutura de Arquivos
\`\`\`
S:\\DEV\\frameworks\\${fwName}
\`\`\`
`;
      fs.writeFileSync(path.join(FRAMEWORKS_OUTPUT_DIR, `${fwName}.md`), fwNote, 'utf8');
      frameworksList.push({ name: fwName, title: info.title });
    }
  }

  const frameworksOverview = `---
tags:
  - ai/framework
  - dashboard
updated_at: "${new Date().toISOString()}"
---

# Frameworks & Agentes de IA

Caminho Local no S: \`S:\\DEV\\frameworks\`

---

## Bibliotecas e Templates Disponíveis
${frameworksList.map(f => `* [[${f.name}|🧩 ${f.title}]]`).join('\n')}
`;
  fs.writeFileSync(path.join(FRAMEWORKS_OUTPUT_DIR, '_Visão Geral Frameworks.md'), frameworksOverview, 'utf8');
  console.log('  ✅ Notas criadas na pasta Frameworks/');

  // ==========================================
  // 6. DASHBOARD GERAL NA RAIZ (_Hub de Skills & MCPs.md)
  // ==========================================
  const dashboardContent = `---
tags:
  - ai/hub
  - dashboard
updated_at: "${new Date().toISOString()}"
---

# Central de IA (Hub de Skills, MCPs, Mods & Apps)

> [!TIP] **Documentação & Guias do Ecossistema**  
> * 🏗️ **Conceito & Arquitetura:** **[[_Arquitetura e Documentação do Ecossistema|Arquitetura, Conceito & Organização Global]]**  
> * 🧠 **Orquestração de Projetos:** **[[Orquestração de Projetos - Minerva & Conselho|Minerva, Conselho dos 5 & Team CODES]]**  
> * 🚀 **Setup em Outro PC:** **[[_Guia de Replicação em Novo PC|Guia Passo a Passo para Replicar em Novo Computador]]**  
> * 🏛️ **Créditos & Atribuições:** **[[_Créditos e Atribuições|Reconhecimento Open-Source & Autores Originais]]**

Estrutura organizada em pastas para navegação no Obsidian:
* 📁 **[[Workspace/Orquestração de Projetos - Minerva & Conselho|Workspace/]]** — Governança, arquitetura do time e orquestração de projetos
* 📁 **[[Skills/]]** — 368 skills com manuais, comandos e instruções completas
* 📁 **[[MCP/_Visão Geral MCP|MCP/]]** — Servidores MCP ativos (\`ai-memory\`, \`rea\`, \`agent-desktop\`, \`magicpath\`, \`kan\`)
* 📁 **[[MODS/Hermes Skins/_Visão Geral das Skins|MODS/]]** — Skins do Hermes e Toolkits de desenvolvimento
* 📁 **[[Frameworks/_Visão Geral Frameworks|Frameworks/]]** — Frameworks e bibliotecas agênticas (\`kan\`, \`alethe-agents\`, \`claude-cookbooks\`, etc.)
* 📁 **[[Opcionais/_Visão Geral Opcionais|Opcionais/]]** — Ferramentas complementares e telemetria local (\`painel-agents\`, \`ai-statusline\`, \`kan-kanban\`)

---

## Estatísticas Gerais
* **Skills Instaladas:** **${skillsData.length}** pastas organizadas
* **Servidores MCP:** **${Object.keys(mcpData).length}** integrados (\`ai-memory\`, \`rea\`, \`agent-desktop\`, \`magicpath\`, \`kan\`)
* **Hermes Skins:** **${skins.length}** temas customizados
* **Frameworks de Agentes:** **${frameworksList.length}** repositórios prontos em \`S:\\DEV\\frameworks\`
* **IAs Integradas:** Antigravity (Google), Codex (OpenAI), Claude Code (Anthropic), Hermes Agent, Maestri

---

## Navegação Rápida

### Servidores MCP
${Object.keys(mcpData).map(m => `* [[MCP/${m}|🔌 ${m}]]`).join('\n')}

### Mods & Visual
* [[MODS/Hermes Skins/_Visão Geral das Skins|🎭 Hermes Skins (16 Temas)]]
* [[MODS/Toolkits/Vibe Coding Toolkit/_Visão Geral|🚀 Vibe Coding Toolkit]]

### Frameworks & Agentes
${frameworksList.map(f => `* [[Frameworks/${f.name}|🧩 ${f.title}]]`).join('\n')}

---

## 🧠 Catálogo de Skills em Destaque

| Skill | Pasta | Origem | Acesso |
| :--- | :--- | :--- | :--- |
${skillsData.slice(0, 50).map(s => `| **${s.name}** | \`Skills/${s.folder}/\` | [Repo](${s.repoUrl}) | [[Skills/${s.folder}/Visão Geral|Abrir Nota]] |`).join('\n')}

*(Todas as outras centenas de skills estão organizadas na pasta **Skills** na barra lateral!)*
`;

  fs.writeFileSync(path.join(VAULT_DIR, '_Hub de Skills & MCPs.md'), dashboardContent, 'utf8');
  console.log('  ✅ Dashboard geral atualizado na raiz do cofre: _Hub de Skills & MCPs.md');
  console.log('🎉 Sincronização hierárquica completa concluída com sucesso!');
}

sync();
