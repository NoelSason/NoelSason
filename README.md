<!-- ══════════════════════════ HEADER ══════════════════════════ -->

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&height=200&color=0:1a1b27,50:414868,100:70a5fd&text=Noel%20Sason&fontColor=c0caf5&fontSize=64&fontAlignY=36&desc=Builder%20·%20Student%20·%20Founder&descAlignY=57&descSize=18&animation=fadeIn" alt="Noel Sason" />
</p>

<p align="center">
  <a href="https://readme-typing-svg.demolab.com">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=22&duration=3200&pause=900&color=70A5FD&center=true&vCenter=true&width=760&lines=Molecular+%26+Cell+Biology+%2B+Data+Science+%40+Berkeley;Building+the+LMS+where+students+actually+do+the+work;Ink%2C+notebooks%2C+and+a+real+shell+%E2%80%94+running+on+an+iPad;I+think+in+systems.+I+care+about+execution.+I+ship." alt="Typing SVG" />
  </a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/UC_Berkeley-003262?style=for-the-badge&logo=googlescholar&logoColor=FDB515" alt="UC Berkeley" />
  <img src="https://img.shields.io/badge/MCB_+_Data_Science-414868?style=for-the-badge" alt="MCB + Data Science" />
  <img src="https://img.shields.io/badge/Class_of_Dec_2027-70a5fd?style=for-the-badge&logoColor=white" alt="Dec 2027" />
</p>

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=NoelSason&label=Profile%20views&color=70a5fd&style=flat-square" alt="Profile views" />
  <a href="https://github.com/NoelSason?tab=followers"><img src="https://img.shields.io/github/followers/NoelSason?label=Followers&style=flat-square&color=70a5fd" alt="Followers" /></a>
</p>

<!-- ══════════════════════════ SNAKE ══════════════════════════ -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/NoelSason/NoelSason/output/github-snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/NoelSason/NoelSason/output/github-snake.svg" />
  <img alt="github contribution grid snake animation" src="https://raw.githubusercontent.com/NoelSason/NoelSason/output/github-snake.svg" />
</picture>

---

I'm studying **Molecular & Cell Biology + Data Science** at UC Berkeley. I build products that fix
broken workflows for the people who have to live inside them — students, clinicians, litigants.

Most of my time goes to **Scope**, with RxBrief and a handful of smaller tools shipped alongside it.

<!-- ══════════════════════════ BUILDING ══════════════════════════ -->

<h2 align="center">═══ ✦ What I'm Building ✦ ═══</h2>

### 🎓 Scope &nbsp;<sub><sup>(formerly Canvascope)</sup></sub>

> **Canvas is the system of record. Scope is the system of work.**

Learning management systems are where instructors *post* things. The actual work happens somewhere
else — readings annotated in GoodNotes, writing in Docs, code in VS Code, questions asked in
ChatGPT — and the LMS only ever sees the final upload.

Scope makes the course itself the workspace. It enters through the LMS a school already runs, and the
direction it's heading is one where every discipline gets the environment it actually needs — a
repository and a terminal for CS, ink and replay for math, papers and lab notebooks for biology.

Three surfaces, one workspace:

<table>
<tr>
<td width="33%" valign="top">

**📓 [Lectra](https://apps.apple.com/us/app/lectra-notes/id6759754531)**<br/>
<sub>iPad · **live on the App Store**</sub>

The high-fidelity client. Pencil-first markup on documents, notebooks beside them, and — when the
reading turns into work — a real Python kernel, shell, and Git.

</td>
<td width="33%" valign="top">

**🔍 The Extension**<br/>
<sub>Chrome MV3 · local-first</sub>

The distribution wedge. Indexes assignments, files, and modules locally, answers questions with
citations, and hands PDFs off to Lectra.

</td>
<td width="33%" valign="top">

**🧭 [Polya](https://askpolya.com)**<br/>
<sub>Next.js · Supabase</sub>

Course-aware tutoring that helps students *learn* — hints and guided steps, never just answers.
Named for George Pólya.

</td>
</tr>
</table>

**Some things I'm proud of in here:**

- **Lectra runs a computer on an iPad.** iOS has no `exec`, so anything that would normally be a
  subprocess had to be written from scratch or embedded as WebAssembly — a hand-built shell, Git,
  and Python runtime, all on-device and offline. Plus SSH, and Mac↔iPad remote desktop over WebRTC.
- **Ink is vector, never raster.** Strokes are stored normalized to 0…1 of the page, so zoom only
  changes `contentsScale` and a stroke copied between differently-sized pages still lands correctly.
  In-progress strokes are split into sealed 64-point chunk layers, making drawing O(1) per frame
  instead of O(stroke length).
- **`.lectra` is a file package that can't drift** — simultaneously the on-disk representation *and*
  the interchange format, so there's no export layout to fall out of sync. Instructor and student
  layers never cross, which is what makes "the professor reissues the packet, you keep your notes"
  possible at all.
- **Polya cites everything.** Every claim traces back to the exact page, slide, or lecture moment it
  came from, and instructors set the assistance level per course.

<sub>`Swift 6` · `SwiftUI + UIKit` · `Chrome MV3` · `Next.js` · `Supabase` · `WebRTC` · `WebAssembly` · `Offline-first`</sub>

<sub>📊 As of 2026-08-11 — 58 Chrome Web Store installs · 56 registered accounts · 40,052 documents synced across 68 devices · Lectra v5.0. Free for students; there's no paid tier.</sub>

---

### 💊 [RxBrief](https://medsphere-nu.vercel.app)

**One tool instead of ten tabs, for clinicians.**

Every feature was scoped directly from interviews with healthcare professionals — it solves the
problems they actually named.

- Instant FDA-sourced label data — indications, dosing, interactions — instead of digging through PDF inserts
- Job openings from Greenhouse, Lever, and RSS normalized into one server-filtered feed
- Real-time Supabase chat keeping the conversation in-app

<sub>`Next.js` · `React` · `TypeScript` · `Supabase` · `openFDA API`</sub>

---

### ⚖️ [SCI Cause-List Alerts](https://india-case-status-omega.vercel.app)

**Closing an information gap for Indian Supreme Court litigants.**

Rather than requiring a lawyer or a daily manual lookup, a scheduled worker checks whether a
subscriber's case is on tomorrow's cause list and emails them proactively — built for people without
easy access to legal counsel.

- Daily worker parses government-published cause-list PDFs against subscriber watch-lists
- Idempotent, audited delivery with self-monitoring that flags failed runs
- Bot-protected signup (Cloudflare Turnstile) and IP rate limiting (Upstash Redis)

<sub>`Next.js` · `TypeScript` · `Prisma` · `PostgreSQL` · `Upstash Redis` · `Resend`</sub>

<!-- ══════════════════════════ RESEARCH ══════════════════════════ -->

<h2 align="center">═══ ✦ Research ✦ ═══</h2>

### 🧬 Lawrence Berkeley National Laboratory

**Research Affiliate — Arkin Lab / CultureBotAI (BBOP)**

I build the pipelines that turn noisy, heterogeneous biological records into structured datasets
other people can actually run analyses on.

- A **DuckDB traversal pipeline over the `kg-microbe` knowledge graph** — METPO ontology terms,
  CHEBI chemicals, ENVO environments, UBERON anatomical sites — making SQL queries across **80+
  microbiome studies** fast
- Automated study onboarding from BugSigDB differential-abundance exports into per-study directories
  with taxa linked to NCBI Taxon IDs, covering colorectal cancer, lung cancer, epilepsy, and skin wounds
- A YAML-driven trait-profile generator emitting wide and long TSVs for downstream statistics
- Standardized environments with `uv` and Justfile task runners

<sub>`Python` · `DuckDB` · `Ontologies` · `uv` · `Just`</sub>

<sub>🔬 Plus something early I'm not talking about yet.</sub>

<!-- ══════════════════════════ COMMUNITY ══════════════════════════ -->

<h2 align="center">═══ ✦ Community ✦ ═══</h2>

- **[South Indian Society @ Berkeley](https://sisberkeley.org)** — Co-President. Built the org's
  website and a native SwiftUI app for **200+ members**, replacing four fragmented tools with
  role-aware access, Stripe ticketing, and realtime updates.
- **[SaRiGaMa Check-In](https://scv-sarigama-checkin.vercel.app)** — digital Sadhya check-in built
  for Onam 2026.
- **[St. Mary's Church](https://church-new.vercel.app)** — parish site, plus a Python/SQLite ledger
  system handling families, charges, partial payments, and remaining balances.

<!-- ══════════════════════════ STACK ══════════════════════════ -->

<h2 align="center">═══ ✦ Stack ✦ ═══</h2>

<p align="center">
  <b>Languages</b><br/>
  <img src="https://img.shields.io/badge/Swift-F05138?style=for-the-badge&logo=swift&logoColor=white" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white" />
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" />
  <img src="https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=postgresql&logoColor=white" />
  <img src="https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white" />
</p>

<p align="center">
  <b>Frontend &amp; Mobile</b><br/>
  <img src="https://img.shields.io/badge/SwiftUI-0071E3?style=for-the-badge&logo=swift&logoColor=white" />
  <img src="https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white" />
  <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black" />
  <img src="https://img.shields.io/badge/Tailwind-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white" />
  <img src="https://img.shields.io/badge/Chrome_MV3-4285F4?style=for-the-badge&logo=googlechrome&logoColor=white" />
</p>

<p align="center">
  <b>Backend &amp; Data</b><br/>
  <img src="https://img.shields.io/badge/Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white" />
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" />
  <img src="https://img.shields.io/badge/Prisma-2D3748?style=for-the-badge&logo=prisma&logoColor=white" />
  <img src="https://img.shields.io/badge/DuckDB-FFF000?style=for-the-badge&logo=duckdb&logoColor=black" />
  <img src="https://img.shields.io/badge/Node.js-5FA04E?style=for-the-badge&logo=nodedotjs&logoColor=white" />
</p>

<p align="center">
  <b>ML &amp; Scientific</b><br/>
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" />
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white" />
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/ONNX-005CED?style=for-the-badge&logo=onnx&logoColor=white" />
</p>

<p align="center">
  <b>Infrastructure</b><br/>
  <img src="https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" />
  <img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white" />
  <img src="https://img.shields.io/badge/Cloudflare-F38020?style=for-the-badge&logo=cloudflare&logoColor=white" />
  <img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black" />
</p>

<!-- ══════════════════════════ BEYOND CODE ══════════════════════════ -->

<h2 align="center">═══ ✦ Beyond Code ✦ ═══</h2>

Before I was building software, I was building systems.

- **California HOSA State Secretary (2023–2024)** — statewide operations, conference logistics, and
  sponsor correspondence across California chapters
- **ASUC Finance Director** — administered roughly **$200,000** in student-org funding across
  allocations, grants, and waivers; tracked 89+ deadlines with zero compliance violations, and
  redesigned reconciliation to cut reimbursement processing time ~40%
- **Kaiser Permanente COPE Health Scholar** — clinical intern across 5+ departments. Hospital
  workflow experience fed directly into how RxBrief got scoped
- I run a **Raspberry Pi homelab** — NAS, Tailscale mesh, Pi-hole, and a pile of self-hosted tooling,
  because the best way to learn infrastructure is to be on call for your own

I think in systems. I care about execution. I ship.

<!-- ══════════════════════════ STATS ══════════════════════════ -->

<h2 align="center">═══ ✦ The Grind ✦ ═══</h2>

<p align="center">
  <img src="https://streak-stats.demolab.com?user=NoelSason&theme=tokyonight&hide_border=true&background=1A1B27&ring=70A5FD&fire=BF91F3&currStreakLabel=70A5FD&sideLabels=C0CAF5&dates=8B8CAD" alt="GitHub Streak" />
</p>

<p align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=NoelSason&theme=tokyo-night&hide_border=true&bg_color=1A1B27&color=70A5FD&line=BF91F3&point=C0CAF5&area=true" alt="Contribution Graph" width="100%" />
</p>

<!-- ══════════════════════════ CONNECT ══════════════════════════ -->

<h2 align="center">═══ ✦ Let's Connect ✦ ═══</h2>

<p align="center">
  <a href="mailto:noel_sason@berkeley.edu"><img src="https://img.shields.io/badge/Email-noel__sason@berkeley.edu-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" /></a>
  <a href="https://noelsason.com"><img src="https://img.shields.io/badge/Website-noelsason.com-70a5fd?style=for-the-badge&logo=safari&logoColor=white" alt="Website" /></a>
  <a href="https://linkedin.com/in/noelsason"><img src="https://img.shields.io/badge/LinkedIn-Noel_Sason-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
  <a href="https://github.com/NoelSason"><img src="https://img.shields.io/badge/GitHub-NoelSason-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" /></a>
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&section=footer&height=140&color=0:70a5fd,50:414868,100:1a1b27&reversal=true" alt="" />
</p>
