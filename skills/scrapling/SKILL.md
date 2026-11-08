---
name: scrapling
description: "Ultra-fast, undetectable web scraping engine in Python that bypasses bot protections, Cloudflare Turnstile, and TLS fingerprinting using StealthFetcher and Camoufox."
---

# Scrapling: Undetectable Web Scraping Engine

O **Scrapling** é um framework moderno e ultrarrápido em Python projetado para raspagem de dados web indetectável, com suporte nativo a contorno de sistemas anti-bot (Cloudflare, Akamai, Datadome, Kasada) e automação de navegadores com Camoufox.

---

## 🚀 Quando usar esta Skill:
- Quando agentes de pesquisa (`deep-research`, `research`, web crawler) precisarem raspar páginas da web que bloqueiam requisições `curl`, `fetch` ou bibliotecas comuns (`requests`/`httpx`).
- Para extrair dados estruturados em alta velocidade com seletores CSS e XPath.
- Para automação de páginas dinâmicas em modo invisível (headless stealth).

---

## 🛠️ Instalação no Ambiente

O Scrapling está clonado em `S:\DEV\frameworks\scrapling`. Para utilizá-lo via `uv` ou `pip`:

```bash
# Instalação com suporte básico a fetch HTTP
uv pip install scrapling

# Instalação completa com suporte a navegadores invisíveis (Camoufox)
uv pip install "scrapling[camoufox]"
python -m camoufox fetch
```

---

## 💻 Exemplos de Uso

### 1. Requisição Rápida com Burlar Fingerprint (Fetcher)
```python
from scrapling import Fetcher

fetcher = Fetcher()
response = fetcher.get("https://example.com")

# Seleção de elementos tipo CSS ou XPath
title = response.css("h1::text").first()
links = response.css("a::attr(href)").all()
print(f"Título: {title}")
```

### 2. Modo Stealth com Camoufox (Burlar Proteções Complexas)
```python
from scrapling import StealthFetcher

# Inicializa o navegador indetectável
stealth = StealthFetcher()
page = stealth.get("https://site-com-protecao-cloudflare.com")

articles = page.css(".article-title::text").all()
for a in articles:
    print(a)
```

---

## 🛡️ Boas Práticas para Agentes
1. Sempre priorize o `Fetcher` leve para sites sem proteção pesada (milissegundos de resposta).
2. Utilize `StealthFetcher` apenas quando o site exigir execução de JavaScript complexo ou proteções antibot ativas.
3. Não sobrecarregue servidores com requisições simultâneas sem intervalo respeitoso.
