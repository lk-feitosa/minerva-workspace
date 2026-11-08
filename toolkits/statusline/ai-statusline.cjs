const fs = require('fs');
const path = require('path');
const os = require('os');
const cp = require('child_process');

// Cores ANSI
const RESET = '\x1b[0m';
const BOLD = '\x1b[1m';
const DIM = '\x1b[2m';
const CYAN = '\x1b[38;2;137;220;235m';
const GREEN = '\x1b[38;2;166;227;161m';
const YELLOW = '\x1b[38;2;249;226;175m';
const RED = '\x1b[38;2;243;139;168m';
const PEACH = '\x1b[38;2;250;179;135m';
const GRAY = '\x1b[38;2;108;112;134m';

const HOME_DIR = os.homedir();
const SETTINGS_FILE = path.join(HOME_DIR, '.gemini', 'antigravity-cli', 'settings.json');
const CACHE_FILE = path.join(HOME_DIR, '.gemini', 'antigravity-cli', 'live_quota.json');
const FETCHER_SCRIPT = path.join(HOME_DIR, '.local', 'bin', 'ai-quota-fetcher.cjs');

// Gerar barra de 10 blocos representando a cota RESTANTE (sobra%)
function makeBar(percentRemaining, width = 10) {
  const p = Math.max(0, Math.min(100, Math.round(percentRemaining)));
  const filled = Math.max(0, Math.min(width, Math.round((p / 100) * width)));
  const empty = width - filled;

  // Cor baseada na sobra de cota:
  // > 50%: Verde
  // 20% - 50%: Amarelo
  // < 20%: Vermelho
  let color = GREEN;
  if (p <= 50) color = YELLOW;
  if (p <= 20) color = RED;

  const bar = `${color}${'▰'.repeat(filled)}${GRAY}${'▱'.repeat(empty)}${RESET}`;
  const pctText = `${color}${p}%${RESET}`;
  return { bar, pctText, color };
}

// Formatar tempo restante de restauração
function formatResetTime(resetsAt) {
  if (!resetsAt) return '--';
  const diffMs = new Date(resetsAt).getTime() - Date.now();
  if (diffMs <= 0) return 'agora';

  const totalMins = Math.floor(diffMs / 60000);
  const hours = Math.floor(totalMins / 60);
  const days = Math.floor(hours / 24);

  if (days > 0) {
    const remHours = hours % 24;
    return remHours > 0 ? `${days}d ${remHours}h` : `${days}d`;
  }
  if (hours > 0) {
    const remMins = totalMins % 60;
    return remMins > 0 ? `${hours}h ${remMins}m` : `${hours}h`;
  }
  return `${totalMins}m`;
}

// Disparar atualização em segundo plano sem travar o terminal
function triggerBackgroundRefresh() {
  try {
    const child = cp.spawn(process.execPath, [FETCHER_SCRIPT], {
      detached: true,
      stdio: 'ignore',
      windowsHide: true
    });
    child.unref();
  } catch (e) {}
}

// Ler cotas do cache com fallback gracioso
function getQuotaData() {
  let cache = null;
  let cacheAge = 999999;

  if (fs.existsSync(CACHE_FILE)) {
    try {
      const stats = fs.statSync(CACHE_FILE);
      cacheAge = (Date.now() - stats.mtimeMs) / 1000;
      cache = JSON.parse(fs.readFileSync(CACHE_FILE, 'utf8'));
    } catch (e) {}
  }

  // Se o cache tiver mais de 90 segundos, atualiza em background
  if (cacheAge > 90) {
    triggerBackgroundRefresh();
  }

  return cache;
}

// Identificar modelo ativo na sessão atual
function getActiveModel(stdinData) {
  const direct =
    stdinData?.model?.display_name ||
    stdinData?.model?.id ||
    (typeof stdinData?.model === 'string' ? stdinData.model : null) ||
    stdinData?.model_info?.display_name ||
    stdinData?.model_info?.id ||
    stdinData?.display_name;

  if (direct) return direct;

  if (fs.existsSync(SETTINGS_FILE)) {
    try {
      const settings = JSON.parse(fs.readFileSync(SETTINGS_FILE, 'utf8'));
      if (settings.model) return settings.model;
    } catch (e) {}
  }

  return 'Gemini 3.8 Flash (Low)';
}

// Formatar nome do modelo com nível de raciocínio (Low / Med / High)
function formatModelName(rawModel, stdinData) {
  let tier = '';
  const effort = (stdinData?.effort || stdinData?.model_info?.effort || '').toLowerCase();

  if (effort === 'high' || /\bhigh\b/i.test(rawModel) || /\bthinking\b/i.test(rawModel)) {
    tier = ` ${PEACH}(High)${RESET}`;
  } else if (effort === 'medium' || effort === 'med' || /\bmedium\b|\bmed\b/i.test(rawModel)) {
    tier = ` ${DIM}(Med)${RESET}`;
  } else if (effort === 'low' || /\blow\b/i.test(rawModel)) {
    tier = ` ${DIM}(Low)${RESET}`;
  } else {
    // Se não especificado no modelo, verifica se no settings tem
    if (fs.existsSync(SETTINGS_FILE)) {
      try {
        const s = JSON.parse(fs.readFileSync(SETTINGS_FILE, 'utf8'));
        if (/\bmed/i.test(s.model)) tier = ` ${DIM}(Med)${RESET}`;
        else if (/\bhigh/i.test(s.model)) tier = ` ${PEACH}(High)${RESET}`;
        else tier = ` ${DIM}(Low)${RESET}`;
      } catch (e) {
        tier = ` ${DIM}(Low)${RESET}`;
      }
    } else {
      tier = ` ${DIM}(Low)${RESET}`;
    }
  }

  // Nome base simplificado e limpo
  let base = 'Gemini';
  if (/argon/i.test(rawModel)) base = 'Gemini Argon';
  else if (/3\.8.*flash/i.test(rawModel)) base = 'Gemini 3.8 Flash';
  else if (/3\.8.*pro/i.test(rawModel)) base = 'Gemini 3.8 Pro';
  else if (/3\.7.*sonnet/i.test(rawModel)) base = 'Claude 3.7 Sonnet';
  else if (/3\.5.*sonnet/i.test(rawModel)) base = 'Claude 3.5 Sonnet';
  else if (/sonnet/i.test(rawModel)) base = 'Claude Sonnet';
  else if (/opus/i.test(rawModel)) base = 'Claude Opus';
  else if (/haiku/i.test(rawModel)) base = 'Claude Haiku';
  else if (/claude/i.test(rawModel)) base = 'Claude';
  else if (/gpt/i.test(rawModel)) base = 'GPT';
  else if (/flash/i.test(rawModel)) base = 'Gemini Flash';
  else if (/pro/i.test(rawModel)) base = 'Gemini Pro';
  else base = rawModel.replace(/\s*\(.*?\)/g, '').trim();

  return `${BOLD}${CYAN}${base}${RESET}${tier}`;
}

// Obter dados da cota apropriada para o modelo em uso
function getModelQuota(quotas, rawModel) {
  const agy = quotas?.agy;
  if (!agy || !agy.meters) return null;

  const isArgon = /argon/i.test(rawModel);
  const isClaudeOrGpt = /claude|gpt|3p/i.test(rawModel);

  let activeMeter = null;
  if (isArgon) {
    activeMeter = agy.meters.find(m => /argon/i.test(m.id || m.label));
  } else if (isClaudeOrGpt) {
    activeMeter = agy.meters.find(m => /claude|gpt|3p/i.test(m.id || m.label));
  } else {
    activeMeter = agy.meters.find(m => /gemini models/i.test(m.id || m.label)) || agy.meters[0];
  }

  if (!activeMeter || !activeMeter.windows || activeMeter.windows.length === 0) {
    return null;
  }

  const wWeekly = activeMeter.windows.find(w => w.window === 'weekly' || w.durationSeconds > 86400) || activeMeter.windows[0];
  const w5h = activeMeter.windows.find(w => w.window === '5h' || w.durationSeconds <= 86400);

  // Seleciona a janela mais relevante (janela curta de 5h se existir, senão semanal)
  const chosenWindow = w5h || wWeekly;
  const remainingFraction = chosenWindow.remainingFraction !== undefined
    ? chosenWindow.remainingFraction
    : (1 - (chosenWindow.usedPercent || 0) / 100);

  return {
    remainingPercent: Math.max(0, Math.min(100, Math.round(remainingFraction * 100))),
    resetsAt: chosenWindow.resetsAt
  };
}

// Obter pasta atual e estado do agente
function getLocationAndState(stdinData) {
  const rawDir =
    stdinData?.workspace?.current_dir ||
    stdinData?.cwd ||
    stdinData?.workspace?.project_dir ||
    stdinData?.current_dir ||
    process.cwd();

  let dirName = '~';
  if (rawDir) {
    const norm = path.normalize(rawDir);
    const normHome = path.normalize(HOME_DIR);
    if (norm.toLowerCase() === normHome.toLowerCase()) {
      dirName = '~';
    } else {
      dirName = path.basename(norm) || norm;
    }
  }

  const rawState = (stdinData?.agent_state || stdinData?.status || stdinData?.state || '').toLowerCase();
  let state = 'ocioso';
  if (rawState.includes('think')) state = 'pensando';
  else if (rawState.includes('run') || rawState.includes('exec')) state = 'executando';
  else if (rawState.includes('wait')) state = 'aguardando';
  else if (rawState.includes('err')) state = 'erro';
  else if (rawState && rawState !== 'idle') state = rawState;

  return { dirName, state };
}

// Processar entrada do stdin de forma não bloqueante
let inputBuffer = '';
process.stdin.setEncoding('utf8');

process.stdin.on('data', chunk => {
  inputBuffer += chunk;
});

process.stdin.on('end', () => {
  render();
});

// Timeout de segurança curto para garantir resposta instantânea
const safetyTimer = setTimeout(() => {
  render();
}, 45);

let rendered = false;
function render() {
  if (rendered) return;
  rendered = true;
  clearTimeout(safetyTimer);

  let stdinData = null;
  if (inputBuffer) {
    try {
      stdinData = JSON.parse(inputBuffer);
    } catch (e) {}
  }

  const quotas = getQuotaData();
  const rawModel = getActiveModel(stdinData);
  const formattedModel = formatModelName(rawModel, stdinData);
  const quotaInfo = getModelQuota(quotas, rawModel);
  const { dirName, state } = getLocationAndState(stdinData);

  // Barra de 10 pedaços + sobra%
  const remPercent = quotaInfo ? quotaInfo.remainingPercent : 100;
  const { bar, pctText } = makeBar(remPercent, 10);

  // Tempo de restaura
  const resetTime = quotaInfo ? formatResetTime(quotaInfo.resetsAt) : '--';

  // Montagem da barra minimalista:
  // [modelo (Low)] [barra] [sobra%] | [tempo] | 📁 [pasta] ([estado])
  const sep = ` ${GRAY}|${RESET} `;
  const output = `${formattedModel} ${bar} ${pctText}${sep}${GRAY}${resetTime}${RESET}${sep}📁 ${CYAN}${dirName}${RESET} ${DIM}(${state})${RESET}\n`;

  process.stdout.write(output);
  process.exit(0);
}
