#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
agent_sort.py - Sistema de Classificacao DAILY vs. LIBRARY de Skills para Minerva & Maestri
Inspirado na arquitetura ECC agent-sort, adaptado para o ecossistema Minerva com busca hibrida instantanea.

Modos de uso:
  1. Classificacao do Projeto (gera .agents/skills.json):
     python toolkits/agent_sort.py [caminho_do_projeto]
     
  2. Busca Instantanea de Skills na LIBRARY (zero tokens consumidos):
     python toolkits/agent_sort.py --search "scraping"
     python toolkits/agent_sort.py --match "preciso criar testes e2e com playwright no front" --json
"""

import os
import sys
import json
import re
import argparse
from pathlib import Path
from collections import Counter

# Skills fundamentais de governanca que SEMPRE pertencem ao DAILY
CORE_GOVERNANCE_SKILLS = [
    "using-agent-skills",
    "planning-and-task-breakdown",
    "spec-driven-development",
    "verification-loop",
    "code-review-and-quality"
]

# Regras de deteccao de stack -> Skills recomendadas para DAILY
STACK_SKILL_RULES = {
    "frontend": {
        "keywords": ["react", "next", "vue", "svelte", "tailwind", "vite", "webpack", "html", "css"],
        "files": ["package.json", "tsconfig.json", "vite.config.ts", "next.config.js", "next.config.mjs", "tailwind.config.js"],
        "recommended_skills": ["frontend-ui-engineering", "frontend-patterns"]
    },
    "backend": {
        "keywords": ["express", "fastify", "nest", "prisma", "fastapi", "django", "flask", "sqlalchemy", "postgres", "sql", "api", "rest"],
        "files": ["package.json", "requirements.txt", "pyproject.toml", "Cargo.toml", "go.mod"],
        "recommended_skills": ["backend-patterns", "api-design", "security-review"]
    },
    "testing": {
        "keywords": ["playwright", "cypress", "jest", "vitest", "pytest", "supertest"],
        "files": ["playwright.config.ts", "playwright.config.js", "pytest.ini", "jest.config.js"],
        "recommended_skills": ["webapp-testing", "tdd-workflow", "e2e-testing"]
    },
    "python_data": {
        "keywords": ["pandas", "numpy", "torch", "scikit-learn", "tensorflow", "pydantic"],
        "files": ["pyproject.toml", "requirements.txt", "Pipfile"],
        "recommended_skills": ["mle-workflow"]
    },
    "reverse_engineering": {
        "keywords": ["decompil", "disassembl", "binary", "frida", "radare", "rizin", "ghidra", "apk"],
        "files": [],
        "recommended_skills": ["reverse-engineer-anything"]
    }
}

def find_skills_directories(base_dir: Path):
    """Localiza os diretorios de skills disponiveis (global e local)."""
    candidates = []
    # 1. Global ~/.agents/skills
    home_agents = Path.home() / ".agents" / "skills"
    if home_agents.is_dir():
        candidates.append(home_agents)
        
    # 2. Local skills directory no workspace
    local_skills = base_dir / "skills"
    if local_skills.is_dir() and local_skills not in candidates:
        candidates.append(local_skills)
        
    # 3. Parent skills directory
    parent_skills = base_dir.parent / "skills"
    if parent_skills.is_dir() and parent_skills not in candidates:
        candidates.append(parent_skills)
        
    return candidates

def parse_skill_metadata(skill_dir: Path):
    """Extrai metadados do arquivo SKILL.md de uma skill."""
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.exists():
        return None
        
    name = skill_dir.name
    description = ""
    tags = []
    
    try:
        content = skill_file.read_text(encoding="utf-8", errors="ignore")
        if content.startswith("---"):
            parts = content.split("---", 2)
            if len(parts) >= 3:
                frontmatter = parts[1]
                for line in frontmatter.splitlines():
                    if line.startswith("name:"):
                        name = line.split(":", 1)[1].strip().strip('"\'')
                    elif line.startswith("description:"):
                        description = line.split(":", 1)[1].strip().strip('"\'')
                # Resto do documento pode fornecer palavras-chave
                body = parts[2]
            else:
                body = content
        else:
            body = content
            
        if not description:
            # Pega primeiras linhas como descricao
            lines = [l.strip() for l in body.splitlines() if l.strip() and not l.startswith("#")]
            description = lines[0] if lines else ""
            
        return {
            "name": name,
            "dir_name": skill_dir.name,
            "path": str(skill_file.resolve()),
            "description": description,
            "tokens": set(re.findall(r"\w{3,}", (name + " " + description).lower()))
        }
    except Exception as e:
        return None

def scan_all_skills(skills_dirs):
    """Escaneia todos os repositorios de skills disponiveis."""
    skills = {}
    for sdir in skills_dirs:
        for entry in sdir.iterdir():
            if entry.is_dir():
                meta = parse_skill_metadata(entry)
                if meta and meta["name"] not in skills:
                    skills[meta["name"]] = meta
    return skills

def detect_project_evidence(project_dir: Path):
    """Analisa arquivos do projeto para identificar stack e tecnologias em uso."""
    evidence = {
        "manifests": [],
        "detected_keywords": set(),
        "categories": set()
    }
    
    for root, dirs, files in os.walk(project_dir):
        # Ignora pastas irrelevantes
        dirs[:] = [d for d in dirs if d not in {".git", "node_modules", ".venv", "venv", "__pycache__", "dist", "build", ".next", ".obsidian", "skills"}]
        
        for file in files:
            file_lower = file.lower()
            rel_path = os.path.relpath(os.path.join(root, file), project_dir)
            
            # Verifica manifests
            for cat, rules in STACK_SKILL_RULES.items():
                if file_lower in rules["files"]:
                    evidence["manifests"].append(rel_path)
                    evidence["categories"].add(cat)
                    
                    # Le conteudo do manifest para refinar keywords
                    file_path = Path(root) / file
                    try:
                        text = file_path.read_text(encoding="utf-8", errors="ignore").lower()
                        for kw in rules["keywords"]:
                            if kw in text:
                                evidence["detected_keywords"].add(kw)
                                evidence["categories"].add(cat)
                    except Exception:
                        pass
                        
    return evidence

def sort_skills_for_project(project_dir: Path, all_skills: dict):
    """Classifica skills em DAILY vs LIBRARY com base em evidencias reais do repositorio."""
    evidence = detect_project_evidence(project_dir)
    daily_skills = {}
    library_skills = {}
    
    # 1. Adiciona Core Governance ao DAILY
    for core in CORE_GOVERNANCE_SKILLS:
        if core in all_skills:
            daily_skills[core] = {
                "description": all_skills[core]["description"],
                "reason": "Core Governance (sempre ativo para orquestracao e qualidade)"
            }
            
    # 2. Adiciona Skills especificas do Stack detectado
    for cat in evidence["categories"]:
        rules = STACK_SKILL_RULES.get(cat, {})
        for sk in rules.get("recommended_skills", []):
            if sk in all_skills and sk not in daily_skills:
                matching_kws = [kw for kw in rules["keywords"] if kw in evidence["detected_keywords"]]
                reason = f"Stack {cat} detectado (evidencias: {', '.join(matching_kws) if matching_kws else 'arquivos de configuracao'})"
                daily_skills[sk] = {
                    "description": all_skills[sk]["description"],
                    "reason": reason
                }
                
    # 3. Todas as demais vao para a LIBRARY
    for name, data in all_skills.items():
        if name not in daily_skills:
            library_skills[name] = {
                "description": data["description"],
                "path": data["path"]
            }
            
    return {
        "project_path": str(project_dir.resolve()),
        "evidence": {
            "manifests": evidence["manifests"],
            "detected_keywords": sorted(list(evidence["detected_keywords"])),
            "categories": sorted(list(evidence["categories"]))
        },
        "daily_count": len(daily_skills),
        "library_count": len(library_skills),
        "daily_skills": daily_skills,
        "library_skills": library_skills
    }

def search_skills(query: str, all_skills: dict, top_k: int = 5):
    """Busca ultra-rapida por termo ou descricao de demanda na LIBRARY (zero tokens LLM)."""
    query_tokens = set(re.findall(r"\w{3,}", query.lower()))
    if not query_tokens:
        return []
        
    scores = []
    for name, data in all_skills.items():
        skill_tokens = data["tokens"]
        name_lower = name.lower()
        desc_lower = data["description"].lower()
        
        # Pontuacao base
        score = 0
        # Correspondencia exata no nome
        for qt in query_tokens:
            if qt in name_lower:
                score += 5.0
            if qt in desc_lower:
                score += 2.0
            if qt in skill_tokens:
                score += 1.0
                
        if score > 0:
            scores.append((score, data))
            
    scores.sort(key=lambda x: x[0], reverse=True)
    return scores[:top_k]

def main():
    parser = argparse.ArgumentParser(description="Classificador DAILY vs LIBRARY de Skills & Busca Hibrida para Minerva")
    parser.add_argument("target_dir", nargs="?", default=".", help="Diretorio do projeto para analisar (padrao: atual)")
    parser.add_argument("--search", "-s", type=str, help="Busca por palavra-chave na biblioteca de skills")
    parser.add_argument("--match", "-m", type=str, help="Busca semantica/intencao de demanda para sugerir skill especifica")
    parser.add_argument("--json", action="store_true", help="Retorna o resultado estritamente em formato JSON")
    parser.add_argument("--output", "-o", type=str, help="Caminho do arquivo json de saida (padrao: .agents/skills.json)")
    
    args = parser.parse_args()
    target_path = Path(args.target_dir).resolve()
    
    # Descobre skills
    skills_dirs = find_skills_directories(target_path)
    all_skills = scan_all_skills(skills_dirs)
    
    # Caso 1: Modo Busca / Match
    query = args.match or args.search
    if query:
        results = search_skills(query, all_skills, top_k=5)
        formatted = []
        for score, sk in results:
            formatted.append({
                "name": sk["name"],
                "score": round(score, 1),
                "description": sk["description"],
                "path": sk["path"]
            })
            
        if args.json:
            print(json.dumps(formatted, indent=2, ensure_ascii=False))
        else:
            print(f"\n🔍 Resultados da Busca por '{query}' ({len(formatted)} encontradas):")
            print("=" * 70)
            for item in formatted:
                print(f"⭐ {item['name']} (Score: {item['score']})")
                print(f"   Descricao: {item['description']}")
                print(f"   Arquivo:   {item['path']}")
                print("-" * 70)
        return

    # Caso 2: Modo Analise e Classificacao do Projeto
    plan = sort_skills_for_project(target_path, all_skills)
    
    if args.json:
        print(json.dumps(plan, indent=2, ensure_ascii=False))
    else:
        print("\n========================================================")
        print("🏛️ MINERVA AGENT-SORT: Classificacao DAILY vs LIBRARY")
        print("========================================================")
        print(f"📂 Projeto: {plan['project_path']}")
        print(f"🔎 Categorias Detectadas: {', '.join(plan['evidence']['categories']) if plan['evidence']['categories'] else 'Generico'}")
        print(f"📦 Manifests: {', '.join(plan['evidence']['manifests']) if plan['evidence']['manifests'] else 'Nenhum manifest explicito'}")
        print(f"🟢 DAILY ({plan['daily_count']} skills ativas carregadas):")
        for sk, info in plan["daily_skills"].items():
            print(f"   - {sk}: {info['reason']}")
            
        print(f"\n📚 LIBRARY ({plan['library_count']} skills indexadas no Obsidian para busca on-demand)")
        print("========================================================\n")
        
    # Salva no .agents/skills.json caso requisitado ou por padrao se existir .agents
    agents_dir = target_path / ".agents"
    out_file = Path(args.output) if args.output else (agents_dir / "skills.json" if agents_dir.exists() else None)
    if out_file:
        out_file.parent.mkdir(parents=True, exist_ok=True)
        out_file.write_text(json.dumps(plan, indent=2, ensure_ascii=False), encoding="utf-8")
        if not args.json:
            print(f"💾 Plano salvo com sucesso em: {out_file}")

if __name__ == "__main__":
    main()
