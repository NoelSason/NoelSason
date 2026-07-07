# Hey, I'm Noel 👋

**Builder. Student. Founder.**

I'm studying Molecular & Cell Biology + Data Science at UC Berkeley. I build products that fix broken workflows for the people who have to live inside them — students, clinicians, litigants, AI agents.

Right now, I split my time across **Canvascope**, **Lectra**, and **RxBrief**, with a couple of smaller tools shipped alongside them.

---

## What I'm Building

### 🔍 Canvascope

**Search your Canvas content by intent, not exact keywords.**

Canvas LMS search is broken. Students know *what* they're looking for but not *what it's called*. Canvascope fixes that.

- Chrome extension that indexes assignments, files, and modules locally
- Privacy-first — your data never leaves your browser
- Works across multiple university Canvas domains
- Intent-aware: searching for a due lab also surfaces related PDFs, modules, and undated materials
- A built-in AI agent that *acts*, not just answers — it reasons in steps, reads your deadlines/grades/calendar, and drafts the to-dos, events, and study plans, with a daily briefing and a hard wall that keeps it from ever submitting your work

This isn't a feature bolted onto Canvas. It's a fundamentally better way to interact with LMS data.

`Chrome Extension` · `Manifest v3` · `Local-first indexing` · `Search ranking`

---

### 📓 Lectra

**A notes-first academic workspace built around how students actually work.**

Not another note-taking app. Lectra is the operating system for your coursework.

- Rich text + Markdown editor with PDF annotation (Apple Pencil optimized)
- Course-based organization with assignment linking
- Full-text search across everything
- Offline-first — works without Wi-Fi, syncs when connected
- Shared indexing layer with Canvascope
- A real coding workspace on iPad — terminal, git, and Python notebooks running fully sandboxed on-device (hand-built shell + git + Python runtime, no cloud)

**What's next:**
- **Course Brain** — a knowledge graph connecting all your course materials

`iOS` · `Web` · `Supabase` · `Offline-first architecture`

---

### 💊 RxBrief

**One tool instead of ten tabs, for clinicians.**

Every feature was scoped directly from interviews with healthcare professionals — it solves the problems they actually named.

- Instant FDA-sourced label data — indications, dosing, interactions — instead of digging through PDF inserts
- Job openings from Greenhouse, Lever, and RSS feeds normalized into one server-filtered feed
- Real-time Supabase chat keeping the conversation in-app

`Next.js` · `React` · `TypeScript` · `Supabase` · `FDA API`

---

### 🧠 PersonalGraph MCP

**A local-first memory server for AI agents.**

Gives any MCP-compatible AI client (Claude Desktop, Claude Code, Cursor) structured, queryable memory about its user instead of starting every conversation from zero — it's the exact system behind this profile's own AI-assisted workflows.

- 16 MCP tools, 5 resources, and 4 prompt templates over a typed personal-knowledge graph
- Four-tier privacy model (public/ai\_allowed/private/sensitive) with secret redaction and append-only audit logging
- Swappable storage interface — JSON today, a documented path to Neo4j/SQLite/Postgres

`TypeScript` · `Node.js` · `MCP SDK` · `Zod`

---

### ⚖️ SCI Cause-List Alerts

**Closing an information gap for Indian Supreme Court litigants.**

Rather than requiring a lawyer or daily manual lookup, a scheduled worker checks whether a subscriber's case is on tomorrow's cause list and emails them proactively — built for people who lack easy access to legal counsel or repeated court-website checks.

- Daily worker parses government-published cause-list PDFs and matches them against subscriber watch-lists
- Idempotent, audited email delivery with self-monitoring that flags failed runs
- Bot-protected signup (Cloudflare Turnstile) and IP rate limiting (Upstash Redis)

`Next.js` · `TypeScript` · `Prisma` · `PostgreSQL` · `Upstash Redis`

---

## Tech Stack

```
Languages        Python · Java · Swift/SwiftUI · TypeScript · JavaScript · SQL
Frontend         Chrome Extensions (MV3) · Next.js · React · Web
Backend          Supabase (auth, storage, data) · Node · Prisma · PostgreSQL · Flask
Infra            Vercel · GitHub Actions · CLI tooling · Upstash Redis
Tools            Git · GitHub · MCP · Automation workflows
```

---

## Beyond Code

Before I was building software, I was building systems.

- **Former CalHOSA State Secretary** — led operations across California chapters
- **Finance Director** in student orgs — managed $10K+ budgets, cut reimbursement turnaround by ~40%
- Deeply interested in the intersection of **technology and medicine**

I think in systems. I care about execution. I ship.

---

## Let's Connect

[![Email](https://img.shields.io/badge/Email-noelsason@berkeley.edu-blue?style=flat-square&logo=gmail&logoColor=white)](mailto:noelsason@berkeley.edu)
[![GitHub](https://img.shields.io/badge/GitHub-noelsason-181717?style=flat-square&logo=github)](https://github.com/noelsason)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Noel_Sason-0A66C2?style=flat-square&logo=linkedin)](https://linkedin.com/in/noelsason)

---

<p align="center">
  <img src="https://github-readme-streak-stats.herokuapp.com?user=noelsason&hide_border=true" alt="GitHub Streak" />
</p>
