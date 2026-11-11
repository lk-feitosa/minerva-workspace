---
tags:
  - ai/skill
  - agent-tooling
  - category/design
  - category/frontend
name: "react-view-transitions"
---

# Skill: react-view-transitions - Transicoes de Visualizacao Fluida (Vercel)

> [!INFO] **Visão Geral**
> **Hub de Categoria:** [[🎨 Design, UI & Frontend Systems]]  
> **Caminho Local no Sistema:** `S:\DEV\agents\skills\react-view-transitions`  
> **Papel Principal:** Front-End Specialist / Test-QA

---

## Instruções Principais & Comandos

```markdown
---
name: vercel-react-view-transitions
description: Guide for implementing smooth, native-feeling animations using React's View Transition API (`<ViewTransition>` component, `addTransitionType`, and CSS view transition pseudo-elements). Use this skill whenever the user wants to add page transitions, animate route changes, create shared element animations, animate enter/exit of components, animate list reorder, implement directional (forward/back) navigation animations, or integrate view transitions in Next.js. Also use when the user mentions view transitions, `startViewTransition`, `ViewTransition`, transition types, or asks about animating between UI states in React without third-party animation libraries.
license: MIT
metadata:
  author: vercel
  version: "1.0.0"
---

# React View Transitions

Animate between UI states using the browser's native `document.startViewTransition`. Declare *what* with `<ViewTransition>`, trigger *when* with `startTransition` / `useDeferredValue` / `Suspense`, control *how* with CSS classes. Unsupported browsers skip animations gracefully.

## When to Animate

Every `<ViewTransition>` should communicate a spatial relationship or continuity. If you can't articulate what it communicates, don't add it.

Implement **all** applicable patterns from this list, in this order:

| Priority | Pattern | What it communicates |
|----------|---------|---------------------|
| 1 | **Shared element** (`name`) | "Same thing — going deeper" |
| 2 | **Suspense revea
```
