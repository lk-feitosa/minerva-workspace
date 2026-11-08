const fs = require('fs');
const path = require('path');
const os = require('os');
const cp = require('child_process');

const CACHE_FILE = path.join(os.homedir(), '.gemini', 'antigravity-cli', 'live_quota.json');
const LOCK_FILE = path.join(os.homedir(), '.gemini', 'antigravity-cli', 'fetcher.lock');

// Evitar execuções concorrentes
if (fs.existsSync(LOCK_FILE)) {
  try {
    const lockStats = fs.statSync(LOCK_FILE);
    if ((Date.now() - lockStats.mtimeMs) < 45000) {
      process.exit(0);
    }
  } catch (e) {}
}

try {
  fs.writeFileSync(LOCK_FILE, Date.now().toString(), 'utf8');
} catch (e) {}

try {
  const agyPath = path.join(os.homedir(), 'AppData', 'Local', 'agy', 'bin', 'agy.exe');
  const agyCmd = fs.existsSync(agyPath) ? `"${agyPath}"` : 'agy';

  const output = cp.execSync(`${agyCmd} -p /usage --output-format json`, {
    timeout: 15000,
    encoding: 'utf8',
    windowsHide: true,
    stdio: ['ignore', 'pipe', 'ignore']
  });

  const raw = JSON.parse(output);
  const groups = raw.command?.data?.groups || [];

  const meters = groups.map(g => {
    return {
      id: g.name,
      label: g.name,
      windows: (g.buckets || []).map(b => {
        const remaining = b.remaining_fraction !== undefined ? b.remaining_fraction : 1;
        const usedPercent = Math.max(0, Math.min(100, (1 - remaining) * 100));
        let durationSeconds = 604800;
        if (b.window === '5h') durationSeconds = 18000;
        return {
          id: b.id,
          name: b.name,
          window: b.window,
          remainingFraction: remaining,
          remainingPercent: Math.round(remaining * 100),
          usedPercent,
          resetsAt: b.reset_time,
          durationSeconds
        };
      })
    };
  });

  const result = {
    agy: {
      meters,
      updatedAt: new Date().toISOString()
    }
  };

  const tmpFile = CACHE_FILE + '.tmp';
  fs.writeFileSync(tmpFile, JSON.stringify(result, null, 2), 'utf8');
  fs.copyFileSync(tmpFile, CACHE_FILE);
  try { fs.unlinkSync(tmpFile); } catch (e) {}
} catch (e) {
  // Silent fail
} finally {
  try {
    if (fs.existsSync(LOCK_FILE)) fs.unlinkSync(LOCK_FILE);
  } catch (e) {}
}
