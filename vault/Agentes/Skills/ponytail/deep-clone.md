---
tags:
  - ai/skill/doc
  - skill/ponytail
skill: "ponytail"
source: "examples\deep-clone.md"
updated_at: "2026-11-08T08:03:33.597Z"
---

# Documento: deep-clone (Skill: ponytail)

> [!NOTE] Documentação de suporte da skill **[[Visão Geral|ponytail]]**.  
> **Caminho de origem:** `examples\deep-clone.md`

---

# Deep Clone

**Task:** "Deep clone this object."

## Without Ponytail

```bash
npm install lodash
```

```js
import { cloneDeep } from "lodash";

const copy = cloneDeep(original);
```

Or the classic hack:

```js
// fragile: loses Date, undefined, Map, Set, circular refs, functions
const copy = JSON.parse(JSON.stringify(original));
```

## With Ponytail

```js
// ponytail: structuredClone does this
const copy = structuredClone(original);
```

**1 dependency (or a fragile hack) → 1 built-in.** `structuredClone` handles `Date`, `Map`, `Set`, `ArrayBuffer`, `RegExp`, circular references, and more, everything `JSON.parse/stringify` silently drops. Available in every browser since 2022 and Node.js since v17. Pull lodash in when you need the rest of it, not for one function.

