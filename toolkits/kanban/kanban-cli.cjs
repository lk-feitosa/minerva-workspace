#!/usr/bin/env node
const { execSync, spawn } = require('child_process');
const path = require('path');
const fs = require('fs');
const http = require('http');

const KAN_COMPOSE_PATH = 'S:\\DEV\\frameworks\\kan\\docker-compose.yml';
const KAN_BASE_URL = process.env.KAN_BASE_URL || 'http://localhost:3000';

function getProjectContext() {
  try {
    const gitRoot = execSync('git rev-parse --show-toplevel 2>nul', { encoding: 'utf8' }).trim();
    if (gitRoot) {
      return {
        name: path.basename(gitRoot),
        root: gitRoot,
        isGit: true
      };
    }
  } catch (e) {
    // Not a git repo
  }

  const currentDir = process.cwd();
  return {
    name: path.basename(currentDir),
    root: currentDir,
    isGit: false
  };
}

function checkKanHealth(timeoutMs = 1500) {
  return new Promise((resolve) => {
    try {
      const url = new URL(KAN_BASE_URL);
      const req = http.request(
        {
          hostname: url.hostname,
          port: url.port || 80,
          path: '/',
          method: 'GET',
          timeout: timeoutMs
        },
        (res) => {
          resolve(true);
        }
      );
      req.on('error', () => resolve(false));
      req.on('timeout', () => {
        req.destroy();
        resolve(false);
      });
      req.end();
    } catch (e) {
      resolve(false);
    }
  });
}

function openUrl(url) {
  try {
    if (process.platform === 'win32') {
      execSync(`start "" "${url}"`, { shell: 'cmd.exe', stdio: 'ignore' });
    } else if (process.platform === 'darwin') {
      execSync(`open "${url}"`, { stdio: 'ignore' });
    } else {
      execSync(`xdg-open "${url}"`, { stdio: 'ignore' });
    }
  } catch (err) {
    console.error(`  [!] Não foi possível abrir o navegador: ${err.message}`);
  }
}

function openMaestriPortal(url) {
  try {
    execSync(`maestri portal create "${url}"`, { stdio: 'inherit' });
    return true;
  } catch (err) {
    return false;
  }
}

async function main() {
  const args = process.argv.slice(2);
  const command = args[0] || 'open';
  const project = getProjectContext();

  console.log(`\n📌 [Kanban CLI] Contexto do Projeto: "${project.name}" (${project.root})`);

  if (command === 'status') {
    const isRunning = await checkKanHealth();
    console.log(`  Estado do Kan (${KAN_BASE_URL}): ${isRunning ? '🟢 ONLINE' : '🔴 OFFLINE'}`);
    return;
  }

  if (command === 'start') {
    console.log('  🚀 Subindo contêineres do Kan via Docker Compose...');
    try {
      execSync(`docker compose -f "${KAN_COMPOSE_PATH}" up -d`, { stdio: 'inherit' });
      console.log('  ✅ Contêineres iniciados com sucesso!');
    } catch (err) {
      console.error('  ❌ Falha ao iniciar Docker Compose. Verifique se o Docker Desktop está em execução.');
    }
    return;
  }

  if (command === 'stop') {
    console.log('  ⏹️ Pausando contêineres do Kan...');
    try {
      execSync(`docker compose -f "${KAN_COMPOSE_PATH}" stop`, { stdio: 'inherit' });
      console.log('  ✅ Contêineres parados com sucesso.');
    } catch (err) {
      console.error('  ❌ Falha ao parar contêineres:', err.message);
    }
    return;
  }

  // Abertura padrão (open / portal)
  const asPortal = command === 'portal' || args.includes('--portal') || args.includes('-p');
  let isRunning = await checkKanHealth();

  if (!isRunning) {
    console.log('  ⏳ Kan não está respondendo em http://localhost:3000.');
    console.log('  Iniciando contêineres automaticamente via Docker Compose...');
    try {
      execSync(`docker compose -f "${KAN_COMPOSE_PATH}" up -d`, { stdio: 'inherit' });
      console.log('  Aguardando servidor inicializar...');
      for (let i = 0; i < 10; i++) {
        await new Promise((r) => setTimeout(r, 2000));
        isRunning = await checkKanHealth();
        if (isRunning) break;
      }
    } catch (err) {
      console.log('  ⚠️ Não foi possível iniciar automaticamente o Docker. Certifique-se de que o Docker Desktop está ativo.');
    }
  }

  const targetUrl = KAN_BASE_URL;

  if (asPortal) {
    console.log(`  🎨 Criando nó de Portal no Maestri Canvas (${targetUrl})...`);
    const success = openMaestriPortal(targetUrl);
    if (!success) {
      console.log('  [!] Maestri CLI não detectado ou sessão inativa. Abrindo no navegador padrão...');
      openUrl(targetUrl);
    }
  } else {
    console.log(`  🌐 Abrindo quadro Kanban do projeto "${project.name}" em: ${targetUrl}`);
    openUrl(targetUrl);
  }

  console.log(`\n💡 Dica com Minerva:\n  Peça no terminal: "Minerva, atualize as tarefas do projeto ${project.name} no Kanban"\n`);
}

main().catch((err) => {
  console.error('Erro no kanban CLI:', err);
});
